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
Including cookies, sessions, HTTP protocol and SQLALchemy

To deploy the app on a production environment it is recommended to use Gunicorn.
1. Delete Heroku remote old repository
```sh
git remote rm heroku
```
2. Check remote repositories
```sh
git remote -v
```
3. Deploy the app with Procfile and gunicorn
```sh
heroku login
git add .
git commit -m "<commit message>"
git push heroku <source_branch>:main
```

Use this comand to try the app locally
```sh
heroku local
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