pipeline {
  agent any

  environment {
    IMAGE = "shrinidhi6/todo-flask-app:${BUILD_NUMBER}"
  }

  stages {
    stage('Build Docker Image') {
      steps {
        script {
          sh 'docker build -t $IMAGE .'
        }
      }
    }

    stage('Push to Docker Hub') {
      steps {
        script {
          docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
            sh 'docker push $IMAGE'
          }
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl set image deployment/todo-flask-app todo-flask-app=$IMAGE --record'
      }
    }
  }
}
