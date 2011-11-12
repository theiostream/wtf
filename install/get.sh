#!/bin/sh

git clone git://github.com/theiostream/wtf.git

cd wtf/install
chmod 755 ./install.py
sudo ./install.py

sudo rm -rf ./wtf