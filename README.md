# Django

COMMAND FOR INSTALLATION OF DJANGO :
=====================================

>>  pip install django / pip3 install django / python -m pip install django / python3 -m pip install django



COMMAND TO CHECK IF DJANGO IS INSTALLED :
==========================================

>> pip show django / pip3 show django


COMMAND FOR CREATING DJANGO PROJECT :
=====================================

>> django-admin startproject projectname


COMMAND TO CREATE A DJANGO APPLICATION :
========================================

>> python manage.py startapp applicationname


COMMAND TO SEE THE MIGRATE SQLCODE :
======================================

>> python manage.py sqlmigrate applicationname filename

i.e python manage.py sqlmigrate dbapp 0001


COMMAND TO EXECUTE THE GENERATED SQL CODE:
===========================================

>> python manage.py migrate


COMMAND TO CREATE SUPERUSER :
==============================

>> python manage.py createsuperuser


COMMAND TO CONVERT MODEL CLASS INTO DATABASE SPECIFIC CODE :
=============================================================

>> python manage.py makemigrations


COMMAND TO RUN THE DJANGO SERVER :
==================================

>> python manage.py runserver


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


COMMAND TO OPEN SHELL/INERACTIVE CONSOLE MODE :
=================================================

> pyhton manage.py shell


COMMAND TO CHECK DJANGO DATABASE CONNECTION :
==============================================

>> from django.db import connection


COMMAND TO CREATE CURSOR OBJECT :
==================================

>> my_cursor=connectionn.cursor()


COMMAND TO EXIT FROM THE SHELL/ICM :
==================================

>> quit()





