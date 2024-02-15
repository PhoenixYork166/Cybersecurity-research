#!/usr/bin/env bash
set -e

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

TIMESTAMP=$(date +%s)
LOGFILE="./kasm_upgrade_${TIMESTAMP}.log"
function notify_err() {
  echo "An error has occurred please review the log at ${LOGFILE}"
}
function cleanup_log() {
    rm -f ${LOGFILE}
}
trap notify_err ERR
exec &> >(tee ${LOGFILE})

KASM_VERSION="1.14.0"
CURRENT_VERSION=$(readlink -f /opt/kasm/current | awk -F'/' '{print $4}')
CURRENT_MAJOR_VERSION=$(echo ${CURRENT_VERSION} | awk -F'\\.' '{print $1}')
CURRENT_MINOR_VERSION=$(echo ${CURRENT_VERSION} | awk -F'\\.' '{print $2}')
KASM_INSTALL_BASE="/opt/kasm/${KASM_VERSION}"
OFFLINE_INSTALL="false"
DATABASE_HOSTNAME="false"
DB_PASSWORD="false"
DATABASE_PORT=5432
DATABASE_USER='kasmapp'
DATABASE_NAME='kasm'
REGISTRATION_TOKEN='false'
DEFAULT_GUAC_TOKEN='false'
GUAC_API_SERVER_HOSTNAME='false'
DEFAULT_GUAC_ID='00000000-0000-0000-0000-000000000000'
SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"
KASM_RELEASE="$(realpath $SCRIPT_PATH)"
ARCH=$(uname -m)
DISK_SPACE=50000000000
DEFAULT_PROXY_LISTENING_PORT='443'
API_SERVER_HOSTNAME='false'
ENABLE_LOSSLESS='false'
USE_ROLLING='false'
CHECK_DISK='true'
USE_SLIM='false'
ARGS=("$@")

if [ "${ARCH}" != "x86_64" ] && [ "${ARCH}" != "aarch64" ] ; then
  if [ "${ARCH}" == "unknown" ] ; then
    echo "FATAL: Unable to detect system architecture"
    cleanup_log
    exit 1
  else
    echo "FATAL: Unsupported architecture"
    cleanup_log
    exit 1
  fi
fi

# Functions
function gather_vars() {
  if [ "${DB_PASSWORD}" == "false" ] ; then
    DB_PASSWORD=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.database.password' /opt/kasm/${CURRENT_VERSION}/conf/app/api.app.config.yaml)
  fi
  MANAGER_TOKEN=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.manager.token' /opt/kasm/${CURRENT_VERSION}/conf/app/agent.app.config.yaml)
  MANAGER_HOSTNAME=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.manager.hostnames.[0]' /opt/kasm/${CURRENT_VERSION}/conf/app/agent.app.config.yaml)
  SERVER_ID=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.agent.server_id' /opt/kasm/${CURRENT_VERSION}/conf/app/agent.app.config.yaml)
  PUBLIC_HOSTNAME=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.agent.public_hostname' /opt/kasm/${CURRENT_VERSION}/conf/app/agent.app.config.yaml)
  MANAGER_ID=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.manager.manager_id' /opt/kasm/${CURRENT_VERSION}/conf/app/api.app.config.yaml)
  SERVER_HOSTNAME=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.server.server_hostname' /opt/kasm/${CURRENT_VERSION}/conf/app/api.app.config.yaml)
  REDIS_PASSWORD=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.redis.redis_password' /opt/kasm/${CURRENT_VERSION}/conf/app/api.app.config.yaml)
  if [ "${DATABASE_HOSTNAME}" == "false" ] ; then
    DATABASE_HOSTNAME=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.database.host' /opt/kasm/${CURRENT_VERSION}/conf/app/api.app.config.yaml)
  fi
  DB_IMAGE_NAME=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.services.db.image'  /opt/kasm/${CURRENT_VERSION}/docker/.conf/docker-compose-db.yaml)
  DATABASE_USER=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.database.username'  /opt/kasm/${CURRENT_VERSION}/conf/app/api.app.config.yaml)
  DATABASE_NAME=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.database.name'  /opt/kasm/${CURRENT_VERSION}/conf/app/api.app.config.yaml)
  if [ -f "/opt/kasm/${CURRENT_VERSION}/conf/app/kasmguac.app.config.yaml" ] && ([ "${ROLE}" == "guac" ] || [ -z "${ROLE}" ]); then
    DEFAULT_GUAC_TOKEN=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.api.token' /opt/kasm/${CURRENT_VERSION}/conf/app/kasmguac.app.config.yaml)
    if [ -z "${DEFAULT_GUAC_TOKEN}" ] || [ "${DEFAULT_GUAC_TOKEN}" == "null" ]; then
      DEFAULT_GUAC_TOKEN=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.api.auth_token' /opt/kasm/${CURRENT_VERSION}/conf/app/kasmguac.app.config.yaml)
    fi
    DEFAULT_GUAC_ID=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.kasmguac.id' /opt/kasm/${CURRENT_VERSION}/conf/app/kasmguac.app.config.yaml)
    GUAC_API_SERVER_HOSTNAME=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.api.hostnames.[0]' /opt/kasm/${CURRENT_VERSION}/conf/app/kasmguac.app.config.yaml)
    GUAC_PUBLIC_HOSTNAME=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.kasmguac.server_address' /opt/kasm/${CURRENT_VERSION}/conf/app/kasmguac.app.config.yaml)
    REGISTRATION_TOKEN=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.kasmguac.registration_token' /opt/kasm/${CURRENT_VERSION}/conf/app/kasmguac.app.config.yaml)
  fi
  API_IMAGE_NAME=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} '.services.kasm_api.image'  /opt/kasm/${CURRENT_VERSION}/docker/.conf/docker-compose-all.yaml)
  if [[ "${API_IMAGE_NAME}" == *-alpine ]]; then
    USE_SLIM="true"
  fi
}

function remove_duplicate_restarts() {
  ${SCRIPT_PATH}/bin/utils/yq_${ARCH} -i 'del(.services[].restart)' /opt/kasm/${CURRENT_VERSION}/docker/docker-compose.yaml
  ${SCRIPT_PATH}/bin/utils/yq_${ARCH} -i '.services[].restart = "always"' /opt/kasm/${CURRENT_VERSION}/docker/docker-compose.yaml
  chown kasm:kasm /opt/kasm/${CURRENT_VERSION}/docker/docker-compose.yaml
  chmod 644 /opt/kasm/${CURRENT_VERSION}/docker/docker-compose.yaml
}

function stop_kasm() {
  /opt/kasm/bin/stop
}

function start_kasm() {
  /opt/kasm/bin/start
}

function backup_db() {
  mkdir -p /opt/kasm/backups/
  # Hotfix in case we have old paths for dumping DB
  sed -i 's/tmp/backup/g' /opt/kasm/${CURRENT_VERSION}/bin/utils/db_backup
  # Run backup
  if [ "${ROLE}" == "db" ] || [ -z "${ROLE}" ] ; then
    bash /opt/kasm/${CURRENT_VERSION}/bin/utils/db_backup -f /opt/kasm/backups/kasm_db_backup.tar -p /opt/kasm/${CURRENT_VERSION}/
  else
    if [ "${CURRENT_MAJOR_VERSION}" == "1" ] && [ "${CURRENT_MINOR_VERSION}" -le "10" ] ; then
      # Kasm versions earlier than 1.11.0 didn't have a backup utility that worked with remote databases
      bash ${SCRIPT_PATH}/bin/utils/db_backup -f /opt/kasm/backups/kasm_db_backup.tar -p /opt/kasm/${CURRENT_VERSION}/ -q "${DATABASE_HOSTNAME}" -c ${DATABASE_USER} -j ${DATABASE_NAME}
    else
      bash /opt/kasm/${CURRENT_VERSION}/bin/utils/db_backup -f /opt/kasm/backups/kasm_db_backup.tar -p /opt/kasm/${CURRENT_VERSION}/ -q "${DATABASE_HOSTNAME}"
    fi
  fi
  if [ ! -f "/opt/kasm/backups/kasm_db_backup.tar" ]; then
    echo "Error backing up database, please follow the instructions at https://kasmweb.com/docs/latest/upgrade/single_server_upgrade.html to manually upgrade your installation"
    start_kasm
    exit 1
  fi
}

function clean_install() {
  echo "Installing Kasm Workspaces ${KASM_VERSION}"
  bash ${SCRIPT_PATH}/install.sh -b -N -e -H -D ${OPTS} ${LOSSLESS} ${SLIM} -Q ${DB_PASSWORD} -M ${MANAGER_TOKEN} -L ${DEFAULT_PROXY_LISTENING_PORT} -c ${DATABASE_USER} -j ${DATABASE_NAME}
}

function db_install() {
  echo "Installing Kasm Workspaces ${KASM_VERSION}"
  if [ "${ROLE}" == "db" ] ; then
    bash ${SCRIPT_PATH}/install.sh -e -H -D ${OPTS} -S db -Q ${DB_PASSWORD} -R ${REDIS_PASSWORD} -L ${DEFAULT_PROXY_LISTENING_PORT} -c ${DATABASE_USER} -j ${DATABASE_NAME}
  else
    bash ${SCRIPT_PATH}/install.sh -N -e -H -D ${OPTS} -S init_remote_db -q "${DATABASE_HOSTNAME}" -Q "${DB_PASSWORD}" -R "${REDIS_PASSWORD}" -L ${DEFAULT_PROXY_LISTENING_PORT} -g "${DATABASE_MASTER_USER}" -G "${DATABASE_MASTER_PASSWORD}" -c ${DATABASE_USER} -j ${DATABASE_NAME}
  fi
}

function agent_install() {
  echo "Installing Kasm Workspaces ${KASM_VERSION}"
  bash ${SCRIPT_PATH}/install.sh -b -N -e -H ${OPTS} ${ROLLING} ${SLIM} -S agent -D -p ${PUBLIC_HOSTNAME} -m ${MANAGER_HOSTNAME} -M ${MANAGER_TOKEN} -L ${DEFAULT_PROXY_LISTENING_PORT}
}

function app_install() {
  echo "Installing Kasm Workspaces ${KASM_VERSION}"
  bash ${SCRIPT_PATH}/install.sh -N -e -H ${OPTS} ${SLIM} -S app -D -q ${DATABASE_HOSTNAME} -Q ${DB_PASSWORD} -R ${REDIS_PASSWORD} -L ${DEFAULT_PROXY_LISTENING_PORT} -c ${DATABASE_USER} -j ${DATABASE_NAME}
}

function proxy_install() {
  echo "Installing Kasm Workspaces ${KASM_VERSION}"
  if [ "${API_SERVER_HOSTNAME}" == "false" ]; then
    echo "FATAL: option -n|--api-hostname is required for the proxy role"
    cleanup_log
    exit 1
  fi
  bash ${SCRIPT_PATH}/install.sh -e ${SLIM} -H ${OPTS} -S proxy -L ${DEFAULT_PROXY_LISTENING_PORT} -n ${API_SERVER_HOSTNAME}
}

function guac_install() {
  echo "Installing Kasm Workspaces ${KASM_VERSION}"
  if [ ! -z "${SERVICE_IMAGE_TARFILE}" ]; then
    OPTS="-s ${SERVICE_IMAGE_TARFILE}"
  fi
  if [ "${GUAC_API_SERVER_HOSTNAME}" != "false" ]; then
    echo "Using API server hostname ${GUAC_API_SERVER_HOSTNAME} for connection proxy server upgrade"
  elif [ "${API_SERVER_HOSTNAME}" != "false" ] && [ "${GUAC_API_SERVER_HOSTNAME}" == "false" ]; then
    GUAC_API_SERVER_HOSTNAME=${API_SERVER_HOSTNAME}
    echo "Using API server hostname ${GUAC_API_SERVER_HOSTNAME} for connection proxy server upgrade"
  else
    echo "FATAL: option -n|--api-hostname is required for the guac role"
    exit 1
  fi
  if [ "${GUAC_PUBLIC_HOSTNAME}" != "false" ]; then
    echo "Using ${GUAC_PUBLIC_HOSTNAME} as the connection proxy server hostname"
  elif [ "${PUBLIC_HOSTNAME}" != "false" ] && [ "${GUAC_PUBLIC_HOSTNAME}" == "false" ]; then
    GUAC_PUBLIC_HOSTNAME=${PUBLIC_HOSTNAME}
    echo "Using ${GUAC_PUBLIC_HOSTNAME} as the connection proxy server hostname"
  else
    echo "FATAL: option -p|--public-hostname is required for the guac role"
    exit 1
  fi
  if [ "${REGISTRATION_TOKEN}" == "false" ]; then
    echo "FATAL: option -k|--registration-token is required for the guac role"
    exit 1
  fi
  bash ${SCRIPT_PATH}/install.sh -e ${SLIM} -H ${OPTS} -S guac -L ${DEFAULT_PROXY_LISTENING_PORT} -n ${GUAC_API_SERVER_HOSTNAME} -k ${REGISTRATION_TOKEN} -p ${GUAC_PUBLIC_HOSTNAME} -l ${DEFAULT_GUAC_TOKEN}
}

function modify_agent_configs() {
  ${SCRIPT_PATH}/bin/utils/yq_${ARCH} -i '.agent.server_id = "'${SERVER_ID}'"' /opt/kasm/${KASM_VERSION}/conf/app/agent.app.config.yaml
  ${SCRIPT_PATH}/bin/utils/yq_${ARCH} -i '.agent.public_hostname = "'${PUBLIC_HOSTNAME}'"' /opt/kasm/${KASM_VERSION}/conf/app/agent.app.config.yaml
  # There may be multiple manager hostnames we want to populate all of them.
  MANAGER_HOSTNAMES=$(${SCRIPT_PATH}/bin/utils/yq_${ARCH} -o j '.manager.hostnames' /opt/kasm/${CURRENT_VERSION}/conf/app/agent.app.config.yaml)
  ${SCRIPT_PATH}/bin/utils/yq_${ARCH} -i ".manager.hostnames |= ${MANAGER_HOSTNAMES}" /opt/kasm/${KASM_VERSION}/conf/app/agent.app.config.yaml
  chown kasm:kasm /opt/kasm/${KASM_VERSION}/conf/app/agent.app.config.yaml
  chmod 644 /opt/kasm/${KASM_VERSION}/conf/app/agent.app.config.yaml
}

function modify_api_configs() {
  ${SCRIPT_PATH}/bin/utils/yq_${ARCH} -i '.manager.manager_id = "'${MANAGER_ID}'"' /opt/kasm/${KASM_VERSION}/conf/app/api.app.config.yaml
  ${SCRIPT_PATH}/bin/utils/yq_${ARCH} -i '.server.server_hostname = "'${SERVER_HOSTNAME}'"' /opt/kasm/${KASM_VERSION}/conf/app/api.app.config.yaml
  chown kasm:kasm /opt/kasm/${KASM_VERSION}/conf/app/api.app.config.yaml
  chmod 644 /opt/kasm/${KASM_VERSION}/conf/app/api.app.config.yaml
}

function modify_guac_configs() {
  if [ "${CURRENT_MAJOR_VERSION}" == "1" ] && [ "${CURRENT_MINOR_VERSION}" -ge "12" ] ; then
    ${SCRIPT_PATH}/bin/utils/yq_${ARCH} -i '.kasmguac.id = "'${DEFAULT_GUAC_ID}'"' /opt/kasm/${KASM_VERSION}/conf/app/kasmguac.app.config.yaml
    ${SCRIPT_PATH}/bin/utils/yq_${ARCH} -i '.api.auth_token = "'${DEFAULT_GUAC_TOKEN}'"' /opt/kasm/${KASM_VERSION}/conf/app/kasmguac.app.config.yaml
    chown kasm:kasm /opt/kasm/${KASM_VERSION}/conf/app/kasmguac.app.config.yaml
    chmod 644 /opt/kasm/${KASM_VERSION}/conf/app/kasmguac.app.config.yaml
  fi
}

function copy_nginx() {
  if [ $(ls -A /opt/kasm/${CURRENT_VERSION}/conf/nginx/containers.d/) ]; then
    cp /opt/kasm/${CURRENT_VERSION}/conf/nginx/containers.d/* /opt/kasm/${KASM_VERSION}/conf/nginx/containers.d/
    chown root:root /opt/kasm/${KASM_VERSION}/conf/nginx/containers.d/*
    chmod 644 /opt/kasm/${KASM_VERSION}/conf/nginx/containers.d/*
  fi
}

function restore_db() {
  if [ "${ROLE}" == "db" ] || [ -z "${ROLE}" ] ; then
    /opt/kasm/${KASM_VERSION}/bin/utils/db_restore -a -f /opt/kasm/backups/kasm_db_backup.tar -p  /opt/kasm/${KASM_VERSION} -c ${DATABASE_USER} -j ${DATABASE_NAME}
    /opt/kasm/${KASM_VERSION}/bin/utils/db_upgrade -p /opt/kasm/${KASM_VERSION}
  else
    /opt/kasm/${KASM_VERSION}/bin/utils/db_restore -a -f /opt/kasm/backups/kasm_db_backup.tar -p  /opt/kasm/${KASM_VERSION} -q "${DATABASE_HOSTNAME}" -g "${DATABASE_MASTER_USER}" -G "${DATABASE_MASTER_PASSWORD}" -c ${DATABASE_USER} -j ${DATABASE_NAME}
    /opt/kasm/${KASM_VERSION}/bin/utils/db_upgrade -p /opt/kasm/${KASM_VERSION} -q "${DATABASE_HOSTNAME}"
  fi
}

function connection_proxy_db_init() {
  if [ -z "${ROLE}" ] || [ "${ROLE}" == "db" ]; then
    if [ "${CURRENT_MAJOR_VERSION}" == "1" ] && [ "${CURRENT_MINOR_VERSION}" -le "11" ] ; then
      # Only seed connection proxy if 1.11 or below
      /opt/kasm/${KASM_VERSION}/bin/utils/db_init -s /opt/kasm/${KASM_VERSION}/conf/database/seed_data/default_connection_proxies.yaml
      start_kasm
    fi
  fi
}

function copy_certificates() {
  # We check for our self signed certificates, and if those are present and have less than 6 months left
  # (two Kasm releases at our current quarterly release cycle) we generate new certificates.
  subject=$(openssl x509 -in /opt/kasm/${CURRENT_VERSION}/certs/kasm_nginx.crt -noout -subject)
  if [[ ${subject} == *"OU=DoFu"* ]] && [[ ${subject} == *"emailAddress=none@none.none"* ]]; then
    openssl x509 -in /opt/kasm/${CURRENT_VERSION}/certs/kasm_nginx.crt -noout -checkend 15768017
    ret_code=$?
    if [ $ret_code -ne 0 ] ; then
      echo "Existing self-signed certs expire within six months generating new self-signed certs"
      sudo openssl req -x509 -nodes -days 1825 -newkey rsa:2048 -keyout ${KASM_INSTALL_BASE}/certs/kasm_nginx.key -out ${KASM_INSTALL_BASE}/certs/kasm_nginx.crt -subj "/C=US/ST=VA/L=None/O=None/OU=DoFu/CN=$(hostname)/emailAddress=none@none.none" 2> /dev/null
      return
    fi
  fi
  echo "Copying existing certs from Kasm Workspaces ${CURRENT_VERSION} install"
  cp -f /opt/kasm/${CURRENT_VERSION}/certs/kasm_nginx.crt ${KASM_INSTALL_BASE}/certs/kasm_nginx.crt
  cp -f /opt/kasm/${CURRENT_VERSION}/certs/kasm_nginx.key ${KASM_INSTALL_BASE}/certs/kasm_nginx.key
  chown kasm:kasm ${KASM_INSTALL_BASE}/certs/kasm_nginx.key
  chmod 600 ${KASM_INSTALL_BASE}/certs/kasm_nginx.key
  chown kasm:kasm ${KASM_INSTALL_BASE}/certs/kasm_nginx.crt
  chmod 600 ${KASM_INSTALL_BASE}/certs/kasm_nginx.crt
}

function display_help() {
  CMD='\033[0;31m'
  NC='\033[0m'
  echo "Kasm Upgrader ${KASM_VERSION}" 
  echo "Usage IE:"
  echo "${0} --add-images --proxy-port 443"
  echo    ""
  echo    "Flag                                        Description"
  echo    "---------------------------------------------------------------------------------------------------------------"
  echo -e "| ${CMD}-h|--help${NC}                     | Display this help menu                                                      |"
  echo -e "| ${CMD}-L|--proxy-port${NC}               | Default Proxy Listening Port                                                |"
  echo -e "| ${CMD}-s|--offline-service${NC}          | Path to the tar.gz service images offline installer                         |"
  echo -e "| ${CMD}-S|--role${NC}                     | Role to Upgrade: [app|db|agent|remote_db|guac|proxy]                        |"
  echo -e "| ${CMD}-p|--public-hostname${NC}          | Agent/Component <IP/Hostname> used to register with deployment.             |"
  echo -e "| ${CMD}-g|--database-master-user${NC}     | Database master username required for remote DB                             |"
  echo -e "| ${CMD}-G|--database-master-password${NC} | Database master password required for remote DB                             |"
  echo -e "| ${CMD}-q|--db-hostname${NC}              | Database Hostname needed when upgrading agent and pulling images            |"
  echo -e "| ${CMD}-T|--db-port${NC}                  | Database port needed when upgrading agent and pulling images (default 5432) |"
  echo -e "| ${CMD}-Q|--db-password${NC}              | Database Password needed when upgrading agent and pulling images            |"
  echo -e "| ${CMD}-b|--no-check-disk${NC}            | Do not check disk space                                                     |"
  echo -e "| ${CMD}-n|--api-hostname${NC}             | Set API server hostname                                                     |"
  echo -e "| ${CMD}-A|--enable-lossless${NC}          | Enable lossless streaming option (1.12 and above)                           |"
  echo -e "| ${CMD}-O|--use-rolling-images${NC}       | Use rolling Service images                                                  |"
  echo -e "| ${CMD}-k|--registration-token${NC}       | Register a component with an existing deployment.                           |"
  echo -e "| ${CMD}--slim-images${NC}                 | Use slim alpine based service containers                                    |"
  echo    "---------------------------------------------------------------------------------------------------------------"
}


function check_role() {
if [ "${ROLE}" != "agent" ] && [ "${ROLE}" !=  "app" ] && [ "${ROLE}" != "db" ] && [ "${ROLE}" != "remote_db" ] && [ "${ROLE}" != "guac" ] &&  [ "${ROLE}" != "proxy" ];
then
  echo "Invalid Role Defined"
  display_help
  cleanup_log
  exit 1
fi
}

# Command line opts
for index in "${!ARGS[@]}"; do
  case ${ARGS[index]} in
    -L|--proxy-port)
      DEFAULT_PROXY_LISTENING_PORT="${ARGS[index+1]}"
      echo "Setting Default Listening Port as ${DEFAULT_PROXY_LISTENING_PORT}"
      ;;
    -S|--role)
      ROLE="${ARGS[index+1]}"
      check_role
      echo "Setting Role as ${ROLE}"
      ;;
    -h|--help)
      display_help
      cleanup_log
      exit 0
      ;;
    -s|--offline-service)
      SERVICE_IMAGE_TARFILE="${ARGS[index+1]}"
      OFFLINE_INSTALL="true"

      if [ ! -f "$SERVICE_IMAGE_TARFILE" ]; then
        echo "FATAL: Service image tarfile does not exist: ${SERVICE_IMAGE_TARFILE}"
        cleanup_log
        exit 1
      fi

      echo "Setting service image tarfile to ${SERVICE_IMAGE_TARFILE}"
      ;;
    -g|--database-master-user)
      DATABASE_MASTER_USER="${ARGS[index+1]}"
      echo "Using Database Master User ${DATABASE_MASTER_USER}"
      ;;
    -G|--database-master-password)
      DATABASE_MASTER_PASSWORD="${ARGS[index+1]}"
      echo "Using Database Master Password from stdin -G"
      ;;
    -q|--db-hostname)
      DATABASE_HOSTNAME="${ARGS[index+1]}"
      echo "Setting Database Hostname as ${DATABASE_HOSTNAME}"
      ;;
    -T|--db-port)
      DATABASE_PORT="${ARGS[index+1]}"
      echo "Setting Database Port to ${DATABASE_PORT}"
      ;;
    -Q|--db-password)
      DB_PASSWORD="${ARGS[index+1]}"
      echo "Setting Default Database Password from stdin -Q"
      ;;
    -n|--api-hostname)
      API_SERVER_HOSTNAME="${ARGS[index+1]}"
      echo "Setting API Server Hostname as ${API_SERVER_HOSTNAME}"
      ;;
    -A|--enable-lossless)
      ENABLE_LOSSLESS="true"
      ;;
    -O|--use-rolling-images)
      USE_ROLLING="true"
      ;;
    -k|--registration-token)
      REGISTRATION_TOKEN="${ARGS[index+1]}"
      ;;
    -b|--no-check-disk)
      CHECK_DISK="false"
      ;;
    --slim-images)
      USE_SLIM="true"
      ;;
    -*|--*)
      echo "Unknown option ${ARGS[index]}"
      display_help
      cleanup_log
      exit 1
      ;;
  esac
done

# Set some installer variables based on flags passed
LOSSLESS=""
if [ "${ENABLE_LOSSLESS}" == "true" ]; then
  LOSSLESS="-A"
fi
ROLLING=""
if [ "${USE_ROLLING}" == "true" ]; then
  ROLLING="-O"
fi
if [ ! -z "${SERVICE_IMAGE_TARFILE}" ]; then
  OPTS="-s ${SERVICE_IMAGE_TARFILE} -I"
else
  OPTS="-I"
fi
SLIM=""
if [ "${USE_SLIM}" == "true" ]; then
  SLIM="--slim-images"
fi

# Perform upgrade
if [ -z "${ROLE}" ]; then
  gather_vars
  remove_duplicate_restarts
  stop_kasm
  backup_db
  clean_install
  modify_agent_configs
  modify_api_configs
  modify_guac_configs
  copy_certificates
  copy_nginx
  restore_db
  start_kasm
  connection_proxy_db_init
  start_kasm
elif [ "${ROLE}" == "db" ]; then
  gather_vars
  remove_duplicate_restarts
  stop_kasm
  backup_db
  db_install
  restore_db
  start_kasm
  connection_proxy_db_init
  start_kasm
elif [ "${ROLE}" == "remote_db" ]; then
  gather_vars
  remove_duplicate_restarts
  stop_kasm
  backup_db
  db_install
  restore_db
elif [ "${ROLE}" == "agent" ]; then
  gather_vars
  remove_duplicate_restarts
  stop_kasm
  agent_install
  modify_agent_configs
  copy_certificates
  copy_nginx
  start_kasm
elif [ "${ROLE}" == "app" ]; then
  gather_vars
  remove_duplicate_restarts
  stop_kasm
  app_install
  modify_api_configs
  copy_certificates
  start_kasm
elif [ "${ROLE}" == "guac" ]; then
  gather_vars
  remove_duplicate_restarts
  stop_kasm
  guac_install
  modify_guac_configs
  copy_certificates
  start_kasm
elif [ "${ROLE}" == "proxy" ]; then
  remove_duplicate_restarts
  stop_kasm
  proxy_install
  copy_certificates
  start_kasm
fi

printf "\n\n"
echo "Upgrade from ${CURRENT_VERSION} to ${KASM_VERSION} Complete"

cleanup_log
