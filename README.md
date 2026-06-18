# 🚀 End-to-End DevOps CI/CD Pipeline

An automated Continuous Integration and Continuous Deployment (CI/CD) pipeline delivering a containerized Python FastAPI application to an AWS Kubernetes Cluster (EKS).

## 🏗️ Architecture Overview

This project demonstrates a modern DevOps workflow:
1. **Source Control:** Code is maintained in Git and hosted on GitHub.
2. **Containerization:** The application is packaged using Docker for consistent environments.
3. **Continuous Integration (CI):** A Jenkins declarative pipeline checks out the code, builds the Docker image, and tags it uniquely per build.
4. **Cloud Registry:** The pipeline securely authenticates with AWS and pushes the image to Amazon Elastic Container Registry (ECR).
5. **Continuous Deployment (CD):** The pipeline dynamically updates Kubernetes manifests and deploys the new image to an Amazon EKS cluster using `kubectl`.

## 🛠️ Technology Stack
* **Application Framework:** Python / FastAPI
* **Containerization:** Docker
* **CI/CD Automation:** Jenkins
* **Cloud Infrastructure:** Amazon Web Services (AWS ECR, AWS EKS)
* **Container Orchestration:** Kubernetes
* **Scripting/CLI:** AWS CLI, Bash, Linux (Ubuntu)

## 💻 Local Development Setup

To test this application locally on your machine:

**1. Build the Docker Image**
`docker build -t devops-fastapi-app .`

**2. Run the Container locally**
`docker run -d -p 8000:8000 --name my-fastapi-container devops-fastapi-app`

**3. Verify Health**
`curl http://localhost:8000`

---
*Developed as a practical demonstration of cloud-native deployment strategies.*
