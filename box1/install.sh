#!/bin/sh

# Pre-requisites
sudo apt-get install python-pip python-bcrypt
sudo pip install flask

# Create the level 1 database
python level1_db.py

# Copy service files
sudo cp box1_splash.service box1_level1.service box1_level2.service /etc/systemd/system
sudo systemctl daemon-reload

# Splash should be started
sudo systemctl enable box1_splash.service
sudo systemctl start box1_splash.service

# Level 1 should be started
sudo systemctl enable box1_level1.service
sudo systemctl start box1_level1.service

# Level 2 should be stopped
sudo systemctl disable box1_level1.service
sudo systemctl stop box1_level1.service