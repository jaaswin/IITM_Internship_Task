
# STAGE 1 — FULL DETAILED PROJECT REPORT  
## DDoS / Excessive-Traffic Detection and Secure File-Upload System

**Organization:** P.G. Senapathy Centre for Computing Resources, IIT Madras  
**Project Type:** Docker-Based Cyber Security Demonstration  
**Stage:** Stage 1 — Controlled Excessive-Traffic Detection, Alerting, Mitigation and Availability Verification  
**Technologies:** Docker, Docker Compose, Python 3.12, Flask, Flask-Limiter, cURL  
**Network:** Private Docker Bridge Network  
**Machines:** 3 Docker containers  
**Application:** HTTP File Upload Service  

The uploaded Stage 1 documentation describes a controlled three-machine security laboratory in which a legitimate client, a controlled traffic generator, and a protected file-upload server are separated into Docker containers. The objective is to demonstrate the complete sequence of **normal operation → excessive traffic → detection → alert → mitigation → recovery/availability verification**. fileciteturn0file0L13-L26

---

# 1. EXECUTIVE SUMMARY

Stage 1 was developed to demonstrate how an HTTP file-upload service can detect and control abnormal or excessive upload traffic without completely stopping the service.

The implementation uses three Docker containers:

- **Machine 1 — Legitimate Client**
- **Machine 2 — Controlled Traffic Generator**
- **Machine 3 — Protected Server + IDS Monitoring**

All three machines communicate through a private Docker bridge network. Machine 1 performs normal file uploads, while Machine 2 generates repeated upload requests. Machine 3 receives the requests, monitors their frequency, generates an IDS-style alert when the configured threshold is reached, and applies application-level rate limiting to excessive requests. fileciteturn0file0L69-L93

The detection mechanism monitors requests to the `/upload` endpoint. The configured monitoring threshold is **5 requests within 60 seconds**. Flask-Limiter is configured for **5 requests per minute per client**. Once additional requests exceed the allowed rate, the application returns **HTTP 429 — Too Many Requests** and records a mitigation message. fileciteturn0file0L222-L278

The most important Stage 1 result is that mitigation does **not** shut down the entire application. After excessive traffic from Machine 2 is blocked, Machine 1 is still able to upload a legitimate file successfully. This proves that the implemented mechanism is designed around **traffic control rather than complete service shutdown**. fileciteturn0file0L279-L287

---

# 2. PROJECT TITLE

## Mitigation DDoS / Excessive-Traffic Detection and Secure File-Upload System

The project is documented as a **Docker-Based Three-Machine Cyber Security Demonstration** using Docker, Docker Compose, Python, Flask and Flask-Limiter on a private Docker network. fileciteturn0file0L2-L10

For technical accuracy, Stage 1 should be presented as a:

> **Controlled excessive-traffic / DoS simulation with DDoS-oriented detection and mitigation concepts**

rather than claiming that a real Internet-scale DDoS attack was performed. The uploaded documentation explicitly identifies this limitation because only one controlled traffic-generator container is used. fileciteturn0file0L61-L68

---

# 3. BACKGROUND

Modern web applications frequently provide file-upload functionality. Although file uploads appear to be simple HTTP operations, every request requires server-side processing.

When a client uploads a file, the application must:

1. Receive the HTTP request.
2. Parse the multipart form data.
3. Identify the uploaded file.
4. Validate the request.
5. Save the file.
6. Generate a response.
7. Perform application and storage operations.

If a large number of requests arrive within a short period, these operations can consume CPU, memory, network bandwidth, storage and application-processing resources. Repeated requests can therefore affect service availability. fileciteturn0file0L27-L35

The purpose of Stage 1 was therefore to create a small, reproducible environment where this behavior could be safely demonstrated.

Instead of using real external systems, Docker was used to simulate independent machines. This allowed the complete security workflow to be demonstrated without generating uncontrolled traffic against an external service. fileciteturn0file0L32-L38

---

# 4. PROBLEM STATEMENT

## 4.1 Problem

The main problem addressed in Stage 1 is:

> **How can an HTTP file-upload server identify excessive upload activity and mitigate it while continuing to serve legitimate users?**

An upload endpoint may become vulnerable to repeated requests. If requests are not controlled, the application may spend resources processing repeated uploads.

The project therefore needed to demonstrate two separate security functions:

### Detection

Determine when upload behavior becomes abnormal.

### Mitigation

Prevent further excessive requests from consuming server resources.

The system monitors requests based on client IP address, evaluates request frequency inside a 60-second window, generates an alert when the configured threshold is reached, and uses rate limiting to reject subsequent excessive requests. fileciteturn0file0L39-L47

---

# 5. WHY I CHOSE THIS APPROACH

The implementation was designed around several practical requirements.

## 5.1 Why three machines?

Three separate machines make the security demonstration easier to understand.

| Machine | Purpose |
|---|---|
| Machine 1 | Legitimate client |
| Machine 2 | Controlled excessive-traffic generator |
| Machine 3 | Protected server + IDS + mitigation |

This separation allows the evaluator to clearly see:

**Legitimate User → Server**

and

**Traffic Generator → Server**

at the same time.

The three-machine separation is explicitly defined in the project architecture and machine-role documentation. fileciteturn0file0L95-L103

---

# 6. WHY DOCKER WAS USED

Docker was selected because it provides isolated and reproducible environments.

Instead of requiring three physical computers, three Docker containers simulate the machines.

The architecture can therefore be reproduced on one development system.

Docker provides:

- Container isolation
- Private networking
- Repeatable deployment
- Easy environment creation
- Easy testing
- Easy cleanup
- Independent machine roles

Docker Compose further simplifies the deployment because all services, networking and configuration can be defined in one YAML file. fileciteturn0file0L104-L115

---

# 7. STAGE 1 OBJECTIVES

The Stage 1 objectives were:

1. Create an isolated three-machine Docker network.
2. Create a file-upload server.
3. Allow legitimate file uploads.
4. Generate controlled excessive upload traffic.
5. Monitor requests based on client IP.
6. Detect abnormal request frequency.
7. Generate an IDS-style alert.
8. Apply application-level rate limiting.
9. Return HTTP 429 when the limit is exceeded.
10. Verify that legitimate traffic continues after mitigation.
11. Produce a repeatable demonstration suitable for project review and viva. fileciteturn0file0L48-L60

These objectives form the basis for determining whether Stage 1 was completed successfully.

---

# 8. OVERALL SYSTEM ARCHITECTURE

The architecture consists of three containers connected through a private Docker bridge network.

### Architecture

```text
                    PRIVATE DOCKER NETWORK
                         ddos-lab
                            |
          +-----------------+------------------+
          |                 |                  |
          v                 v                  v
   +-------------+   +-------------+   +------------------+
   |  MACHINE 1  |   |  MACHINE 2  |   |    MACHINE 3    |
   | Legitimate  |   | Controlled  |   | Protected Server|
   |   Client    |   |  Traffic    |   |    + IDS        |
   +-------------+   | Generator   |   | + Rate Limiter  |
          |          +-------------+   +------------------+
          |                 |                  |
          | legitimate      | excessive       |
          | upload          | requests        |
          +-----------------+----------------->|
                                             |
                                      +--------------+
                                      | File Upload  |
                                      | IDS Monitor  |
                                      | Rate Limit   |
                                      +--------------+
```

The uploaded report's architecture diagram on **page 3** shows this three-machine arrangement and the separation between legitimate traffic, excessive requests and the protected server. fileciteturn0file0L69-L93

---

# 9. MACHINE 1 — LEGITIMATE CLIENT

Machine 1 represents a normal user.

Its responsibility is to create and upload:

```text
legitimate.txt
```

The purpose of Machine 1 is important because it establishes the **baseline normal behavior** before the excessive-traffic test.

The successful upload from Machine 1 proves that:

- The network works.
- The server is reachable.
- The `/upload` endpoint works.
- Multipart file upload works.
- The server can store the uploaded file.
- Normal traffic is not incorrectly blocked.

The machine role and responsibility are documented on page 4. fileciteturn0file0L95-L103

---

# 10. MACHINE 2 — CONTROLLED TRAFFIC GENERATOR

Machine 2 represents the source of excessive traffic.

A file named:

```text
attack.txt
```

was created inside Machine 2.

The purpose was not to attack an external system, but to generate controlled repeated HTTP upload requests against Machine 3 inside the private Docker environment.

The test sends ten requests:

```bash
for i in {1..10}; do
  echo "Request $i"
  curl -s -o /dev/null -w "HTTP Status: %{http_code}\n" \
  -F "file=@attack.txt" \
  http://machine3-server:5000/upload
done
```

The test is intentionally limited and controlled. fileciteturn0file0L327-L334

---

# 11. MACHINE 3 — PROTECTED SERVER

Machine 3 is the most important component.

It performs four major functions:

### 1. File Upload Server

It receives HTTP POST requests.

### 2. Monitoring

It records upload request activity.

### 3. Detection and Alerting

It detects abnormal request frequency.

### 4. Mitigation

It blocks requests exceeding the configured rate.

The Flask application runs on port `5000` inside the container.

Docker maps:

```text
Host Port 8080 → Container Port 5000
```

Therefore:

```text
Host:
http://localhost:8080/

Container network:
http://machine3-server:5000/
```

The Compose configuration and port mapping are documented in the uploaded report. fileciteturn0file0L138-L165

---

# 12. PRIVATE NETWORK DESIGN

The Docker network is:

```text
ddos-lab
```

The Docker Compose-generated network observed during implementation was:

```text
ddos-file-upload-lab_ddos-lab
```

The network uses the Docker bridge driver.

During the documented test, the network used:

```text
Subnet: 172.18.0.0/16
Gateway: 172.18.0.1
```

Example addresses observed during one run were:

```text
Machine 1 → 172.18.0.2
Machine 2 → 172.18.0.3
Machine 3 → 172.18.0.4
```

However, these IP addresses can change when containers are recreated. Therefore, the project uses:

```text
machine3-server
```

instead of hard-coding a container IP. Docker's internal DNS resolves this service name to the current container address. fileciteturn0file0L116-L124

This is an important implementation decision because it makes the test environment more reliable when containers are recreated.

---

# 13. PROJECT DIRECTORY STRUCTURE

The documented project structure is:

```text
DAY_13/
│
├── .gitignore
├── ReadMe.md
├── docker-compose.yml
│
└── server/
    ├── app.py
    ├── Dockerfile
    └── requirements.txt
```

The root directory contains the Docker Compose configuration.

The `server` directory contains the Flask application, Dockerfile and dependencies. fileciteturn0file0L125-L137

---

# 14. TECHNOLOGIES USED

| Technology | Purpose |
|---|---|
| Docker | Containerized machine simulation |
| Docker Compose | Multi-container orchestration |
| Docker Bridge Network | Private communication |
| Python 3.12 | Application runtime |
| Flask | HTTP file-upload server |
| Flask-Limiter | Rate limiting |
| cURL | HTTP request and upload testing |
| Bash / PowerShell | Environment control and testing |

These technologies and their roles are documented in the Stage 1 report. fileciteturn0file0L104-L115

---

# 15. DOCKER COMPOSE IMPLEMENTATION

The Compose design creates three services.

### Machine 3

```yaml
machine3:
  build: ./server
  container_name: machine3-server
  ports:
    - "8080:5000"
  networks:
    - ddos-lab
```

### Machine 1

```yaml
machine1:
  image: python:3.12-slim
  container_name: machine1-client
  command: ["sleep", "infinity"]
  networks:
    - ddos-lab
```

### Machine 2

```yaml
machine2:
  image: python:3.12-slim
  container_name: machine2-attacker
  command: ["sleep", "infinity"]
  networks:
    - ddos-lab
```

### Network

```yaml
networks:
  ddos-lab:
    driver: bridge
```

This configuration allows all three containers to communicate privately while keeping the server accessible from the host through port `8080`. fileciteturn0file0L138-L165

---

# 16. SERVER DOCKERFILE

The server uses:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN mkdir -p /app/uploads

EXPOSE 5000

CMD ["python", "-u", "app.py"]
```

The Dockerfile creates a lightweight Python environment, installs the required packages, copies the application, creates the upload directory and starts Flask.

The `-u` option is important for the demonstration because it makes Python output unbuffered, allowing monitoring and mitigation messages to appear promptly in Docker logs. fileciteturn0file0L166-L178

---

# 17. PYTHON DEPENDENCIES

The server requires:

```text
Flask
Flask-Limiter
```

Flask provides the HTTP application framework.

Flask-Limiter provides the request-rate limiting mechanism. fileciteturn0file0L179-L183

---

# 18. FILE-UPLOAD IMPLEMENTATION

The server exposes:

```text
/upload
```

The endpoint accepts:

```text
POST
multipart/form-data
```

The application first checks whether a file was provided.

If no file exists:

```text
HTTP 400
```

is returned.

If the filename is missing, another validation error is returned.

For a valid upload, the file is saved to:

```text
/app/uploads
```

The documented implementation performs this process using Flask's `request.files`, validates the filename and saves the file. fileciteturn0file0L184-L221

---

# 19. WHY THE UPLOAD FUNCTION WAS IMPORTANT

The file-upload endpoint was selected because it provides a realistic application-level workload.

Each upload involves:

```text
HTTP request
      ↓
Multipart parsing
      ↓
File extraction
      ↓
Filename handling
      ↓
File storage
      ↓
HTTP response
```

Repeated requests therefore provide a simple way to demonstrate excessive application-layer traffic.

The Stage 1 report also identifies additional security controls that would be needed for production, including:

- Filename sanitization
- File-type validation
- File-size restrictions
- Malware scanning
- Authentication
- Authorization
- Secure storage

These were intentionally outside the current Stage 1 implementation. fileciteturn0file0L219-L221

---

# 20. IDS MONITORING MECHANISM

The IDS component is implemented at the application level.

It maintains:

```python
request_times = {}
```

The configuration is:

```python
ALERT_THRESHOLD = 5
MONITOR_WINDOW = 60
```

This means:

> If five upload requests are observed from a client within the monitoring window, an abnormal-activity alert is generated.

The monitoring system associates requests with the client's IP address.

The relevant logic is conceptually:

```text
Receive /upload request
        ↓
Identify client IP
        ↓
Get current timestamp
        ↓
Remove timestamps older than 60 seconds
        ↓
Add current request
        ↓
Count recent requests
        ↓
Display monitoring message
        ↓
If count == 5
        ↓
Generate alert
```

This implementation is documented in detail in the uploaded report. fileciteturn0file0L222-L258

---

# 21. WHY A 60-SECOND WINDOW WAS USED

The monitoring mechanism needs both:

- A request count
- A time window

A count by itself would not tell us whether requests were generated rapidly or slowly.

For example:

```text
5 requests over 1 hour
```

is very different from:

```text
5 requests within 60 seconds
```

The implementation therefore uses:

```text
MONITOR_WINDOW = 60 seconds
```

This makes the detection behavior easy to demonstrate and explain during a project review.

---

# 22. ALERT GENERATION

When the request count reaches the threshold, the application prints:

```text
[ALERT] Abnormal upload activity detected
from <client-ip>
(5 requests in 60 seconds)
```

The alert provides visible evidence that the detection mechanism has identified an abnormal request pattern.

The documented representative output shows:

```text
[MONITOR] Upload request #5 from 172.18.0.2

[ALERT] Abnormal upload activity detected
from 172.18.0.2
(5 requests in 60 seconds)
```

This log sequence is particularly useful for the showcase because an evaluator can directly see the relationship between the request count and the generated alert. fileciteturn0file0L359-L373

---

# 23. DETECTION VS MITIGATION

One of the most important concepts demonstrated in Stage 1 is the difference between **detection** and **mitigation**.

## Detection

Detection answers:

> "Is abnormal activity occurring?"

In this project:

```text
5 requests within 60 seconds
        ↓
IDS-style alert
```

## Mitigation

Mitigation answers:

> "What should the server do about the excessive requests?"

In this project:

```text
Requests exceed configured rate
        ↓
Flask-Limiter
        ↓
HTTP 429
        ↓
Request blocked
```

The uploaded documentation explicitly distinguishes these two functions. fileciteturn0file0L448-L464

---

# 24. RATE LIMITING IMPLEMENTATION

The `/upload` endpoint is protected using:

```python
@limiter.limit("5 per minute")
```

Therefore, a client is permitted up to five upload requests per minute under the configured rule.

Additional requests are rejected by Flask-Limiter.

The server returns:

```text
HTTP 429
```

which means:

> Too Many Requests

The application also logs a mitigation message:

```text
[MITIGATION] Excessive traffic blocked
from <client-ip>
```

The mitigation implementation is documented on page 8 of the report. fileciteturn0file0L259-L278

---

# 25. WHY HTTP 429 WAS USED

HTTP `429 Too Many Requests` is useful because it provides clear observable evidence.

Instead of simply dropping requests silently, the server tells the client that the configured request rate has been exceeded.

Therefore, during the showcase:

```text
HTTP 200
```

means the request was accepted.

While:

```text
HTTP 429
```

means the rate limit has been exceeded and the request was rejected.

This makes the mitigation easy to demonstrate and verify.

---

# 26. COMPLETE SECURITY FLOW

The complete Stage 1 workflow is:

```text
                    NORMAL TRAFFIC

Machine 1
   |
   | legitimate upload
   v
Machine 3
   |
   | HTTP 200
   v
File stored successfully
```

Then:

```text
                EXCESSIVE TRAFFIC

Machine 2
   |
   | Request 1 → 200
   | Request 2 → 200
   | Request 3 → 200
   | Request 4 → 200
   | Request 5 → 200 + ALERT
   | Request 6 → 429
   | Request 7 → 429
   | ...
   v
Machine 3
   |
   +--> IDS Monitoring
   |
   +--> Alert
   |
   +--> Rate Limiter
   |
   +--> Mitigation
```

Finally:

```text
              AVAILABILITY VERIFICATION

Machine 1
   |
   | legitimate upload
   v
Machine 3
   |
   | HTTP 200
   v
Service remains available
```

This three-stage flow—normal operation, excessive traffic and recovery—is the central proof of Stage 1.

---

# 27. ENVIRONMENT SETUP

The documented implementation used Docker and Docker Compose.

The environment was checked using:

```bash
docker --version
docker compose version
```

The documented completed environment used:

```text
Docker 29.8.0
Docker Compose v5.5.1
```

The project was opened and Compose configuration was validated:

```bash
cd C:\Users\jaasw\ddos-file-upload-lab

docker compose config
```

Then the environment was built:

```bash
docker compose up -d --build
```

Finally:

```bash
docker ps
```

was used to verify the containers. fileciteturn0file0L288-L303

---

# 28. STEP-BY-STEP DEMONSTRATION

## Step 1 — Start the Environment

Run:

```bash
docker compose up -d --build
```

Then:

```bash
docker ps
```

Expected containers:

```text
machine1-client
machine2-attacker
machine3-server
```

This demonstrates that the three-machine laboratory has been successfully created.

---

# 29. STEP 2 — SHOW THE NETWORK

Run:

```bash
docker network inspect ddos-file-upload-lab_ddos-lab
```

During the showcase, explain:

> "All three containers are connected to the same private Docker bridge network. This allows the experiment to remain isolated from an external target."

The report recommends showing this as part of the live presentation. fileciteturn0file0L412-L418

---

# 30. STEP 3 — SHOW MACHINE 3

Open the server logs:

```bash
docker logs -f machine3-server
```

Keep this terminal visible.

This is the most important terminal during the attack demonstration because it displays:

```text
[MONITOR]
[ALERT]
[UPLOAD]
[MITIGATION]
```

The use of `flush=True` and Python's unbuffered mode was specifically implemented so these messages appear immediately. fileciteturn0file0L369-L373

---

# 31. STEP 4 — TEST NORMAL OPERATION

Enter Machine 1:

```bash
docker exec -it machine1-client bash
```

Create the legitimate file:

```bash
echo "This is a legitimate file from Machine 1" > legitimate.txt
```

Verify it:

```bash
cat legitimate.txt
```

Upload it:

```bash
curl -s -F "file=@legitimate.txt" \
http://machine3-server:5000/upload
```

Expected:

```json
{
  "message": "File uploaded successfully",
  "status": "success"
}
```

This establishes the normal baseline. fileciteturn0file0L304-L315

---

# 32. STEP 5 — VERIFY SERVER STORAGE

Enter Machine 3:

```bash
docker exec -it machine3-server bash
```

Check:

```bash
ls -l /app/uploads
```

Then:

```bash
cat /app/uploads/legitimate.txt
```

The file should exist and contain the expected content.

This proves that the complete upload pipeline worked:

```text
Machine 1
   ↓
HTTP POST
   ↓
Machine 3
   ↓
Flask
   ↓
/app/uploads
```

The uploaded report records this successful file verification. fileciteturn0file0L316-L321

---

# 33. STEP 6 — PREPARE MACHINE 2

Enter Machine 2:

```bash
docker exec -it machine2-attacker bash
```

Create:

```bash
echo "Controlled traffic test from Machine 2" > attack.txt
```

Verify:

```bash
cat attack.txt
```

This file is then used to generate controlled repeated requests. fileciteturn0file0L322-L325

---

# 34. STEP 7 — GENERATE CONTROLLED EXCESSIVE TRAFFIC

Run:

```bash
for i in {1..10}; do
  echo "Request $i"
  curl -s -o /dev/null -w "HTTP Status: %{http_code}\n" \
  -F "file=@attack.txt" \
  http://machine3-server:5000/upload
done
```

The documented test produced:

```text
Requests 1–5 → HTTP 200
Requests 6–10 → HTTP 429
```

during the configured rate-limit period. fileciteturn0file0L327-L334

---

# 35. STEP 8 — SHOW THE IDS DETECTION

At the fifth request, the monitoring system reaches:

```text
5 requests
within 60 seconds
```

and produces:

```text
[ALERT] Abnormal upload activity detected
```

This is the **detection stage**.

During the presentation, point directly to this line and explain:

> "The IDS-style application monitor has identified that this client has reached the configured abnormal-activity threshold."

The fifth-request threshold is explicitly documented in the implementation. fileciteturn0file0L248-L258

---

# 36. STEP 9 — SHOW MITIGATION

After the rate limit is exceeded, additional requests produce:

```text
HTTP 429
```

The server also logs:

```text
[MITIGATION] Excessive traffic blocked
```

This demonstrates the mitigation stage.

The actual response can be displayed using:

```bash
curl -i -F "file=@attack.txt" \
http://machine3-server:5000/upload
```

Expected:

```text
HTTP/1.1 429 TOO MANY REQUESTS
```

with a JSON response indicating that the rate limit was exceeded. fileciteturn0file0L335-L341

---

# 37. STEP 10 — PROVE THE SERVICE IS STILL AVAILABLE

This is the most important final verification.

Return to Machine 1:

```bash
docker exec -it machine1-client bash
```

Upload again:

```bash
curl -s -F "file=@legitimate.txt" \
http://machine3-server:5000/upload
```

Expected:

```text
HTTP 200
```

with a successful upload response.

This demonstrates:

```text
Excessive traffic
       ↓
Detected
       ↓
Blocked
       ↓
Legitimate traffic
       ↓
Still accepted
```

The report identifies this as a key result because it demonstrates that the mitigation blocks excessive requests while keeping the service operational. fileciteturn0file0L342-L347

---

# 38. ACTUAL TEST RESULTS

| Test | Result | Meaning |
|---|---|---|
| Host → Server | HTTP 200 | Server reachable |
| Machine 1 upload | HTTP 200 | Legitimate upload accepted |
| Server file verification | File exists | Upload stored successfully |
| Machine 2 requests 1–5 | HTTP 200 | Requests initially within configured rate |
| Fifth request | IDS alert | Detection threshold reached |
| Machine 2 requests 6–10 | HTTP 429 | Excessive traffic blocked |
| Machine 1 after mitigation | HTTP 200 | Legitimate service continues |

These are the documented observed results from the completed test. fileciteturn0file0L348-L358

---

# 39. LOG ANALYSIS

The representative logs show:

```text
[MONITOR] Upload request #5 from 172.18.0.2

[ALERT] Abnormal upload activity detected from 172.18.0.2
(5 requests in 60 seconds)

[UPLOAD] File 'attack.txt' uploaded from 172.18.0.2

[MONITOR] Upload request #6 from 172.18.0.2

[MITIGATION] Excessive traffic blocked from 172.18.0.2
```

This is extremely useful for demonstrating the complete security chain.

### Log 1 — Monitoring

```text
[MONITOR]
```

Shows that the request was observed.

### Log 2 — Detection

```text
[ALERT]
```

Shows that the threshold was reached.

### Log 3 — Mitigation

```text
[MITIGATION]
```

Shows that excessive traffic was blocked.

The report explains that this sequence demonstrates the relationship between monitoring, detection, alerting and mitigation. fileciteturn0file0L359-L373

---

# 40. HOW I SHOWCASED THE PROJECT

For a project review or viva, the recommended showcase sequence is:

### 1. Start the environment

```bash
docker compose up -d --build
```

### 2. Show containers

```bash
docker ps
```

Explain:

> "These three containers represent three independent machines."

### 3. Show network

```bash
docker network inspect ddos-file-upload-lab_ddos-lab
```

Explain:

> "All three machines are connected through a private Docker bridge network."

### 4. Show server logs

```bash
docker logs -f machine3-server
```

### 5. Show legitimate operation

Enter Machine 1 and upload:

```text
legitimate.txt
```

Show:

```text
HTTP 200
```

### 6. Verify storage

Show:

```text
/app/uploads/legitimate.txt
```

### 7. Start Machine 2

Create:

```text
attack.txt
```

### 8. Generate ten controlled requests

Run the request loop.

### 9. Show detection

Point to:

```text
[ALERT]
```

### 10. Show mitigation

Point to:

```text
HTTP 429
[MITIGATION]
```

### 11. Prove availability

Return to Machine 1 and upload again.

Show:

```text
HTTP 200
```

This exact sequence is recommended in the uploaded report's live showcase section. fileciteturn0file0L412-L434

---

# 41. HOW THE STAGE 1 REQUIREMENTS WERE SATISFIED

The project can be mapped requirement-by-requirement.

| Requirement | Implementation | Evidence |
|---|---|---|
| Isolated environment | Docker private bridge network | Three containers connected to `ddos-lab` |
| Legitimate client | Machine 1 | `legitimate.txt` upload |
| Traffic generator | Machine 2 | Repeated `curl` requests |
| Protected server | Machine 3 | Flask application |
| File upload | `/upload` | Multipart POST |
| Monitoring | `request_times` | Tracks timestamps |
| Detection | 5 requests / 60 sec | `[ALERT]` |
| Alerting | Application log | `[ALERT] Abnormal upload activity detected` |
| Mitigation | Flask-Limiter | `5 per minute` |
| Blocking | HTTP 429 | Excessive requests rejected |
| Logging | Docker logs | Monitor/alert/mitigation messages |
| Availability | Machine 1 after mitigation | HTTP 200 |
| Repeatability | Docker Compose | Environment can be rebuilt |

The project documentation explicitly lists the corresponding objectives and observed results. fileciteturn0file0L48-L60 fileciteturn0file0L348-L358

---

# 42. SECURITY ANALYSIS

Stage 1 demonstrates several security principles.

## 42.1 Isolation

The traffic is confined to a private Docker network.

This prevents the demonstration from requiring an external target. fileciteturn0file0L374-L380

## 42.2 Monitoring

The server tracks upload requests according to client IP and time.

## 42.3 Detection

The system identifies high-frequency upload activity.

## 42.4 Alerting

The server explicitly logs abnormal behavior.

## 42.5 Mitigation

Flask-Limiter rejects excessive requests.

## 42.6 Observability

HTTP status codes and logs provide visible evidence.

## 42.7 Availability Verification

A legitimate request is tested after mitigation.

This final point is particularly important because it demonstrates that the security control does not simply shut down the entire application. fileciteturn0file0L374-L384

---

# 43. WHY THIS IS NOT A REAL INTERNET DDoS ATTACK

This point should be explained clearly during the presentation.

The implementation uses:

```text
One controlled traffic-generator container
```

rather than:

```text
Multiple distributed Internet systems
```

Therefore, the technically accurate description is:

> **Controlled excessive-traffic / DoS simulation with DDoS-oriented detection and mitigation concepts.**

The experiment is intentionally isolated inside Docker.

It does not represent:

- Internet-scale traffic
- A botnet
- A distributed real-world attack
- A production DDoS campaign

The uploaded documentation explicitly states this limitation. fileciteturn0file0L61-L68

---

# 44. WHAT MAKES THE DEMONSTRATION SUCCESSFUL

The project is not considered successful merely because HTTP 429 was generated.

The complete success condition consists of several stages:

```text
1. Server starts
        ↓
2. Client connects
        ↓
3. Legitimate upload works
        ↓
4. Excessive requests are generated
        ↓
5. Requests are monitored
        ↓
6. Threshold is reached
        ↓
7. Alert is generated
        ↓
8. Excessive requests are blocked
        ↓
9. Legitimate client still works
```

The completed implementation demonstrated this entire sequence. fileciteturn0file0L481-L494

---

# 45. IMPORTANT LIMITATIONS

Stage 1 is intentionally a controlled demonstration and therefore has limitations.

### 45.1 Single traffic source

Only one traffic-generator container is used.

Therefore it does not simulate a true distributed botnet.

### 45.2 In-memory rate limiting

Flask-Limiter currently uses in-memory storage.

This is not appropriate for a production distributed environment.

### 45.3 Request history is temporary

The monitoring history exists in process memory and is lost when the application restarts.

### 45.4 Fixed thresholds

The system uses fixed values:

```text
5 requests
60 seconds
5 requests/minute
```

It does not dynamically adapt to system conditions.

### 45.5 Application-level IDS

The IDS is implemented inside the Flask application rather than as an independent network IDS sensor.

### 45.6 Upload security

Additional production controls are needed for:

- Authentication
- Authorization
- File-size validation
- File-type validation
- Filename sanitization
- Secure storage
- Malware scanning

### 45.7 No persistent SIEM

There is no persistent security-event database or external alerting platform.

These limitations are explicitly identified in the Stage 1 documentation. fileciteturn0file0L385-L395

---

# 46. FUTURE ENHANCEMENTS

The next development stage could extend the current system with:

### Infrastructure

- Redis/shared storage for rate-limiter state
- Reverse proxy
- WAF
- Load balancer
- Network IDS/IPS

### Application security

- Authentication
- Authorization
- File-size restrictions
- File-type restrictions
- Filename sanitization
- HTTPS/TLS
- Secure storage

### Monitoring

- Persistent security event database
- Dashboard
- Request-rate graphs
- Alert history
- SIEM integration

### Detection

- Adaptive thresholds
- Request-rate analysis
- Resource-utilization monitoring
- Multiple controlled traffic sources

### Automation

- Automated testing
- Automated alerting
- Configurable thresholds through environment variables

These enhancements are listed in the uploaded report's future-enhancement section. fileciteturn0file0L396-L411

---

# 47. VIVA EXPLANATION — SHORT VERSION

If the evaluator asks:

### "Explain your project."

You can say:

> "My Stage 1 project is a controlled DDoS/excessive-traffic detection and mitigation system implemented using Docker. I created three containers representing three machines. Machine 1 is the legitimate client, Machine 2 is the controlled excessive-traffic generator, and Machine 3 is the protected Flask file-upload server. All three communicate through a private Docker bridge network.
>
> The server monitors upload requests based on client IP address. If five upload requests occur within the 60-second monitoring window, the system generates an IDS-style abnormal-activity alert. Flask-Limiter is configured to allow five requests per minute, and subsequent excessive requests receive HTTP 429 Too Many Requests.
>
> I demonstrated the complete process by first uploading a legitimate file from Machine 1 and verifying that it was stored successfully. Then I generated ten controlled requests from Machine 2. The first five requests were accepted, the fifth triggered the alert, and subsequent requests were blocked with HTTP 429. Finally, I uploaded the legitimate file again from Machine 1 and received HTTP 200. This proved that the mitigation blocked excessive traffic while keeping the service available to legitimate users." fileciteturn0file0L481-L494

---

# 48. VIVA QUESTIONS AND ANSWERS

## Q1. What is the purpose of this project?

**Answer:**

The project demonstrates secure file-upload communication, excessive-traffic detection, alert generation and application-layer mitigation using Docker. fileciteturn0file0L436-L439

---

## Q2. Why did you use three machines?

**Answer:**

To separate the legitimate client, traffic generator and protected server so that the security workflow could be demonstrated clearly. fileciteturn0file0L440-L442

---

## Q3. Why did you use Docker?

**Answer:**

Docker provides isolated and reproducible environments and allows the three machines to communicate through a controlled private network. fileciteturn0file0L443-L445

---

## Q4. Why did you use Docker Compose?

**Answer:**

Docker Compose allows all three services, networking, images and port mappings to be defined and managed together. fileciteturn0file0L446-L447

---

## Q5. What does your IDS monitor?

**Answer:**

It monitors requests to the `/upload` endpoint and tracks recent request timestamps for each client IP. fileciteturn0file0L448-L449

---

## Q6. What is your detection threshold?

**Answer:**

Five upload requests within a 60-second monitoring window. fileciteturn0file0L450-L451

---

## Q7. What happens when the rate limit is exceeded?

**Answer:**

Flask-Limiter rejects additional requests and the application returns HTTP 429. fileciteturn0file0L452-L455

---

## Q8. What does HTTP 429 mean?

**Answer:**

HTTP 429 means **Too Many Requests**. It indicates that the configured request rate has been exceeded. fileciteturn0file0L454-L455

---

## Q9. Does mitigation stop the whole server?

**Answer:**

No. The final test shows that Machine 1 can successfully upload a legitimate file after excessive requests have been blocked. fileciteturn0file0L456-L457

---

## Q10. Is this a real DDoS attack?

**Answer:**

No. It is a controlled excessive-traffic/DoS simulation inside a private Docker laboratory. fileciteturn0file0L458-L459

---

## Q11. Why use `machine3-server` instead of the IP address?

**Answer:**

Docker provides internal DNS resolution for the service name, while container IP addresses can change when containers are recreated. fileciteturn0file0L460-L461

---

## Q12. What is the difference between detection and mitigation?

**Answer:**

Detection identifies the abnormal request pattern and generates the alert. Mitigation rejects subsequent excessive requests. fileciteturn0file0L462-L464

---

# 49. STAGE 1 COMPLETION MATRIX

A useful way to present Stage 1 during evaluation is:

```text
┌──────────────────────────────────────────────┐
│          STAGE 1 COMPLETION                  │
├──────────────────────────────────────────────┤
│ Docker Environment              ✓            │
│ Three Machine Architecture      ✓            │
│ Private Network                 ✓            │
│ File Upload Service             ✓            │
│ Legitimate Upload               ✓            │
│ Request Monitoring              ✓            │
│ IP-Based Tracking               ✓            │
│ Threshold Detection             ✓            │
│ IDS Alert                       ✓            │
│ Rate Limiting                   ✓            │
│ HTTP 429 Blocking               ✓            │
│ Mitigation Logging              ✓            │
│ Legitimate Traffic Recovery     ✓            │
│ Live Demonstration              ✓            │
│ Repeatable Environment          ✓            │
└──────────────────────────────────────────────┘
```

This maps directly to the documented objectives and observed test results. fileciteturn0file0L48-L60 fileciteturn0file0L348-L358

---

# 50. FINAL CONCLUSION

Stage 1 successfully established a controlled cybersecurity laboratory for demonstrating excessive HTTP traffic against a file-upload application.

The implementation started with a legitimate file-upload workflow and then introduced controlled excessive traffic from a separate Docker container. The server monitored the upload requests by client IP and maintained a 60-second monitoring window. When the configured threshold of five requests was reached, the application generated an IDS-style abnormal-activity alert.

The rate-limiting component then provided the mitigation mechanism. Additional requests were rejected with HTTP 429, and the server generated explicit mitigation logs.

Most importantly, the project did not end with simply demonstrating that requests could be blocked. The final availability test showed that the legitimate client could still upload successfully after the excessive traffic had been blocked. This established the complete security cycle:

```text
NORMAL TRAFFIC
      ↓
MONITORING
      ↓
ABNORMAL ACTIVITY
      ↓
DETECTION
      ↓
ALERT
      ↓
MITIGATION
      ↓
EXCESSIVE REQUESTS BLOCKED
      ↓
LEGITIMATE SERVICE CONTINUES
```

Therefore, Stage 1 demonstrates the practical relationship between **monitoring, detection, alerting, mitigation and service availability verification** in a controlled environment. The implementation is repeatable because the entire laboratory is containerized using Docker and Docker Compose. fileciteturn0file0L481-L494

For a production deployment, the documented limitations would need to be addressed through persistent/shared rate-limiter storage, stronger upload validation, authentication and authorization, secure storage, HTTPS/TLS, external monitoring, SIEM integration and additional network security controls. fileciteturn0file0L385-L411

