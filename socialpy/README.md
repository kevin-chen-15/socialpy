Socialpy
========

Synopsis
========

This Django project is a conversion of my web design project in college.
The project's goal was to make a social media site as a way of learning
traditional web technologies like PHP and Javascript. I did this conversion
to learn how Django works. I hope this can be useful to anyone who wants to
learn Django.

This is a basic social media website where one can make an account using a
username and password. There, they can make a profile by inputing a name,
e-mail, and uploading a picture to serve as their avatar. Profiles can also
be commented on by those who have logged into the website.

Requirements
========================

Python Pillow requires a few libraries installed globally libjpeg-dev,
libfreetype6-dev, zlib1g-dev and libpng12-dev. In Ubuntu, use **apt-get** to
install these libraries:

    sudo apt-get install libjpeg-dev libfreetype6-dev

It is highly recommended to install the following python packages in a python
virtualenv, the benefits of using python virtualenv can be found in many resources.
Once a python virtualenv is activated, use **pip** to install the required
python packages in the requirements.txt. 

	pip install -r requirements.txt

Setting up the Superuser (see USERGUIDE)
=================================

To create a super user

    python manage.py createsuperuser

input the username, e-mail, and password of the super user.

Initiate the Project
=======================

After downloading the requirements, setting up the database, and creating the
superuser, first clean up the cache used by thumbnail:

	python manage.py thumbnail cleanup

then run the site using:

    python manage.py runserver

Django default IP is 127.0.0.1 (localhost), and at port 8000. You can specify
these options after runserver command.

# socialpy
