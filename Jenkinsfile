
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'GitHub repository checkout successful!'
            }
        }

        stage('Check Workspace') {
            steps {
                sh '''
                    echo "Current workspace:"
                    pwd

                    echo "Files available:"
                    ls -la

                    echo "Checking required files:"
                    ls -l test.py Requirements.txt

                    echo "Checking test files:"
                    find . -name "test_*.py" -o -name "*_test.py"
                '''
            }
        }

        stage('Python Environment') {
            steps {
                sh 'docker run --rm python:3.12-slim python --version'
            }
        }

        stage('Docker Verification') {
            steps {
                sh 'docker version'
            }
        }
    }
}
