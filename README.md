# Backend to `ChillEdu`

## How to install 
1. Download repo and work on the SHELL from the ChillEdu level, 
2. Initialize virtual environment in it: `python -m venv env`,
3. Run that venv: \
    LLINUX or MAC `source env/bin/activate`, \
    WINDOWS google say `\env\Scripts\activate.bat` if it doesnt work do it `cd env` `cd Scripts` `activate` `cd ..` `cd ..`
4. Install dependencies: `pip install -r requirements-dev.txt`,
5. Create a new file such as `.env.example` and chance his name to `.env`
6. Create a new secret key: `python generateSecretKey.py`
7. Copy it and paste it into `.env` up to SECRET_KEY \
    e.g. `SECRET_KEY=n-9#+mf&sziujs^g1!+liv5gn@%0*)7dp)gtm^16eqyl+bvjlr`
8. (optional) Change database settings in settings.py if you want to use different (non-sqlite) db backend, 
9. Make migrations: `python manage.py makemigrations`,
10. Migrate database: `python manage.py migrate`,
11. Create admin: `python manage.py createsuperuser`,
12. To run dev server: `python manage.py runserver`

## Tips for devs

### Dumping pip installations into the file
If you installed new pip dependency you need to allow others to know about it. To do so it is best to save all requirements
in one file, which in this case in named `requirements.txt`. You can do this by typing following command: 

`pip freeze > requirements.txt`


## Urls
`/admin` --> login to superadmin panel \
`/api/login` --> POST request about login \
`/api/children/registration` --> POST request about children registration \
`/api/children/<id>/` --> GET request about children detail \
`/api/addcash/<id>/` --> Add cash to children by id \
`/api/myadmin/<id>/` --> GET request about admin detail \
and a lot of more [`list`](https://chilledu-backend.herokuapp.com/api/)

## Hosting
The app is hosted on [Heroku](https://chilledu-backend.herokuapp.com/) 
1. Superadmin credentials _login:_ `admin` _password:_ `admin`
2. The app falls asleep after 30 minutes of inactivity.
3. The app wakes up for 10 seconds.

# Frontend to `ChillEdu`

https://github.com/Karina-00/Hackathon
