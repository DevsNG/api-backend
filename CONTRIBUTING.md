If you're here, thanks for deciding to contribute to this project - we need you!
The project is built with Python's [django](https://www.djangoproject.com) and [django rest framework](https://www.django-rest-framework.org), so be sure you have [Python already installed](https://www.python.org/downloads/) into your machine.

## Table of Contents:
- [Getting Started](#getting-started)
- [Adding new categories](#adding-categories)
- [Modifying Categories](#modifyingupdating-categories)
- [Inputting Data](#inputting-data)
- [General Code Changes](#general-code-changes)
- [Community](#community)

##  Getting Started
To contribute to the project, you can add new categories, update existing categories, make changes to improve security, change views methods, or. just something as little as converting a `PositiveIntegerField` to a `PositiveSmallIntegerField` in the models.
Just as long as there's a good enough reason for that, as *should* be stated in your pull request.
*In whatever contribution you make, please update the `contributors.MD` file to include your NAME, SLACK USERNAME, GITHUB AND TWITTER LINKS, following the order seen in the file*

To start, fork the project and clone the copy into your local machine. Set up a virtual environment by running `virtualenv env` and activate the virtual environment by running `env\Scripts\activate`.
After activating the virtual env, install required modules by running `pip install -r requirements.txt`, assuming you have [pip installed](https://www.makeuseof.com/tag/install-pip-for-python/). 
Create a new Python file in your project root named `secrets.py`, and add: `SECRET_KEY = 'can_be-any%thing' `. Open the `settings.py` file and set `DEBUG = True`. Don't bother about AWS keys, as Django uses it's own media settings when DEBUG is set to True.

## Adding Categories

This project was designed using Django's best practices, including creating an `app` for each individual category, each with it's own directory with `serializers.py`, `views.py`, `urls.py` and `models.py` files. This helps in debugging and in modularity.
The `models.py` file is used to architect the fields present in the category you're adding. 
The `serializers.py` file is used for - you guessed it right - [serializing](https://www.django-rest-framework.org/api-guide/serializers/#serializers) our models.

To create a new category, run `python manage.py createapp <category_name>`. Add the new app to Django in the `settings.INSTALLED_APPS`. Add it into the admin panel by making appropriate changes in the `category_name/admin.py` file.
Also create a `urls.py` file for the app url patterns, and `include` it in the root urls, following the procedures used in other included apps' url patterns.
Open the `models.py` file and design your model. Please open  models file of an already established category app to see and follow the same procedure, e.g, if a category has a time field that represents just the *year*, without a day and month, please use a `PositiveSmallIntegerField()` instead of a `DateField()` or `DateTimeField()`; and also adding `null=True, blank=True, default='N\A'` as parameters to the model fields for optional fields, or fields which might have values in some instances of the category, and not in some.

After creating your models, create a `serializers.py` field to create your serializers - using preferably a `serializer.ModelSerializer` class extension. Then open up the `views.py` file and create a `generics` view, again, using an alreadt established app's views file as reference. Our API data is set to be handle `filtering`, `ordering` and `searching`, so please add that to the views.
Test your changes via the localhost, and try adding a few utems to your new category, assuming you kbow how to run local server and create super users in Django. If everything works well, use [this guide](https://guides.github.com/activities/forking/) to make a pull request.
Please ensure to add a very descriptive 'essay' about your changes and/or additions - seriously, please.

## Modifying/Updating Categories

Maybe for some reason you think an alread existing category or categories need(s) some changes to it's field, or should not be there at all, please also fork, clone, set up virtual environment, and `pip install -r requirements.txt` as above. Open the `models.py` file of the category's app directory and make your changes to it. If the changes should be in the views or serializers, please do that, while not forgetting to include changes and reason for them in your pull request.

## Inputting Data

Setting up views and serializers is not the major problem, data inputting is! So we'll greatly appreciate contributions in this category. To help fill/input data in any category, please fill out [this form](#). Before then, if the category has an ImageField(), please have the copy of the image uploaded to a cloud sharing site (preferably google drive or dropbox) and provide the sharing link in the form. Please make sure the uploaded image's shareable feature is turned on.
It should take 3-72 hours for the data to be reviewed and added by an admin, depending on amount of data to be processed.

## General Code Changes

This could be from added security, or code refactoring, or installation of a package to ease a process, or even taking your yime out to add comments to code lines. Whatever the case may be, please add it with the reason in your pull request.

## Community

You can find the Developers Nigeria (Devs Ng) slack group [here](https://devs.ng). Please be sure to send a join request.
We will take on community projects from time to time.

