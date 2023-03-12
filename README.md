# Employee_Information-System
## Database ERD
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



#### One Department can have multiple Employees, but each Employee can only belong to one Department. This is a one-to-many relationship, and is represented by the department_id foreign key in the Employees table.

### One position can have multiple employees, but each employee can only have one position. This is also a one-to-many relationship, and is represented by the position_id foreign key in the Employees table.

### There is no direct relationship between the department and position tables. However, both tables have a many-to-one relationship with the employees table through their foreign keys. This means that an Employee belongs to one Department and one Position, which are connected through the Employees table.
