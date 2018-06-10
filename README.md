# Introduction
- Project for DevOps Systems Engineering
- Author: Qin Dong
- Date: June 9th 2018

# Problems and Research
The whole apporach and problems are based the holistic overview of this challenge through files:
docker-compose.yml --> conf.d folder --> Dockerfile --> app.py --> Front-end
- The system needs to be configure with postgreSQL, nginx, flaskapp with right ports
- Database(PostgreSQL) needs to be configure
- The quantity should be an integer only
- All class objects need to be converted to string/int which is compatible with html(index, table)

# Approaching Steps
- Modify all files through the process above

# Compile Instruction
To build: 
docker-compose up --build

To run:
docker-compose up

To remove:
docker-compose down

