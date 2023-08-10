pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'main',
                url : 'https://github.com/jglick/simple-maven-project-with-tests.git'
            }

        }
        stage('Build'){
            steps{
                echo "Build stage"
            }
        }
        stage('Test'){
            steps{
                echo "Test stage"
            }
        }
        stage('Deploy'){
            steps{
                echo "Deploy stage"
            }
        }
    }
}



