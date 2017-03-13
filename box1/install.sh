#!/bin/bash

# Pre-requisites
sudo apt-get install python-pip python-bcrypt python-dev
sudo pip install flask flask_restful

# Create the level 1 database
python level1_db.py

# Create the level 2 password file
python level2_secrets.py

# Copy service files
sudo cp box1_splash.service box1_level1.service box1_level2.service /etc/systemd/system
sudo systemctl daemon-reload

sudo cp puzzlebox /etc/sudoers.d/
sudo chown root /etc/sudoers.d/puzzlebox
sudo chgrp root /etc/sudoers.d/puzzlebox

# Splash should be started
sudo systemctl enable box1_splash.service
sudo systemctl start box1_splash.service

# Level 1 should be started
sudo systemctl enable box1_level1.service
sudo systemctl start box1_level1.service

# Level 2 should be stopped
sudo systemctl disable box1_level1.service
sudo systemctl stop box1_level1.service