# blog-ginko
A blog program for me to learn Django &amp; Web.

## Build & Run

### Dependencies

```bash
$ sudo pip install -U django djangorestframework pillow
```
`pillow` is required by Django `ImageField`.

### Create PyCharm Project

Create a new project in **PyCharm** with "File / New Project...", specify the path to `mysite` as the location, e.g., `/home/adam/github/blog-ginko/mysite`.

PyCharm will ask:
> The directory '...' is not empty. Would you like to create a project from existing sources instead?

Click Yes. Follow the instructions, then your projcet should be opened in PyCharm.

### Migrate DB

`Sqlite3` is used during the development. Run `migrate.sh` to migrate the DB:
```
$ ./migrate.h
```

`migrate.sh` is no magic but the following commands:
```bash
rm -r blog/migrations
python3 manage.py makemigrations ginko
python3 manage.py migrate
```

This will recreate DB tables (If your DB is sqlite3, there will be a file named "db.sqlite3" under current folder).
You need to do this almost whenever you change the fields of your models.

### Run

```bash
$ ./run.sh
```
Which is actually:
```
$ python3 manage.py runserver
```

Now you should be able to access `http://127.0.0.1:8000/` in your Browser.
