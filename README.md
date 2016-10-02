# template-py
Repository to hold SOFE 3700 project template that is python and PostgreSQL db application that stores nba statistics in db and acts as a web server and creates a REST api to serve JSON files.

# Setup
- [Windows](#windows-setup)
- [Linux](#linux-setup)
- [Pycharm Setup](#pycharm-ide-setup)
- [Running Project](#run-project)
- [Testing Project](#testing)
- [Running Project Without Testing](#without-testing)
- [Additional Styling](#styling)

# Windows Setup
- TODO: need to add stuff about adding to paths to ensure exe compat
- Install git [if not already installed](https://git-scm.com/download/win)
- Clone project *run in cmd as admin*
```
git clone https://github.com/sealneaward/template-py
```
- Install [Python 2.7](https://www.python.org/downloads/release/python-2712/)
- Install dependencies *run in cmd as admin in project folder*
- More documentation on [venv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
```
pip install virtualenv virtualenvwrapper
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```
- Install [PostgreSQL](https://www.postgresql.org/download/windows/)
- Install [pgAdmin3](https://www.pgadmin.org/download/windows.php)

### PostgreSQL Database Setup
- Follow the instruction [here](https://confluence.atlassian.com/display/CONF30/Database+Setup+for+PostgreSQL+on+Windows)
- Make sure to create a new login user for **user**: *root* with **password**: *root*
- When creating a database, make sure to create a database with the following info

| Database       | Owner           | Password  |
| ------------- | ------------- | ----- |
| nba    | root | root |

![PostgreSQL Setup](img/schema.png)

- Use the .sql scripts in the db/schema folder to create the tables. Run as queries.

# PyCharm IDE Setup
- download and install [PyCharm](https://www.jetbrains.com/pycharm/)
- you can get a free license from JetBrains if you are a [student](https://www.jetbrains.com/student/)
- to add your venv as an interpreter follow these [instructions](https://www.jetbrains.com/help/pycharm/2016.1/adding-existing-virtual-environment.html)

![VENV Interpreter Setup](img/interpreter.png)

### PyCharm Debugging
- click on the dropdown arrow ![Arrow](img/arrow.png) and select edit configurations
- add a python configuration with the following settings

![Configuration Setup](img/configuration.png)

# Linux Setup
- Install git if not already installed
```
sudo apt-get install git
```
- setup virtualenvironment in project folder [more documentation](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
```
sudo pip install virtualenv virtualenvwrapper
virtualenv venv
source venv/bin/activate
sudo pip install -r requirements.txt
deactivate
```

### PostgreSQL Database Setup
- run these commands in terminal
```
sudo su postgres

```