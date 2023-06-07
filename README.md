# FastAPI_Docker
Developed an API using FastAPI that gets the data and stores the data in MongoDB. The entire process runs in containers using Docker 


**Steps**
  1.) 
      Developed an API that is used to get the details from a Public API to retrieve the data.
      The Public API used is **"https://randomuser.me/api/"**

   2.)
       Once the details is fetched, we will store the details in MongoDB.
       
   3.) 
       Run the application inside container using **Docker**
      
 Installed Modules
  
    1.) pymongo ==> Mongo DB Driver for Python
    2.) fastapi ==> API is developed using FastAPI
    3.) requests ==> In order to get the data from the Public API
    4.) uvicorn ==> To run the fastapi on the Uvicorn server
    
    All the modules are present in the "Requirements.txt"
    
    Dockerfile and DockerCompose files are present in the Code Repository
    
  Dockerfile
  
    FROM python:latest ==> Fastapi is developed in python. So using Python as Base Image

    WORKDIR /code ==> To make "code" as a directory inside container as working directory

    COPY ./requirements.txt /code/requirements.txt ==> copying the requirements file from local to container working directory

    RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt ==> Installing all the modules present in requirements.txt in docker container

    COPY ./app /code/app ==> copying all the source code from local to docker container file system

    CMD ["uvicorn","app.sourcecode:app","--host","0.0.0.0","--port","8000"] ==> Running the fastAPI server using CMD with options
    
  Docker Commands
  
    **docker build -t fastapi .** ==> fastapi == Image name, . == Dockerfile to build an image
   
  Docker Compose
      
      version: '3'
      services:
        mongodb:
          image: mongo
          ports:
            - 27017:27017
          volumes:
            - mongovolume:/var/lib/mongodb/data
        fastcontainer:
          image: fastapi
          ports:
            - 8000:8000  
      volumes:
        mongovolume: {}
    
    mongodb and fastcontainer are the names of the containers
    mongo,fastapi are the image names
    ports to bind the localhost with docker container ports
    volumes to persist the data, so that data is persisted even the container got deleted
    
   Docker Command
   
    docker-compose -f dockercompose.yaml up ==> To start the containers present inside the dockercompose.yaml file
    docker-compose -f dockercompose.yaml down ==> To stop the containers present inside the dockercompose.yaml file
    
    docker exec -it container_name bash ==> To run the container in bash mode
    
    docker ps ==> To list the containers
    
  Output of the details is fetched it will be stored in MongoDB. The data is persisted using **Docker Volumes**
  
  The Data stored in MongoDB
  
<img width="958" alt="image" src="https://github.com/phaniteja5789/FastAPI_Docker/assets/36558484/d32bc712-a8a3-4189-b469-b913e8780cdc">
