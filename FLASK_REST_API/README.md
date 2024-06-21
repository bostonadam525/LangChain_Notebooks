# Flask REST API
* How to create a simple REST API using Flask in Python.

1. create venv
  `python -m venv .venv`
  
2. activate venv
  source .venv/Scripts/activate 
  
  * shut down venv with: deactivate 
  
  
3. install dependencies
* pip install flask 
* pip install flask_restful (for REST API)
* pip install flask_sqlalchemy (ORM - object relational mapping to talk to database with REST API)


4. Create a requirements.txt file 
* pip freeze > requirements.txt (includes additional dependencies) --> could use this to install dependencies (pip install -r requirements.txt)



5. Create gitignore
* touch .gitignore (add .venv file to this --> don't want to send this to github!


## Now start building REST API 
1. Create file api.py 


2. at bottom of api.py put this code:

if __name__ == '__main__':
    app.run(debug=True)

This Python code checks if the script is being run directly (not imported as a module in another script). 
If it is run directly, it starts the Flask web server with debug mode enabled. 
Debug mode allows for automatic reloading of the application on code changes and provides a debugger on error pages.


3. Add sqlalchemy to program (and eventually the database)




4. Create new file 'create_db.py'

5. once created --> run in bash --> python create_db.py --> creates database in folder called 'instance'
