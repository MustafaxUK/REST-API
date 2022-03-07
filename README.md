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


FUNCTIONALITY WITHOUT USING POSTMAN

1. Getting all the contacts

 To get all the contacts you can simply 

open the URL("http://127.0.0.1:5000/") and add contacts after the slash:

http://127.0.0.1:5000/contacts

You should now see all the contacts added prior

2. Getting a contact by ID

 Whenever we create a new contact a new ID will be assigned to the contact. The ID can be used to access a specific contact by adding another "/<id> after "contacts" for example:

 http://127.0.0.1:5000/contacts/1

 You will now only get the contact with the ID 1

 This can be done with any contact

3. Adding a contact

 To add a contact:
 
 3.1 Open the terminal
 3.2 Type: py 
 3.3 >>>: from application import db, Contact
 3.4 >>>: db.session.add(Contact(phone_number="ANY NUMBER", name="ANY NAME", email="ANY EMAIL"))
 3.5 >>>: db.session.commit()

 Now you should have added successfully a new contact using the constructor from the Contact class. 

4. Deleting a contact

 We delete contacts by their ID's to do that:

 4.1 Open the terminal
 4.2 Type: py
 4.3 >>>: from application import db, Contact
 4.4 >>>: contact = Contact.query.get("ANY ID")
 4.5 >>>: db.session.delete(contact)
 4.6 >>>: db.session.commit()

 You should now have successfully deleted a contact by it's id



