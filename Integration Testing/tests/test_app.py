import pytest
from app import create_app
from utils.create_db import create_db
import os

@pytest.fixture(scope="session", autouse=True)
def create_test_database(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "test_database.db"
    create_db(database_filename)
    os.environ["DATABASE_FILENAME"] = str(database_filename)


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(__name__)
    testing_client = flask_app.test_client(use_cookies=False)
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()

def test_get_all_books_initial(test_client):
    # Given
    expected_response = []
    expected_status_code = 200

    # When
    response = test_client.get("/books")

    # Then
    assert expected_status_code == response.status_code
    assert expected_response == response.json

def test_enter_new_book (test_client):
    # Given
    request_payload = {
        "name": "Conversations with friends",
        "author": "Sally Rooney",
        "sales": 2000
    }

    expected_body = {
        "id": 1,
        "name": "Conversations with friends",
        "author": "Sally Rooney",
        "sales": 2000
    }
    expected_status_code = 201

    expected_body_keys = ["id", "name", "author", "sales"]

    # When
    response = test_client.post('/books', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert set(expected_body_keys) == response.json.keys()
    assert int == type(response.json["id"])

def test_enter_new_book_2 (test_client):
    # Given
    request_payload = {
        "name": "Normal People",
        "author": "Sally Rooney",
        "sales": 100
    }

    expected_body = {
        "id": 2,
        "name": "Normal People",
        "author": "Sally Rooney",
        "sales": 100
    }
    expected_status_code = 201

    expected_body_keys = ["id", "name", "author", "sales"]

    # When
    response = test_client.post('/books', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert set(expected_body_keys) == response.json.keys()
    assert int == type(response.json["id"])

def test_enter_new_book_3 (test_client):
    # Given
    request_payload = {
        "name": "Three Wishes",
        "author": "Liliane",
        "sales": 20
    }

    expected_body = {
        "id": 3,
        "name": "Three Wishes",
        "author": "Liliane",
        "sales": 20
    }
    expected_status_code = 201

    expected_body_keys = ["id", "name", "author", "sales"]

    # When
    response = test_client.post('/books', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert set(expected_body_keys) == response.json.keys()
    assert int == type(response.json["id"])

def test_enter_new_book_4 (test_client):
    # Given
    request_payload = {
        "name": "Song of ice and fire",
        "author": "George R. R. Martin",
        "sales": 150
    }

    expected_body = {
        "id": 4,
        "name": "Song of ice and fire",
        "author": "George R. R. Martin",
        "sales": 150
    }
    expected_status_code = 201

    expected_body_keys = ["id", "name", "author", "sales"]

    # When
    response = test_client.post('/books', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert set(expected_body_keys) == response.json.keys()
    assert int == type(response.json["id"])

def test_fetch_all_my_books(test_client):
    # Given
    expected_response = [
        {
            "id": 1,
            "name": "Conversations with friends",
            "author": "Sally Rooney",
            "sales": 2000
        },
        {
            "id": 2,
            "name": "Normal People",
            "author": "Sally Rooney",
            "sales": 100
        },
        {
            "id": 3,
            "name": "Three Wishes",
            "author": "Liliane",
            "sales": 20
        },
        {
            "id": 4,
            "name": "Song of ice and fire",
            "author": "George R. R. Martin",
            "sales": 150
        }
    ]
    expected_status_code = 200

    # When
    response = test_client.get("/books")

    # Then
    assert expected_status_code == response.status_code
    assert expected_response == response.json

def test_remove_from_database_books(test_client):
    # Given
    id_to_delete = 1
    expected_body = {
        "message": "book deleted successfully"
    }

    # When
    response = test_client.delete(f'/books/{id_to_delete}')

    # Then
    assert expected_body == response.json

def test_fetch_after_removal(test_client):
    # Given
    expected_response = [
       {
            "id": 2,
            "name": "Normal People",
            "author": "Sally Rooney",
            "sales": 100
        },
        {
            "id": 3,
            "name": "Three Wishes",
            "author": "Liliane",
            "sales": 20
        },
        {
            "id": 4,
            "name": "Song of ice and fire",
            "author": "George R. R. Martin",
            "sales": 150
        }
    ]    
    expected_status_code = 200
    
    # When
    response = test_client.get("/books")

    # Then
    assert expected_status_code == response.status_code
    assert expected_response == response.json

def test_updated_books(test_client):
    # Given
    request_payload = {
        "id": 2,
        "name": "B",
    }

    expected_body = {
        "id": 2,
        "name": "B",
        "author": "Sally Rooney",
        "sales": 100
    }
    expected_status_code = 404

    # When
    response = test_client.post('/up', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert int == type(response.json["id"])