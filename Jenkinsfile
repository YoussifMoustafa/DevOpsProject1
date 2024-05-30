pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh "echo 'Building....'"
                sh "docker build -t youssifmoustafa/docker:back-1.${env.BUILD_NUMBER} back-api/"
                sh "docker build -t youssifmoustafa/docker:front-1.${env.BUILD_NUMBER} api-fron/"
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-cred', 
                        usernameVariable: 'USER', 
                        passwordVariable: 'PASS'
                        )]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                    sh "docker push youssifmoustafa/docker:back-1.${env.BUILD_NUMBER}"
                    sh "docker push youssifmoustafa/docker:front-1.${env.BUILD_NUMBER}"
                }
            }
        }
    stage('deploy') {
            steps {
                sh "echo 'Deploying....'"
                sh "kubectl set image deployment/deployment-front -n=default front-static=youssifmoustafa/docker:back-1.${env.BUILD_NUMBER}"
                sh "kubectl set image deployment/deployment-front -n=default front-static=youssifmoustafa/docker:front-1.${env.BUILD_NUMBER}"
            }
        }
    }
}
