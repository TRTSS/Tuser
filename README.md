# Ziplit.Tuser
## Free quick user bases for your projects

Tuser allows you to create databases for users of your project.

## Features
* Quick start. You don't need to design a database for a long time - just one command will save you from torment.
* Safety. The data is completely secured by an encryption system and access level differentiation.
* Comfortable. All in one package without unnecessary things.
* Completely free of charge. Although I will not refuse donations :0

## Setup

### Install via pip
Enter the following line in the terminal
```
    $ pip install tuser     // in case pip using
    $ pip3 install tuser    // in case pip3 using
```

### Create base for project
Now you need to create a database and attach it to your project. To do this, enter the following command:

```
    $ tuser quick
```
Then choose a name for your database:
```
    Base name: testbase
```
After that Tuser will create config file in 'site-packages' folder. Do not change it and keep it safe.

## Terminal commands
### See structure of your base
To see the structure of you base type in the terminal following line:
```
    $ tuser struct
```
### Add field to your base
To add field to your base type following line:
```
    $ tuser add-field [field-name] [int/varchar]
```
At the moment Tuser can add 2 types of fields to your base:
* Integer (int)
* Varchar (varchar)

Max length of varchar is 255 chars.

### Recreate or clear base
For create new base or complete clear existing user 'quick' command:
```
    $ tuser quick
```
## Using in project
### Concierge checkpoint
Create a Concierge object. Concierge is a checkpoint for all users and connections with Tuser.
```python
    from Tuser.Concierge import Concierge
    checkpoint = Concierge()
```
### Concierge structure 
Concierge is an object that store all your Tuser base data from name to pass data. Also contains user object.
```
    Concierge fields:
        - User  (public)
        - Login (private)
        - Pass  (private)
        - Base  (private)
      
    Concierge methods: 
        - Register      (username: str, password: str)              -> OperationStatus 
        - Login         (username: str, password: str)              -> OperationStatus 
        - SetUserField  (fieldName: str, fieldValue, userId = None) -> OperationStatus 
        - GetUserField  (fieldName: str, userId = None)             -> OperationStatus
        
    Concierge response template: OperationStatus object
```

### User registration 
Use _Register_ method of Concierge object to add a new user. If there is no configuration file, Tuser will throw an exception.
        Takes 2 arguments username and password. Returns the operation status object.
```python
    from Tuser.Concierge import Concierge
    checkpoint = Concierge()

    checkpoint.Register("some_username", "some_password")
```
### User login
Use _Login_ method of Concierge object to log in user. If there is no configuration file, Tuser will throw an exception. Takes 2
        arguments: username and password. Returns the operation status object. In case of successful authorization,
        the Concierge object will contain the user object in the 'user' field.
```python
    from Tuser.Concierge import Concierge
    checkpoint = Concierge()

    checkpoint.Login("some_username", "some_password")
```
### Set user field
Use _SetUserField_ method to set a value to user field. If there is no configuration file,
        Tuser will throw an exception. Takes 2 required arguments: field name and value. Takes 1 optional
        argument - User ID. If the user ID is not set, the current authorized user from the Concierge object is taken
        as the ID. Returns the operation status object.

Make sure you are setting an existing field. To create user field use [Tuser terminal command](#add-field-to-your-base).
```python
    from Tuser.Concierge import Concierge
    checkpoint = Concierge()

    checkpoint.SetUserField("user_score", 500)      # without pointing user id. Will set a field for current authorized user from Concierge object
    checkpoint.SetUserField("user_score", 500, 4)   # with pointing user Id
    status = checkpoint.SetUserField(fieldName="user_score", fieldValue=500, userId=5) # recommended form for calling method
```
### Get user field 
Use _GetUserField_ method to get value of user field. If there is no configuration file, Tuser will
        throw an exception. Takes 1 required argument - the name of the field. Takes 1 optional argument - User
        ID. If the user ID is not set, the current authorized user from the Concierge object is taken as the ID.
        Returns the operation status object. 


Value of the field will be stored in _data_ field of operation status object.

Make sure you are setting an existing field. To create user field use [Tuser terminal command](#add-field-to-your-base).
```python
    from Tuser.Concierge import Concierge
    checkpoint = Concierge()

    status = checkpoint.GetUserField("some_field")
    value = status.data
```

### Operation status object
It is an object that contains data of sent request to the Tuser API. Here is a structure of OperationStatus and its possible fields.

| Name          | Type          | Description                                    |
|---------------|---------------|------------------------------------------------|
| ok            | required bool | Result of the request                          |
| systemVerbose | optional str  | Message if the 'ok' field is False             |
| errorCode     | optional int  | Code of error if the 'ok' field is False       |
| data          | optional Any  | Field that may contain some data from requests |

