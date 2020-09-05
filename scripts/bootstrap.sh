#!/usr/bin/env bash

# set -o xtrace
set -o errexit
set -o nounset
set -o pipefail

apt update
apt dist-upgrade -y

apt install -y nginx
apt install -y sqlite3

apt install -y python3-pip python3-dev python3-setuptools
apt install -y build-essential libssl-dev libffi-dev
