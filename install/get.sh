#!/bin/sh

git clone git://git.github.com/theiostream/wtf.git

chmod 755 ./install.py
sudo ./install.py

sudo rm -rf ../../wtf