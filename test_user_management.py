# test_user_management.py

import pytest
from user_management import add_user, get_user_by_id, get_all_users, User

# Setup: Clear user_db before each test
@pytest.fixture(autouse=True)
def clear_user_db():
    # This will reset the user_db list before each test
    from user_management import user_db
    user_db.clear()

# Unit Test 1: Test adding a user
def test_add_user():
    add_user(1, "JohnDoe", "john@example.com")
    user = get_user_by_id(1)
    assert user is not None
    assert user.username == "JohnDoe"
    assert user.email == "john@example.com"

# Unit Test 2: Test retrieving a user by ID (positive case)
def test_get_user_by_id():
    add_user(2, "JaneDoe", "jane@example.com")
    user = get_user_by_id(2)
    assert user is not None
    assert user.username == "JaneDoe"
    assert user.email == "jane@example.com"

# Unit Test 3: Test retrieving a user by ID (negative case, user doesn't exist)
def test_get_user_by_id_not_found():
    user = get_user_by_id(999)  # User with ID 999 doesn't exist
    assert user is None

# Integration Test 1: Test adding a user and retrieving all users
def test_add_and_get_all_users():
    add_user(3, "Alice", "alice@example.com")
    add_user(4, "Bob", "bob@example.com")
    
    all_users = get_all_users()
    assert len(all_users) == 2  # There should be 2 users in the list
    assert all_users[0].username == "Alice"
    assert all_users[1].username == "Bob"

# Integration Test 2: Test adding a user and retrieving by ID
def test_add_and_get_user_by_id():
    add_user(5, "Charlie", "charlie@example.com")
    user = get_user_by_id(5)
    assert user is not None
    assert user.username == "Charlie"
    assert user.email == "charlie@example.com"
