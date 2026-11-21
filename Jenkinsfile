
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'GitHub repository checkout successful!'
            }
            stage('Check Workspace') {
    steps {
        sh '''
            echo "Workspace location:"
            pwd

            echo "Workspace contents:"
            ls -la

            echo "Workspace environment variable:"
            echo "$WORKSPACE"
        '''
    }
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
