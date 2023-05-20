# Schools Intervention System
Group Name: LAMRtech

Group Members: Logan Halsall, Abegayle Williams, Mario Munroe, Raphiel Collins

## Note
**Uses a PostgreSQL database**
You will need to ensure you install PostgreSQL on your computer. You can do so by installing PostgreSQL from the link below and following the instructions:

<https://www.postgresql.org/download/>

When installing PostgreSQL, select the **PostgreSQL Server**, **pgAdmin 4** and **Command Line Tools** components. Ensure you deselect the _Stack Builder_ component during the installation as it is not necessary for this course.

- Install PostgreSQL
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
