pipeline {
  agent any
  stages {
    stage('Log Tools versions') {
      steps {
        sh '''git --version
java -version'''
        git(url: 'git@github.com:talisman006/PyFlask.git', branch: 'main', poll: true)
      }
    }

  }
}