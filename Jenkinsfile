pipeline {
  agent any
  stages {
    stage('Github pull') {
      steps {
        git(url: 'git@github.com:talisman006/PyFlask.git', branch: 'main', credentialsId: 'github')
      }
    }

    stage('Run rest_app.py') {
      steps {
        sh 'bat \'start /min python rest_app.py\''
      }
    }

    stage('Run web_app.py') {
      steps {
        sh 'bat \'start /min python web_app.py\''
      }
    }

    stage('Run backend_testing.py') {
      steps {
        sh 'bat \'python backend_testing.py\''
      }
    }

    stage('Run frontend _testing.py') {
      steps {
        sh 'bat \'python frontend_testing.py\''
      }
    }

    stage('Run combined_testing.py') {
      steps {
        sh 'bat \'python combined_testing.py\''
      }
    }

    stage('Run clean_environemnt.py') {
      steps {
        sh 'bat \'python clean_environemnt.py\''
      }
    }

  }
}