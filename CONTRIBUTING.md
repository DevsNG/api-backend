If you're here, thanks for deciding to contribute to this project - we need you!
The project is built with Python's [django](https://www.djangoproject.com) and [django rest framework](https://www.django-rest-framework.org), so be sure you have [Python already installed](https://www.python.org/downloads/) into your machine.

##  Getting Started
To contribute to the project, you can add new categories, update existing categories, make changes to improve security, change views methods, or. just something as little as converting a `PositiveIntegerField` to a `PositiveSmallIntegerField` in the models.
Just as long as there's a good enough reason for that, as *should* be stated in your pull request.

To start, fork the project and clone the copy into your local machine. Set up a virtual environment by running `virtualenv env` and activate the virtual environment by running `env\Scripts\activate`.
After activating the virtual env, install required modules by running `pip install -r requirements.txt`, assuming you have [pip installed](https://www.makeuseof.com/tag/install-pip-for-python/). 
Create a new Python file in your project root named `secrets.py`, and add: `SECRET_KEY = 'can_be-any%thing' `. Open the `settings.py` file and set `DEBUG = True`. Don't bother about AWS keys, as Django uses it's own media settings when DEBUG is set to True.

## Adding Categories

This project was designed using Django's best practices, including creating an `app` for each individual category, each with it's own directory with `serializers.py`, `views.py`, `urls.py` and `models.py` files. This helps in debugging and in modularity.
The `models.py` file is used to architect the fields present in the category you're adding. 
The `serializers.py` file is used for - you guessed it right - [serializing](https://www.django-rest-framework.org/api-guide/serializers/#serializers) our models.

To create a new category, run `python manage.py createapp <category_name>`. Add the new app to Django in the `settings.INSTALLED_APPS`. Add it into the admin panel by making appropriate changes in the `category_name.admin.py` file.
Open the `models.py` file and design your model. Please open  models file of another category app to follow the same procedure, e.g, if a category has a time field that represents just the *year*, without a day and month, please use a `PositiveSmallIntegerField()` instead of a `DateField()` or `DateTimeField()`
