import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:5000"

def test_api():
    print("Testing RESTful API")
    print("=" * 50)
    
    # Test GET / (root endpoint)
    print("1. Testing root endpoint")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    # Test GET /users
    print("2. Getting all users")
    response = requests.get(f"{BASE_URL}/users")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    # Test POST /users (create user)
    print("3. Creating a new user")
    new_user = {
        "name": "Test User",
        "email": "test@example.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        created_user = response.json()["data"]
        user_id = created_user["id"]
        print(f"Created user with ID: {user_id}")
        print()
        
        # Test GET /users/<id>
        print(f"4. Getting user by ID ({user_id})")
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
        
        # Test PUT /users/<id> (update user)
        print(f"5. Updating user {user_id}")
        updated_data = {
            "name": "Updated Test User",
            "email": "updated@example.com"
        }
        response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
        
        # Test DELETE /users/<id>
        print(f"6. Deleting user {user_id}")
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
    
    # Test health endpoint
    print("7. Testing health endpoint")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    # Test error handling
    print("8. Testing error handling (non-existent user)")
    response = requests.get(f"{BASE_URL}/users/999")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Make sure the server is running on http://localhost:5000")