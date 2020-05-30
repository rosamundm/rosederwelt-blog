See my blog posts about setting up the environment:

https://rosederwelt.com/deploying-my-wagtail-blog-digital-ocean-pt-1/

https://rosederwelt.com/deploying-my-wagtail-blog-digital-ocean-pt-2/

If you clone this project, you'll have to change the settings path in `manage.py` and `wsgi.py` to:
`mysite.settings.dev_example`


If you don't set up a PostgreSQL one as shown in the Digital Ocean tutorial, you will also have to change the database to a sqlite3 one in `base.py`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Generate said database by running `python manage.py migrate`, then `python manage.py createsuperuser` so that you can log into the admin of your new site. (Then `python manage.py migrate` again for the change to take.)

Don't forget to set `DEBUG=True` in development and add `localhost` to `ALLOWED_HOSTS` so you can actually see stuff as you're developing! 

