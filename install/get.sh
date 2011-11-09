#!/bin/sh

git clone git://github.com/theiostream/wtf.git

chmod 755 ./wtf/install/install.py
sudo ./wtf/install/install.py

sudo rm -rf ./wtf