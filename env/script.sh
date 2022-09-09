#!/usr/bin/env bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get install -y zlib1g-dev build-essential libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev python-dev python-setuptools python-pip python-smbus openssl libffi-dev

# Install python 3.8.3
cd /opt
sudo wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz

sudo tar xzf Python-3.8.3.tgz
cd Python-3.8.3
sudo ./configure --enable-optimizations
sudo make altinstall

sudo apt-get install -y libssl-dev curl python3-pip

