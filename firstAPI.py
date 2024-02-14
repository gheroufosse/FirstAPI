from fastapi import FastAPI, Path, Query, HTTPException, status  # import the FastAPI class
from typing import Optional  # to make the query parameter optional
from pydantic import BaseModel  # to create a class for the request body

app = FastAPI()  # initialize the FastAPI


class Item(BaseModel):  # create a class for the request body
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):  # create a update class for the request body
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


# We need to create an endpoint to handle the requests


# localhost/hello # ending path after the main domain


# methods to handle the requests -> GET, POST, PUT, DELETE, handle the requests, make actions

# GET -> return information
# POST -> create information, send information to an endpoint
# PUT -> update information
# DELETE -> delete information


# Set up a route
@app.get("/")  # Make sure that the endpoint is right above the function
def home():
    return {"Data": "Test FastAPI"}  # return a dictionary, some information


# Running our FastAPI
# uvicorn firstAPI:app --reload
# type this command in the terminal to run the FastAPI, with reload to update the changes directly
# then enter the localhost:8000 in the browser to see the result
# You can see the documentation of the API by adding /docs at the end of the URL
# localhost:8000/docs -> documentation of the API


@app.get("/about")
def about():
    return {"Data": "About page"}


# Path parameters

inventory = {}

# set up an endpoint to get the information from the ID of the product


@app.get("/get-item/{item_id}")  # {item_id} is the path parameter
def get_item(
    item_id: int,
):  # type hint: the item_id needs to be an integer -> tells fastAPI to expect an integer
    return inventory[item_id]  # return the inventory at the item_id


# -> You can only take multiple path parameters inside your endpoint
# @app.get("/get-item/{item_id}/{name}") # {item_id} is the path parameter
# def get_item(item_id: int, name: str): # type hint: the item_id needs to be an integer -> tells fastAPI to expect an integer
#     return inventory[item_id] # return the inventory at the item_id

############################################
# Working with Path                        #
############################################


@app.get("/get-item/{item_id}")  # {item_id} is the path parameter
def get_item(
    item_id: int = Path(description="The ID of the item you'd like to view"),
):  # You can add this Path function to add a description to the path parameter
    return inventory[item_id]


# => If you go to docs, you see the small description of the path parameter


############################################
# Query Parameters                        #
############################################

# "facebook.com/home?redirect=/tim&msg=fail/"  -> ? = query parameters

# new endpoint with a query parameter example


@app.get("/get-by-name")
def get_item(
    name: Optional[
        str
    ] = None,  # add the "= None", and the parameter will be optional => not an error anymore
):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found")


# http://localhost:8000/get-by-name?name=Milk -> find the milk in the inventory
# http://localhost:8000/get-by-name/  -> if we don't add the name, it will return an error : field required

# Use the Optinal[str] to make the code clearer than just = None


# @app.get("/get-by-name")
# def get_item(
#     test: int,  # add a new non-optional parameter --> needs to be first, the order matters
#     name: Optional[
#         str
#     ] = None,  # add the "= None", and the parameter will be optional => not an error anymore
# ):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"Data": "Not found"}


# OR we can start by a *, and it works


# @app.get("/get-by-name")
# def get_item(
#     *,  # add a new non-optional parameter --> needs to be first, the order matters
#     name: Optional[
#         str
#     ] = None,  # add the "= None", and the parameter will be optional => not an error anymore
#     test: int
# ):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"Data": "Not found"}


# http://localhost:8000/get-by-name?name=Milk&test=2 -> find the milk in the inventory and add the test parameter, here tells nothing


# You can also combine query and path parameters


# @app.get("/get-by-name/{item_id}")
# def get_item(*, item_id: int, name: Optional[str] = None, test: int):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"Data": "Not found"}


# http://localhost:8000/get-by-name/1?name=Milk&test=2 -> find the milk in the inventory


############################################
# Request Body                            #
############################################


@app.post("/create-item")  # allows to create a new item in the database
def create_item(
    item_id: int,
    item: Item,
):  # create a new item, and the item is of type Item (class), known as a base model
    if item_id in inventory:
        return {"Error": "Item ID already exists."}

    inventory[item_id] = (
        item  # you can just add the item instead of the python dictionary
    )
    return inventory[item_id]


# Put method
# update the information about the item already stored in the dictionary


@app.put("/update-item/{item_id}")
def update_item(
    item_id: int,
    item: UpdateItem,
):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID does not exist")

    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]


@app.delete("/delete-item")
def delete_item(
    item_id: int = Query(
        ...,
        title="The ID of the item to delete",
        description="This is the ID of the item, you want to delete",
        gt=0,
    )
):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID does not exist")

    del inventory[item_id]
    return {"Success": "Item deleted successfully"}


# Status codes and error responses

# Status codes: return kind of what happend with the http endpoint request
# Default status code: 200 -> everything is okay
# 404 -> not found

# Rather than returning a dictionary, we can return a HTTPException
# raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found")

