# CIIE-Website Description

This project implements a webapp for event management with some key features such as email activation and mobile OTP verification. The project uses a simple API built in flask to simulate the transfer of sensitive data between the server and the API using 3DES technique and implementation of Mobile OTP verification as an additional security layer. A custom Flask API is built since in reality no payment API uses the 3DES algorithm and it just simulates the project title for Capstone.

This is repository contains a full project of Software Engineering and Capstone projects with the source code of the website, SRS report, MOM from the customer, Design Document, a Full report, Feedback from customer, Coding metrics, etc.

To run this webapp project, follow the instructions below.

Step:
1. Download the project in a new directory, e.g. "new_project". Now, enter the following commands in the terminal "cd new_project".
2. Now, in this directory you should see all the files of the project.
2.1 In order to run this project, you need to install python's official packet manager, i.e. "pipenv" on your system. 
2.2 After installing pipenv successfully, just run this command in terminal "pipenv install". 
Note: This command "pipenv install" should only be run in the directory where it contains the Pipfile & Pipfile.lock

After this command finishes execution, all the dependencies will be installed on your machine. Now, just activate the enviroment using "pipenv shell"

3. Change directory to NU_CIIE, "cd NU_CIIE"
4. Start the server, "python manage.py runserver".

Afer this, to run the payment API:
0. API program is in the "API" folder under the name "api.py".
1. Open another terminal and run "python3 api.py".
Note: Make sure to install Flask before running this.

Technologies Used:
1. python3.6
2. django ~>2.0

Coding metrics tool used:
1. Prospector
2. dodgy
3. mccabe
4. pep8
5. profile-validator
6. pyflakes
7. pylint
