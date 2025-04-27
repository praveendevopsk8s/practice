pipeline {
    agent any

    stages {
        stage('Clone the repo') {
            steps {
                echo 'Cloning the repo'
                
            }
        }
        stage('Building') {
            steps {
                echo 'Building steps'
                sh('bash ./jenkinsscript.sh')
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

