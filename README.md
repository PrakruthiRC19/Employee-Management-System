# Employee Management System

A RESTful Employee Management System built using Django and Django REST Framework. The application allows users to manage employee records through CRUD APIs and test API functionality using Postman.

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* Postman

## Features

* Create employee records
* Retrieve all employees
* Retrieve employee details by ID
* Update employee information using PUT
* Partially update employee information using PATCH
* Delete employee records
* Salary validation
* Duplicate email validation
* Gmail email validation
* Custom API responses and HTTP status codes

## Employee Details

The system manages the following employee information:

* ID
* Name
* Salary
* Email
* Address
* Role

## API Endpoints

| Method | Endpoint              | Description                       |
| ------ | --------------------- | --------------------------------- |
| GET    | `/api/`               | Retrieve all employees            |
| POST   | `/api/`               | Create a new employee             |
| GET    | `/api/<employee_id>/` | Retrieve an employee by ID        |
| PUT    | `/api/<employee_id>/` | Update all employee details       |
| PATCH  | `/api/<employee_id>/` | Partially update employee details |
| DELETE | `/api/<employee_id>/` | Delete an employee                |

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd employee_management
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Install the required dependencies:

```bash
pip install django djangorestframework
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## API Testing

The REST APIs were tested using Postman for:

* GET requests
* POST requests
* PUT requests
* PATCH requests
* DELETE requests
* Request and response validation
* HTTP status code validation

## Author

**Prakruthi R C**
