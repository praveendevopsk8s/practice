pipeline {
    agent any

    stages {
        stage('Clone the repo') {
            steps {
                echo 'Cloning the repo...'
                
            }
        }

        stage('Building') {
            steps {
                echo 'Running build steps...'
                sh 'bash ./jenkinsscript.sh'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                echo 'Installing Python packages...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t smartflaskapp:latest .'
            }
        }

        stage('Docker Run') {
            steps {
                echo 'Running Docker container...'
                sh 'docker run -d -p 5000:5000 --name flaskcontainer smartflaskapp:latest'
            }
        }

        stage('Health Check') {
            steps {
                echo 'Performing health check...'
                sh 'sleep 5'
                sh 'curl --fail http://localhost:5000 || exit 1'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            sh 'docker rm -f flaskcontainer || true'
        }
    }
}
