DevOps Project 1 Documentation

Project Overview

This project demonstrates a three-tier architecture using Docker and Kubernetes. The architecture includes:

    Presentation Tier: User interface.
    Application Logic Tier: Business logic and process rules.
    Storage Tier: Persistent data storage.

Project Structure

Directories

    api-fron/: Frontend API.
    back-api/: Backend API.
    k8s/: Kubernetes manifests.
    mysql/: MySQL database setup.

    Key Files

    Jenkinsfile: CI/CD pipeline configuration.
    k8s/back.yaml: Backend service Kubernetes manifest.
    k8s/cluster-config.yaml: Cluster configuration.
    k8s/front.yaml: Frontend service Kubernetes manifest.
    k8s/ingress.yaml: Ingress controller configuration.
    k8s/sqldeploy.yaml: SQL deployment manifest.
    k8s/sql-pv.yaml: Persistent Volume configuration.
    k8s/sql-secret.yaml: Secret management for SQL.
    

    Commands and Usage
Docker Commands

    Build Image:
sudo docker build -t <image_name> <path>

Run Container:
sudo docker run -p <host_port>:<container_port> --name <container_name> --network <network_name> -it -d <image_name>

Delete Image:
sudo docker rmi <image_name> -f

Docker Compose Up:
sudo docker-compose up

Docker Compose Down:
sudo docker-compose down

Delete Container:
sudo docker rm <container_name> -f

Restart Docker:
sudo systemctl restart docker

Get Container IP:
sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name/id>

Create Network:
sudo docker network create -d bridge <network_name>

Connect Network:
sudo docker network connect <network_name> <container_name>

Inspect Network:
sudo docker network inspect <network_name>



MySQL Commands

    Connect to MySQL:
mysql -h <ip_address> -u <username> -p<password>


Kubernetes Deployment

Deploy the application using the provided Kubernetes manifests:

Apply backend services:
kubectl apply -f k8s/back.yaml

Apply frontend services:
kubectl apply -f k8s/front.yaml

Apply ingress controller:
kubectl apply -f k8s/ingress.yaml

Deploy SQL services:
kubectl apply -f k8s/sqldeploy.yaml
kubectl apply -f k8s/sql-pv.yaml
kubectl apply -f k8s/sql-secret.yaml


CI/CD Pipeline

The Jenkinsfile in this repository sets up a CI/CD pipeline that automates the build, test, and deployment processes. To set it up, follow these steps:

    Install Jenkins and necessary plugins.
    Configure Jenkins with your GitHub repository.
    Run the pipeline defined in the Jenkinsfile to build and deploy your application.

Contributing

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Create a new Pull Request.

    License

This project is licensed under the MIT License - see the LICENSE file for details.
Contact

Youssif Moustafa - LinkedIn
For more details, visit the GitHub repository.



![Screenshot from 2024-05-30 16-25-11](https://github.com/YoussifMoustafa/DevOpsProject1/assets/104654955/57951b23-291a-489b-aef4-68e8f1d26d90)
