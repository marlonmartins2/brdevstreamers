# Br Dev Streamers - Backend

![Logo](./logo.svg)

The main purpose of this project is giving visibility to Brazilian Developers that stream in Twitch.


## Requirements

[x] Python 3

[x] Happyness 🙂


## How to run?

Create a `.env` file with the following content:

```
ENV=dev
CLIENT_ID= #client ID for your Twitch App
CLIENT_SECRET= #client Secret for your Twitch App
TWITTER_API_KEY=
TWITTER_API_SECRET= 
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_SECRET=
GITHUB_TOKEN=
PRIVATE_KEY= #private key (prod env only)
CERT= #cert (prod env only)
API_TOKEN= #token for private api (you choose here)
DB= #sqlite db location
```


## Set up the Postgres DB:

```
docker run -d \
    --name some-postgres -p 5432:5432 \
    -e POSTGRES_PASSWORD=$POSTGRES_PWD \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v /custom/mount:/var/lib/postgresql/data \
    postgres
```


Then you can run:

### `pipenv install`

Then:

### `pipenv shell`

And finally:

### `python main.py`


## Production Deployment

There's a Dockerfile in this project, so you can simply run:

### `docker build -t brdevstreamers-server .`


And

### `docker run --name brdevstreamers-server -p 8000:8000 -v "/home/brdevstreamers/letsencrypt:/etc/letsencrypt" -v "/home/brdevstreamers/db:/code/brstreamers" -d brdevstreamers-server`