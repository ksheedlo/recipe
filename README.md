# recipe

Software Engineering Lab - Fall 2012

## Project Setup

You'll need a machine running Ubuntu. Run the project setup scripts:

    $ sudo ./setup_workstation.sh
    $ ./setup_python_env.sh

Activate the virtual Python environment:

    $ . python_env/bin/activate

You should be good to go. Sync the db and start the server.

    $ cd app
    $ python manage.py syncdb
    $ python manage.py runserver

If you're reading this from a zipped distribution on CULearn, I've included a
copy of my most up-to-date database. Some of the entries in the db are
references to files that may or may not work based on your directory structure.
I've only ever run the code on two computers. Please don't hunt me down if you
can't get the db to work.

## Using the Web Server

Go ahead and start the server as described above. Browse to
http://localhost:8000/recipe/ You should see stuff. If the db is fresh, there
won't be any recipes. You can go to http://localhost:8000/admin/ and add things
from there. This is the default Django admin site. If you somehow get my db
slice to work, you won't be able to log in. Otherwise, you should have created
an account when you ran syncdb. As you add things to the admin site, they should
begin to show up on the home page and also generate their own detail pages.
Appetizers, cocktails, etc. will all show up on the appropriate category page.

## Quirks and Useful Details

You might have to run the ./build\_ui script to setup the initial HTML/CSS
template files. This is an artifact from a time when I thought the ui code was
going to be somewhat more complicated and have templating going on possibly in
CSS and Javascript files as well as the HTML, which turned out not to happen.

If everything blows up and you don't know what's going on, you might try setting
app.settings.RECIPE\_ROOT to this project's root directory. I've attempted to
detect it when settings load, and I've successfully used the same code snippet
in other projects, but it's untested for this project.

## Github

You can find the most up-to-date code on my github at
[recipe](https://github.com/ksheedlo/recipe). I'm not actively maintaining this
project.


