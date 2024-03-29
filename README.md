# Product-Management-API

## How to run
1. Clone the repository
2. Run `python -m venv venv` to create a virtual environment
3. Run `source venv/bin/activate` to activate the virtual environment
4. Run `pip install -r requirements.txt` to install the dependencies
5. Run `python manage.py migrate` to create the database
6. Run `python manage.py runserver` to start the server
7. Open `http://localhost:8000` in your browser
8. Run `python manage.py test` to run the tests
9. Run `deactivate` to deactivate the virtual environment

## API Endpoints
1. `GET api/products/` - List all products
2. `POST api/products/` - Create a new product
3. `GET api/products/<id>/` - Retrieve a product
4. `PUT api/products/<id>/` - Update a product
5. `PATCH api/products/<id>/` - Partially update a product
6. `DELETE api/products/<id>/` - Delete a product

## API Documentation
1. `GET api/swagger/` - Swagger UI Documentation
2. `GET api/redoc/` - ReDoc Documentation

## API Authentication
1. No authentication required for any endpoint
