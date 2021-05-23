import requests
import pytest


registered_User_id =-1
# ToDO a) Test the Register API by registering the user successfully using https://reqres.in/api/register and by logging in using the data used for the registration on API https://reqres.in/api/login. Pass it only if the user is created and able to login
def test_RegisterUserAndVerifyLogin():
    url_Register = "https://reqres.in/api/register"
    url_Login = "https://reqres.in/api/login"
    userDetails = {"email": "eve.holt@reqres.in", "password": "123"}

    responce_register = requests.post(url_Register,  data=userDetails)
    assert responce_register.status_code == 200, f"Registration Failed {responce_register.text} "

    registered_User_data = responce_register.json()
    global registered_User_id
    registered_User_id = registered_User_data["id"]
    print(f"registered_User_id {registered_User_id}")

    responce_login = requests.post(url_Login, data=userDetails)
    assert responce_login.status_code == 200, "Login Failed"


#TODO b) Using details of the user created in step a,  Delete the user registered above and assert an unsuccessful login attempt on login API https://reqres.in/api/login. Pass it only if the user created in Step a is deleted and unable to login
# Delete functionality of given linke is not working
# Test case can be designed as follows but it wont work until functionality is not implemented
def test_DeleteUserAndVerifyLogin():
    url_Delete = f"https://reqres.in/api/users/2"
    print(url_Delete)
    responce_register = requests.delete(url_Delete)
    assert responce_register.status_code == 204, "Delete Failed"

    url_Login = "https://reqres.in/api/login"
    userDetails = {"email": "eve.holt@reqres.in", "password": "123"}

    responce_login = requests.post(url_Login, data=userDetails)
    assert responce_login.status_code != 200 , "User is not deleted"


# Todo c) Assert a resource on https://reqres.in/api/unknown where page=1 and ID=2, year=2001
def test_ResourceData():
    flag_UresourcesFound = False
    endPoint = "https://reqres.in/api/unknown"
    responce = requests.get(url = endPoint)
    data = responce.json()
    for item in data["data"]:
        if item["id"]==2 and item["year"]==2001:
            print(item)
            flag_UresourcesFound = True
    assert True == flag_UresourcesFound, "resource not found where page=1 and ID=2, year=2001"


#TODO d) Assert a user on https://reqres.in/api/users?page=2 where the assertion is passed if the payload contains user with ID=7, Lastname =Lawson
def test_USERData():
    flag_UserFound = False
    endPoint = "https://reqres.in/api/users?page=2"
    responce = requests.get(url = endPoint)
    responce_data = responce.json()
    for item in responce_data["data"]:
        if item["id"]==7 and item["last_name"]=='Lawson':
            flag_UserFound = True
    assert True == flag_UserFound, "User not found with ID=7, Lastname =Lawson"


#TODO e) Assert the payload in API https://reqres.in/api/users/2 where it will check for first_name as "John" and fails the test if it's not "John"
def test_VerifyFirst_name():
    flag_UserFound = False
    endPoint = "https://reqres.in/api/users/2"
    responce = requests.get(url = endPoint)
    responce_data = responce.json()
    assert "John" == responce_data["data"]["first_name"], "first_name is not 'John' "



