pipeline {
    agent any

    stages {
        stage('Build') {
            steps { 
                withEnv(["HOME=${env.WORKSPACE}"]){
                 sh 'sudo -S docker build -t ${JOB_NAME}-${BUILD_NUMBER} .'
                 sh 'python3 router/app.py'
                }
            }
        }
        stage('Test') {
            steps {
                sh 'sudo -S python3 -m pip install --upgrade pip && pip install -r requirements.txt'
                sh 'python3 ./tests/test.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker build . --file Dockerfile --tag devsec-test:latest'
                echo 'Deploying....'
            }
        }
    }
}