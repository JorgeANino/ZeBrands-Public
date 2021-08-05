# Zebrand's Backend Test 
* [READ INSTRUCTIONS](INSTRUCTIONS.md)

## Notes

* The application was deployed in AWS and also has interaction with AWS SES to send emails. You can make requests to the app through this link: http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/

* A postman collection was included inside zebrands folder.

* An architecture proposal was added inside the zebrands folder.

### Created admin credentials

Note: This admin should be used in order to create new admins.

* email: jorgebackendtest@gmail.com
* password: admin

# Available Endpoints (Documentation)

**Generate token (Login)**
----
  Generates token for a user

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/token/

* **Method:**

  `POST`

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:**
      ```
      {
      "refresh": "TestToken",
      "access": "TestToken"
      }
      ```
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**`{ detail : "No active account found with the given credentials." }`

* **Sample Call:**
  ```
  axios
    axios.post('http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/token/',
    {"email": "test_email@test.com", "password": "Test1234"},
    {headers: { Authorization: `Bearer ${token}`}});
  ```


**Refresh token**
----
  Refreshes an already used token

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/token/refresh/

* **Method:**

  `POST`

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:**
    ```
    {
      "refresh": "TestToken",
      "access": "TestToken"
    }
    ```
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** 
      ```
      {
          "detail": "Token is invalid or expired",
          "code": "token_not_valid"
      }
      ```
    

* **Sample Call:**

  ```
  axios
    axios.post('http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/token/',
    {"refresh": "TestToken"});
  ```
  

**Get Products**
----
  Returns json data with all the products created

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:**
    ```
    [
        {
            "id": "36b6b568-c39c-4af0-9fc1-f8e2fa9ee179",
            "created_at": "2021-08-04T19:09:06.248501Z",
            "updated_at": "2021-08-04T19:09:06.248525Z",
            "sku": "123A",
            "name": "Test Name",
            "price": 123.25,
            "brand": "ZeBrands"
        }
    ]
    ```
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**`{ detail : "Authentication credentials were not provided." }`

* **Sample Call:**
  ```
  axios
    axios.get('http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/', {headers: { Authorization: `Bearer ${token}`}});
  ```
  
**Get Product**
----
  Returns json data of a product 

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/<<product_id>>/

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:**
    ```
    {
        "id": "36b6b568-c39c-4af0-9fc1-f8e2fa9ee179",
        "created_at": "2021-08-04T19:09:06.248501Z",
        "updated_at": "2021-08-04T19:09:06.248525Z",
        "sku": "123A",
        "name": "Test Name",
        "price": 123.25,
        "brand": "ZeBrands"
    }
    ```
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**`{ detail : "Authentication credentials were not provided." }`

* **Sample Call:**
  ```
  axios
    axios.get('http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/36b6b568-c39c-4af0-9fc1-f8e2fa9ee179/', {headers: { Authorization: `Bearer ${token}`}});
  ```

**Create Product**
----
  Creates a product

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/

* **Method:**

  `POST`

* **Body params:**
  * sku: (str) SKU ID of the product
  * name: (str) Name of the product
  * price: (int) Price of the product
  * brand (str) Brand of the product

* **Example body:**
  ```
    {
        "sku": "123A",
        "name": "Test Name",
        "price": 123.25,
        "brand": "ZeBrands"
    }
  ```


* **Success Response:**

  * **Code:** 201 CREATED<br />
    **Content:**
    ```
    {
        "id":"302b6cb9-4a02-46e9-a4b3-7f9e7a9c9b02","created_at":"2021-08-04T19:48:47.515490Z","updated_at":"2021-08-04T19:48:47.515517Z",
        "sku":"123A",
        "name":"Test Name",
        "price":123.25,
        "brand":"ZeBrands"
    }
    ```
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**`{ detail : "Authentication credentials were not provided." }`
  * **Code:** 400 BAD REQUEST <br />
    **Content:**`{ name : ["This field is required."] }`

* **Sample Call:**
  ```
  axios
    axios.post(" http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/", 
        {
        "sku":"123A",
        "name":"Test Name",
        "price":123.25,
        "brand":"ZeBrands"
        }, 
        {
          headers: { Authorization: `Bearer ${token}` },
        });
  ```
  

**Delete Product**
----
  Deletes a product

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/<<product_id>>/

* **Method:**

  `DELETE`

* **Success Response:**
  
  * **Code:** 204 NO CONTENT
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
      **Content:**`{ detail : "Not found." }`

* **Sample Call:**
  ```
  axios
    axios.delete(`http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/023ab351-8627-45f0-9497-47c34a97efbd/`, {
        headers: { Authorization: `Bearer ${token}` },
      })
  ```
  
**Update product**
----
  Updates a product

  Returns json data of a product 

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/<<product_id>>/

* **Method:**

  `PUT`

* **Body params:**
  * sku: (str) SKU ID of the product
  * name: (str) Name of the product
  * price: (int) Price of the product
  * brand (str) Brand of the product

* **Example body:**
  ```
    {
        "sku": "123B",
        "name": "Test Name",
        "price": 123.25,
        "brand": "ZeBrands"
    }
  ```

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:**
    ```
    {
      "id": "36b6b568-c39c-4af0-9fc1-f8e2fa9ee179",
      "created_at": "2021-08-04T19:09:06.248501Z",
      "updated_at": "2021-08-04T19:09:06.248525Z",
      "sku": "123B",
      "name": "Test Name",
      "price": 123.25,
      "brand": "ZeBrands"
    }
    ```
    
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**`{ detail : "Authentication credentials were not provided." }`

* **Sample Call:**
  ```
  axios
    axios.put('http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/36b6b568-c39c-4af0-9fc1-f8e2fa9ee179/', {headers: { Authorization: `Bearer ${token}`}});
  ```

**Partially update product**
----
  Partially updates a product

  Returns json data of a product 

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/<<product_id>>/

* **Method:**

  `PATCH`

* **Body params:**
  * sku: (str) SKU ID of the product<br>
  or
  * name: (str) Name of the product<br>
  or
  * price: (int) Price of the product<br>
  or
  * brand (str) Brand of the product<br>

* **Example body:**

{
    "sku": "123B"
}

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:**
    ```
    {
        "id": "36b6b568-c39c-4af0-9fc1-f8e2fa9ee179",
        "created_at": "2021-08-04T19:09:06.248501Z",
        "updated_at": "2021-08-04T19:09:06.248525Z",
        "sku": "123B",
        "name": "Test Name",
        "price": 123.25,
        "brand": "ZeBrands"
    }
    ```
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**`{ detail : "Authentication credentials were not provided." }`

* **Sample Call:**
  ```
  axios
    axios.patch('http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/product/36b6b568-c39c-4af0-9fc1-f8e2fa9ee179/', {headers: { Authorization: `Bearer ${token}`}});
  ```

**Get Superusers**
----
  Returns json data with all the superusers created

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:**
      ```
        [
            {
                "id": 1,
                "email": "admin@zebrands.com",
                "first_name": "",
                "last_name": "",
                "roles": [
                    {
                        "id": 1,
                        "name": "Admin"
                    }
                ]
            },
            {
                "id": 2,
                "email": "jorgebackendtest@gmail.com",
                "first_name": "",
                "last_name": "",
                "roles": [
                    {
                        "id": 1,
                        "name": "Admin"
                    }
                ]
            },
            {
                "id": 4,
                "email": "test2@zebrands.com",
                "first_name": "Test Name3",
                "last_name": "Test Last2",
                "roles": [
                    {
                        "id": 1,
                        "name": "Admin"
                    }
                ]
            }
        ]
      ```
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**`{ detail : "Authentication credentials were not provided." }`

* **Sample Call:**
  ```
  axios
    axios.get('http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/', {headers: { Authorization: `Bearer ${token}`}});
  ```
**Get Superuser**
----
  Returns json data of a superuser

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/<<user_id>>/

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:**
    ```
    {
        "id": 4,
        "email": "test2@zebrands.com",
        "first_name": "Test Name3",
        "last_name": "Test Last2",
        "roles": [
            {
                "id": 1,
                "name": "Admin"
            }
        ]
    }
    ```
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**`{ detail : "Authentication credentials were not provided." }`

* **Sample Call:**
  ```
  axios
    axios.get('http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/4/', {headers: { Authorization: `Bearer ${token}`}});
  ```

**Create Superuser**
----
  Creates a superuser

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/

* **Method:**

  `POST`

* **Body params:**
  * first_name: (str) First name of the superuser
  * last_name: (str) Last name of the superuser
  * email: (str) Email of the superuser
  * pasword (str) Password of the superuser

* **Example body:**
  ```
    {
      "first_name": "Test Name",
      "last_name": "Test Last",
      "password": "test123456",
      "email": "test@zebrands.com"
    }
  ```


* **Success Response:**

  * **Code:** 201 CREATED<br />
    **Content:**
    ```
    {
        "id": 4,
        "email": "test2@zebrands.com",
        "first_name": "Test Name2",
        "last_name": "Test Last2",
        "roles": [
            {
                "id": 1,
                "name": "Admin"
            }
        ]
    }
    ```
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**`{ detail : "Authentication credentials were not provided." }`
  * **Code:** 400 BAD REQUEST <br />
    **Content:**`{ password : ["This field is required."] }`

* **Sample Call:**
  ```
  axios
    axios.post("http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/", 
        {
            "first_name": "Test Name",
            "last_name": "Test Last",
            "password": "test123456",
            "email": "test@zebrands.com"
        }, 
        {
          headers: { Authorization: `Bearer ${token}` },
        });
  ```
  

**Delete Superuser**
----
  Deletes a superuser

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/<<user_id>>/

* **Method:**

  `DELETE`

* **Success Response:**
  
  * **Code:** 204 NO CONTENT
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
      **Content:**`{ detail : "Not found." }`

* **Sample Call:**
  ```
  axios
    axios.delete(`http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/4/`, {
        headers: { Authorization: `Bearer ${token}` },
      })
  ```
  

**Update Superuser**
----
  Updates a superuser

  Returns json data of a superuser 

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/<<user_id>>/

* **Method:**

  `PUT`

* **Body params:**
  * first_name: (str) First name of the superuser
  * last_name: (str) Last name of the superuser
  * email: (str) Email of the superuser
  * pasword (str) Password of the superuser

* **Example body:**
  ```
  {
    "first_name": "Test Name",
    "last_name": "Test Last",
    "password": "test123456",
    "email": "test@zebrands.com"
  }
  ```


* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:**
      ```
        {
            "id": 4,
            "email": "test2@zebrands.com",
            "first_name": "Test Name2",
            "last_name": "Test Last2",
            "roles": [
                {
                    "id": 1,
                    "name": "Admin"
                }
            ]
        }
      ```
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**`{ detail : "Authentication credentials were not provided." }`

* **Sample Call:**
  ```
  axios
    axios.put('http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/4/', {headers: { Authorization: `Bearer ${token}`}});
  ```

**Partially Update Superuser**
----
  Partially updates a superuser

  Returns json data of a superuser 

* **ROLES ALLOWED**

  * ADMIN

* **URL**

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/<<user_id>>/

* **Method:**

  `PATCH`

* **Body params:**
  * first_name: (str) First name of the superuser<br>
  or
  * last_name: (str) Last name of the superuser<br>
  or
  * email: (str) Email of the superuser<br>
  or
  * pasword (str) Password of the superuser

* **Example body:**
  ```
  {
      "first_name": "Test Name3"
  }
  ```
* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:**
      ```
        {
            "id": 4,
            "email": "test2@zebrands.com",
            "first_name": "Test Name3",
            "last_name": "Test Last2",
            "roles": [
                {
                    "id": 1,
                    "name": "Admin"
                }
            ]
        }
      ```
    
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:**`{ detail : "Authentication credentials were not provided." }`

* **Sample Call:**
  ```
  axios
    axios.patch('http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/4/', {headers: { Authorization: `Bearer ${token}`}});
  ```

**Retrieve me**
----
  Retrieves the data of the user that calls the endpoint

* ***ROLES ALLOWED***

  * ADMIN
  * USER

* ***URL***

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/me/

* ***Method:***

  `GET`

* ***Success Response:***

  * ***Code:*** 200 OK<br />
    **Content:** 
    ```
    {
        "id": 1,
        "email": "admin@zebrands.com",
        "first_name": "Test",
        "last_name": "Test",
        "roles": [
            {
                "id": 1,
                "name": "Admin"
            }
        ]
    }
    ```
    
 
* ***Error Response:***

  * ***Code:*** 401 UNAUTHORIZED <br />
    **Content:** `{ detail : "Authentication credentials were not provided." }`

* ***Sample Call:***

  ```
  axios
      axios.get("http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/me/", {
          headers: { Authorization: `Bearer ${token}` },
        });
  ```


**Blacklist token (Logout)**
----
  Black lists a refresh token

* ***ROLES ALLOWED***

  * ADMIN

* ***URL***

  http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/logout/

* ***Method:***

  `POST`

* ***Body params:***
  * refresh: Refresh token to be blacklisted

* ***Example body:***
  ```
  {
      "refresh": "Testtoken"
  }
  ```

* ***Success Response:***

  * ***Code:*** 200 OK
 
* ***Error Response:***

  * ***Code:*** 400 BAD REQUEST

* ***Sample Call:***
  ```
  axios
    axios.post("http://ec2-3-129-17-89.us-east-2.compute.amazonaws.com/user/logout/", {
      refresh: "testRefresh",
    });
  ```