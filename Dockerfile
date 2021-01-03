FROM debian:stable

# [Option] Install zsh
ARG INSTALL_ZSH="true"
# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="true"

# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
COPY .devcontainer/library-scripts/*.sh /tmp/library-scripts/
RUN bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts

WORKDIR /home/vscode/app
ENV PATH=/home/vscode/app/node_modules/.bin:$PATH

# Install Tini
RUN apt-get update \
    && apt-get install -y tini

# Install pip3
RUN apt-get update \
    && apt-get install -y python3-pip

# Install pip3 modules
RUN apt-get update \
    && pip3 install soco \
    && pip3 install pylint \
    && pip3 install --upgrade autopep8

COPY ./main.py .
 
CMD ["python3", "-u", "./main.py"]

# for testing:
# CMD ["sleep", "infinity"]