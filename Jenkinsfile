
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
        
        stage('Install Dependencies & Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                        -v jenkins_home:/jenkins-home \
                        -w /jenkins-home/workspace/FastAPI-CI-CD \
                        python:3.12-slim \
                        sh -c "pip install --no-cache-dir -r Requirements.txt pytest && pytest -v"
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t my-fastapi-app-with-jenkins .
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
