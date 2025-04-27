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
                    pytest --cov=main utests --junitxml=./xmlReport/output.xml
                    python -m coverage xml
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
    }
}
