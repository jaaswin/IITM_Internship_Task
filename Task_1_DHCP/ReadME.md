# TASK 1

## DHCP Configuration, Reservation, Migration and Automation

### Internship Documentation Report

**P.G. Senapathy Centre for Computing Resources**
**Indian Institute of Technology Madras (IIT Madras)**

**Prepared by:** Jayaaswin M.
**Internship Year:** 2026

**Daily Internship Documentation Repository:**
https://github.com/jaaswin/IIT_Madras_Internship

---

# 1. Introduction

As part of my internship at the **P.G. Senapathy Centre for Computing Resources, IIT Madras**, Task 1 focused on understanding and implementing **DHCP (Dynamic Host Configuration Protocol)**.

The task was completed in multiple phases, starting with basic DHCP server installation and configuration, followed by MAC-based IP reservation using ISC DHCP, and finally migration to **Kea DHCP** with an automated reservation workflow.

This task provided practical knowledge of **IP address allocation, MAC addresses, DHCP configuration, IP reservation, DHCP migration, APIs and automation**.

---

# 2. Objective

The main objectives of Task 1 were:

* To understand the purpose of DHCP.
* To install and configure a DHCP server.
* To understand automatic IP address allocation.
* To test DHCP operation using a client system.
* To configure MAC-based IP reservation.
* To understand the limitations of the existing ISC DHCP setup.
* To study migration from ISC DHCP to Kea DHCP.
* To understand the Kea Control Agent and API.
* To automate DHCP reservation using a structured data source and Python.

---

# 3. What is DHCP?

**DHCP (Dynamic Host Configuration Protocol)** is a network protocol used to automatically provide network configuration information to client devices.

A DHCP server can provide information such as:

* IP address
* Subnet mask
* Default gateway
* DNS server

Instead of manually configuring an IP address on every client, DHCP can assign the required network information automatically.

---

# 4. Importance of DHCP

DHCP simplifies network administration by automatically assigning network configuration to client devices.

It helps to:

* Reduce manual IP configuration.
* Avoid duplicate IP addresses.
* Manage IP address ranges.
* Provide gateway information.
* Provide DNS server information.
* Reserve specific IP addresses for selected devices.

DHCP is therefore an important service in managed computer networks.

---

# 5. DHCP Working Process

The basic DHCP process can be represented as:

```text
Client
   |
   | DHCP Discover
   v
DHCP Server
   |
   | DHCP Offer
   v
Client
   |
   | DHCP Request
   v
DHCP Server
   |
   | DHCP ACK
   v
Client receives IP configuration
```

The four main steps are commonly known as:

```text
DORA

Discover
Offer
Request
Acknowledgement
```

---

# 6. Task Structure

Task 1 was completed in three phases:

```text
TASK 1: DHCP
     |
     +----------------------+
     |                      |
     v                      v
Phase 1                 Phase 2
DHCP Setup              ISC DHCP
& Testing               IP Reservation
     |                      |
     +----------+-----------+
                |
                v
             Phase 3
          Kea DHCP Migration
          & Automation
```

---

# 7. Phase 1: DHCP Installation, Configuration and Testing

## 7.1 Objective

The first phase focused on setting up a DHCP server and testing automatic IP address assignment.

The main activities were:

* DHCP server installation.
* DHCP configuration.
* Definition of the DHCP subnet.
* Configuration of the IP address range.
* Configuration of gateway and DNS information.
* Connecting a client system.
* Testing automatic IP assignment.

---

## 7.2 DHCP Network Configuration

The DHCP test configuration used the following network details:

```text
Subnet       : 192.168.10.0/24
IP Range     : 192.168.10.100 - 192.168.10.200
Gateway      : 192.168.10.1
DNS Servers  : 8.8.8.8, 1.1.1.1
Interface    : enp0s3
```

The configuration defined the network from which client devices could obtain IP addresses.

---

## 7.3 DHCP Configuration Structure

The configuration can be represented as:

```text
DHCP Server
     |
     +-- Network: 192.168.10.0/24
     |
     +-- IP Range: 192.168.10.100-200
     |
     +-- Gateway: 192.168.10.1
     |
     +-- DNS: 8.8.8.8, 1.1.1.1
     |
     +-- Interface: enp0s3
```

---

## 7.4 DHCP Testing

After configuration, the client system was connected to the DHCP test network.

The client requested network configuration from the DHCP server.

The DHCP server successfully assigned an IP address from the configured range.

This confirmed that the basic DHCP configuration was working.

---

# 8. Phase 2: ISC DHCP MAC-Based IP Reservation

## 8.1 Objective

The second phase focused on **IP address reservation** using ISC DHCP.

Normally, DHCP assigns an available IP address from a configured pool.

For some devices, however, it may be useful to provide the same IP address every time the device connects.

This can be achieved using the device's **MAC address**.

---

## 8.2 What is DHCP Reservation?

DHCP reservation associates a specific device's MAC address with a specific IP address.

The basic concept is:

```text
MAC Address
     |
     v
DHCP Server
     |
     v
Reserved IP Address
```

For example:

```text
Client MAC Address
        |
        v
192.168.10.10
```

When the same client requests an IP address, the DHCP server can provide the reserved address.

---

## 8.3 MAC Address

A **MAC address (Media Access Control address)** is a hardware-level address associated with a network interface.

Example format:

```text
AA:BB:CC:DD:EE:FF
```

The MAC address can be used by the DHCP server to identify a particular client.

---

## 8.4 Reservation Process

The reservation process involved:

1. Identifying the client's MAC address.
2. Adding the MAC address to the DHCP configuration.
3. Assigning a fixed IP address to that client.
4. Applying the updated DHCP configuration.
5. Renewing the client's DHCP lease.
6. Verifying the assigned IP address.

The reservation was successfully tested.

**Status:** Completed

**Date:** 07/09/2026

---

# 9. Phase 3: Kea DHCP Migration and Automation

## 9.1 Objective

The third phase focused on understanding the migration from **ISC DHCP to Kea DHCP** and developing an automated DHCP reservation workflow.

The work was divided into two stages:

```text
Phase 3
   |
   +-----------------------------+
   |                             |
   v                             v
Migration                     Automation
ISC DHCP → Kea                DHCP Reservation
```

---

# 10. ISC DHCP to Kea DHCP Migration

**ISC DHCP** was the existing DHCP implementation studied during the earlier phases.

**Kea DHCP** is a newer DHCP server implementation designed with a modular architecture and API-based management capabilities.

The migration involved understanding how DHCP configuration and reservation information can be moved from the ISC DHCP environment to Kea DHCP.

The migration workflow was studied as:

```text
ISC DHCP
    |
    | Migration
    v
Kea DHCP
    |
    v
Kea Configuration
    |
    v
DHCP Service
```

---

# 11. Difference Between ISC DHCP and Kea DHCP

| Feature           | ISC DHCP                   | Kea DHCP                       |
| ----------------- | -------------------------- | ------------------------------ |
| Architecture      | Traditional DHCP server    | Modern modular architecture    |
| Configuration     | Configuration files        | Configuration files and APIs   |
| Automation        | More manual                | Better suited for automation   |
| API Support       | Limited compared with Kea  | Strong API support             |
| Control           | Mainly configuration based | Configuration + Control Agent  |
| Future Management | Older implementation       | Designed for modern management |

The comparison helped in understanding why migration to Kea can be useful for modern DHCP management and automation.

---

# 12. Kea Control Agent

The **Kea Control Agent** provides an interface for interacting with Kea DHCP services.

It allows management operations to be performed through an API.

The basic concept is:

```text
Automation Script
       |
       | API Request
       v
Kea Control Agent
       |
       v
Kea DHCP Server
       |
       v
DHCP Configuration / Reservation
```

This provides a foundation for automating DHCP management tasks.

---

# 13. Automated DHCP Reservation

The next stage was to automate the process of adding DHCP reservations.

Instead of manually entering each reservation into a configuration file, reservation information was maintained in a structured data source.

The workflow used:

```text
Google Sheets / CSV
        |
        v
Python Script
        |
        v
Kea API
        |
        v
Kea DHCP Server
        |
        v
DHCP Reservation
```

---

# 14. Why CSV / Structured Data Was Used

A structured data file provides an organized way to store reservation information.

For example:

```text
MAC Address        IP Address
AA:BB:CC:DD:EE:FF  192.168.10.10
11:22:33:44:55:66  192.168.10.11
```

This makes it easier to:

* Store multiple reservations.
* Modify reservation information.
* Process data using Python.
* Reduce manual configuration.
* Use the same data for automation.

---

# 15. Python Automation

Python was used as part of the automation workflow.

The basic process was:

```text
Read Reservation Data
        |
        v
Process MAC + IP Information
        |
        v
Create API Request
        |
        v
Send Request to Kea
        |
        v
Create / Update Reservation
```

This demonstrated how programming can be integrated with network administration tasks.

---

# 16. Complete Task 1 Workflow

The complete DHCP task can be represented as:

```text
DHCP Installation
        |
        v
DHCP Configuration
        |
        v
Client IP Assignment
        |
        v
ISC DHCP Reservation
        |
        v
Reservation Testing
        |
        v
Migration to Kea DHCP
        |
        v
Kea Control Agent
        |
        v
Python Automation
        |
        v
Automated DHCP Reservation
```

---

# 17. Practical Skills Learned

During Task 1, I gained practical knowledge of:

* DHCP server setup.
* IP address allocation.
* Subnet configuration.
* Gateway configuration.
* DNS configuration within DHCP.
* MAC address identification.
* DHCP reservations.
* Lease renewal and testing.
* ISC DHCP.
* Kea DHCP.
* Kea Control Agent.
* REST/API-based management.
* Python-based network automation.
* Structured data handling using CSV/Google Sheets.

---

# 18. Learning Outcome

This task helped me understand how DHCP works in a practical network environment rather than only from a theoretical perspective.

I learned how a DHCP server can automatically provide network configuration to clients and how specific devices can receive reserved IP addresses.

The migration and automation phase also introduced me to the use of **APIs and Python for network management**, showing how repetitive network administration tasks can be automated.

---

# 19. Result

The DHCP task was completed successfully through the following stages:

### Phase 1

**DHCP Installation, Configuration and Testing**

Basic DHCP operation was configured and tested successfully.

### Phase 2

**ISC DHCP MAC-Based IP Reservation**

A specific client's MAC address was associated with a reserved IP address and tested successfully.

### Phase 3

**Kea DHCP Migration and Automation**

The migration from ISC DHCP to Kea DHCP and the automated DHCP reservation workflow were studied and implemented as part of the internship task.

**Overall Status: Completed**

---

# 20. GitHub Documentation

The reports and daily internship updates are maintained in the internship GitHub repository.

The documentation is organized according to the internship days and includes the work completed during each day.

The repository is used to maintain:

* Daily internship reports.
* Task documentation.
* Configuration details.
* Testing observations.
* Screenshots.
* Technical learning.
* Task progress.

---

# 21. Conclusion

Task 1 provided practical exposure to DHCP server administration, IP address management and network automation.

The task progressed from basic DHCP configuration to MAC-based IP reservation and finally to Kea DHCP migration and automated reservation.

Through this work, I gained a better understanding of how DHCP services are configured, tested and managed in a network environment, as well as how automation can reduce repetitive administrative work.

**Task 1: DHCP Configuration, Reservation, Migration and Automation was completed successfully.**
