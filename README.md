# python_deploy
Repository Description:

This repository provides a step-by-step guide to creating a Python web application using the Flask framework, following the instructions from the YouTube video titled "How to Create a Web Application in Python using Flask" by Dave Gray. You can find the video here.

What's Included:

Clear and concise documentation with detailed explanations for each step.
Sample code and templates for building your Flask application.
Guidance on setting up a virtual environment and managing dependencies with pip.
Insights into creating routes, handling forms, and incorporating templates.
Tips and best practices for creating a functional and elegant web application.
Who Is This For:

This repository is suitable for Python developers, beginners and intermediates, looking to get started with web development using Flask. Whether you're new to Flask or want to review the process, this guide will help you build a web application from scratch.

Get Started:

Follow the step-by-step guide to build your own Flask-based web application. Start by setting up your environment and gradually progress towards creating a fully functional web app.

Feedback and Contributions:

We welcome contributions, suggestions, and feedback to improve this guide and make it more helpful for the community. Feel free to open issues or pull requests.


STEP BY STEP

install virtual enviroment: $ py -m venv .venv

activate virtual enviroment: $ .venv\Scripts\activate

deactivate virtual enviroment: $ (.venv) deactivate

install dependencies: $ (.venv) pip install requests python-dotenv Flask

upgrade the Python package manager: $ (.venv) py -m pip install -U pip

create requirements.txt: $ (.ven) pip freeze > requirements.txt

create .env file

create .gitignore
	.venv
	.env

create github repositorie: $ (.ven) git .init

create a production-quality pure-Python WSGI (Web Server Gateway Interface) server: $ (.ven) pip install waitress

update requirements.txt: $ (.ven) pip freeze > requirements.txt

create your app

manage version using github
@ (.env) git add . 
@ (.env) git remote add origin <githit_repositorie_link>
@ (.env) git push --set-upstream origin main


License:

This repository is open-source and available under the MIT License.

Happy coding and enjoy building your Flask web application!
