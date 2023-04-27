Hi,
I have created a docker-compose which installs all dependencies. The Fast API endpoint is in the port 8008.



## Deploy with docker compose

```shell
docker-compose up -d --build
```
## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE          COMMAND       CREATED              STATUS              PORTS                                               NAMES
7087a6e79610   5c1778a60cf8   "/start.sh"   About a minute ago   Up About a minute   80/tcp, 0.0.0.0:8000->8000/tcp, :::8008->8008/tcp   fastapi-application
```

After the application starts, navigate to `http://localhost:8008` in your web browser and you should see the following json response:


Stop and remove the containers
```
$ docker compose down
```
