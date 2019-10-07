# Bmi Calculator django-project

## Getting Started

First, clone the repository to your local machine:

```bash
git clone https://github.com/pnija/bmiproject.git
```
Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv -p python3 project-env
$ source project-env/bin/activate
$ cd bmiproject/
$ pip install -r requirement.txt
```
Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

