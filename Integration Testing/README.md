## Define Integration testing

Integration testing is a type of testing meant to check the combinations of different units, their interactions, the way subsystems unite into one common system, and code compliance with the requirements.
##### Example of integration testing : 
*when we check login and sign up features in an e-commerce app, we view them as separate units.*

## Pytest
Pytest is a testing tool on Python that enables you to create marks, or custom labels, for any test you like. A test may have multiple labels, and you can use them for granular control over which tests to run.

## What's the project about?
It's a Flask API that handles the get, post, delete and update an application of handling a book store's stock of books.

## How to run our Flask application
```d
$  py -3 -m venv .venv
$  .venv\Scripts\activate
```
```d
$  set DATABASE_FILENAME=books.db
$  python utils/create_db.py
$  python app.py 
```
That's all you need for your server to start running up.

## Testing Scenarios

1. Create the table *books* 
2. Fetch all the books from the database that should return nothing *it's empty*
3. Add 3 books
4. Fetch all the books from the database
5. Delete the first book in the table *books*
6. Try deleting the previously deleted book
7. Try deleting a nonexistent book
8. Fetch all books from the database again *we should have all the elements except for the first one*
9. Updating a book's name

*Note:* The test create its own database in a temporary file.

## Running Tests
```d
$  pytest -v
```
**Results in a screenshot**
![pytest]()


```d
$  pytest -vvv --cov=app tests/
```
**Results in a screenshot**
![cov]()
