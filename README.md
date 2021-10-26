# LearningPython and Docker

## Python bases
It has many examples of using python:
- Lists / Lists as Stacks / Tuples / Dictionaries / Sets / Queues
- String formatting / Logical operators / Loops / Functions
- Regular expressions / Recursion / Files management
- OOP (Object Oriented Programming) / Classes / Inheritance
- Threads (Multiprocessing) / Asynchronous / Decorators
- Generators / Iterators / SQL and NoSQL Databases use

## Flask app
It contains a Flask app too with some templates and API Rest services examples. 
Including cookies, sessions, HTTP protocol and SQLALchemy.

## Gunicorn Deployment in Heroku
Heroku CLI needed.
To deploy the app in a production environment it is recommended to use Gunicorn.

1. Clone the repo, checkout to the "main-gunicorn" branch and login into Heroku CLI:
```sh
git clone https://github.com/luks04/LearningPython.git
cd LearningPython
git checkout main-gunicorn
heroku login
```
2. Delete Heroku remote old repository:
```sh
git remote rm heroku
```
3. Check remote repositories:
```sh
git remote -v
```
4. Use this command to try the app locally:
```sh
heroku local
```
5. Deploy the app with a Procfile using gunicorn:
```sh
heroku create <app_name>
git add .
git commit -m "<commit message>"
git push heroku <source_branch>:main
```
6. To show the logs use the next command:
```sh
heroku logs --tail
```
## Docker
The Flask app is containerized using Docker.
To deploy with Docker on Heroku (Heroku CLI needed):

```sh
heroku login
git add .
git commit -m "<commit message>"
heroku stack:set container
git push heroku <source_branch>:master
```

To show the logs
```
heroku logs --tail
```