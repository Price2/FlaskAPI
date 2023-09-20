# Flask API for Product and Category Management

A simple Flask API project for managing products and categories.

## Table of Contents

- [Introduction](#introduction)
- [Endpoints](#endpoints)
  - [Products](#products)
  - [Categories](#categories)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Models](#models)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Flask API allows you to manage products and categories. It provides endpoints for adding, retrieving, updating, and deleting products and categories.

## Endpoints

### Products

- **GET /api/products**  
  Retrieve a list of products based on query parameters.

- **GET /api/products/{id}**  
  Retrieve a product by its ID.

- **POST /api/products**  
  Create a new product.

- **PUT /api/products/{id}**  
  Update a product by its ID.

### Categories

- **GET /api/categories**  
  Retrieve a list of categories based on query parameters.

- **POST /api/categories**  
  Create a new category.

## Getting Started

Follow these instructions to get the project up and running on your local machine:

1. Clone the repository:

   ```bash
   git clone https://github.com/Price2/FlaskAPI
   cd FlaskAPI


   Create and activate a virtual environment (optional but recommended):


python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/Linux:
source venv/bin/activate
Install the required dependencies from the requirements.txt file:



pip install -r requirements.txt
Configure your database connection in the db.py file.

Start the Flask application:


python main.py
Usage
You can use tools like Postman to interact with the API. Here are some example requests:

Retrieve Products
GET /api/products
Retrieve a list of all products.

GET /api/products/{id}
Retrieve a product by its ID.

GET /api/products?name=Product1&price=100&quantity=5
Retrieve products based on query parameters.

Create a Product
POST /api/products
Create a new product by sending a JSON request body:


{
  "name": "Product Name",
  "price": 100,
  "quantity": 5,
  "imgURL": "https://example.com/image.jpg",
  "category_id": 1
}
Update a Product
PUT /api/products/{id}
Update an existing product by sending a JSON request body similar to the one used for creation.
Retrieve Categories
GET /api/categories
Retrieve a list of all categories.

GET /api/categories?name=Category1
Retrieve categories based on query parameters.

Create a Category
POST /api/categories
Create a new category by sending a JSON request body:


{
  "name": "Category Name"
}
Models
The API uses two main models:

Product

id (Primary Key)
name
price
quantity
imgURL
category_id (Foreign Key)
Category

id (Primary Key)
name
products (Relationship with Product)
Database
The API uses an SQLite database by default. You can configure your database connection in the db.py file.
