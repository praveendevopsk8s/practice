pipeline {
    agent any

    stages {
        stage('Clone the repo') {
            steps {
                echo 'Cloning the repo'
                git branch: 'main', url: 'https://github.com/praveendevopsk8s/practice.git'
            }
        }
        stage('Building') {
            steps {
                echo 'Building steps'
                sh '''
                    bash -c "python3 -m venv venv"
                    bash -c "source venv/bin/activate"
                    bash -c "pip install -r requirements.txt"
                    '''
                }
            }
        stage('Test') {
            steps {
                echo 'Testing Stage'
                 sh '''
            python3 main.py  # Run the app (replace with your app's entry point)
        '''
                }
            }
            
        }        
    }

