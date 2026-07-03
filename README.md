# GigHub Freelance Gigs API

A FastAPI-based REST API for managing freelance gigs.

**Admission Number:** C027-01-2287/2024

---

## Project Description

GigHub Freelance Gigs API is a RESTful API developed using FastAPI. It allows users to create, retrieve, update, and delete freelance gigs. The API also supports filtering, searching, and pagination to make managing gigs easier.

---

## Features

- Create a new gig
- View all gigs
- View a gig by ID
- Update an existing gig
- Delete a gig
- Search gigs
- Filter gigs by category
- Pagination support
- Automatic API documentation using Swagger UI

---

## Technologies Used

- Python 3
- FastAPI
- Uvicorn
- Pydantic

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/mitchellnjerih-cloud/Gighub-api.git
```

2. Navigate into the project

```bash
cd Gighub-api
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
uvicorn main:app --reload
```

---

## API Documentation

After starting the server, open:

- Swagger UI:
  http://127.0.0.1:8000/docs

- ReDoc:
  http://127.0.0.1:8000/redoc

---

## Project Structure

```text
Gighub-api/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore
└── Screenshots/
```

---

## Screenshots

### Swagger UI

![Swagger UI](Screenshots/code%20(1).png)

### GET All Gigs

![GET Gigs](Screenshots/code%20(2).png)

### Create Gig

![Create Gig](Screenshots/code%20(3).png)

### Update Gig

![Update Gig](Screenshots/code%20(4).png)

### Delete Gig

![Delete Gig](Screenshots/Delete%20gig%20(1).png)

---

## Author

**Mitchell Njeri**

Admission Number: **C027-01-2287/2024**

---

## License

This project is for educational purposes.