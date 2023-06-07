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
    
  Output of the details is fetched it will be stored in MongoDB. The data is persisted using **Docker Volumes**
  
  The Data stored in MongoDB
  
    <img width="958" alt="image" src="https://github.com/phaniteja5789/FastAPI_Docker/assets/36558484/4c2aebff-5a2f-4c70-b2af-4cdba3e7498b">
