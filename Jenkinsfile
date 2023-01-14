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
        shell 'bat "start /min python rest_app.py > rest_app.log"'
      }
    }

    stage('Run web_app.py') {
      steps {
        shell 'bat "start /min python web_app.py > web_app.log"'
      }
    }

    stage('Run backend_testing.py') {
      steps {
        shell 'bat "python backend_testing.py > backend_testing.log"'
      }
    }

    stage('Run frontend _testing.py') {
      steps {
        shell 'bat "python frontend_testing.py > frontend_testing.log"'
      }
    }

    stage('Run combined_testing.py') {
      steps {
        shell 'bat "python combined_testing.py > combined_testing.log"'
      }
    }

    stage('Run clean_environemnt.py') {
      steps {
        shell 'bat "python clean_environemnt.py > clean_environemnt.log"'
      }
    }
  }
  post {
    always {
      archiveArtifacts artifacts: '*.log'
    }
  }
}
