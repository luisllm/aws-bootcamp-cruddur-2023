# Week 1 — App Containerization
## My journal - week1

-  **Did all the tasks in the week1 to-do list**

![image week1-to-do1](./images/week1-todo1.png)

![image week1-to-do2](./images/week1-todo2.png)

![image week1-to-do3](./images/week1-todo3.png)

![image week1-to-do4](./images/week1-todo4.png)

![image week1-to-do5](./images/week1-todo5.png)



-  **Pushed and tagged the images to DockerHub**

![image week1-images-in-dockerhub](./images/week1-images-in-dockerhub.png)


-  **Installed Docker on my local machine and pulled the images**

```
vagrant@ubuntu-focal64:~$ docker image ls
REPOSITORY                                                 TAG         IMAGE ID       CREATED        SIZE
luislongom/aws-bootcamp-cruddur-2023-frontend-react-js     1.0         253b333a0fbd   39 hours ago   1.15GB
luislongom/aws-bootcamp-cruddur-2023-backend-flask         1.0         0b1cc8aa9727   39 hours ago   129MB
```


-  **Documented the backend APIs with readme.com**

![image week1-backend-apis](./images/week1-week1-backend-apis.png)


-  **Implemented a healthcheck in the Docker compose file for the frontend**

```
  frontend-react-js:
    environment:
      REACT_APP_BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./frontend-react-js
    ports:
      - "3000:3000"
    volumes:
      - ./frontend-react-js:/frontend-react-js
    healthcheck:
      test: curl --fail http://localhost:3000 || exit 1
      interval: 60s
      retries: 5
      start_period: 20s
      timeout: 10s
```



-  **Run the Dockerfile command as an external script**

![image billing](./images/week1-.png)


-  **Launch an EC2 instance that has docker installed, and pull a container to demonstrate you can run your own docker processes**

![image billing](./images/week1-.png)



-  **Used multi-stage building for a Dockerfile build**

![image billing](./images/week1-.png)


-  **Research best practices of Dockerfiles and attempt to implement it in your Dockerfile**

![image billing](./images/week1-.png)


