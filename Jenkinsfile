pipeline {
    agent any
    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }
    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev', 'uat', 'prod'], description: 'Deployment target')
        booleanParam(name: 'PUBLISH_ARTIFACT', defaultValue: true, description: 'Publish artifact')
    }
    environment {
        APP_NAME = 'demo-service'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Validate') {
            steps { sh 'bash scripts/validate.sh' }
        }
        stage('Test') {
            steps { sh 'python scripts/report.py --mode test' }
        }
        stage('Build Docker Image') {
            steps { sh 'docker build -t ${APP_NAME}:${IMAGE_TAG} -f docker/Dockerfile .' }
        }
        stage('Quality Gate') {
            steps {
                echo 'SonarQube quality-gate integration point'
                sh 'python scripts/report.py --mode quality'
            }
        }
        stage('Publish Artifact') {
            when { expression { params.PUBLISH_ARTIFACT } }
            steps { echo 'Nexus/artifact repository integration point' }
        }
        stage('Deploy') {
            steps { sh "bash scripts/deploy.sh ${ENVIRONMENT} ${IMAGE_TAG}" }
        }
        stage('Verify') {
            steps { sh 'bash scripts/verify.sh' }
        }
    }
    post {
        success { echo 'Pipeline completed successfully.' }
        failure { echo 'Pipeline failed; follow rollback procedure.' }
        always { archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true }
    }
}
