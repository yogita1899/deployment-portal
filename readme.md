# Self-Service Deployment Portal Backend

## Project Overview

This project implements a **Self-Service Deployment Portal Backend** that allows developers to register a new microservice.
Once the service is registered, the platform automatically generates infrastructure and deployment resources required to run the service.

The goal of this project is to simulate an **Internal Developer Platform (IDP)** that reduces manual DevOps work.

---

## Problem Statement

Developers usually need help from DevOps teams to:

* Create container registries
* Setup CI/CD pipelines
* Create Kubernetes deployment files
* Configure IAM permissions

This portal automates these tasks.

---

## Feature – Register Microservice

Developers can register a new microservice using an API.

### API Endpoint

POST /register-service

### Request Body

```json
{
  "service_name": "payment-service",
  "team_name": "fintech",
  "repo_url": "https://github.com/yogita1899/fintech-backend-app.git"
}
```

### Input Fields

| Field        | Description                            |
| ------------ | -------------------------------------- |
| service_name | Name of the microservice               |
| team_name    | Team responsible for the service       |
| repo_url     | Git repository containing service code |

---

## Automation Performed

After registering a service, the system automatically creates:

### 1. Container Registry (ECR)

Stores Docker images for the microservice.

### 2. IAM Role

Creates a role with permissions required for the service.

### 3. Kubernetes Deployment Manifest

Example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-service
spec:
  replicas: 2
  selector:
    matchLabels:
      app: payment-service
  template:
    metadata:
      labels:
        app: payment-service
    spec:
      containers:
      - name: payment-service
        image: <ECR_IMAGE>
        ports:
        - containerPort: 80
```

### 4. CI/CD Pipeline

A Jenkins pipeline is automatically generated to build and deploy the service.

Example:

```groovy
pipeline {
  agent any

  stages {

    stage('Build') {
      steps {
        sh 'docker build -t payment-service .'
      }
    }

    stage('Push Image') {
      steps {
        sh 'docker push <ECR_REPO>'
      }
    }

    stage('Deploy') {
      steps {
        sh 'kubectl apply -f deployment.yaml'
      }
    }

  }
}
```

---

## Project Structure

```
deployment-portal/
│
├── app.py
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│
├── templates/
│   ├── deployment.yaml
│   ├── Jenkinsfile
│
└── README.md
```

---

## How to Run the Project

### Clone the repository

```
git clone https://github.com/yogita1899/fintech-backend-app.git
```

### Install dependencies

```
pip install flask
```

### Start backend service

```
python app.py
```

Server will start on:

```
http://localhost:5000
```

---

## Test the API

```
curl -X POST http://localhost:5000/register-service \
-H "Content-Type: application/json" \
-d '{
"service_name":"payment-service",
"team_name":"fintech",
"repo_url":"https://github.com/yogita1899/fintech-backend-app.git"
}'
```

---

## Technologies Used

* Python / Flask
* Terraform
* Kubernetes
* Jenkins CI/CD
* Docker

---
