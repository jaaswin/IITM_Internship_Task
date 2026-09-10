# DNS SERVER INSTALLATION, CONFIGURATION AND TESTING

## Internship Documentation Report

**P.G. Senapathy Centre for Computing Resources**
**Indian Institute of Technology Madras (IIT Madras)**

**Prepared by:** Jayaaswin M.
**Internship Year:** 2026

**Daily Internship Documentation Repository:**
[GitHub – IIT Madras Internship Repository](https://github.com/jaaswin/IIT_Madras_Internship?utm_source=chatgpt.com)

---

# 1. Introduction

As part of my internship at the **P.G. Senapathy Centre for Computing Resources, IIT Madras**, I worked on the installation, configuration and testing of a **DNS (Domain Name System) server** in a Linux environment.

DNS is an essential network service that translates human-readable domain names into IP addresses. This allows users to access network services using domain names instead of remembering numerical IP addresses.

The task provided practical exposure to DNS concepts, Linux-based network services, DNS configuration and client-side testing.

---

# 2. Objective

The main objectives of this task were:

* To understand the purpose and importance of DNS.
* To understand the DNS name-resolution process.
* To install a DNS server in a Linux environment.
* To configure the DNS service.
* To understand basic DNS configuration concepts.
* To test DNS resolution from a client system.
* To verify successful domain-name resolution using network testing commands.

---

# 3. What is DNS?

**DNS (Domain Name System)** is a distributed naming system used to translate domain names into IP addresses.

For example:

```text
www.example.com
       |
       v
   DNS Server
       |
       v
   IP Address
```

Humans can easily remember names such as:

```text
www.example.com
```

while computers use IP addresses for network communication.

DNS provides the translation between the domain name and its corresponding IP address.

---

# 4. Importance of DNS

Without DNS, users would have to remember the IP address of every website or network service they want to access.

DNS provides:

* Easy-to-remember domain names.
* Automatic name-to-IP address resolution.
* Centralized name management.
* Support for network services and applications.
* Efficient access to websites and other network resources.

Therefore, DNS is one of the fundamental services used in computer networks.

---

# 5. DNS Resolution Process

The basic DNS resolution process is:

```text
Client
   |
   | Requests www.example.com
   v
DNS Server
   |
   | Finds corresponding IP address
   v
IP Address
   |
   v
Destination Server
   |
   v
Network Communication
```

### Step-by-step process

1. The client requests a domain name.
2. The DNS resolver processes the request.
3. The DNS system searches for the corresponding IP address.
4. The IP address is returned to the client.
5. The client uses the IP address to communicate with the destination server.

---

# 6. DNS Server Environment

The DNS server was installed and configured in a **Linux environment**.

The overall setup was:

```text
+------------------+
|    DNS Server    |
|      Linux       |
+--------+---------+
         |
         | DNS Resolution
         |
+--------v---------+
|   Client Laptop  |
+------------------+
```

The client system was used to verify whether the configured DNS service could successfully resolve domain names.

---

# 7. DNS Server Installation

The DNS server software was installed on the Linux system.

The installation process included:

1. Updating the available package information.
2. Installing the required DNS server package.
3. Checking the DNS service.
4. Starting or enabling the DNS service.
5. Preparing the DNS configuration.
6. Verifying the configuration before testing.

The commands used during the actual installation and configuration were documented as part of the internship work.

---

# 8. DNS Configuration

After installation, the DNS server configuration was prepared.

The configuration process involved understanding:

* DNS server settings.
* Network interfaces.
* Client access.
* DNS forwarding.
* DNS zones.
* DNS records.
* Name-resolution behaviour.

Configuration files were checked carefully before testing the DNS service.

---

# 9. Important DNS Concepts Learned

## 9.1 Domain Name

A domain name is a human-readable name used to identify a website or network service.

Example:

```text
www.example.com
```

---

## 9.2 IP Address

An IP address identifies a device or service in an IP network.

Example:

```text
192.168.10.10
```

DNS can associate a domain name with its corresponding IP address.

---

## 9.3 DNS Record

DNS records store information related to a domain.

One commonly used record is an **A record**, which maps a domain name to an IPv4 address.

Example:

```text
www.example.com  →  192.168.10.10
```

---

## 9.4 DNS Resolver

A DNS resolver receives a DNS request from a client and obtains the required DNS information.

---

## 9.5 DNS Server

A DNS server processes DNS queries and provides DNS information to clients.

---

# 10. DNS Testing

After completing the installation and configuration, DNS resolution was tested from the client system.

The following command was used:

```text
ping www.example.com
```

The command output showed that the domain name was resolved to an IP address.

Example:

```text
Pinging www.example.com [IP Address] with 32 bytes of data:
Reply from IP Address: bytes=32 time=...
```

The appearance of the resolved IP address confirmed that DNS name resolution had taken place.

---

# 11. Testing Procedure

The DNS testing process followed these steps:

### Step 1: Open the client terminal

The client system terminal was opened.

### Step 2: Enter the domain name

The following command was executed:

```text
ping www.example.com
```

### Step 3: Observe DNS resolution

The system resolved:

```text
www.example.com
```

into its corresponding IP address.

### Step 4: Observe the response

The output displayed the resolved IP address and the response from the destination.

This confirmed that the client was able to perform DNS resolution successfully.

---

# 12. DNS Testing Flow

```text
Client Laptop
      |
      | ping www.example.com
      v
DNS Resolution
      |
      v
Domain Name
www.example.com
      |
      v
Resolved IP Address
      |
      v
Destination Server
      |
      v
Reply Received
```

---

# 13. Observation

During testing, the `ping` command displayed the resolved IP address for the requested domain.

The observed flow was:

```text
Domain Name
     ↓
DNS Resolution
     ↓
IP Address
     ↓
Network Communication
     ↓
Reply
```

This confirmed that the DNS resolution process was functioning correctly from the client system.

---

# 14. Learning Outcomes

Through this task, I learned:

* The purpose and importance of DNS.
* How DNS translates domain names into IP addresses.
* The basic DNS resolution process.
* How to install DNS server software in Linux.
* Basic DNS server configuration.
* The purpose of DNS records.
* The difference between domain names and IP addresses.
* How to test DNS resolution from a client system.
* How `ping` can be used to observe DNS resolution.
* The importance of DNS in network infrastructure.
* The relationship between DNS and other network services such as DHCP.

---

# 15. DNS and DHCP Relationship

During the internship, both DHCP and DNS were studied.

They perform different but related functions.

| Feature       | DHCP                                | DNS                        |
| ------------- | ----------------------------------- | -------------------------- |
| Full Form     | Dynamic Host Configuration Protocol | Domain Name System         |
| Main Purpose  | Provides network configuration      | Resolves domain names      |
| Example       | Assigns an IP address to a client   | Resolves `www.example.com` |
| Main Function | IP configuration                    | Name resolution            |

### Simple Relationship

```text
DHCP
  |
  | Provides network configuration
  v
Client
  |
  | Requests domain
  v
DNS
  |
  | Resolves domain
  v
IP Address
```

---

# 16. Practical Workflow

The complete DNS task was carried out through the following stages:

```text
DNS Server Installation
          |
          v
DNS Configuration
          |
          v
Service Verification
          |
          v
Client Configuration
          |
          v
DNS Resolution Test
          |
          v
Ping Test
          |
          v
Successful DNS Resolution
```

---

# 17. Result

The **DNS Server Installation, Configuration and Testing** task was completed successfully.

The DNS service was tested from the client system using:

```text
ping www.example.com
```

The domain name was successfully resolved to an IP address, confirming that DNS name resolution was functioning correctly.

### Status: COMPLETED

---

# 18. Skills and Knowledge Gained

This task improved my practical knowledge in:

### Networking

* DNS
* IP addressing
* Domain names
* Name resolution
* Client-server communication

### Linux

* Linux network services
* Service management
* Configuration files
* Network testing commands

### DNS Administration

* DNS installation
* DNS configuration
* DNS records
* DNS resolution
* Client-side testing

### Troubleshooting

* Checking DNS resolution
* Observing command output
* Verifying network communication
* Identifying whether a domain is successfully resolved

---

# 19. Documentation and GitHub Repository

The daily internship work, reports and related documentation are maintained in my GitHub repository:

**IIT Madras Internship Repository**

[github.com/jaaswin/IIT_Madras_Internship](https://github.com/jaaswin/IIT_Madras_Internship?utm_source=chatgpt.com)

The repository is used to maintain the internship documentation in an organized manner, including daily work and technical reports.

The DNS server report is included as part of the internship documentation to maintain a record of the work completed during the internship.

---

# 20. Overall Outcome

This task provided practical experience in **DNS server installation, configuration and testing** in a Linux networking environment.

I developed a clear understanding of how DNS translates human-readable domain names into IP addresses and how a client communicates with a DNS service during name resolution.

The successful test using:

```text
ping www.example.com
```

provided practical confirmation of DNS resolution.

The task strengthened my understanding of **Linux networking, DNS services, network troubleshooting and client-server communication**.

---

# 21. Conclusion

The DNS Server Installation, Configuration and Testing task was successfully completed.

The task helped me move from theoretical understanding of DNS to practical implementation and testing in a Linux environment. I learned how DNS supports network communication by translating domain names into IP addresses and how to verify DNS functionality from a client system.

This experience also helped me understand the relationship between **DHCP and DNS**, two important services in network infrastructure.

The completed work and daily internship documentation are maintained in the **IIT Madras Internship GitHub repository** for reference and future learning.

### Final Status: COMPLETED
