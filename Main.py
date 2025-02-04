# Here is a playground where we will try importing a Python library known as "requests" to have
# our local Pycharm IDE able to send out HTTP requests (the protocol most client/server relationships
# use on the internet use to talk to each other in the hypertext transfer protocol)
# Those HTTP requests will be used to talk to an API, i.e. someone else's application out there on the internet
# that could be used to provide us some data, or that we could modify/delete/create some data on their server/application
# Here is the official documentation website for the Python requests library: https://requests.readthedocs.io/en/latest/user/quickstart/
# First we will need to use the "pip install requests" console terminal command in order to import our library into Pycharm
# it to use the library

# For some reason I had trouble using Windows Powershell and running the "pip install requests" command, however Pycharm
# had an in built feature on how to install the library

# Now that we have used the python package manager known as pip to import the needed library, lets import the library
# into this project
import requests
# The json library allows us to manipulate the JSON we will get back after an HTTP request is sent (the response from the server will usually be in the format of JSON)
import json

# Now that we have the requests library imported into our Python project, we can use it to send HTTP requests
# Lets try sending an HTTP request to a dummy API that someone has thoughtfully decided to host for people trying to play around such as myself
# API's that we can use throughout this project are:
# https://jsonplaceholder.typicode.com/
# httpbin.org/
# https://gorest.co.in/
# Common HTTP Methods:
    # GET – Retrieve data from the server (e.g., get user information).
    # POST – Send data to the server to create a new resource (e.g., register a new user).
    # PUT – Update an existing resource completely (e.g., edit user details).
    # PATCH – Partially update a resource (e.g., update just the email).
    # DELETE – Delete a resource (e.g., remove a user account).

# We will need to send the correct HTTP request to the correct API endpoint that we can get a response back from
# We will try each basic HTTP request operations as listed above
# First lets try a GET HTTP request
#Note how we are capturing the response we get back from the server when we use the request libarary's GET method to send out an HTTP GET request to the API endpoint we specify
responseObject = requests.get('https://jsonplaceholder.typicode.com/posts')
#Lets print the response we got back from the server after sending our GET HTTP request
print(responseObject, "\n")
#We should have gotten a response code of 200, which means everything went ok
#Note how the responseObject we got back when printed prints as <Response [200]>, the actual "Response" part of the object can be broken up further if we know how to use the requests python library
#To show case this, we can use the nested print(type()) function to show us what type of response we got back from the server, and we can see the requests library has handled the response in its own built in class object.
#This class allows us to use methods to further parse the response we got back from the server. Try printing the response object and using the dot "." operator at the end to see all the availble methods you could use when printing the object
#such as: print(responseObject.)
print(type(responseObject))
#The inbuilt .content member of the class we get as a response allows us to view the data in bytes, as denoted by the "b' " when we print the .content member of the response object/class we receive back
print("Here is the response we got back in bytes: ", responseObject.content)
print("Here is the JSON of the response we got back: ", responseObject.json())
print(type(responseObject.json()))
print("Lets now try printing the JSON in a pretty way by using the JSON library: ")
#Capturing JSON data into a variable to pass to the JSON library
captureJSONData = responseObject.json()
prettiestJSONoutputEver = json.dumps(captureJSONData, indent=4)
print(prettiestJSONoutputEver)

print("Does printing directly without capturing data into a variable work?: ", "\n", json.dumps(responseObject.json(), indent=4))


# Next lets try a POST HTTP request, this will allow us to use their API to post something on their server
# This will be our data payload, in a dictionary/JSONesque format
dataPayloadToSendInPostHTTPRequest = {'name':'Jynx Maze', 'job':'Cocksucker'}
responseObjectForPostRequest = requests.post('https://reqres.in/api/users', dataPayloadToSendInPostHTTPRequest)
print("This is our HTTP Post Request response: ", responseObjectForPostRequest)
print("Lets break up the post request object we received: ")
print("Here is the .content member of the class we received back: ", responseObjectForPostRequest.content)
print("Here is the JSON function used against the object we received back: ", responseObjectForPostRequest.json())

#Lets see if we can retrive the user we just submitted to the API by using the HTTP GET request again
dataPayloadWeWantToFindOnAPIserver = {'name':'Jynx Maze', 'job':'Cocksucker'}
secondGetResponseObject = requests.get('https://reqres.in/api/users/966')
print("This is the second GET HTTP request we've gotten, lets see the status code, and then unpack the object later : ", secondGetResponseObject)
print("Using the .content member: ", secondGetResponseObject.content)
print("Using the .json() function: ",secondGetResponseObject.json())

# Next lets try a PUT HTTP request, this will allow us to completely update the object we previously posted to their server in the code above

# Next lets try a PATCH HTTP request, this will allow us to partially update the object we previously posted to their server in the code some time above

# Next lets try a DELETE HTTP request, this will allow us to delete the object we previously posted to their server in the code up above

# Next lets try another GET HTTP request to see if we can still get the object we previously posted and deleted. This should fail if our DELETE HTTP request above was successful
