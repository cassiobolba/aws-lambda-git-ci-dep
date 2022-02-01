# aws-lambda-deploy
Project to deploy an AWS Lambda Function and AWS API Gateway using Git Lab CI/CD.

## Resources
* Open source API from http://api.openweathermap.org
* AWS Lambda
* AWS API Gateway
* Git Lab CI

## Basic Description
1 - The open source API provides a path to retrieve temperature data from their database by passing a city name   
2 - AWS lamda hits the API passing the city name to retrieve it temperature in a customized string   
3 - API Gateway deploy an endpoint to AWS which receive the city like: awsarn<my-deploymen>/weather/{city name}   
4 - City name in the endpoint path is read by Lambda   
5 - The Git CI pipeline is reponsible for deploying the Lambda Function and API Gateway to AWS automatically   
6 - Git CI uses standard Git Runner and AWS CLI with AWS SAM CLI to make the deployment   
7 - If the deployment is made from a branch, it deploys to "dev environment", if from master deploy to production   
8 - Git Lab is also responsible for code versioning control   
