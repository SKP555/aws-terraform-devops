# 🚀 AWS Terraform DevOps Project

End-to-end infrastructure setup on AWS using Terraform, following DevOps best practices.

---

## 📌 Project Overview

This project demonstrates how to build cloud infrastructure from scratch using Infrastructure as Code (Terraform).

---

## ⚙️ Tech Stack

- AWS (VPC, EC2, Networking)
- Terraform
- Linux

---

## 🧠 Architecture (Current)

Internet → Internet Gateway → Public Subnet → EC2 Instance

---

# 📌 Phase 1: VPC Creation

Created a custom VPC using Terraform.

### Screenshot
![VPC](./images/vpc.png)

---

# 📌 Phase 2: Networking Setup

- Created Public Subnet
- Configured Internet Gateway
- Set up Route Table with internet access

### Screenshots
![Subnet](./images/subnet.png)
![Internet Gateway](./images/igw.png)
![Route Table](./images/route-table.png)

---

# 📌 Phase 3: EC2 Deployment

- Launched EC2 instance using Terraform
- Configured Security Group (SSH + HTTP)

### Screenshots
![EC2](./images/ec2.png)

---

## 📈 Progress

- [x] VPC
- [x] Subnet
- [x] Internet Gateway
- [x] Route Table
- [x] EC2 Instance
- [ ] Web Server Deployment
- [ ] Docker
- [ ] CI/CD
- [ ] Monitoring
- [ ] AI Integration

---

## 👤 Author

Sonu Krishna  
DevOps | Cloud | AWS
