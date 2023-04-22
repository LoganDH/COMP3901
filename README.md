# Schools Intervention System

Group Name: LAMRtech

Group Members: Logan Halsall, Abegayle Williams, Mario Munroe, Raphiel Collins

## Note from Logan
Uses a postgresql database:
    - Install postgresql
    - Create user using the command: create user "comp3901";
    - Create database using the command: create database "comp3901";
    - Create password using the command: \password comp3901
        - The password is: comp3901
    - Change owner using the command: alter database comp3901 owner to comp3901;

### Set the environment variables so you can connect to the database.

```bash
export SECRET_KEY="Som3$ec5etK*y"
export DATABASE_URL="postgresql://comp3901:comp3901@localhost/comp3901"
```

Or on Windows:

```powershell
set SECRET_KEY="Som3$ec5etK*y"
set DATABASE_URL="postgresql://comp3901:comp3901@localhost/comp3901"
```

- Create a Python virtual environment e.g. `python -m venv venv` (You may need to use `python3` instead)

- Enter the virtual environment using `source venv/bin/activate` (or `.\venv\Scripts\activate` on Windows)

- Install the dependencies using Pip. e.g. `pip install -r requirements.txt`. Note: Ensure you have PostgreSQL already installed and a database created.

- Run the migrations by typing `flask db upgrade`.

- Start the development server using `flask --debug run`.








# NOTES FROM THE ORIGINAL REPOSITORY
### source: https://github.com/LoganDH/flask-db-demo-logan

# Example Database app

This is an example database app using PostgreSQL, Flask-SQLAlchemy and Flask-Migrate

You will need to ensure you install PostgreSQL on your computer. You can do so by installing PostgreSQL from the link below and following the instructions:

<https://www.postgresql.org/download/>

When installing PostgreSQL, select the **PostgreSQL Server**, **pgAdmin 4** and **Command Line Tools** components. Ensure you deselect the _Stack Builder_ component during the installation as it is not necessary for this course.

Create a database and ensure you have a database user that you can use to connect to the database.

To begin using this app you can do the following:

1. Clone the repository to your local machine.
2. Create a Python virtual environment e.g. `python -m venv venv` (You may need to use `python3` instead)
3. Enter the virtual environment using `source venv/bin/activate` (or `.\venv\Scripts\activate` on Windows)
4. Install the dependencies using Pip. e.g. `pip install -r requirements.txt`. Note: Ensure you have PostgreSQL already installed and a database created.
5. Edit the `app/__init__.py` file and enter your database credentials and database name.
6. Run the migrations by typing `flask db upgrade`
7. Start the development server using `flask --debug run`.

## Separate Config file

I have included a separate config file `app/config.py` that can be used for setting up
configuration for different environments e.g. Development and Production

Edit `app/__init__.py` and uncomment the following lines:

```python
# from .config import Config
...
# app.config.from_object(Config)
```

Using the separate config file will also require you to set environment variables on your local computer or server at the command line. For example on Linux or MacOS:

```bash
export SECRET_KEY="my-super-secret-key"
export DATABASE_URL="postgresql://yourusername:yourpassword@localhost/databasename"
```

Or on Windows:

```powershell
set SECRET_KEY="my-super-secret-key"
set DATABASE_URL="postgresql://yourusername:yourpassword@localhost/databasename"
```

### .env Files

You can also create a `.env` file in the root of your project and add your Environment variables there. See `.env.sample` as an example. The `config.py` file is already setup to automatically load the `.env` file.
