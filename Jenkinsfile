
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'GitHub repository checkout successful!'
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
