Group 26 - Database and Cloud Security Assignment 1
Tang Yu Xuan 1211103236
Teh Yvonne 1211100571
Tan Hui Jeen 1211101196

Sneaker selling platform.

How to set up? 
Pre-requisite:
- Installed latest python (stable version)
- Installed SSMS

Setting up the Django project:
1. In the project folder, open the terminal then type 'pipenv shell' to activate the Python virtual environment. (ENSURE the virtual environment is always activated before running the server)
2. To install the required packages, type 'pipenv install -r requirements.txt'
3. Now Ensure that in the settings.py, the databases variable is set as follows:
   DATABASES = {
    'default': {
            'ENGINE': 'mssql',
            'NAME': 'yourdatabasename',
            'USER': 'yourssmsusername',
            'PASSWORD': 'yourpassword',
            'HOST': 'MYSERVER\SQLEXPRESS',
            'PORT': '',
            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',}, 
}
}
4. Now, to connect Django with SSMS, type 'python manage.py makemigrations' then 'python manage.py migrate'. This will connect Django with SSMS. If there are no errors means your Django has connected to SSMS successfully.
5. Log in to SSMS, and restore the database named test.bak file.
6. Now, run the Django server by typing 'python manage.py runserver'. A link '127.0.0.1' will be shown in the terminal, Ctrl + left click the link to access the link. Now the customer interface is accessed.

How to access the admin panel?
1. Once the database is restored, go to the endpoint '/admin'. ('127.0.0.1'/admin/) and enter the credentials:
username: pete
password: Pa$$w0rd

How to login into Customer Interface?
1. Once the database is restored, go to the endpoint '/'. ('127.0.0.1'/) and enter the credentials:
username: test123
passw0rd: fKHNBjjuc9k2Wmt

OR 

You can choose to sign up a new user.

  
