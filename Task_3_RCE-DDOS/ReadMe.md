# Cybersecurity Three-Stage Project

This repository contains the complete documentation and implementation of a **three-stage cybersecurity project**. Each stage has its own detailed report, source code, configuration, testing procedure, and evidence.

## Project Overview

### 🔹 Stage 1 — DDoS / Excessive-Traffic Detection & Mitigation

A Docker-based three-machine laboratory demonstrating:

* Secure file upload
* Excessive HTTP traffic detection
* IDS-style monitoring and alerting
* Rate limiting
* HTTP 429 mitigation
* Legitimate service availability after mitigation

### 🔹 Stage 2 — RCE + Distributed HTTP Traffic Detection & Mitigation

A VirtualBox-based security laboratory demonstrating:

* Controlled RCE
* Kali Linux, Ubuntu, Client 1 and Client 2
* Distributed HTTP traffic simulation
* Source-IP monitoring
* Threshold-based detection
* Alert generation
* Temporary source-IP blocking
* HTTP 429 mitigation

### 🔹 Stage 3 — SecureVault RCE & Secure File Upload

A Docker-based application security laboratory demonstrating:

* Insecure file upload
* PHP file execution
* Controlled Remote Code Execution
* Server-side command execution
* Security impact analysis
* RCE mitigation
* Secure file-upload architecture

## Overall Security Flow

```text
Stage 1
Traffic Detection & Mitigation
        ↓
Stage 2
RCE + Distributed Traffic + Mitigation
        ↓
Stage 3
SecureVault RCE Analysis + Secure Architecture
```

## Technologies

`Docker` · `Docker Compose` · `VirtualBox` · `Python` · `Flask` · `PHP` · `Apache` · `cURL` · `Linux`

## Purpose

The project demonstrates the progression from **security monitoring and traffic mitigation** to **RCE analysis and secure application design**, with all experiments performed in controlled laboratory environments.


> **Note:** The individual Stage 1, Stage 2, and Stage 3 folders contain the complete documentation and detailed implementation information for each stage.
