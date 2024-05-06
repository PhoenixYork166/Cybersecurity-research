FROM kalilinux/kali-rolling

# Set environment variables for APT
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory to container's /tools
WORKDIR /tools

# Metadata params
ARG BUILD_DATE
ARG VERSION
ARG PROJECT_URL
ARG VCS_REF
ARG TARBALL
ARG RELEASE_DESCRIPTION

# https://github.com/opencontainers/image-spec/blob/master/annotations.md
LABEL org.opencontainers.image.created="$BUILD_DATE" \
      org.opencontainers.image.source="$PROJECT_URL" \
      org.opencontainers.image.revision="$VCS_REF" \
      org.opencontainers.image.vendor="OffSec" \
      org.opencontainers.image.version="$VERSION" \
      org.opencontainers.image.title="Kali Linux ($RELEASE_DESCRIPTION branch)" \
      org.opencontainers.image.description="Official Kali Linux container image for $RELEASE_DESCRIPTION" \
      org.opencontainers.image.url="https://www.kali.org/" \
      org.opencontainers.image.authors="Kali Developers <devel@kali.org>"

# Copy archive-key.asc file from this host to container /etc/apt/trusted.gpg.d/
COPY archive-key.asc /etc/apt/trusted.gpg.d/

# Copy host directory files into container /tools
COPY . /tools/

# Ensure the commands runs as root
USER root

# Switch to the correct Kali repository
RUN echo "deb https://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list

# Clean APT cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Update Kali Repository
RUN apt-get update --fix-missing

# Install Tools
#RUN apt-get update && apt-cache search net-tools && \
RUN apt-get install -y --no-install-recommends net-tools tcpdump vim tmux iproute2 gawk hping3 python3-scapy

# Clean up APT when done
RUN apt-get clean && \
rm -rf /var/lib/apt/lists/*

EXPOSE 8080

CMD ["bash"]