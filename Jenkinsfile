pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "network-anomaly-detector"
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Repository cloned successfully.'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Run Docker Container (Test Locally)') {
            steps {
                echo 'Running the container for testing...'
                sh 'docker run --rm $DOCKER_IMAGE'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                sh 'kubectl apply -f deployment.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Checking deployed pods...'
                sh 'kubectl get pods'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Build or Deployment failed.'
        }
    }
}
