# Docker Compose

> Docker compose helps to composite (glue) multiple docker container together. The configuration is defined in `docker-compose.yml`.

- `docker compose up` - start the full application
- `docker compsose stop` - stop the service
- `docker compsose down` - stop the service, remove the containers
- `docker compose ps` - list the containers
- `docker compose run <container_name> CMD` - run the command in the container

## Create a `docker-compose.yml`

[medium article](https://towardsdatascience.com/docker-compose-for-absolute-beginners-how-does-it-work-and-how-to-use-it-examples-733ca24c5e6c) 

Note: string like this does not be quoted:
```
environment:
  MYSQL_DATABASE: mydocker
  MYSQL_ROOT_PASSWORD: root
  MYSQL_USER: user
  MYSQL_PASSWORD: mypassword
```

Usage:
```yml
version: '3'

services:
    service_name_1:
        container_name: container_name
        hostname: name_shown_in_host
        image: docker_image
        volumes:
          - HOST:CONTAINER
        environment:
          - MY_ENV_VAR=var1
        ports:
          - 54321:5432  # <HOST>:<CONTAINER>
        restart: unless-stopped

    # this service has a `Dockerfile`
    service_name_2:
        container_name: api_server
        hostname: NAME
        build:
          context: ./api_server
          dockerfile: Dockerfile
        ports:
         - 54322:5000
        volumes:
          - ./beersnob_api/src/:/usr/src/app/
          - /usr/src/app/node_modules
        restart: unless-stopped
        environment:
          CUSTOM_ENV: ${MY_ENV_CONFIG}
        depends_on:
          - another_service_name

    service_name_3:
        container_name: web_server_container
        hostname: web_server
        build:
          context: ./web_server
          dockerfile: Dockerfile
        ports:
        - 80:80    # http
        - 443:443  # https 
        volumes:
        - ./beersnob_webserver/src/test:/usr/share/nginx/html
        restart: always
        depends_on:
        - service_name_1
```

### terminology

- `container_name`: the name display at `docker ps`
- `hostname`: Inside this "custom network", you can access it by this hostname. Eample: Inside this network, the `web_server` service can access `api_server` by `http://api_server/`.
- `image`: docker image
- `volumes`: data persistence
- `environment`: environment variables, see **environment variable** section
- `ports`: mapping the ports `<HOST>:<CONTAINER_PORT>`
- `restart`
- `build`: build the image
    - `context`: the root of the service.
    - `dockerfile`: name of the Dockerfile
- `depends_on`: start the service after the specified service is on

### environment variable

> Every container can set different variable. If a container only has one running image, there might have special usage.

A `mysql` image, when you create a service by `docker-compose.yml`, you can create a mysql database with the name, password, database name you want.

For example:
```
services:
  my_db:
    image: mysql:oracle
    restart: always
    environment:
      MYSQL_DATABASE: mydb
      MYSQL_USER: user
      MYSQL_PASSWORD: mypassword
```

This will run a container that creates a database inside. With a database `mydb`, with `user` with `mypassword`

#### Use a file to set variable

The `environment` variable can be passed. In the above example, 

```yml
environment:
    CUSTOM_ENV: ${MY_ENV_CONFIG}
```

We can pass run it by:
```bash
docker compose --env-file <file_path> up
```

For example, suppose we have a directory tree:
```
.
└── env_config
    ├── env-dev
    └── env-prod
```

Do:
```bash
# for development 
docker compose --env-file env_config/env-dev up

# for production
docker compose --env-file env_config/env-prod up
```

## Auto-create a network for services

If you run docker via `docker compose up`. Docker will create a default network named `<DIR_NAME>_default`. All services will be in that network.

For example, in directory `docker-jave/` run `docker compose up`
```bash
./docker-java
├── app
│   ├── app.jar
│   └── Dockerfile
└── docker-compose.yml

# network
$ docker compose up
NETWORK ID     NAME                  DRIVER    SCOPE
224d6cbb275b   bridge                bridge    local
f9c1b067f950   docker-java_default   bridge    local  # a network created
b4c50088ab1b   host                  host      local
0d8cf1187c9f   none                  null      local
```

## UserId uid of the files and directories

[stackoverflow](https://stackoverflow.com/a/55241769) 

When I running a docker mysql container, the running container has changed the owner, as long as its some other files.
```bash
            #  user : group
drwxr-xr-x  3   999 derry 4096 12月 29 13:44 docker-java
```

Docker creates and populates the directory with the user that mysql image uses. That user, of course, has an `uid` within the container. That `uid` happens to be 999.

## Docker Compose wait for container X before starting Y

[discussion](https://stackoverflow.com/questions/31746182/docker-compose-wait-for-container-x-before-starting-y/41854997) 

Situation: 2 services initializing: 1 mysql database, 1 web application. When web app is initialized and trying to connect to database, the database is not ready yet. Therefore, the web app throws exception and exit. 

For now, the solution is by `restart`: 
```yml
version: '3'

services:
    db:
        //...

        // this to check if web app is ready
        healthcheck:
            test: ["CMD", "curl", "-f", "http://localhost:3306"]
            interval: 30s
            timeout: 10s
            retries: 5

    webapp:
        //...
        restart: on-failure
```

The `restart` option is ignored in swarm mode.
