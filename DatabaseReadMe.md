# Commands for setting up sql database 

1. sudo service postgresql start
2. sudo passwd postgres
3. su postgres
4. psql
5. create user "adityababar07" with encrypted password '149489';
6. create database mywebsite;
7. grant all privileges on database mywebsite to adityababar07;

# Commands for migrations

1. python manage.py makemigrations appname
2. python manage.py migrate appname
3. python manage.py runserver
