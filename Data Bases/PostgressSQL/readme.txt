# SQL query to create a todos table using sql query in supa base or neon.tech.

CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    title TEXT UNIQUE NOT NULL,
    description TEXT
);

# to add some data into the table using sql query.

INSERT INTO
     todos (title , description , status )
VALUES 
    ('lahore', 'any description', TRUE)


# to select and read data from a table using sql query

SELECT * FROM todos;

# to select the specific data from the table using sql query

SELECT title FROM todos;
or
SELECT title, description FROM todos;

# to select the date for a specific conditnon in the table using sql query

SELECT * FROM todos WHERE id=1;

and so on 

# Now we have to initialize the project and the library that we have to use to maintian our variations in the data base it alembic 
to add the package we have to tun,

poetry add alembic

#and after it we have to add

poetry add psycopg2-binary

#and after that we have to start the alembic

poetry run alembic init (folder name to start)

poetry run alembic init alembic 

change url of sqlalchemy.url = ******* file in alembic.ini file in alembic folder 

#now we have to creat a folder in the alembic folder that we will hae the <name>.py file that will provide the model shap of the table that we want to create in the data base. 

#I have created model folder and todo_model.py file in it.

#in the file we we will import these models

from sqlalchemy import Column, Integer, String, Boolean

and 

from sqlalchemy.ext.declarative import declarative_base

# after it we have to interconnect the model with env.py in alembic folder to sync with the alembic and for that we will import 

from models.todo_model import Base

#Now we have to run the model with variations

 -- poetry run alembic revision --autogenerate -m "create todos table"

 -- poetry run alembic upgrade head 

 