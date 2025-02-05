# Here is a playground where we will try importing a Python library known as "requests" to have
# our local Pycharm IDE able to send out HTTP requests (the protocol most client/server relationships
# use on the internet use to talk to each other in the hypertext transfer protocol)
# Those HTTP requests will be used to talk to an API, i.e. someone else's application out there on the internet
# that could be used to provide us some data, or that we could modify/delete/create some data on their server/application
# Here is the official documentation website for the Python requests library: https://requests.readthedocs.io/en/latest/user/quickstart/
# First we will need to use the "pip install requests" console terminal command so we have can the python "requests"
# library on our machine. Once it's on our machine we can import the library into Pycharm to use it on this project

# For some reason I had trouble using Windows Powershell and running the "pip install requests" command, however Pycharm
# had an in built feature on how to install the library when I tried importing it here in the project. I just had to right click
# on the import statement and it was able to import the "requests" library through a drop down menu. I would definitely research
# why the "pip install requests" was not able to fully install on the machine through the Windows Powershell command line.

# Now that we have the Python "requests" library on our machine, we are now able to use it and import it into this project
import requests
# The json library allows us to manipulate the JSON we will get back after an HTTP request is sent (the response body from the server will usually be in the format of JSON)
import json

# Now that we have the requests library imported into our Python project, we can use it to send HTTP requests
# Lets try sending an HTTP request to a dummy API that someone has thoughtfully decided to host for people trying to play around such as myself
# API's that we can use throughout this project are:
# https://jsonplaceholder.typicode.com/
# httpbin.org/
# https://gorest.co.in/

# I have decided to go with https://gorest.co.in/ since it will actually allow POST requests to go through and modify it's server data base
# (i.e. it will actually hold the data you are sending it instead of just echoing it back in a response much like how the other API servers I listed
# and tested will do). This server will actually allow us to test a HTTP GET request after we have sent a HTTP POST request to the server.

# Common HTTP Methods:
    # GET – Retrieve data from the server (e.g., get user information).
    # POST – Send data to the server to create a new resource (e.g., register a new user).
    # PUT – Update an existing resource completely (e.g., edit user details).
    # PATCH – Partially update a resource (e.g., update just the email).
    # DELETE – Delete a resource (e.g., remove a user account).

# It is imperative that when working with an API you choose, no matter which one you choose, you should look around at the API website
# and find as much documentation as you possibly can to gather what endpoints (URL's) to send which HTTP requests to, to know which resources
# the API offers and what is avaible to you through these HTTP reqeusts/communications. You may need an authentication token for some services/resources/to use certain HTTP requests

# We will need to send the correct HTTP request to the correct API endpoint that we can get a response back from
# We will try each basic HTTP request operations as listed above
# First lets try a GET HTTP request
#Note how we are capturing the response we get back from the server when we use the request libarary's GET method to send out an HTTP GET request to the API endpoint we specify
responseObject = requests.get('https://gorest.co.in/public/v2/users')
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
#Capturing JSON data into a variable to pass to the JSON library
captureJSONData = responseObject.json()
print(type(captureJSONData))
#The in-built json library has a method called dumps that, WHY CAN'T WE PRETTY PRINT USING PYTHON LIST??
prettiestJSONoutputEver = json.dumps(captureJSONData, indent=4)
print(type(prettiestJSONoutputEver))
print("Lets now try printing the JSON in a pretty way by using the JSON library: ")
print(prettiestJSONoutputEver)

print("Does printing directly without capturing data into a variable work?: ", "\n", json.dumps(responseObject.json(), indent=4))

#HTTP POST Request access token:
#1b55a246d2dc5cd680f0d8597f164b4f8471cd32138baf255fca76867411098d

AccessToken = "1b55a246d2dc5cd680f0d8597f164b4f8471cd32138baf255fca76867411098d"

universalCustomAuthorizationHeaderToUseWithAllHTTPrequests = dict()
universalCustomAuthorizationHeaderToUseWithAllHTTPrequests['Authorization'] = 'Bearer ' + AccessToken

dataToSendViaPostHTTPrequest = dict()
dataToSendViaPostHTTPrequest['name'] = 'Jynx Maze'
dataToSendViaPostHTTPrequest['email'] = 'vagina@swallowed.com'
dataToSendViaPostHTTPrequest['gender'] = 'female'
dataToSendViaPostHTTPrequest['status'] = 'active'

# Next lets try a POST HTTP request, this will allow us to use their API to post something on their server
# This will be our data payload, in a dictionary/JSONesque format

responseObjectForPostRequest = requests.post('https://gorest.co.in/public/v2/users', data = dataToSendViaPostHTTPrequest,  headers = universalCustomAuthorizationHeaderToUseWithAllHTTPrequests)
print("This is our HTTP Post Request response: ", responseObjectForPostRequest)
print("Lets break up the post request object we received: ")
print("Here is the .content member of the class we received back: ", responseObjectForPostRequest.content)
print("Here is the JSON function used against the object we received back: ", responseObjectForPostRequest.json())

captureJSONDataFromPostRequestResposne = responseObjectForPostRequest.json()

prettiestJSONoutputEverForPostRequest = json.dumps(captureJSONDataFromPostRequestResposne, indent=4)

print(prettiestJSONoutputEverForPostRequest)
print(type(prettiestJSONoutputEverForPostRequest))

idFromPOSTHTTPrequest = captureJSONDataFromPostRequestResposne["id"]

print(type(idFromPOSTHTTPrequest))



print("The ID of the user we created/POST'ed on the server side of things is: ", idFromPOSTHTTPrequest, " which we can tell by parsing the JSON data that came from the response of the POST request. We have now captured that in a variable to do a look up with a HTTP GET request." )

headerToSendWithHTTPGetRequest = dict()
headerToSendWithHTTPGetRequest['Authorization'] = 'Bearer ' + AccessToken


secondGetResponseObject = requests.get(f"https://gorest.co.in/public/v2/users/{idFromPOSTHTTPrequest}", headers=universalCustomAuthorizationHeaderToUseWithAllHTTPrequests)

print(secondGetResponseObject)

print(type(secondGetResponseObject.json()))

captureJSONDataForSecondGetHTTPrequest = secondGetResponseObject.json()

print(type(captureJSONDataForSecondGetHTTPrequest))

prettiestJSONoutputEverForSecondGetHTTPrequst = json.dumps(captureJSONDataForSecondGetHTTPrequest, indent=4)

print(type(prettiestJSONoutputEverForSecondGetHTTPrequst))

print(prettiestJSONoutputEverForSecondGetHTTPrequst)

# Next lets try a PATCH HTTP request, this will allow us to partially update the object we previously posted to their server in the code some time above
payloadToUpdate = dict()
payloadToUpdate['status'] = 'inactive'

capturePatchHTTPrequestResponse = requests.patch(f"https://gorest.co.in/public/v2/users/{idFromPOSTHTTPrequest}", data=payloadToUpdate, headers=universalCustomAuthorizationHeaderToUseWithAllHTTPrequests)
print(capturePatchHTTPrequestResponse)

getJSONDataFromPatchResponse = capturePatchHTTPrequestResponse.json()
prettyJSONOutputForPatchResponse = json.dumps(getJSONDataFromPatchResponse, indent=4)
print(prettyJSONOutputForPatchResponse)

#Lets see if the patch worked with a 3rd get request
captureThirdGetRequestResponse = requests.get(f"https://gorest.co.in/public/v2/users/{idFromPOSTHTTPrequest}", headers=universalCustomAuthorizationHeaderToUseWithAllHTTPrequests)
print(captureThirdGetRequestResponse)

getJSONDataFromThirdGetRequestResponse = captureThirdGetRequestResponse.json()
prettyJSONOutputForThirdGetResposne = json.dumps(getJSONDataFromThirdGetRequestResponse, indent=4)
print(prettyJSONOutputForThirdGetResposne)

# Next lets try a PUT HTTP request, this will allow us to completely update the object we previously posted to their server in the code above
payloadToUseForPutRequest = dict()
payloadToUseForPutRequest['name'] = 'Angela White'
payloadToUseForPutRequest['email'] = 'balls@swallowed.com'
payloadToUseForPutRequest['gender'] = 'female'
payloadToUseForPutRequest['status'] = 'active'
payloadToUseForPutRequest['tits'] = 'fucking huge'

capturePutHTTPrequestResponse = requests.put(f"https://gorest.co.in/public/v2/users/{idFromPOSTHTTPrequest}", data=payloadToUseForPutRequest, headers=universalCustomAuthorizationHeaderToUseWithAllHTTPrequests)
print(capturePutHTTPrequestResponse)

getJSONDataFromPutResponse = capturePutHTTPrequestResponse.json()
prettyJSONOutputForPutResponse = json.dumps(getJSONDataFromPutResponse, indent=4)
print(prettyJSONOutputForPutResponse)

#Lets try another get request to see if the server accepted our PUT HTTP request
captureFourthGetResponse = requests.get(f"https://gorest.co.in/public/v2/users/{idFromPOSTHTTPrequest}", headers=universalCustomAuthorizationHeaderToUseWithAllHTTPrequests)
print(captureFourthGetResponse)

getJSONDataFromFourthGetResponse = captureFourthGetResponse.json()
prettyJSONforFourthGetResponse = json.dumps(getJSONDataFromFourthGetResponse, indent=4)
print(prettyJSONforFourthGetResponse)

# Next lets try a DELETE HTTP request, this will allow us to delete the object we previously posted to their server in the code up above
captureDeleteHTTPResponse = requests.delete(f"https://gorest.co.in/public/v2/users/{idFromPOSTHTTPrequest}", headers=universalCustomAuthorizationHeaderToUseWithAllHTTPrequests)
print(captureDeleteHTTPResponse)
print(type(captureDeleteHTTPResponse))

#print(captureDeleteHTTPResponse.json())
#getJSONDataFromDeleteResposne = captureDeleteHTTPResponse.json()
#prettyJSONOutputForDeleteResponse = json.dumps(getJSONDataFromDeleteResposne, indent=4)
#print(prettyJSONOutputForDeleteResponse)

# Next lets try another GET HTTP request to see if we can still get the object we previously posted and deleted. This should fail if our DELETE HTTP request above was successful
captureFifthGetHTTPResponse = requests.get(f"https://gorest.co.in/public/v2/users/{idFromPOSTHTTPrequest}", headers=universalCustomAuthorizationHeaderToUseWithAllHTTPrequests)
print(captureFifthGetHTTPResponse)

#getJSONDataFromFifthGetHTTPresponse = captureFifthGetHTTPResponse.json()
#prettyJSONOutputForFifthGetHTTPresponse = json.dumps(getJSONDataFromFifthGetHTTPresponse)
#print(prettyJSONOutputForFifthGetHTTPresponse)