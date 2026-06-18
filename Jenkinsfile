pipeline {
    agent any
    
    environment {
        AWS_REGION = 'us-east-1'
        ECR_REPO = 'devops-fastapi-app'
        IMAGE_TAG = "${env.BUILD_ID}" // Uses the Jenkins build number for unique tagging
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
                sh 'aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com'
                sh 'docker tag ${ECR_REPO}:${IMAGE_TAG} ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}'
                sh 'docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}'
            }
        }
        
        stage('Deploy to EKS Cluster') {
            steps {
                echo 'Updating manifest and deploying to Kubernetes...'
                // Swap the placeholder in deploy.yaml with the actual image URI built in this run
                sh 'sed -i "s|image: AWS_ACCOUNT_ID.*|image: ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}|g" deploy.yaml'
                
                // Apply the configuration to the cluster
                sh 'kubectl apply -f deploy.yaml'
            }
        }
    }
}
