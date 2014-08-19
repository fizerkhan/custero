# Flask-Plivo

Boilerplate project template for [plivo](https://www.plivo.com/) with a Flask-based application.

### Install dependencies

Following steps are only needed one time

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Export configurations in development

    export PLIVO_AUTH_ID=<copy_from_pilvo>
    export PLIVO_AUTH_TOKEN=<copy_from_pilvo>
    export PLIVO_NUMBER=<copy_from_pilvo>
    export TEST_NUMBER=<test_mobile_number>

### Run server

    source venv/bin/activate
    foreman start

### Deploy to Heroku

1. Create an heroku application
2. Add an heroku git repo. **git remote add heroku <heroku_git_url>**
3. Push it to heroku. **git push heroku master**
