#!/bin/bash

# ============================================================
# TASK 1 - DHCP CONFIGURATION, RESERVATION AND AUTOMATION
# IIT Madras Computer Centre Internship - 2026
# ============================================================


# ============================================================
# PHASE 1 - DHCP INSTALLATION, CONFIGURATION AND TESTING
# ============================================================

# Update Ubuntu package information
sudo apt update

# Install ISC DHCP Server
sudo apt install isc-dhcp-server

# Check the DHCP server service status
sudo systemctl status isc-dhcp-server

# Start the DHCP server
sudo systemctl start isc-dhcp-server

# Enable DHCP server to start automatically at boot
sudo systemctl enable isc-dhcp-server

# Check network interfaces
ip addr

# Display detailed network interface information
ip link


# ============================================================
# DHCP CONFIGURATION
# ============================================================

# Open the DHCP configuration file
sudo nano /etc/dhcp/dhcpd.conf

# Example DHCP configuration:
#
# subnet 192.168.10.0 netmask 255.255.255.0 {
#     range 192.168.10.100 192.168.10.200;
#     option routers 192.168.10.1;
#     option domain-name-servers 8.8.8.8, 1.1.1.1;
# }


# Specify the network interface used by DHCP
sudo nano /etc/default/isc-dhcp-server

# Example:
#
# INTERFACESv4="enp0s3"


# Restart DHCP service after configuration changes
sudo systemctl restart isc-dhcp-server

# Check DHCP service status
sudo systemctl status isc-dhcp-server


# ============================================================
# DHCP TESTING
# ============================================================

# Display the client's network configuration
ip addr

# Display routing information
ip route

# Release the current DHCP lease
sudo dhclient -r

# Request a new DHCP lease
sudo dhclient

# Check the assigned IP address
ip addr

# Test network connectivity
ping 192.168.10.1


# ============================================================
# PHASE 2 - ISC DHCP MAC-BASED IP RESERVATION
# ============================================================

# Display network interfaces and MAC addresses
ip link

# Display detailed interface information
ip addr

# Open the DHCP configuration file
sudo nano /etc/dhcp/dhcpd.conf


# Example MAC-based DHCP reservation:
#
# host laptop {
#     hardware ethernet XX:XX:XX:XX:XX:XX;
#     fixed-address 192.168.10.10;
# }


# Restart DHCP after adding the reservation
sudo systemctl restart isc-dhcp-server

# Check DHCP service status
sudo systemctl status isc-dhcp-server

# Release the existing DHCP lease
sudo dhclient -r

# Request a new DHCP lease
sudo dhclient

# Verify the assigned IP address
ip addr


# ============================================================
# PHASE 3 - KEA DHCP MIGRATION
# ============================================================

# Update package information
sudo apt update

# Install Kea DHCP server packages
sudo apt install kea-dhcp4-server

# Check Kea DHCP service
sudo systemctl status kea-dhcp4-server

# Start Kea DHCP service
sudo systemctl start kea-dhcp4-server

# Enable Kea DHCP service
sudo systemctl enable kea-dhcp4-server

# Open the Kea DHCP configuration
sudo nano /etc/kea/kea-dhcp4.conf


# Validate the Kea configuration
sudo kea-dhcp4 -t -c /etc/kea/kea-dhcp4.conf

# Restart Kea DHCP service
sudo systemctl restart kea-dhcp4-server

# Check Kea service status
sudo systemctl status kea-dhcp4-server


# ============================================================
# KEA CONTROL AGENT
# ============================================================

# Check the Kea Control Agent service
sudo systemctl status kea-ctrl-agent

# Start the Kea Control Agent
sudo systemctl start kea-ctrl-agent

# Enable the Control Agent
sudo systemctl enable kea-ctrl-agent

# Restart the Control Agent after configuration changes
sudo systemctl restart kea-ctrl-agent

# Check Control Agent status
sudo systemctl status kea-ctrl-agent


# ============================================================
# KEA API TESTING
# ============================================================

# Test communication with the Kea Control Agent
curl -X POST \
-H "Content-Type: application/json" \
-d '{"command":"list-commands","service":["dhcp4"]}' \
http://127.0.0.1:8000/


# ============================================================
# PHASE 3 - DHCP RESERVATION AUTOMATION
# ============================================================

# Check Python version
python3 --version

# Check whether pip is available
pip3 --version

# Create a Python virtual environment if required
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required Python package if used
pip install requests


# ============================================================
# CSV RESERVATION DATA
# ============================================================

# Example CSV structure:
#
# MAC Address,IP Address
# AA:BB:CC:DD:EE:FF,192.168.10.10
# 11:22:33:44:55:66,192.168.10.11


# ============================================================
# RUN DHCP AUTOMATION SCRIPT
# ============================================================

# Run the Python automation script
python3 dhcp_automation.py


# ============================================================
# VERIFY AUTOMATED RESERVATION
# ============================================================

# Check network interface information
ip addr

# Release the current DHCP lease
sudo dhclient -r

# Request a new DHCP lease
sudo dhclient

# Verify the assigned IP address
ip addr

# Test network connectivity
ping 192.168.10.1


# ============================================================
# END OF TASK 1
# ============================================================
#
# Phase 1: DHCP Installation, Configuration and Testing
# Phase 2: ISC DHCP MAC-Based IP Reservation
# Phase 3: Kea DHCP Migration and Automated Reservation
#
# ============================================================