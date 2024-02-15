#!/usr/bin/env bash
set -e
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

OS_ID='unknown'
OS_VERSION_ID='unknown'
SUPPORTED='false'
INSTALL_COMPOSE='false'
INSTALL_DOCKER='false'
MIN_DOCKER_VERSION='18.06'
MIN_DOCKER_COMPOSE_VERSION='2.1.1'
SKIP_V4L2LOOPBACK=$1
SKIP_CUSTOM_RCLONE=$2
SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"

CPU_ARCH="$(uname -m)"
ARCH=$(uname -m | sed 's/aarch64/arm64/g' | sed 's/x86_64/amd64/g')

function verlte() {
    [  "$1" = "`echo -e "$1\n$2" | sort -V | head -n1`" ]
}

# Checks if version $1 is less than $2
function verlt() {
    [ "$1" = "$2" ] && return 1 || verlte $1 $2
}

function check_docker_dependencies (){
    echo "Checking if docker and docker compose are installed."
    set +e
    DOCKER_VERSION=$(docker system info | grep "Server Version" | awk '{ print $3 }')
    DOCKER="$(command -v docker)"
    DOCKER_COMPOSE="$(docker compose 2>/dev/null)"
    DOCKER_COMPOSE_VERSION="$( (docker-compose version --short | sed s/v//g) 2>/dev/null)"
    set -e
    if [ -z "${DOCKER}" ] ; then
        INSTALL_DOCKER='true'
    else
        echo "Docker is installed"

        if [ -z "${DOCKER_VERSION}" ] ; then
            echo "Unable to check Docker version, is the Docker daemon running?"
            echo "Aborting Kasm Workspaces install."
            exit -1
        elif verlt "${DOCKER_VERSION}" "${MIN_DOCKER_VERSION}" ; then
            echo "The installed Docker Version: $DOCKER_VERSION is an unsupported version of Docker."
            echo "Aborting Kasm Workspaces install."
            exit -1
        else
            echo "$DOCKER_VERSION is a supported version of docker."
        fi
        
        
        if (docker system info | grep 'Docker Root Dir' | grep -q '/var/snap/docker') > /dev/null 2>&1 ; then
            echo "Detected version of Docker is installed via snap. This is unsupported."
            echo "Aborting Kasm Workspaces install."
            exit -1
        fi
    fi

    if [ -z "${DOCKER_COMPOSE}" ] ; then
        echo "Docker Compose is not installed."
	INSTALL_COMPOSE='true'
	install_docker_compose
    else
        echo "Docker compose is installed"

        if [ -z "${DOCKER_COMPOSE_VERSION}" ] ; then
            echo "Unable to determine docker compose version"
            echo "Aborting workspaces install"
            exit -1
        elif verlt "${DOCKER_COMPOSE_VERSION}" "${MIN_DOCKER_COMPOSE_VERSION}" ; then
            echo "${DOCKER_COMPOSE_VERSION} is an old version of docker compose, installing a new version"
            INSTALL_COMPOSE='true'
        else
            echo "${DOCKER_COMPOSE_VERSION} is a supported version of docker compose"
        fi
    fi

    if [ "${INSTALL_DOCKER}" == 'false' ] && [ "${INSTALL_COMPOSE}" == 'false' ] ; then
        echo "Commands docker and docker compose detected."
	install_rclone_plugin
        echo "Skipping Dependency Installation."
        exit 0
    fi
}

function install_docker_compose (){
   echo "Installing Docker Compose"
   mkdir -p /usr/local/lib/docker/cli-plugins
   curl -L https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/lib/docker/cli-plugins/docker-compose
   chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
}

function install_centos (){
    echo "CentOS 7.x/8.x/9.x Install"
    echo "Installing Base CentOS Packages"

    NO_BEST=""
    if [ "${1}" == '"8"' ] || [ "${1}" == '"9"' ]; then
        NO_BEST="--nobest"
    fi

    yum install -y yum-utils \
        device-mapper-persistent-data \
        lvm2 \
        lsof \
        nc

    sudo yum-config-manager \
        --add-repo \
        https://download.docker.com/linux/centos/docker-ce.repo

    echo "Installing Docker-CE"
    yum install -y docker-ce $NO_BEST
    systemctl start docker
}


function install_ubuntu (){
    echo "Ubuntu 18.04/20.04/22.04 Install"
    echo "Installing Base Ubuntu Packages"
    apt-get update
    apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        netcat-openbsd \
        software-properties-common

    if dpkg -s docker-ce | grep Status: | grep installed ; then
      echo "Docker Installed"
    else
      echo "Installing Docker-CE"

      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      add-apt-repository -y "deb [arch=$(dpkg --print-architecture)] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get update
      apt-get -y install docker-ce
    fi
}

function install_debian (){
    echo "Debian 10.x/11.x/12.x Install"
    echo "Installing Base Debian Packages"
    apt-get update
    sudo apt-get install -y \
         apt-transport-https \
         ca-certificates \
         curl \
         gnupg2 \
          netcat-openbsd \
         software-properties-common

    if dpkg -s docker-ce | grep Status: | grep installed ; then
      echo "Docker Installed"
    else
      echo "Installing Docker-CE"

      curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
      mkdir -p /etc/apt/sources.list.d
      echo "deb [arch=$(dpkg --print-architecture)] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
      apt-get update
      apt-get -y install docker-ce
    fi
}

function install_oracle (){
    echo "RHEL Linux 7.x/8.x/9.x Install"
    echo "Installing Base Packages"

    NO_BEST=""
    if [[ "${1}" == '"8.'* ]] || [[ "${1}" == '"9.'* ]]; then
        NO_BEST="--nobest"
    else
        sudo yum-config-manager --enable ol7_developer
    fi

    yum install -y yum-utils \
        device-mapper-persistent-data \
        lvm2 \
        lsof \
        nc

    sudo yum-config-manager \
        --add-repo \
        https://download.docker.com/linux/centos/docker-ce.repo

    echo "Installing Docker-CE"
    yum install -y docker-ce $NO_BEST
    systemctl start docker
}

function install_openssl (){
    if [ "${OS_ID}" == "ubuntu" ] && ( [ "${OS_VERSION_ID}" == '"18.04"' ] || [ "${OS_VERSION_ID}" == '"20.04"' ] || [ "${OS_VERSION_ID}" == '"22.04"' ] ) ; then
        sudo apt-get update
        sudo apt-get install -y openssl
    fi
    if [ "${OS_ID}" == "debian" ] && ( [ "${OS_VERSION_ID}" == '"10"' ] || [ "${OS_VERSION_ID}" == '"11"' ] || [ "${OS_VERSION_ID}" == '"12"' ] ) ; then
        sudo apt-get update
        sudo apt-get install -y openssl
    fi
    if [ "${OS_ID}" == '"centos"' ] && ( [ "${OS_VERSION_ID}" == '"7"' ] || [ "${OS_VERSION_ID}" == '"8"' ] || [ "${OS_VERSION_ID}" == '"9"' ] ) ; then
        yum install -y openssl
    fi
    if [ "${OS_ID}" == '"ol"' ] && ( [[ "${OS_VERSION_ID}" == '"7.'* ]] || [[ "${OS_VERSION_ID}" == '"8.'* ]] || [[ "${OS_VERSION_ID}" == '"9.'* ]] ) ; then
        yum install -y openssl
    fi
    if [ "${OS_ID}" == '"rocky"' ] && ( [[ "${OS_VERSION_ID}" == '"8.'* ]] || [[ "${OS_VERSION_ID}" == '"9.'* ]] ) ; then
        dnf install -y openssl
    fi
    if [ "${OS_ID}" == '"almalinux"' ] && ( [[ "${OS_VERSION_ID}" == '"8.'* ]] || [[ "${OS_VERSION_ID}" == '"9.'* ]] ) ; then
        dnf install -y openssl
    fi
}

function install_v4l2loopback (){
    if ( [ "${OS_ID}" == "ubuntu" ] && ( [ "${OS_VERSION_ID}" == '"18.04"' ] || [ "${OS_VERSION_ID}" == '"20.04"' ] || [ "${OS_VERSION_ID}" == '"22.04"' ] ) ) || \
       ( [ "${OS_ID}" == "debian" ] && ( [ "${OS_VERSION_ID}" == '"10"' ] || [ "${OS_VERSION_ID}" == '"11"' ] || [ "${OS_VERSION_ID}" == '"12"' ] ) ) && \
       [ "${SKIP_V4L2LOOPBACK}" == "false" ] ; then
        if [ ! -d /var/lib/dkms/v4l2loopback ] && [ ! -f /.dockerenv ] ; then
            OSVID=$(echo ${OS_VERSION_ID} | sed 's/"//g')
            apt-get update
            curl -o \
                /tmp/${OS_ID}_${OSVID}-v4l2loopback-dkms.deb -L \
                "https://kasmweb-build-artifacts.s3.amazonaws.com/v4l2loopback-ubuntu/${OS_ID}_${OSVID}-v4l2loopback-dkms.deb" && \
            apt install -y /tmp/${OS_ID}_${OSVID}-v4l2loopback-dkms.deb
            rm -f /tmp/${OS_ID}_${OSVID}-v4l2loopback-dkms.deb
            ${SCRIPT_PATH}/bin/utils/yq_$(uname -m) -i '(.group_settings.[] | select(.name=="allow_kasm_webcam" and .group_id=="68d557ac-4cac-42cc-a9f3-1c7c853de0f3")) .value = "True"' ${SCRIPT_PATH}/conf/database/seed_data/default_properties.yaml
        fi
    fi
}

if [ -f /etc/os-release ] ; then
    OS_ID="$(awk -F= '/^ID=/{print $2}' /etc/os-release)"
    OS_VERSION_ID="$(awk -F= '/^VERSION_ID/{print $2}' /etc/os-release)"
fi

if ! openssl version > /dev/null 2>&1; then
    echo "Installing OpenSSL"
    install_openssl
fi

function install_lsof (){
    if [ "${OS_ID}" == "ubuntu" ] && ( [ "${OS_VERSION_ID}" == '"18.04"' ] || [ "${OS_VERSION_ID}" == '"20.04"' ] || [ "${OS_VERSION_ID}" == '"22.04"' ] ) ; then
        sudo apt-get update
        sudo apt-get install -y lsof
    fi
    if [ "${OS_ID}" == "debian" ] && ( [ "${OS_VERSION_ID}" == '"10"' ] || [ "${OS_VERSION_ID}" == '"11"' ] || [ "${OS_VERSION_ID}" == '"12"' ] ) ; then
        sudo apt-get update
        sudo apt-get install -y lsof
    fi
    if [ "${OS_ID}" == '"centos"' ] && ( [ "${OS_VERSION_ID}" == '"7"' ] || [ "${OS_VERSION_ID}" == '"8"' ] || [ "${OS_VERSION_ID}" == '"9"' ] ) ; then
        yum install -y lsof
    fi
    if [ "${OS_ID}" == '"ol"' ] && ( [[ "${OS_VERSION_ID}" == '"7.'* ]] || [[ "${OS_VERSION_ID}" == '"8.'* ]] || [[ "${OS_VERSION_ID}" == '"9.'* ]] ) ; then
        yum install -y lsof
    fi
    if [ "${OS_ID}" == '"rocky"' ] && ( [[ "${OS_VERSION_ID}" == '"8.'* ]] || [[ "${OS_VERSION_ID}" == '"9.'* ]] ) ; then
        yum install -y lsof
    fi
    if [ "${OS_ID}" == '"almalinux"' ] && ( [[ "${OS_VERSION_ID}" == '"8.'* ]] || [[ "${OS_VERSION_ID}" == '"9.'* ]] ) ; then
        yum install -y lsof
    fi
}

function install_rclone_plugin () {
    if [ ! -f /usr/bin/fusermount ]; then
        if ( [ "${OS_ID}" == "debian" ] && ( [ "${OS_VERSION_ID}" == '"9"' ] || [ "${OS_VERSION_ID}" == '"10"' ] || [ "${OS_VERSION_ID}" == '"11"' ] ) ) || ( [ "${OS_ID}" == "ubuntu" ] && ( [ "${OS_VERSION_ID}" == '"18.04"' ] || [ "${OS_VERSION_ID}" == '"20.04"' ] || [ "${OS_VERSION_ID}" == '"22.04"' ] ) ); then
            apt-get update
            apt-get install -y fuse
        elif ( [ "${OS_ID}" == '"ol"' ] && ( [[ "${OS_VERSION_ID}" == '"7.'* ]] || [[ "${OS_VERSION_ID}" == '"8.'* ]] || [[ "${OS_VERSION_ID}" == '"9.'* ]] ) ) || ( [ "${OS_ID}" == '"centos"' ] && ( [ "${OS_VERSION_ID}" == '"7"' ] || [ "${OS_VERSION_ID}" == '"8"' ] || [ "${OS_VERSION_ID}" == '"9"' ] ) ); then
            yum install -y fuse
        fi 
    fi
    DOCKER_PLUGIN_DIR=$(docker info | awk -F': ' '/Docker Root Dir/ {print $2}')-plugins
    if [ ! -d ${DOCKER_PLUGIN_DIR}/rclone ]; then
        echo "installing rclone docker plugin"
        mkdir -p ${DOCKER_PLUGIN_DIR}/rclone/config
        mkdir -p ${DOCKER_PLUGIN_DIR}/rclone/cache
        docker plugin install rclone/docker-volume-rclone:${ARCH} args="-v" --alias rclone --grant-all-permissions
        if [ "${SKIP_CUSTOM_RCLONE}" == "false" ] ; then
            rm -f ${DOCKER_PLUGIN_DIR}/rclone/cache/docker-plugin.state
            ln -s /dev/null ${DOCKER_PLUGIN_DIR}/rclone/cache/docker-plugin.state
	fi
    fi
}

if ! lsof -v > /dev/null 2>&1; then
    echo "Installing lsof"
    install_lsof
fi

install_v4l2loopback
check_docker_dependencies

if [ "${OS_ID}" == "ubuntu" ] && ( [ "${OS_VERSION_ID}" == '"18.04"' ] || [ "${OS_VERSION_ID}" == '"20.04"' ] || [ "${OS_VERSION_ID}" == '"22.04"' ] ) ; then
    SUPPORTED='true'
    if [ $INSTALL_DOCKER == 'true' ] ; then
        install_ubuntu
    fi

    if [ $INSTALL_COMPOSE == 'true' ] ; then
        install_docker_compose
    fi
fi

if [ "${OS_ID}" == "debian" ] && ( [ "${OS_VERSION_ID}" == '"10"' ] || [ "${OS_VERSION_ID}" == '"11"' ] || [ "${OS_VERSION_ID}" == '"12"' ] ) ; then
    SUPPORTED='true'
    if [ $INSTALL_DOCKER == 'true' ] ; then
        install_debian
    fi

    if [ $INSTALL_COMPOSE == 'true' ] ; then
        install_docker_compose
    fi
fi

if [ "${OS_ID}" == '"centos"' ] && ( [ "${OS_VERSION_ID}" == '"7"' ] || [ "${OS_VERSION_ID}" == '"8"' ] || [ "${OS_VERSION_ID}" == '"9"' ] ) ; then
    SUPPORTED='true'
    if [ $INSTALL_DOCKER == 'true' ] ; then
        install_centos ${OS_VERSION_ID}
    fi

    if [ $INSTALL_COMPOSE == 'true' ] ; then
        install_docker_compose
    fi
fi

if [ "${OS_ID}" == '"ol"' ] && ( [[ "${OS_VERSION_ID}" == '"7.'* ]] || [[ "${OS_VERSION_ID}" == '"8.'* ]] || [[ "${OS_VERSION_ID}" == '"9.'* ]] ) ; then
    SUPPORTED='true'
    if [ $INSTALL_DOCKER == 'true' ] ; then
        install_oracle ${OS_VERSION_ID}
    fi

    if [ $INSTALL_COMPOSE == 'true' ] ; then
        install_docker_compose
    fi
fi

if [ "${OS_ID}" == '"rocky"' ] && ( [[ "${OS_VERSION_ID}" == '"8.'* ]] || [[ "${OS_VERSION_ID}" == '"9.'* ]] ) ; then
    SUPPORTED='true'
    if [ $INSTALL_DOCKER == 'true' ] ; then
        install_oracle ${OS_VERSION_ID}
    fi

    if [ $INSTALL_COMPOSE == 'true' ] ; then
        install_docker_compose
    fi
fi

if [ "${OS_ID}" == '"almalinux"' ] && ( [[ "${OS_VERSION_ID}" == '"8.'* ]] || [[ "${OS_VERSION_ID}" == '"9.'* ]] ) ; then
  	  SUPPORTED='true'
    if [ $INSTALL_DOCKER == 'true' ] ; then
        install_oracle ${OS_VERSION_ID}
    fi

    if [ $INSTALL_COMPOSE == 'true' ] ; then
        install_docker_compose
    fi
fi

if [ "${SUPPORTED}" == "false" ] ; then
   echo "Installation Not Supported for this Operating System. Exiting"
   exit -1
fi

install_rclone_plugin

echo "Dependency Installation Complete"
