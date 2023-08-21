pipeline {
    agent any

    stages{        
        stage('Deploy django') {
            steps{
                sh '''
                   ansible-playbook -i ~/workspace/ansible-project/ansible/hosts.yml -l app01 ~/workspace/ansible-project/ansible/playbooks/application-gunicorn-ngix.yml --extra-vars "DB_HOST=192.168.56.121 EMAIL_HOST=192.168.56.131"
                '''
            }
        }       
    }
}
