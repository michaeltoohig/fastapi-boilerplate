# fastapi-boilerplate

FastAPI boilerplate based on the full-stack FastAPI repo by @tiangolo minus the frontend and docker. It also uses an `.env` file for envvars and a few other small changes.

## TODO

I have not yet handled multiple environments such as dev/testing/prod using different databases but I've accepted its okay for now but would accept a pull-request to fix that.

I also need to add the celery broker into the environment so you can choose your broker but now I've decided to use redis which is currently hardcoded into the celery setup just like the source material.
