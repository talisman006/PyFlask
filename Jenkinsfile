pipeline {
  agent any
  stages {
    stage('Github clone') {
      steps {
        git(url: 'https://github.com/talisman006/PyFlask.git', branch: 'main', credentialsId: 'github_new')
      }
    }

    stage('Run rest_app.py') {
      steps {
        script {
          shell 'bat "start /min python rest_app.py"'
        }
      }
    }

    stage('Run web_app.py') {
      steps {
        script {
          shell 'bat "start /min python web_app.py"'
        }
      }
    }

    stage('Run backend_testing.py') {
      steps {
        script {
          shell 'bat "python backend_testing.py"'
        }
      }
    }

    stage('Run frontend _testing.py') {
      steps {
        script {
          shell 'bat "python frontend_testing.py"'
        }
      }
    }

    stage('Run combined_testing.py') {
      steps {
        script {
          shell 'bat "python combined_testing.py"'
        }
      }
    }

    stage('Run clean_environemnt.py') {
      steps {
        script {
          shell 'bat "python clean_environemnt.py"'
        }
      }
    }

  }
}
