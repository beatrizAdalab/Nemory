# Nemory

## Initialize database and migrations
#### before run the app, please run below command

    flask db init - this will create a folder inside the app directory.
    
    flask db migrate - this will create all the migrations.
    
    flask db upgrade
    

### Endpoints

|HTTP Verb|  Url Path                                 | Description                     |
|:------- |:------------------------------------------|:------------------------------- |
|  GET    | /nemory/api/v1.0/words                    |URL to read a collection of word |
|  GET    | /nemory/api/v1.0/words?word=term          |URL to read a single word filter by word|
|  GET    | /nemory/api/v1.0/words?category=verb      |URL to read a list of words filter by category |
|  GET    | /nemory/api/v1.0/users                    |URL to read a collection of users |
|  GET    | /nemory/api/v1.0/user/<id>                |URL to read an user detail by id |
|  POST   | /nemory/api/v1.0/user                     |URL to create new user|
|  PUT    | /nemory/api/v1.0/user/<id>                |URL to update an user filtered by id|
|  DELETE    | /nemory/api/v1.0/user/<id>             |URL to delete an user filtered by id|
|  GET    | /nemory/api/v1.0/activities               |URL to read a collection of activities|
|  POST   | /nemory/api/v1.0/activity                 |URL to to create new activity|
|  GET   | /nemory/api/v1.0/activity <br>  /nemory/api/v1.0/activity?action=ask               |URL to to create new activity. <br>  Allowed filters parametres: 'id_user','term','result' and 'action'|