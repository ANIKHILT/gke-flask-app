# gke-flask-app

1. Create a GKE cluster: gcloud container clusters create my-cluster --num-nodes=3

2. Get credentials for the cluster: gcloud container clusters get-credentials my-cluster

3. Deploy to Kubernetes
   
Apply the Kubernetes deployment files:

i. kubectl apply -f deployment.service1.yaml

ii. kubectl apply -f deployment.service2.yaml

iii. kubectl apply -f deployment.service3.yaml


Summary:

a. Set up Flask application with routes and HTML templates.

b. Create requirements.txt to manage dependencies.

c. Create Dockerfile to containerize the application.

d. Build and push Docker images to Docker Hub.

e. Create GKE cluster using Google Cloud SDK.

f. Deploy Kubernetes deployment files to GKE.


This setup ensures that each service runs independently and uses the correct Docker images from your GitHub repository.
