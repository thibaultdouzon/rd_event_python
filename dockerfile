FROM ubuntu:24.10

RUN apt update && apt upgrade -y
RUN apt install -y build-essential openssh-server curl

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
