# Introduction
- Project for DevOps Systems Engineering
- Author: Qin Dong
- Date: June 9th 2018

# Problems and Research
The whole apporach is based on the holistic overview of this challenge through files:
docker-compose.yml --> Dockerfile (while confiuring docker and app) --> app.py --> Front-end
docker-compose.yml --> conf.d folder(while configuring flaskapp)

- The system needs to be configure with postgreSQL(port:5432), nginx(port:80), flaskapp(port:8080) with right ports
- Database(PostgreSQL) needs to be configure
- Initialize the database and process data migration before running the app
- The quantity should be an integer only
- Only handles the form submit, process the form validation in POST request


# Approaching Steps
- Modify all files through the process above

# Compile Instruction
To build: 
docker-compose up --build

To run:
docker-compose up
open the browser at localhost:8080

To remove:
docker-compose down

# Execution status

- Homepage shortcut

![Image text](https://github.com/gelatoonny/challenge/blob/master/images/home.png)

- Table shortcut

![Image text](https://github.com/gelatoonny/challenge/blob/master/images/table.png)



