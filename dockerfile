FROM ubuntu:24.10

RUN apt update && apt upgrade -y
RUN apt install -y build-essential openssh-server curl libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl git \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

COPY resources /resources


# install vscode for remote server
RUN echo "8 37" | apt install -y ./resources/code.deb

# open ssh server
EXPOSE 22
RUN echo "root:root" | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN mkdir /root/dev
WORKDIR /root/dev

EXPOSE 8000

CMD ["/bin/bash"]
