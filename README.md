# CCNY Chatbot

Group project for Senior Project Design where we are creating an interactive chatbot for The City College of New York website (https://www.ccny.cuny.edu).

## Team Members

1. Cindy Weng Zhu
2. David Jimenez
3. Sheriff Sanni
4. Nahin Imtiaz
5. Sajid Mahmud

# Project Architecture

The CCNY Chatbot project uses ReactJS and Django collaboratively to host the client and the server respectively. To that end, follow the following instructions to make sure the necessary components are installed on your system.

# Setting Up Installation

You must have **Node.js and NPM** (Node Project Manager) installed to run the React portion of the project. Also the Django back-end requires that you have **Python** installed on your operating system.
Download **Node.js** (includes NPM) [here](https://nodejs.org/en/)
Download **Python** [here](https://www.python.org/downloads/release/python-3101/)

# Setting Up Your Local Repository

_The following assumes [Git](https://github.com/git-guides/install-git) is installed on your operating system_

1. In your Git terminal navigate to the directory in which you would like to save the project and run the following: 'git clone https://github.com/cindyweng18/ccnychatbot.git'
2. Navigate to the project folder by running the following: 'cd ./ccnychatbot'
3. Run the following command to install the proper dependencies: 'npm install'
4. You may also have to install the Django corsheader module. Do so with the following command: 'pip install django-cors-headers'

# Running the Project Locally

You must first open two terminals at two different directories. One in ('...ccnychatbot\server'), and another in ('...ccnychatbot\client').

1. Firstly, in the terminal opened to ('...ccnychatbot\server'), run the following command to run the server: 'python manage.py runserver 8000'
   _(The '8000' refers to the port number and may be replaced as you wish, however, the server and client cannot be hosted on the same port number)_
2. In the terminal opened to ('...ccnychatbot\client'), run the following command to run the client: 'npm start'
3. The webapp should open up in a tab on your default browser. Click the icon in the bottom right and ask away!
