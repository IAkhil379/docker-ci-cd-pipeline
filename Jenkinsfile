pipeline {
    agent any
    
    environment {
        // In a real Jenkins server, you would store your Account ID as a secret credential
        AWS_REGION = 'us-east-1'
        ECR_REPO = 'devops-fastapi-app'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker image...'
                sh 'docker build -t ${ECR_REPO}:${IMAGE_TAG} .'
            }
        }
        
        stage('Push to AWS ECR') {
            steps {
                echo 'Authenticating and pushing to Elastic Container Registry...'
                // Logs into AWS, tags the image for ECR, and pushes it to the cloud
                sh 'aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com'
                sh 'docker tag ${ECR_REPO}:${IMAGE_TAG} ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}'
                sh 'docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}'
            }
        }
        
        stage('Deploy to Server') {
            steps {
                echo 'Placeholder: Pulling image and running on deployment server...'
                // Deployment commands will go here
            }
        }
    }
}
