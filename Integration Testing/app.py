import os
import sqlite3
from flask import Flask, jsonify, request
import string
import random

# Pytest: a test tool that enables you to create marks, or custom labels, for any test you like.
# A test may have multiple labels, and you can use them 
# for granular control over which tests to run.
from pytest import console_main

#This function helps to create a flask app the moment we run python app.py
def create_app(name):
    app = Flask(name)
    database_file_name = os.environ.get('DATABASE_FILENAME', 'database.db')
    #Connecting to internal database
    db_connection = sqlite3.connect(database_file_name, check_same_thread=False)
    app.config.from_mapping(
        DATABASE_CON = db_connection
    )
    
    #getting the list of books api
    @app.get('/books')
    def get_all_books():
        #Connecting to database
        db_connection = app.config['DATABASE_CON']
        db_connection.row_factory = sqlite3.Row
        #Initializing th cursor
        curseur = db_connection.cursor()
        #Executing a database select request
        curseur.execute(
            "SELECT * FROM books"
        )
        #Retrieve all the data
        data = curseur.fetchall()
        #return the results in a JSON format
        return(jsonify(
            [
                {
                    "id": book['id'],
                    "name": book['name'],
                    "author": book['author'],
                    "sales": book['sales']    
                } for book in data
            ])
        )
    
    
    #adding books api
    @app.post('/books')
    def create_book():
        #retrieving the request data in a JSON format
        request_body = request.get_json()
        # we get the name in the request
        name = request_body['name']
        # Get the author from the request
        author = request_body['author']
        # Get number of sales
        sales = request_body['sales']
        #connect to the DB
        db_connection = app.config["DATABASE_CON"]
        #Initializing the DB cursor
        curseur = db_connection.cursor()
        #executing the insert request
        curseur.execute(
            "INSERT INTO books(name,author,sales) VALUES (?,?,?)",
            (name, author, sales)
        )
        #Commiting the results
        db_connection.commit() 
        book_id = curseur.lastrowid
        db_connection.row_factory = sqlite3.Row
        #Selecting everythin to test whether the insert operation is successful or not
        curseur = db_connection.cursor()
        curseur.execute(
            "SELECT * FROM books WHERE id = ?",
            (book_id,)
        )
        
        data = curseur.fetchone()
        #return results + status code
        return(dict(data),201)    

    @app.delete('/books/<string:id>')
    def delete_book(id):
        db_connection = app.config["DATABASE_CON"]
        curseur = db_connection.cursor()
        curseur.execute('DELETE FROM books where id = ?', (id,))
        if curseur.rowcount == 0:
            return {
                "message": "book not deleted successfully"
            }
        elif curseur.rowcount == 1:
            return {
                "message": "book deleted successfully"
            }    
    return app

    @app.post('/up')
    def update_book():
        request_body = request.get_json()
        id = request_body['id']
        name = request_body['name']
        db_connection = app.config["DATABASE_CON"]
        curseur = db_connection.cursor()
        curseur.execute(
            "UPDATE books set name = ? where id = ?", (name, id,)
        )
        db_connection.commit() 
        book_id = curseur.lastrowid
        db_connection.row_factory = sqlite3.Row
        
        curseur = db_connection.cursor()
        curseur.execute(
            "SELECT * FROM books WHERE id = ?",
            (book_id,)
        )
        
        data1 = curseur.fetchone()
        data = curseur.fetchone()
        return(dict(data),200)


if __name__ == "__main__":
    app = create_app(__name__)
    app.run()