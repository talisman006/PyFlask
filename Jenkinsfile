pipeline {
  environment {
    "${env.PATH};C:\\Users\\Riki\\AppData\\Local\\Microsoft\\WindowsApps"
  }
  agent any
  stages {
    stage('Github clone') {
      steps {
        git(url: 'https://github.com/talisman006/PyFlask.git', branch: 'main', credentialsId: 'github_new')
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
