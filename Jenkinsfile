pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
        CONTAINER_NAME = "myapp_container"
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

       
 stage('SonarQube Scan') {
            steps {
                script {
                    // This requires SonarQube Scanner configured in Jenkins tools
                    def scannerHome = tool 'sonar-scanner'
                    withSonarQubeEnv('sonar-testing') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }


        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                  docker stop $CONTAINER_NAME || true
                  docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                  docker run -d \
                    --name $CONTAINER_NAME \
                    -p 8000:8000 \
                    $IMAGE_NAME
                '''
            }
        }
    }
}
