SET UP
1. Clone the git repository

 -- Windows --

 git clone https://github.com/MustafaxUK/REST-API.git

 -- macOS/linux --

 git clone https://github.com/MustafaxUK/REST-API.git

 2. Activate the virtual environment
  
  -- Windows --
 
 Open the terminal and move to the directory where the cloned repository is located. You can move a directory by typing "cd" and then the next folder you want to go into. For example: 

 cd Documents

 Do that until you are in the "Scripts" folder. For example:

 cd Documents/REST-API/.venv/Scripts

 Now that you are in the Scripts folder run:

 activate

 You should now see the .venv in the beginning

   -- macOS/linux --
 
 Open the terminal and move to the directory where the cloned repository is located. You can move a directory by typing "cd" and then the next folder you want to go into. For example: 

 cd Documents

 Do that until you are in the "Scripts" folder. For example:

 cd Documents/REST-API/.venv/Scripts

 Now that you are in the Scripts folder run:

 source activate

 You should now see the .venv in the beginning

 3. Move down to the REST-API folder

 -- Windows --
 
 You can move down a folder by simply typing:

 cd..

 Do so until you are at the REST-API folder

 -- macOS/linux --
 
 You can move down a folder by simply typing:

 cd ..

 Do so until you are at the REST-API folder

 4. Set FLASK_APP=application.py and run flask run

  -- Windows --

  Open the terminal and type:

 set FLASK_APP=application.py

 After you have set FLASK_APP you can type:

 flask run

 You should now get a few messages and the url to access the contacts

 -- macOS/linux --

 Open the terminal and type:

 export FLASK_APP=application.py

 After you have set FLASK_APP you can type:

 flask run

 You should now get a few messages and the url to access the contacts


FUNCTIONALITY

1. Getting all the contacts



2. Getting a contact by id



3. Adding a contact




4. Deleting a contact

