# CCNY Chatbot

Group project for Senior Project Design where we are creating an interactive chatbot for The City College of New York website (https://www.ccny.cuny.edu).

## Team Members

1. Cindy Weng Zhu
2. David Jimenez
3. Sheriff Sanni
4. Nahin Imtiaz
5. Sajid Mahmud

# Project Architecture
*The main repository https://github.com/cindyweng18/ccnychatbot had exceeded the bandwidth limit available. As a result we were forced to divide the client-side and server-side into two seperate repositories.*
The CCNY Chatbot project uses ReactJS and Django collaboratively to host the client and the server respectively. To that end, follow the following instructions to make sure the necessary components are installed on your system.

# Setting Up Installation
This readme includes the installation and running instructions for **both** the server and client. Following these instructions properly will install the entire project.
You must have **Node.js and NPM** (Node Project Manager) installed to run the React portion of the project. Also the Django back-end requires that you have **Python** installed on your operating system.
Download **Node.js** (includes NPM) [here](https://nodejs.org/en/)
Download **Python** [here](https://www.python.org/downloads/release/python-3101/)

# Setting Up the chatbot (janus)

_The following assumes [Git](https://github.com/git-guides/install-git) and [Git-lfs](https://git-lfs.github.com/) is installed on your operating system_

1. Clone the project using git `git clone https://github.com/sajidmahmud69/janus.git`
2. Open 2 _terminal_ windows if you are on unix based system such as ubuntu/mac or open 2 _command prompt_ windows if you are on windows. **Note: keep this 2 windows open at all times when you are running the program**
3. Navigate to the chatbot directory where you have cloned the project `cd chatbot` on both windows.
4. On one _terminal_ navigate to server directory using `cd server` and the other terminal navigate to client using `cd client`
5. **Skip to step 7 if you have a nvidia gpu on your computer**
6. **_IF YOU DO NOT HAVE A GPU_: go to `requirements.txt` file and delete `torch==1.10.0+cu113`, `torchaudio==0.10.0+cu113`, `torchinfo==1.5.3`, and `torchvision==0.11.1+cu113` and save the file**
7. On the window where server directory is open run the following commands:
- If you are on mac/ubuntu use the following procedures
   ```
   python3 -m venv chatbot
   source chatbot/bin/activate
   pip3 install -r requirements.txt
   ```
- If you are on windows use the following procedures
   ```
   python -m venv chatbot
   cd chatbot
   Scripts\activate
   cd ..
   pip install -r requirements.txt
   ```
8. _If you skipped step 6_ then install [pytorch](https://pytorch.org/) otherwise go to step 9
9. On the server window run the command `python manage.py runserver` if you are on windows, if you are one mac/ubuntu `python3 manage.py runserver`
10. This should start the django server ***Keep this window open***
11. Go to the other window where client directory is open
12.   ```
      npm install
      npm start
      ```
13. The first `npm install` will install all the reactjs packages using the node manage npm and second `npm start` will start the client side
14. Go to your preferred browser and go to the url `localhost:3000` and you should be ready to use the chatbot

# Use the chatbot
Once you go to the url `localhost:3000` wait for the welcome animation to finish then click on the **use chatbot** button to use the chatbot. That will bring a white page with messagin icon on the bottom right corner. Click on that icon and start messaging
