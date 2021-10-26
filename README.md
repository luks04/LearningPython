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

## Docker Deployment in Heroku
Heroku CLI needed.
The Flask app is containerized using Docker, so to deploy the app in a production environment it is recommended to use Gunicorn.

1. Clone the repo, checkout to the "main-docker" branch and login into Heroku CLI:
```sh
git clone https://github.com/luks04/LearningPython.git
cd LearningPython
git checkout main-docker
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
4. Deploy the app with a Dockerfile using gunicorn and a heroku.yml:
```sh
heroku create <app_name>
heroku stack:set container
git add .
git commit -m "<commit message>"
git push heroku <source_branch>:main
```
5. To show the logs use the next command:
```sh
heroku logs --tail
```

> Note: Use the next commands to upload changes to Heroku server: 
`Heroku remote repo and Heroku login is required`
```sh
git add .
git commit -m "<commit message>"
git push heroku <source_branch>:main
```