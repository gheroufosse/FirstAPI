# FirstAPI

Following the Tech with Tim tutorial on YouTube (https://www.youtube.com/watch?v=-ykeT6kk4bk&ab_channel=TechWithTim).

Advantage #1 : Data validation


Why is FastAPI relevant ?  => Define in advance the type of input data your API is going to get.
Automatically done for you -> return an error if not the right type of data


Advantage #2 : Auto documentation

Automatically generate documentation for your data thanks to the type of data and the information that you give.



Advantage #3 : Auto completion and code suggestion



## What is an API ?

API stands for "Application Programming interface" -> provide an interface to manipulate application and retrieve information.
For example, if we talk about an application like Amazon, it probably has one or multiple API's.
One of their API is maybe responsible for their inventory system.

This API is separated from the main front web. If you're looking for an item, the API returns the information about that item to the front web and it's then displayed. You have only one API instead of for example 5 back ends. It's good practice to separate front and back end.


## What kind of data an API is working with ?

JSON : JavaScript Object Notation
Whenever you return information to an end point, that information is going to be translated to JSON. Data exchange within API's is in the JSON format, so they also can be mistakes between information.


## Request body and post method

Request body is used to send some information to the API (?)

