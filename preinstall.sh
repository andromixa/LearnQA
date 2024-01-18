#!/bin/bash

# Run script using sudo

apt-get update

# Uninstall all old versions and corresponding data
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
apt-get -y purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
rm -rf /var/lib/docker
rm -rf /var/lib/containerd

# Install GIT
apt-get install -y git

# Create dir for repository
cd $HOME
mkdir ./tests_repos
cd ./tests_repos

# Clone repo in created directory
git clone https://github.com/andromixa/LearnQA.git

# Install docker
apt-get install -y docker.io docker-compose
groupadd docker
usermod -aG docker $USER

# Reboot workstation
reboot

# To run tests go to tests directory and use: docker-compose up --build
