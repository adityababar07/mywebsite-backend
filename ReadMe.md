<h1>This Is My Portfolio Webpage. :)</h1>
<p>
    This is a website built using react.js and django.
    <p>
        <ol>
            <li>React for frontend</li>
            <li>Django for backend</li>
        </ol>
    </p>
    <p>
    frontend would be hosted on firebase and backend on heroku 
    </p>
</p>


# for creating super user

pthon manage.py createsuperuser

# Deploying to firebase with comment
firebase deploy --only hosting -m "Deploying the best new feature ever."

# Delete database in heroku

1. heroku pg:reset DATABASE_URL
2. heroku run python manage.py ------
3. heroku restart