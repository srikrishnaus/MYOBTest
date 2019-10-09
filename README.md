MYOB interview test project
Written API endpoints, deployable in Python, to return data in JSON format as per the requirements,
Built Python tests, to evaluate the Python code and the API integrations
Built a code deployment mechanism in Docker.
Registered & connected to Jenkins CI build evaluation system. 
Created a simple web interface to discover and execute the API's
Getting Started
These instructions will get an overview of the project up and running on your local machine. 
Prerequisites
Python
Flask
Pycharm
Docker
Github
Jenkins
Flask is a microframework for Python based library.
Flask is a good choice for a REST API because it is:
•	Written in Python (that can be an advantage);
•	Simple to use;
•	Flexible;
•	Multiple good deployment options;
•	RESTful request dispatching
Accessing
This simple web application is a static one and is accessible via http://127.0.0.1:5000/
Running the tests
Unit tests were performed using app_tests.py 
Deployment
Application was Integrated and deployed through Jenkins using Docker container.
Ubuntu image was used in Docker file as a base OS.
