# apt update
# apt upgrade

# VSCODE 

# apt install build-essential
# apt install ./code.deb

# SSHD

# apt install openssh-server
# echo 'root:root' | chpasswd
# sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# /usr/sbin/sshd -D &

# 

docker run -it -p 8000:8000 -p 8022:22 -v ${PWD}/resources:/resources --rm ubuntu:24.10