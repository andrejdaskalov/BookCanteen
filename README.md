# BookCanteen: A Design and Human-Computer Interaction Project
## Created by Andrej Daskalov 201125
---
## Overview of the project
This web app will allow students to create accounts and post listings for course materials they want to sell. Other students can browse these listings and purchase the materials they need. The app will handle payments and shipping, and provide a messaging system for buyers and sellers to communicate. The app will also have a search feature to help users find the materials they need more easily. The app will be built using Django, and will use a database to store user information, listings, and transaction data.

## Link to hosted app
[http://adaskalov.pythonanywhere.com/](http://adaskalov.pythonanywhere.com/)

## Source code available here on GitHub
[https://github.com/andrejdaskalov/BookCanteen](https://github.com/andrejdaskalov/BookCanteen)

## How to run the project
1. Clone the repository
2. Install the neccessary requirements:
```bash
pip install django Pillow
```
> You need Python 3.10 or higher to run this project.
This installs Django, a web framework and Pillow, a Python Imaging Library.
3. Run the server:
```bash
python manage.py runserver
```
4. Open the link provided in the terminal
> The default is http://localhost:8000/
> The admin user credentials are admin,admin
