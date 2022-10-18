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
<<<<<<< HEAD
                sh 'pytest'
=======
                sh 'behave --junit'
>>>>>>> 09d5cbf3ad2e4347f0e95b29c7184eb9c8189080
            }
        }
    }
}
