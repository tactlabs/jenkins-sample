pipeline {

  agent any

  options {

    buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr: '5')
    disableConcurrentBuilds()
    parallelsAlwaysFailFast()

  }
  stages {
 stage('Parallel') {
      parallel {
        stage('docker-compose up') {
          steps {
            sh 'docker-compose up'
          }
        }
        stage('test') {
          steps {
            sh 'sleep 10'
            sh 'docker-compose down --remove-orphans'
          }
        }
      }
    }
  }

  post { 
    always {
      sh 'docker-compose down --remove-orphans'
    }
  }

}
