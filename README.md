
# Player Score Management APIs
I'm attempting to create Django based web backend with SQLite3 database using Docker.

### Requirements
``` 
1) Create 2 APIs using the Django REST framework

2) The APIs should return statistical information of: 

    a) The overall score of player grouped by country

    b) the name of all players who have an overall  score above 90 
```


## How to install and run the application
### 1. Pre-requisits
To run the project, you need to have Docker and Docker Compose installed.
```
https://docs.docker.com/get-docker/
https://docs.docker.com/compose/install/
```

### 2. Clone the project 
Clone the repository to the local
``` 
$ git clone 
```
cd in to the project directory.
### 3. Run the application with docker-compose
Once Docker and Docker Compose is installed, run the following command:
``` 
$ docker-compose up
```
To start the containers in demon mode, use the following command instead:
``` 
$ docker-compose up -d
```

## Application overview
Once the application is started, it will be accessible at 8000 port in the local system. 

### API description
#### 1. Average Score API
The api will return average of overall score of players grouped by country
```
GET : http://127.0.0.1:8000/Players_data/avgscore

Sample Response :
[
    {
        "Nationality": "Argentina",
        "Overall": 89
    },
    {
        "Nationality": "Belgium",
        "Overall": 89
    }
]
```

#### 2. Filter by Score API
The api will return the name of all players who have an overall score above requested value.
```
GET : http://127.0.0.1:8000/Players_data/filterscore/90

Sample Response :
[
    {
        "Name": "L. Messi"
    },
    {
        "Name": "Cristiano Ronaldo"
    },
    {
        "Name": "Neymar Jr"
    }
]
```
