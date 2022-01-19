pipeline {
    agent any

    stages {
        stage('Build') {
            steps { 
                withEnv(["HOME=${env.WORKSPACE}"]){
                 sh 'sudo -S docker build -t ${JOB_NAME}-${BUILD_NUMBER} . && sudo -S python3 -m pip install --upgrade pip && pip install -r requirements.txt'
                 sh 'python3 app.py'
                }
            }
        }
        stage('Test') {
            steps {
                sh 'python3 ./tests/test.py test'
            }
        }
        stage('Deploy') {
            steps {
                withRegistry(https://hub.docker.com/r/rupesh1050[,docker]) {
                    node {
                    git '…' // checks out Dockerfile and some project sources
                    def newApp = docker.build "rupesh1050/devsec-test-dev:${env.BUILD_TAG}"
                    newApp.push()
                    }

            }
        }
    }
}