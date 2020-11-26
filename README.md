# Todo API
## Setup
Build docker image:

`docker-compose build`

## Run the server
`docker-compose up`

If you want to change server's port, goes to `docker-compose.yml` and change the port number in `command`

## Testing
Run all unit tests in the project with command:

`docker-compose run --rm app sh -c "python manage.py test"`