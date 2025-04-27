pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                echo "Checkout"
                sh 'ls -l'
            }
        }

        stage('Prepare Environment') {
            steps {
                echo "Prepare Environment"
                sh('bash ./jenkinsscript.sh')
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running Unit Tests"
                sh '''
                    python3 -m venv myenv
                    export PYTHONPATH=$PYTHONPATH:$(pwd)
                    pytest --cov=main utests --junitxml=./xmlReport/output.xml
                    python3 -m coverage xml
                '''
            }
        }

        stage('Publish Junit report') {
            steps {
                echo "Publish Junit Report"
                junit skipMarkingBuildUnstable: true, testResults: 'xmlReport/output.xml'
            }
        }

        stage('Publish Code Coverage') {
            steps {
                echo "Publish Code Coverage"
                cobertura coberturaReportFile: 'coverage.xml'
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
