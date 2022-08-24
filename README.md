# Mohamed-S-Helal-Django-Order-System-API

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`get_products` | GET | READ | Get all products
`purchase_product/:id` | GET | READ | Purchase a product
`get_purchased` | GET | READ | Get all purchased products by user
`create_product`| POST | CREATE | Create a new product
`modify_product/:id` | PUT | UPDATE | Update a product
`delete_product/:id` | DELETE | DELETE | Delete a product

## Use
We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation), or we can use [Postman](https://www.postman.com/)

### Commands using [httpie](https://github.com/jakubroztocil/httpie#installation):

First we need to create a user, so we can log in
```
http POST http://127.0.0.1:8000/auth/register/ email="email@email.com" username="USERNAME" password="PASSWORD" password2="PASSWORD"
```

After we create an account we can use those credentials to get a token

To get a token first we need to request
```
http http://127.0.0.1:8000/auth/token/ username="username" password="password"
```

Get all products
```
http GET http://127.0.0.1:8000/products/get_products/ "Authorization: Bearer {YOUR_TOKEN}" 
```
Purchase a product
```
http POST http://127.0.0.1:8000/products/purchase_product/{product_id}/ "Authorization: Bearer {YOUR_TOKEN}" 
```
Get purchased products
```
http GET http://127.0.0.1:8000/products/get_purchased/ "Authorization: Bearer {YOUR_TOKEN}" 
```
Create a new product
```
http POST http://127.0.0.1:8000/products/create_product/ "Authorization: Bearer {YOUR_TOKEN}" name="product name" description="product description" 
```
Update a product
```
http PUT http://127.0.0.1:8000/products/modify_product/{product_id}/ "Authorization: Bearer {YOUR_TOKEN}" name="product name updated" description="product description updated" 
```
Delete a product
```
http DELETE http://127.0.0.1:8000/products/delete_product/{product_id}/ "Authorization: Bearer {YOUR_TOKEN}"
```





