#!/bin/bash

# ============================================================
# TASK 2 - DNS SERVER INSTALLATION, CONFIGURATION & TESTING
# IIT Madras Computer Centre Internship - 2026
# ============================================================


# ============================================================
# 1. UPDATE UBUNTU PACKAGE INFORMATION
# ============================================================

# Updates the list of available software packages.
sudo apt update


# ============================================================
# 2. INSTALL DNS SERVER
# ============================================================

# Installs the BIND9 DNS server package.
sudo apt install bind9


# ============================================================
# 3. CHECK DNS SERVICE STATUS
# ============================================================

# Checks whether the BIND9 DNS service is running.
sudo systemctl status bind9


# ============================================================
# 4. START DNS SERVICE
# ============================================================

# Starts the DNS server service.
sudo systemctl start bind9


# ============================================================
# 5. ENABLE DNS SERVICE
# ============================================================

# Makes the DNS service start automatically when the system boots.
sudo systemctl enable bind9


# ============================================================
# 6. CHECK DNS CONFIGURATION
# ============================================================

# Checks the main BIND DNS configuration for syntax errors.
sudo named-checkconf


# ============================================================
# 7. VIEW DNS CONFIGURATION
# ============================================================

# Opens the main DNS configuration file.
sudo nano /etc/bind/named.conf


# Opens the local DNS configuration file.
sudo nano /etc/bind/named.conf.local


# Opens the DNS options configuration.
sudo nano /etc/bind/named.conf.options


# ============================================================
# 8. DNS SERVICE RESTART
# ============================================================

# Restarts BIND9 after making configuration changes.
sudo systemctl restart bind9


# Checks whether the DNS service is running correctly.
sudo systemctl status bind9


# ============================================================
# 9. CHECK DNS SERVER PORT
# ============================================================

# Displays services listening on network ports.
# DNS normally uses port 53.
sudo ss -tulpn | grep :53


# ============================================================
# 10. CHECK SERVER IP ADDRESS
# ============================================================

# Displays the IP addresses assigned to network interfaces.
ip addr


# Displays the routing table.
ip route


# ============================================================
# 11. DNS TESTING USING NSLOOKUP
# ============================================================

# Tests DNS name resolution for example.com.
nslookup www.example.com


# Tests DNS name resolution using the configured DNS server.
# Replace DNS_SERVER_IP with the actual DNS server IP.
nslookup www.example.com DNS_SERVER_IP


# ============================================================
# 12. DNS TESTING USING DIG
# ============================================================

# Queries the DNS server for the domain name.
dig www.example.com


# Displays a shorter DNS query result.
dig +short www.example.com


# Query a specific DNS server.
# Replace DNS_SERVER_IP with the actual DNS server IP.
dig @DNS_SERVER_IP www.example.com


# ============================================================
# 13. CLIENT-SIDE DNS TESTING
# ============================================================

# Tests whether the client can resolve www.example.com
# and communicate with the resolved address.
ping www.example.com


# ============================================================
# 14. CHECK DNS RESOLVER CONFIGURATION
# ============================================================

# Displays the current DNS resolver configuration.
resolvectl status


# Displays the DNS resolver configuration file.
cat /etc/resolv.conf


# ============================================================
# 15. RESTART NETWORK/DNS RESOLVER IF REQUIRED
# ============================================================

# Restarts the system DNS resolver.
sudo systemctl restart systemd-resolved


# ============================================================
# 16. FINAL DNS SERVICE CHECK
# ============================================================

# Confirms that BIND9 is active after configuration and testing.
sudo systemctl status bind9


# ============================================================
# TEST RESULT
# ============================================================

# The following command was used for the final client-side test:
#
# ping www.example.com
#
# The output displayed the resolved IP address for
# www.example.com and received replies from the destination.
#
# This confirmed successful DNS name resolution from
# the client system.
#
# ============================================================
# END OF TASK 2
# ============================================================