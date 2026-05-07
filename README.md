# AI-Driven Self-Healing DevOps Platform on AWS

## Overview

This project is an end-to-end AI-enabled DevOps platform built on AWS using Terraform, Docker, GitHub Actions, CloudWatch, and Python automation.

The platform automates infrastructure provisioning, container deployment, CI/CD pipelines, monitoring, alerting, log collection, and self-healing remediation.

The main objective of this project was to simulate a real-world production DevOps environment while implementing foundational AIOps concepts.

---

# Architecture

```text
Developer
    ↓
GitHub Repository
    ↓
GitHub Actions CI/CD
    ↓
AWS EC2 Instance
    ↓
Docker Containerised Application
    ↓
CloudWatch Monitoring + Logs
    ↓
AI Log Analyzer
    ↓
Self-Healing Automation
```

---

# Key Features

## Infrastructure as Code (IaC)

* Provisioned AWS infrastructure using Terraform
* Automated creation of:

  * VPC
  * Public Subnet
  * Internet Gateway
  * Route Tables
  * Security Groups
  * EC2 Instance

## Docker Containerisation

* Dockerised NGINX web application
* Built custom Docker image
* Deployed containers on AWS EC2

## CI/CD Automation

* Implemented GitHub Actions pipeline
* Automatic Docker build and deployment
* Push-to-deploy workflow
* Automated container redeployment on code changes

## Monitoring & Observability

* Integrated AWS CloudWatch Agent
* Collected:

  * CPU metrics
  * Memory metrics
  * Disk metrics
* Centralised Docker logs in CloudWatch Logs

## Alerting System

* Configured CloudWatch alarms
* Integrated SNS email notifications
* Real-time incident alerting

## AI-Powered Log Analysis

* Built Python-based AI log analyser
* Analysed Docker container logs
* Detected anomaly patterns:

  * error
  * failed
  * timeout
  * exception
  * critical

## Self-Healing Automation

* Automatically restarted failed containers
* Simulated self-healing DevOps workflows
* Demonstrated foundational AIOps concepts

---

# Tech Stack

| Category               | Technologies   |
| ---------------------- | -------------- |
| Cloud Platform         | AWS            |
| Infrastructure as Code | Terraform      |
| Containerisation       | Docker         |
| CI/CD                  | GitHub Actions |
| Monitoring             | CloudWatch     |
| Alerting               | SNS            |
| Programming            | Python         |
| OS                     | Ubuntu Linux   |
| Web Server             | NGINX          |

---

# Project Structure

```text
aws-terraform-devops/
│
├── .github/
│   └── workflows/
│       └── docker.yml
│
├── app/
│   ├── Dockerfile
│   └── index.html
│
├── ai-monitor/
│   └── ai_log_analyzer.py
│
├── images/
│
├── main.tf
├── provider.tf
├── .gitignore
├── README.md
```

---

# CI/CD Workflow

The GitHub Actions pipeline performs the following:

1. Detects code push to main branch
2. Connects securely to EC2 using GitHub Secrets
3. Copies updated application files
4. Builds Docker image automatically
5. Restarts Docker container
6. Deploys updated application live

This enables a complete automated deployment workflow.

---

# Monitoring Workflow

```text
EC2 + Docker
      ↓
CloudWatch Agent
      ↓
CloudWatch Metrics & Logs
      ↓
CloudWatch Alarms
      ↓
SNS Email Notifications
```

---

# AI Self-Healing Workflow

```text
Container Logs
      ↓
AI Log Analyzer
      ↓
Detect Errors/Failures
      ↓
Trigger Self-Healing
      ↓
Restart Container Automatically
```

---

# Screenshots

## Infrastructure

Add screenshots for:

* VPC
* Subnet
* Route Table
* Security Group
* EC2 Instance

## CI/CD Pipeline

Add screenshots for:

* GitHub Actions successful pipeline
* Workflow execution
* Automated deployment

## Monitoring

Add screenshots for:

* CloudWatch metrics
* CloudWatch alarms
* SNS notifications
* CloudWatch log groups

## AI Self-Healing

Add screenshots for:

* AI log analyzer output
* Error detection
* Container restart automation

---

# Example AI Analyzer Output

```text
🔍 AI Log Analyzer Started...

⚠ Potential issues detected:

- Detected keyword: error
- Detected keyword: failed

🤖 AI Self-Healing Triggered...
Restarting container...

✅ Container restarted successfully: sonu-container
```

---

# Security Best Practices Implemented

* Used GitHub Secrets for SSH credentials
* Ignored Terraform state files using .gitignore
* Restricted infrastructure access through Security Groups
* Used IAM Role for CloudWatch permissions

---

# Future Enhancements

Planned improvements:

* Kubernetes (EKS) deployment
* Load Balancer integration
* Auto Scaling Groups
* Prometheus + Grafana monitoring
* Real LLM integration for AI analysis
* Slack/Discord alerting
* Predictive anomaly detection
* Automated rollback strategy
* Multi-environment deployments

---

# Challenges Faced and Solutions Implemented

| Challenge                                                 | Solution                                                                                            |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Terraform VPC was accidentally deleted manually from AWS  | Rebuilt infrastructure cleanly using Terraform to restore state consistency                         |
| Invalid AWS AMI ID error during EC2 creation              | Updated to a valid Ubuntu AMI supported in the selected AWS region                                  |
| EC2 instance type not eligible for Free Tier              | Changed instance type to a Free Tier eligible instance                                              |
| SSH authentication failed while connecting to EC2         | Corrected SSH username from `ec2-user` to `ubuntu` and fixed PEM file permissions using `chmod 400` |
| Website not accessible publicly                           | Configured Security Group inbound rules for HTTP and custom application ports                       |
| UTF-8 emoji rendering issue on webpage                    | Added proper UTF-8 meta tags in HTML document                                                       |
| Git push rejected due to remote conflicts                 | Pulled latest remote repository changes and resolved sync issue                                     |
| GitHub Actions deployment failed                          | Debugged YAML formatting and corrected workflow indentation                                         |
| Docker container changes were not reflecting              | Resolved Docker build caching issue using `--no-cache`                                              |
| CI/CD deployment used incorrect application directory     | Fixed SCP deployment target path in GitHub Actions workflow                                         |
| CloudWatch metrics not appearing                          | Attached IAM role with `CloudWatchAgentServerPolicy` to EC2 instance                                |
| CloudWatch Agent initially not configured                 | Created and validated CloudWatch Agent JSON configuration                                           |
| AI log analyzer initially detected existing system errors | Improved understanding of Docker/system logs and refined anomaly detection workflow                 |

---

# Learning Outcomes

This project helped strengthen practical knowledge in:

* AWS Cloud Infrastructure
* Terraform IaC
* Linux Administration
* Docker Containerisation
* CI/CD Automation
* GitHub Actions
* Monitoring & Observability
* CloudWatch & SNS
* Python Automation
* AIOps Concepts
* Self-Healing Systems

---

# Author

Sonu Krishna

GitHub: [https://github.com/SKP555](https://github.com/SKP555)
LinkedIn: [https://www.linkedin.com/in/sonukrsna](https://www.linkedin.com/in/sonukrsna)

---

# Final Result

Successfully built a cloud-native AI-driven self-healing DevOps platform capable of:

* Automated infrastructure provisioning
* Automated CI/CD deployment
* Monitoring and alerting
* Centralised log aggregation
* AI-style anomaly detection
* Self-healing container remediation

