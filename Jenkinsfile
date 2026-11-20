pipeline {
    agent any

    stages {
        stage('Source Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Dependency Installation & Build') {
            steps {
                echo 'Installing Python dependencies...'
                powershell 'python -m pip install --upgrade pip'
                powershell 'python -m pip install -r requirements.txt'
            }
        }

        stage('Automated Test & Validation') {
            steps {
                echo 'Running automated tests...'
                powershell 'python -m pytest test_exporter.py'
            }
        }

        stage('Deployment Packaging') {
            steps {
                echo 'Packaging exporter into dedicated deployment directory...'
                powershell '''
                    if (Test-Path "deploy") { Remove-Item -Recurse -Force "deploy" }
                    New-Item -ItemType Directory -Name "deploy" | Out-Null
                    Copy-Item "exporter.py" -Destination "deploy\"
                    Copy-Item "requirements.txt" -Destination "deploy\"
                    Get-ChildItem "deploy"
                '''
                archiveArtifacts artifacts: 'deploy/*', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! Deployment artifact is ready.'
        }
        failure {
            echo 'Pipeline failed! Inspect console logs.'
        }
    }
}
