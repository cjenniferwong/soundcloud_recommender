
## TODO:
* Write a script to look at people I made recommendations to, and check how many of those recommendations were liked.

## Instructions:
* To run locally:
  1. Start by running the virtual environment: `pipenv shell`
  2. Run the webserver with `heroku local web`
  3. The site will be available on `localhost:5000`
* To deploy:
  1. Add and commit everything (`git add ...., git commit -m ....`)
  2. Push to heroku: `git push heroku master`
  3. Site will be available at [http://soundcloud-recommender.heroku.com/](http://soundcloud-recommender.heroku.com/)

* Database access instructions:
  1. Locally, run `sh .env` to setup the DATABASE_URL
  2. Run `heroku pg:psql` in terminal to connect to the database
