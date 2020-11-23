# Nemory

Nemory is a full REST API built with flask to manage an application for memorizing English vocabulary for Spanish speakers.
It is the first test version developed for the BACKEND-DEVELOPMENT course taught by [REDI](https://www.redi-school.org/career-program-munich).



<br>
## Initialize database and migrations
#### before run the app, please run below command

    flask db init - this will create a folder inside the app directory.
    
    flask db migrate - this will create all the migrations.
    
    flask db upgrade
    
### Token
|HTTP Verb|  Url Path                                 | Description                     | Comments                        |
|:------- |:------------------------------------------|:------------------------------- |:--------------------------------|
|  POST   | /nemory/api/v1.0/user/login               |URL to read a collection of word |   Payload: Json with name and password: <br>![get login](./readme-images/payload_token.png?raw=true "Optional Title") <br> Response ok:  <br>![get login](./readme-images/response_token.png?raw=true "Optional Title")|


<br>
Use of header token for endpoints with security:

![get login](./readme-images/header_token.png?raw=true "Optional Title")


<br>

### Endpoints

|HTTP Verb|  Url Path                                 | Description                     | Comments                        |
|:------- |:------------------------------------------|:------------------------------- |:--------------------------------|
|  GET    | /nemory/api/v1.0/words                    |URL to read a collection of word | public access                   |
|  GET    | /nemory/api/v1.0/words?word=term          |URL to read a single word filter by word|public access <br>query string: term <br> result ok: ![get words by term](./readme-images/response_ok_words_by_term.png?raw=true "Optional Title")  <br> not found the term: ![get words by term](./readme-images/response_not_found_term.png?raw=true "Optional Title") |
|  GET    | /nemory/api/v1.0/words?category=verb      |URL to read a list of words filter by category |public access <br> query string: category  <br> result ok: ![get words by term](./readme-images/response_ok_by_category.png?raw=true "Optional Title") <br> not found the category: ![get words by term](./readme-images/response_not_found_term.png?raw=true "Optional Title") |
|  GET    | /nemory/api/v1.0/users                    |URL to read a collection of users |token access     <br> result ok: ![get users](./readme-images/users_ok.png?raw=true "Optional Title")|
|  GET    | /nemory/api/v1.0/user/id               |URL to read an user detail by id |token access |
|  POST   | /nemory/api/v1.0/user                     |URL to create new user| public access <br> payload to create a new user: ![get words by term](./readme-images/payload_new_user.png?raw=true "Optional Title")<br>  name and email must be unique <br> if ok we receive the object of the new user|
|  PUT    | /nemory/api/v1.0/user/id                |URL to update an user filtered by id| token access  <br> You can update the following fields: name, lastname, email or password all or just the ones you need <br> example payload to upload user: ![upload user](./readme-images/upload_user.png?raw=true "Optional Title")|
|  DELETE    | /nemory/api/v1.0/user/id             |URL to delete an user filtered by id|token access |
|  GET    | /nemory/api/v1.0/activities               |URL to read a collection of activities| token access <br> activities: ![get activities](./readme-images/activities_ok.png?raw=true "Optional Title")|
|  POST   | /nemory/api/v1.0/activity                 |URL to to create new activity|token acces <br> payload new activiy: ![new activity payload](./readme-images/payload_new_act.png?raw=true "Optional Title") <br> result ok: ![ok new activity ](./readme-images/success_act.png?raw=true "Optional Title") <br> When the action is "ask" and the payload is correct, it returns result: True, otherwise False|
|  GET   | /nemory/api/v1.0/activity <br>  /nemory/api/v1.0/activity?action=ask               |URL to to create new activity. <br>  Allowed filters parametres: 'id_user','term','result(0 "false" or 1 "true")' and 'action'|token access |