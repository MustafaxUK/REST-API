Set up & Installation


REQUIREMENTS

1. Make sure that Python is installed

 -- Windows --

 Run start & search for cmd
 Check if Python is installed by running: Python3
 if Python is an unrecognized command install the latest version of Python in the Microsoft Store

 -- macOS -- 
 
 If you have not installed Homebrew yet, install Homebrew by copy and pasting this in the terminal:

 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

 Open Homebrew and install python by copy and pasting:

 $ brew install python


2. Make sure that PIP is installed 

 -- Windows/macOS --

 Open your terminal
 Check if PIP3 is installed by typing: pip3 --version

 if PIP3 is not installed then download the get pip file from this link and store it in the same directory as Python is installed:

 https://bootstrap.pypa.io/get-pip.py

 Now open your terminal again, change the current path of the directory to the directory where the file exists and type:

 python get-pip.py

 You should now have successfully installed pip

 if you want to confirm that pip has been installed you can do so by running again:

 pip3 --version or pip -V


 3. Setting up a virtual environment

 

1. Clone the git repository and create and environment

 -- Windows --

 git clone https://github.com/MustafaxUK/REST-API.git

 -- macOS --

 git clone https://github.com/MustafaxUK/REST-API.git
