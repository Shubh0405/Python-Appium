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
                sh 'pip3 install pytest-bdd'
            }
        }

        stage('run tests') {
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
}
