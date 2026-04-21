import pytest
import requests
import json

# Base configuration
BASE_URL = "http://localhost:8080/v1"
# Note: Add authentication headers if required
# headers = {"Authorization": "Bearer YOUR_TOKEN_HERE"}

class TestUsersAPI:
    """Test cases for Users API"""
    
    # Test cases for GET /users
    def test_get_users_default_page(self):
        """TC_GetUsers_01: Normal scenario - Get user list with default page"""
        url = f"{BASE_URL}/users"
        response = requests.get(url)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data["code"] == 200
        assert "data" in data
        assert isinstance(data["data"], list)
    
    def test_get_users_with_specific_page(self):
        """TC_GetUsers_02: Normal scenario - Get user list with specific page"""
        url = f"{BASE_URL}/users"
        params = {"page": 2}
        response = requests.get(url, params=params)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data["code"] == 200
        assert "data" in data
        assert isinstance(data["data"], list)
    
    def test_get_users_min_page(self):
        """TC_GetUsers_03: Boundary value - Page number is minimum (1)"""
        url = f"{BASE_URL}/users"
        params = {"page": 1}
        response = requests.get(url, params=params)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data["code"] == 200
        assert "data" in data
        assert isinstance(data["data"], list)
    
    def test_get_users_max_page(self):
        """TC_GetUsers_04: Boundary value - Page number is very large"""
        url = f"{BASE_URL}/users"
        params = {"page": 999999}
        response = requests.get(url, params=params)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data["code"] == 200
        assert "data" in data
        # Data should be empty array or follow business logic
    
    def test_get_users_invalid_page_type(self):
        """TC_GetUsers_05: Parameter type error - Page is non-integer"""
        url = f"{BASE_URL}/users"
        params = {"page": "abc"}
        response = requests.get(url, params=params)
        
        # Expecting 400 or 422 based on framework implementation
        assert response.status_code in [400, 422], f"Expected 400/422, got {response.status_code}"
    
    # Test cases for POST /users
    def test_create_user_with_all_fields(self):
        """TC_CreateUser_01: Normal scenario - Create user with all fields"""
        url = f"{BASE_URL}/users"
        payload = {
            "name": "赵六",
            "email": "zhaoliu@example.com",
            "age": 30
        }
        response = requests.post(url, json=payload)
        
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        data = response.json()
        assert data["code"] == 201
        assert data["message"] == "创建成功"
        assert "data" in data
        assert "id" in data["data"]
        assert data["data"]["name"] == "赵六"
        assert data["data"]["email"] == "zhaoliu@example.com"
    
    def test_create_user_with_required_fields_only(self):
        """TC_CreateUser_02: Normal scenario - Create user with required fields only"""
        url = f"{BASE_URL}/users"
        payload = {
            "name": "孙七",
            "email": "sunqi@example.com"
        }
        response = requests.post(url, json=payload)
        
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        data = response.json()
        assert data["code"] == 201
        assert data["message"] == "创建成功"
        assert "data" in data
        assert "id" in data["data"]
    
    def test_create_user_missing_name(self):
        """TC_CreateUser_03: Missing parameter - Required field 'name' is missing"""
        url = f"{BASE_URL}/users"
        payload = {
            "email": "test@example.com"
        }
        response = requests.post(url, json=payload)
        
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    
    def test_create_user_missing_email(self):
        """TC_CreateUser_04: Missing parameter - Required field 'email' is missing"""
        url = f"{BASE_URL}/users"
        payload = {
            "name": "测试用户"
        }
        response = requests.post(url, json=payload)
        
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    
    def test_create_user_invalid_email_format(self):
        """TC_CreateUser_05: Parameter format error - Invalid email format"""
        url = f"{BASE_URL}/users"
        payload = {
            "name": "测试用户",
            "email": "invalid-email"
        }
        response = requests.post(url, json=payload)
        
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    
    def test_create_user_invalid_age_type(self):
        """TC_CreateUser_06: Parameter type error - 'age' field type is wrong"""
        url = f"{BASE_URL}/users"
        payload = {
            "name": "测试用户",
            "email": "test@example.com",
            "age": "twenty"
        }
        response = requests.post(url, json=payload)
        
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    
    def test_create_user_min_age(self):
        """TC_CreateUser_07: Boundary value - 'age' is minimum value (0)"""
        url = f"{BASE_URL}/users"
        payload = {
            "name": "边界用户",
            "email": "boundary@example.com",
            "age": 0
        }
        response = requests.post(url, json=payload)
        
        # Could be 201 or 400 depending on business rules
        if response.status_code == 201:
            data = response.json()
            assert data["code"] == 201
        elif response.status_code == 400:
            # Should contain error message
            pass
        else:
            assert False, f"Unexpected status code: {response.status_code}"
    
    def test_create_user_max_age(self):
        """TC_CreateUser_08: Boundary value - 'age' is maximum value (150)"""
        url = f"{BASE_URL}/users"
        payload = {
            "name": "边界用户",
            "email": "boundary2@example.com",
            "age": 150
        }
        response = requests.post(url, json=payload)
        
        # Could be 201 or 400 depending on business rules
        if response.status_code == 201:
            data = response.json()
            assert data["code"] == 201
        elif response.status_code == 400:
            # Should contain error message
            pass
        else:
            assert False, f"Unexpected status code: {response.status_code}"
    
    # Test cases for GET /users/{userId}
    def test_get_user_detail_existing(self):
        """TC_GetUserDetail_01: Normal scenario - Get existing user detail"""
        url = f"{BASE_URL}/users/1"
        response = requests.get(url)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data["code"] == 200
        assert "data" in data
        assert data["data"]["id"] == 1
        assert "name" in data["data"]
        assert "email" in data["data"]
        assert "age" in data["data"]
    
    def test_get_user_detail_not_found(self):
        """TC_GetUserDetail_02: Error scenario - User ID does not exist"""
        url = f"{BASE_URL}/users/99999"
        response = requests.get(url)
        
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
    
    def test_get_user_detail_invalid_id_type(self):
        """TC_GetUserDetail_03: Parameter type error - User ID is non-numeric"""
        url = f"{BASE_URL}/users/abc"
        response = requests.get(url)
        
        # Could be 400 or 404 depending on routing
        assert response.status_code in [400, 404], f"Expected 400/404, got {response.status_code}"
    
    def test_get_user_detail_min_id(self):
        """TC_GetUserDetail_04: Boundary value - User ID is minimum (1)"""
        url = f"{BASE_URL}/users/1"
        response = requests.get(url)
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert data["code"] == 200
    
    def test_get_user_detail_zero_id(self):
        """TC_GetUserDetail_05: Boundary value - User ID is 0 or negative"""
        url = f"{BASE_URL}/users/0"
        response = requests.get(url)
        
        assert response.status_code in [404, 400], f"Expected 404/400, got {response.status_code}"