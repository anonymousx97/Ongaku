#!/usr/bin/env bash

apt update
apt dist-upgrade -y
apt update

apt install -y git nano python python-pip termux-api

chmod -w /data/data/com.termux/files/usr/libexec/termux-am/am.apk

git clone https://github.com/anonymousx97/Ongaku

cd Ongaku

sed -i "s%ongaku_workdir=.*%ongaku_workdir=$(pwd)%" "scripts/ong"

cp "scripts/ong" "${PATH}"

pip install virtualenv
virtualenv venv --system-site-packages
source venv/bin/activate

pip install git+https://github.com/thedragonsinn/ub-core

while true; do
    echo -e "Config.Env Setup.\n• Enter 1 to start.\n• Enter 2 if you already have a config prepared."
    read -r input

    [[ $input -eq 1 ]] && ./scripts/create_client.py && break
    [[ $input -eq 2 ]] && break

done

deactivate

termux-notification-list
