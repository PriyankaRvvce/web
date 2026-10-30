
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Retrieving Python code from GitHub'
                checkout scm
            }
        }

        stage('Build / Syntax Check') {
            steps {
                bat 'python -m py_compile app1.py test-app1.py'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python app1.py'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest -v test-app1'
            }
        }
    }

    post {
        success {
            echo 'Python CI Pipeline: SUCCESS'
        }

        failure {
            echo 'Python CI Pipeline: FAILURE'
        }

        always {
            echo 'Pipeline execution completed'
        }
    }
}
