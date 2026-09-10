```python
"""
============================================================
TASK 1 - DHCP RESERVATION AUTOMATION
IIT Madras Computer Centre Internship - 2026
============================================================

Purpose:
    This Python program demonstrates the automation workflow
    for adding DHCP reservations to a Kea DHCP server.

Workflow:
    CSV / Reservation Data
            |
            v
       Python Script
            |
            v
       Kea Control Agent
            |
            v
         Kea DHCP
            |
            v
     DHCP Reservation

Main technologies used:
    - Python
    - CSV
    - HTTP/REST API
    - Kea DHCP
    - Kea Control Agent

Note:
    Replace the example MAC address and IP address with the
    actual reservation information used in the test environment.
============================================================
"""

# ------------------------------------------------------------
# IMPORT REQUIRED MODULES
# ------------------------------------------------------------

# csv is used to read MAC address and IP address information
# from a CSV file.
import csv

# requests is used to send HTTP requests to the Kea
# Control Agent API.
import requests


# ------------------------------------------------------------
# KEA CONTROL AGENT SETTINGS
# ------------------------------------------------------------

# Address of the Kea Control Agent.
# Port 8000 is commonly used by the Control Agent.
KEA_API_URL = "http://127.0.0.1:8000/"


# ------------------------------------------------------------
# CSV FILE
# ------------------------------------------------------------

# This file contains the DHCP reservation information.
#
# Example:
#
# MAC Address,IP Address
# AA:BB:CC:DD:EE:FF,192.168.10.10
#
CSV_FILE = "dhcp_reservations.csv"


# ------------------------------------------------------------
# FUNCTION: READ RESERVATION DATA
# ------------------------------------------------------------

def read_reservations():
    """
    Reads DHCP reservation information from the CSV file.

    The CSV file contains:
        - MAC address
        - IP address

    Returns:
        A list containing reservation information.
    """

    reservations = []

    # Open the CSV file in read mode.
    with open(CSV_FILE, "r", newline="") as file:

        # DictReader reads each row using the column names.
        reader = csv.DictReader(file)

        # Process each reservation in the CSV file.
        for row in reader:

            mac_address = row["MAC Address"].strip()
            ip_address = row["IP Address"].strip()

            reservations.append({
                "hw-address": mac_address,
                "ip-address": ip_address
            })

    return reservations


# ------------------------------------------------------------
# FUNCTION: CREATE KEA RESERVATION
# ------------------------------------------------------------

def create_reservation(reservation):
    """
    Sends a reservation request to the Kea DHCP Control Agent.

    The reservation contains:
        - MAC address of the client
        - IP address to be reserved

    The Control Agent forwards the command to Kea DHCP.
    """

    # Create the API request.
    payload = {
        "command": "reservation-add",
        "service": ["dhcp4"],

        "arguments": {
            "subnet-id": 1,
            "reservation": reservation
        }
    }

    # Send the request to the Kea Control Agent.
    response = requests.post(
        KEA_API_URL,
        json=payload,
        timeout=10
    )

    # Check the HTTP response.
    if response.status_code == 200:

        print("Reservation request sent successfully.")

        # Display the response returned by Kea.
        print("Kea Response:")
        print(response.text)

    else:

        print("Failed to send reservation request.")
        print("HTTP Status:", response.status_code)
        print("Response:", response.text)


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

def main():
    """
    Main function of the DHCP automation program.

    Steps:
        1. Read reservation information from CSV.
        2. Process each reservation.
        3. Send each reservation to Kea through the API.
    """

    print("==============================================")
    print(" DHCP RESERVATION AUTOMATION")
    print("==============================================")

    print("\nReading reservation data...")

    # Read reservation information from the CSV file.
    reservations = read_reservations()

    print("Number of reservations:", len(reservations))

    # Process each reservation.
    for reservation in reservations:

        print("\n----------------------------------------------")
        print("MAC Address:", reservation["hw-address"])
        print("Reserved IP:", reservation["ip-address"])
        print("----------------------------------------------")

        # Send reservation to Kea.
        create_reservation(reservation)

    print("\nAutomation process completed.")


# ------------------------------------------------------------
# PROGRAM ENTRY POINT
# ------------------------------------------------------------

# This ensures that main() runs only when this file is
# executed directly.
if __name__ == "__main__":
    main()


"""
============================================================
EXPLANATION OF THE AUTOMATION
============================================================

1. CSV FILE
-----------
The reservation information is stored in a CSV file.

Example:

MAC Address,IP Address
AA:BB:CC:DD:EE:FF,192.168.10.10

The CSV file makes it easy to maintain multiple
DHCP reservations.

2. PYTHON
---------
Python reads the reservation information from the CSV file.

3. API REQUEST
--------------
Python creates an HTTP request containing the MAC address
and reserved IP address.

4. KEA CONTROL AGENT
--------------------
The request is sent to the Kea Control Agent.

5. KEA DHCP SERVER
------------------
The Control Agent communicates with the Kea DHCP service.

6. RESERVATION
--------------
Kea processes the request and creates the DHCP reservation
for the specified client.

============================================================
WHY AUTOMATION IS USED
============================================================

Manual DHCP reservation requires an administrator to edit
configuration information for every device.

Automation reduces repetitive manual work.

Instead of:

    MAC Address
         |
         v
    Manually edit
    configuration
         |
         v
    Restart / update
    DHCP service

The automated process becomes:

    CSV / Google Sheets
             |
             v
        Python Script
             |
             v
       Kea Control API
             |
             v
        DHCP Reservation

============================================================
IMPORTANT
============================================================

The subnet ID, API URL, CSV column names and Kea API
command must match the actual Kea configuration used in
the internship test environment.

This file is intended as the documented automation script
for Task 1, Phase 3.
============================================================
"""
```

### Supporting CSV file

Keep the data separately as:

`dhcp_reservations.csv`

```csv
MAC Address,IP Address
AA:BB:CC:DD:EE:FF,192.168.10.10
11:22:33:44:55:66,192.168.10.11
```

So your **Phase 3 GitHub folder** can look like:

```text
DAY_08/
│
├── Kea_DHCP_Migration_Report.pdf
├── dhcp_automation.py
├── dhcp_reservations.csv
├── kea-dhcp4.conf
└── screenshots/
```

**Important:** The exact Kea API payload depends on how your Kea server and subnet are configured. Before actually running this script, replace the example MAC/IP values and verify the `subnet-id` and API endpoint against your working configuration.
