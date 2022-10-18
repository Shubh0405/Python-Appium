pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('install packages') {
            steps {
                sh 'pip3 install selenium'
                sh 'pip3 install Appium-Python-Client'
                sh 'pip3 install behave'
            }
        }

        stage('run tests') {
            steps {
                sh 'behave --junit'
            }
        }
    }
}
