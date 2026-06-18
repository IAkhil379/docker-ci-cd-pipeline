# DevOps CI/CD Pipeline Project

This repository contains a containerized FastAPI application built as part of a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline. 

## Project Architecture
* **Application:** Python / FastAPI
* **Containerization:** Docker
* **CI/CD:** Jenkins (Planned)
* **Cloud Infrastructure:** AWS (Planned)

## Local Development
To run this application locally on your machine, you need Docker installed.

### 1. Build the Docker Image
`docker build -t devops-fastapi-app .`

### 2. Run the Container
`docker run -d -p 8000:8000 --name my-fastapi-container devops-fastapi-app`

### 3. Verify Health
`curl http://localhost:8000`
