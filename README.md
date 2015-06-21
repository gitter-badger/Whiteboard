Whiteboard
===

[![Join the chat at https://gitter.im/agundy/Whiteboard](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/agundy/Whiteboard?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Whiteboard helps keep track of your homework and grades for your classes and allows groups to keep track of members grades for membership requirements.

Getting Started:
----------------
To get a working development environment first ensure you have Pip installed.
https://pypi.python.org/pypi/pip#downloads
Once pip is installed run the following commands.
```bash
pip install -r requirements/common.txt
cd trackSchool
make start
```

To get a development environment with some test data already in the database, instead invoke
```bash
make load-data
```
A web server can be viewed at [localhost](http://127.0.0.1:8000). To get started with the local server use the following credentials:

A Student login is available with
Username: test@rpi.edu
Password: password

An Admin account can be accessed with
Username: admin
Password: password

Core Functionality:
-------------------
- Track School related assignments
- Integrate w/ Google Calender
- Manage Class Grades
- Prioritize by grade(impact on class standing)
- Recommend best time to do homework(consider sleep/early classes)
- Actively remind to input assignments

Fall Goals
------------
- Have ability to integrate with other calenders.
- Add a priority picker for homework to help decide what to work on
- Get a REST API set up to all for mobile development
- Grade Reporting to Groups / Group Requirements
- Email functionality actually working / Validating
- Deploy Beta Server
- Release version 1.0

Future Goals
------------

- Data Visualization
    - Course Grade over semester
    - Time Doing Homework
    - Bar graph of grades per class and per assignment type
- Grade predictor

Project Structure
-----------------

This project will attempt to adhere to PEP 8 Standards and follow a branching structure with a Master branch and Development branches as key components of the system. A great read on this branching structure can be read [here](http://nvie.com/posts/a-successful-git-branching-model/). Commits should be small with a succinct message that tells what was changed. Pull requests should be made when adding code into the development branch for code review.
