
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        // Stage 1: Checkout source code
        stage('Checkout') {
            steps {
                checkout scm
                echo 'GitHub repository checkout successful!'
            }
        }

        // Stage 2: Verify project files
        stage('Check Workspace') {
            steps {
                sh '''
                    echo "Workspace location:"
                    pwd

                    echo "Project files:"
                    ls -la
                '''
            }
        }

        // Stage 3: Install dependencies and run tests
        stage('Install Dependencies & Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                        -v jenkins_home:/jenkins-home \
                        -w "/jenkins-home${WORKSPACE#/var/jenkins_home}" \
                        python:3.12-slim \
                        sh -c "pip install --no-cache-dir -r Requirements.txt pytest && pytest -v"
                '''
            }
        }

        // Stage 4: Build Docker image
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -f dockerfile -t my-fastapi-app .
                '''
            }
        }

        // Stage 5: Push image to Docker Hub
        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_TOKEN'
                    )
                ]) {
                    sh '''
                        set +x

                        echo "$DOCKER_TOKEN" | docker login \
                            --username "$DOCKER_USER" \
                            --password-stdin

                        docker tag my-fastapi-app \
                            reddy091/cidcwithjenkins:latest

                        docker push reddy091/cidcwithjenkins:latest

                        docker logout
                    '''
                }
            }
        }

    }
}
