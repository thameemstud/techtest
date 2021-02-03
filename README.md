# Directory APP

## Please follow the given steps to run the `App`

### We can Run the `App` Manually install all the dependencies




### Step 2. Run and setup Manually

### Prerequisities

In order to run this app you'll need to install Python 3.6 

* [Python3](https://www.python.org/downloads/)

#### Follow the below steps, once you install the python

1. Download the project 

2. Go inside the project home folder `Directory`

3. Run command `pip3 install -r requirements.txt` to install all the projects dependencies 

4. Run command `python3 manage.py runserver` to start the project

5. Go to this url : http://127.0.0.1:8000/ and it will redirect to http://127.0.0.1:8000/directory/teachers/list/

6. For bulk upload, Click on the `create bulk` button on the top right in the teachers list page and upload the provided csv and zip files

7. If the user is not logged in then it will take to login page, then provide the given username and password 

       - Username : admin
       - Password : abc123

7. Also in the create bulk page it will hightlight any duplicates or incorrect data exists in the csv file.
