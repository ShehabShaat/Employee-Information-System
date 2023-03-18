



# Employee-Information-System

This is a web-based application built with Django that allows users to manage employee information. Users can perform various CRUD (Create, Read, Update, Delete) operations on employee records, such as adding new employees, viewing employee information, updating employee information, and deleting employee records.

## Installation

To use this project, you will need to have Python and Django installed on your computer.  

```
python -m pip install --user virtualenv
python -m virtualenv venv 
venv\Script\activate
```

To run this project on your pc fllow the below step:

### Step 1 :

```
git clone git@github.com:ShehabShaat/Employee_Information-System.git
cd Employee_Information-System
```

### Step 2 :

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
py manage.py runserver 8000
```

### Step 3:

This will start the development server, and you can access the application by visiting `http://localhost:8000/` in your web browser.
 [demo](ehab-shaat.herokuapp.com/)






# Database ERD
                   +-----------------------+
                   |     Department        |
                   +-----------------------+
                   | PK: id                |
                   | name        | Text     |
                   | description | Text     |
                   | status      | Integer  |
                   | date_added  | DateTime |
                   | date_updated| DateTime |
                   +-----------------------+

                              |
                              |
                    1       |
                   ___      |
                  |   | N   |
                  |   V     |
                   ---      |
                              |
                              |
                   +-----------------------+
                   |       Position        |
                   +-----------------------+
                   | PK: id                |
                   | name        | Text     |
                   | description | Text     |
                   | status      | Integer  |
                   | date_added  | DateTime |
                   | date_updated| DateTime |
                   +-----------------------+

                              |
                              |
                    1       |
                   ___      |
                  |   | N   |
                  |   V     |
                   ---      |
                              |
                              |
                   +-----------------------+
                   |       Employees       |
                   +-----------------------+
                   | PK: id                |
                   | code        | Char     |
                   | firstname   | Text     |
                   | middlename  | Text     |
                   | lastname    | Text     |
                   | gender      | Text     |
                   | dob         | Date     |
                   | contact     | Text     |
                   | address     | Text     |
                   | email       | Text     |
                   | department_id | FK(Department) |
                   | position_id   | FK(Position)   |
                   | date_hired    | Date     |
                   | salary       | Float    |
                   | status       | Integer  |
                   | date_added   | DateTime |
                   | date_updated | DateTime |
                   +-----------------------+

## Explain ERD
#### One Department can have multiple Employees, but each Employee can only belong to one Department. This is a one-to-many relationship, and is represented by the department_id foreign key in the Employees table.

### One position can have multiple employees, but each employee can only have one position. This is also a one-to-many relationship, and is represented by the position_id foreign key in the Employees table.

### There is no direct relationship between the department and position tables. However, both tables have a many-to-one relationship with the employees table through their foreign keys. This means that an Employee belongs to one Department and one Position, which are connected through the Employees table.
## Credits

This project was developed by [Shehab Shaat](https://github.com/ShehabShaat/) as part of Django-back-end.
### Special thanks to [Asem Saleh](https://www.linkedin.com/in/asem-k-saleh/) for his great efforts in providing this instructable
