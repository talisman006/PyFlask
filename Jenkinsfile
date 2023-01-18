def logPath = 'D:\\PycharmProjects\\PyFlask\\Jenkins_Logs\\'
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
        shell "start /min python rest_app.py >> ${logPath}rest_app.log"
      }
    }
    stage('Run web_app.py') {
      steps {
        shell "start /min python web_app.py >> ${logPath}web_app.log"
      }
    }
    stage('Run backend_testing.py') {
      steps {
        shell "python backend_testing.py >> ${logPath}backend_testing.log"
      }
    }
    stage('Run frontend_testing.py') {
      steps {
        shell "python frontend_testing.py >> ${logPath}frontend_testing.log"
      }
    }
    stage('Run combined_testing.py') {
      steps {
        shell "python combined_testing.py >> ${logPath}combined_testing.log"
      }
    }
    stage('Run clean_environment.py') {
      steps {
        shell "python clean_environment.py >> ${logPath}clean_environment.log"
      }
    }
  }
  }

