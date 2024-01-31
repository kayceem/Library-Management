# Library Management System

This is a simple library management system made using FASTAPI and MYSQL.

## Table of Contents

-   [Library Management System](#library-management-system)
    -   [Table of Contents](#table-of-contents)
    -   [Introduction](#introduction)
    -   [Features](#features)
    -   [Requirements](#requirements)
    -   [Setup](#setup)
        -   [1. Clone the Repository](#1-clone-the-repository)
        -   [2. Create a Python Environment](#2-create-a-python-environment)
        -   [3. Activate Virtual Environment](#3-activate-virtual-environment)
        -   [4. Install Dependencies](#4-install-dependencies)
        -   [5. Configure the Database](#5-configure-the-database)
        -   [6. Set Environment Variables](#6-set-environment-variables)
    -   [Usage](#usage)

## Introduction

This application provides APIs for managing your library's inventory, including books, customers, and borrowers. It is built with FASTAPI for a fast and efficient backend, and MYSQL for robust data storage.

## Features

-   Manage Books: Add books in the library inventory.
-   Manage Book Details: Add and update books details in the library inventory.
-   Manage Borrowers: Track borrowers and their borrowing history.
-   Data Security: Utilizes JWT for secure authentication and authorization.

## Requirements

List the prerequisites for running your application:

-   Python (3.10 or above)
-   MySQL Server (8.0 or above)

## Setup

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/kayceem/library-management.git
cd library-management
```

### 2. Create a python environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

On Windows

```bash
.\venv\Scripts\activate
```

On Unix or MacOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt

```

### 5. Configure the Database

```bash
CREATE DATABASE Library_Management;
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON Library_Management.* TO 'username'@'localhost';
FLUSH PRIVILEGES;

```

### 6. Set Environment Variables

Create a .env file in the root of your project and add the following environment variables:

```bash
DB_HOST=localhost
DB_USER=username
DB_PASSWORD=password
DB_NAME=Library_Management
DB_PORT=3306
secret_key=your_secret_key
algorithm=HS256

```

## Usage

### 1. Generate some fake data (Optional)

```bash
python ./fake_data.py

```

### 2. Run FastAPI Application

```bash
python ./main.py

```

## Notes

The application runs on port `8000`.

### Route Security

All routes are secured, except for `/admin` and `/login`. Users must have a valid JSON Web Token (JWT) to interact with other routes.

### Default Credentials (if using fake_data.py)

If the `fake_data.py` script is used to generate data, the default credentials are as follows:

-   **Username:** admin
-   **Password:** Password1@

### Testing

For testing API routes Insomnia was used.
![API Testing](./Insomnia%200343%20073.png)

### Assumptions

-   **One book per ISBN**
-   **.env file was included in repo for ease of use**
