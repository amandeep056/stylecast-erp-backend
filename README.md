StyleCast ERP Backend

A multi-tenant ERP backend designed for fashion brands to manage products, inventory, orders, shipping rules, and analytics.

The system is built using FastAPI, PostgreSQL, and SQLAlchemy, and exposes REST APIs that can power a modern SaaS dashboard for brand operations.

Overview

StyleCast ERP enables fashion brands to manage their operational workflows through a centralized backend system. The platform supports product catalog management, inventory tracking, order processing, shipping configuration, and analytics reporting.

Each brand operates as a tenant within the system, ensuring data isolation while allowing the platform to scale across multiple brands.

Tech Stack

Backend Framework
FastAPI

Database
PostgreSQL

ORM
SQLAlchemy

Validation
Pydantic

Authentication
JWT Authentication

API Documentation
Swagger UI (auto-generated)

Features

Brand Management
Register and manage brand tenants.

Authentication
Secure login and registration using JWT.

Product Catalog
Create and manage products belonging to a brand.

Product Variants
Support different sizes, SKUs, or variations.

Inventory Management
Track stock levels and update inventory quantities.

Order Management
Create orders and automatically update inventory.

Shipping Rules
Define shipping fees, regions, and free shipping thresholds.

Analytics APIs
Provide insights such as total sales, order count, and top selling products.

Project Structure
stylecast-erp
│
├── app
│   ├── main.py
│   ├── db.py
│
│   ├── models
│   │   ├── brand.py
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── shipping.py
│
│   ├── schemas
│   │   ├── brand.py
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── variant.py
│   │   ├── inventory.py
│   │   ├── order.py
│   │   ├── shipping.py
│   │   └── analytics.py
│
│   ├── routes
│   │   ├── auth.py
│   │   ├── brand.py
│   │   ├── product.py
│   │   ├── variant.py
│   │   ├── inventory.py
│   │   ├── order.py
│   │   ├── shipping.py
│   │   └── analytics.py
│
├── README.md
├── DESIGN.md
├── requirements.txt
└── .env.example
API Documentation

FastAPI automatically generates API documentation.

After running the server, open:

http://127.0.0.1:8000/docs

This interface allows testing all endpoints directly.

Running the Project
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/stylecast-erp-backend.git
cd stylecast-erp-backend
2. Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Mac/Linux

python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file using the example:

cp .env.example .env

Example configuration

DATABASE_URL=postgresql://user:password@localhost/stylecast
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
5. Run the Server
uvicorn app.main:app --reload

Server runs at

http://127.0.0.1:8000
Key API Modules

Authentication
User login and registration.

Products
Create, update, and manage product catalog.

Variants
Manage product variations and SKUs.

Inventory
Track and update stock levels.

Orders
Create orders and manage order status.

Shipping Rules
Configure shipping fees and regions.

Analytics
Retrieve business insights such as sales metrics and top products.

Multi-Tenant Architecture

The platform supports multiple brands through tenant isolation using a brand_id field across core entities.

All queries are scoped by the brand context to ensure brands cannot access another brand's data.

Design Document

The complete system design and architecture details are documented in:

DESIGN.md

This document covers:

database schema

system architecture

API modules

order processing workflow

analytics design

security considerations

Future Improvements

Role-based access control
Warehouse-level inventory tracking
Advanced analytics dashboards
Payment gateway integration
Webhook integrations

Author-

Amandeep Singh
MSc Computer Science