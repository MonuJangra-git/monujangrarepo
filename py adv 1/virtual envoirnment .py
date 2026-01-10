'''we create a virtual environment and install packages in it
using venv module which is included in standard library
to create a virtual environment we use following command in terminal or command prompt
python -m venv env_name  
this will create a folder with name env_name in current directory
to activate the virtual environment we use following command
on windows
.\env_name\Scripts\activate
on linux or mac
source env_name/bin/activate
to deactivate the virtual environment we use following command
deactivate
to install packages in virtual environment we use pip command
pip install package_name
to list installed packages we use
pip list
to freeze the installed packages in a file we use
pip freeze > requirements.txt
to install packages from requirements.txt file we use
pip install -r requirements.txt
this is how we can create and use virtual environment in python
we use virtual environment to manage dependencies for different projects
and to avoid conflicts between packages and their versions
this is very useful when we are working on multiple projects with different dependencies
also we can easily share our project with others by providing requirements.txt file
so that they can create virtual environment and install required packages easily
also virtual environment helps to keep our global python environment clean and organized
and avoid unnecessary packages installed globally
above all virtual environment is a best practice for python development
thus always use virtual environment for your projects
thank you

'''