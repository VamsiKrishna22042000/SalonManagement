# SalonManagement
# 💇‍♀️ Salon Management System (SMS) Backend

A high-performance, scalable backend solution designed to streamline and automate all core operations of a modern salon. Built using **FastAPI**, the system provides robust, secure APIs for managing user accounts, staff services, and the entire appointment lifecycle.

## 1. Project Overview & Goal

The Salon Management System (SMS) is a **comprehensive backend solution** forming the foundation for a complete salon management platform. It is engineered to be **robust, scalable, and secure**, adhering to modern API development best practices with **FastAPI**.

## 2. Core Features (Phase 1: Foundation)

The system functionality is divided into the following key functional modules:

### 👥 User & Authentication Management

* **User Registration & Login:** Secure registration and session management.

* **Role-Based Access Control (RBAC):** Differentiating permissions for **admins**, **staff**, and **clients**.

* **Profile Management:** User profile viewing and modification.

### 🧑‍🔧 Staff & Service Management

* **Staff Management:** Complete **CRUD** (Create, Read, Update, Delete) operations for staff members.

* **Service Catalog:** Management of a dynamic catalog, including categories and **pricing**.

* **Staff-Service Association:** Linking specific services with qualified staff members.

### 📅 Appointment Booking & Scheduling

* **Online Scheduling:** Intuitive system for creating appointments.

* **Real-time Availability:** Checking staff and service schedules to prevent double-bookings.

* **Booking Status Tracking:** Managing statuses like Confirmed, Pending, Completed, and Cancelled.

* **Booking History:** Comprehensive management and history log.

## 3. Technical Stack & Architecture

The system utilizes a modern, performance-driven technical stack:

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | **FastAPI** | High-performance, asynchronous API development. |
| **Database** | **PostgreSQL** | Reliable, feature-rich relational data storage. |
| **ORM & Migrations** | **SQLAlchemy** & **Alembic** | Object-Relational Mapping (ORM) and robust database schema migrations. |
| **Authentication** | **JWT (JSON Web Tokens)** | Stateless and secure API token authentication. |
| **Documentation** | **OpenAPI (Swagger/Redoc)** | Automatic, interactive API documentation generation. |
| **Configuration** | **`.env` Files** | Environment variable management for sensitive settings. |

## 4. API Endpoint Structure (Phase 1)

The API is logically grouped for clear functionality and ease of use (all endpoints are prefixed with `/api/v1`):

| Route Group | Endpoints | Functionality |
| :--- | :--- | :--- |
| **`/users`** | `register`, `login`, `profile` | User authentication, session, and profile management. |
| **`/staff`** | `staff/`, `staff/{id}` | Staff CRUD and management. |
| **`/services`** | `services/`, `assignments/` | Service catalog management and staff-service associations. |
| **`/bookings`** | `bookings/`, `availability/` | Appointment scheduling, management, and availability checks. |

## 5. Security & Development Practices

### Security Features

* **Secure Password Hashing:** User passwords are securely hashed before storage.

* **JWT Authentication:** Ensures every API request is authenticated and authorized.

* **Role-Based Access Control (RBAC):** Enforces permissions at the endpoint level.

### Development Setup

* **Virtual Environment:** Standardized environment for dependency isolation.

* **Dependency Management:** Clear tracking of project requirements via a standard file (e.g., `requirements.txt`).

* **Alembic Integration:** Tools for managing and applying database schema changes easily.

* **Scalability & Maintainability:** Architecture designed for long-term support and growth.

## 6. 🚀 Phase 2 Roadmap: Advanced Features & AI Integration

The system will move beyond core operations to integrate advanced business features, payment processing, and intelligent AI components, setting the foundation for a best-in-class management platform.

### 6.1. 📦 Inventory & Retail Management

This module introduces full control over salon retail products, ensuring accurate stock levels and supporting product sales.

| Feature | Description | Key API Endpoints (Examples) |
| :--- | :--- | :--- |
| **Product Catalog** | Complete **CRUD** for retail items, including SKU, cost, price, and category. | `POST /api/v2/products/` |
| **Stock Tracking** | Real-time tracking of current stock levels. Supports **deduction** upon sale or service consumption. | `PUT /api/v2/inventory/{sku}/update_stock` |
| **Low Stock Alerts** | Automated system to flag products falling below a defined reorder threshold. | (Internal System Alerts/Logs) |
| **Retail Sales** | Endpoints to register product sales, separate from service bookings. | `POST /api/v2/sales/retail` |

### 6.2. 💳 Payment Integration

Integrating a robust payment gateway to handle financial transactions, deposits, and refunds securely.

| Feature | Description | Key API Endpoints (Examples) |
| :--- | :--- | :--- |
| **Payment Gateway** | Integration with a third-party service (e.g., Stripe, PayPal) for secure transaction processing. | (Uses External API) |
| **Pre-Payments/Deposits** | Ability to require a deposit for certain services or high-value bookings. | `POST /api/v2/payments/deposit` |
| **Invoicing** | Automatic generation of detailed invoices/receipts upon service or retail sale completion. | `GET /api/v2/invoices/{id}` |
| **Refunds** | API to process partial or full refunds against captured payments. | `POST /api/v2/payments/refund` |

### 6.3. 🧠 AI & Intelligent Features

The system is enhanced with two key AI components for personalization and operational efficiency.

#### 🎯 Hyper-Personalization & Recommendations

* **Goal:** Increase client retention and upselling by recommending relevant products and services.

* **Mechanism:** Development of a **Recommendation Engine** (e.g., Collaborative Filtering) based on historical service and purchase data.

* **API Output:** When a client is viewed, the API suggests the next recommended service (e.g., "Due for a color refresh") and complementary retail products.

* **Endpoint:** `GET /api/v2/recommendations/client/{id}`

#### 🗣️ Voice Assistant Booking (NLP)

* **Goal:** Allow clients to book appointments 24/7 using natural language (e.g., via a chatbot or smart speaker integration layer).

* **Mechanism:** Integration with a **Natural Language Processing (NLP)** service (like Dialogflow or a custom model) to interpret client requests.

* **Backend Flow:** The NLP service converts voice/text input (e.g., "Book a men's cut with Jane next Friday") into structured data that is then processed by the existing `/api/v1/bookings` routes.

* **Endpoint:** `POST /api/v2/voice/booking` (An interface endpoint for the NLP service)

## 7. 🛠️ Phase 2 Technical Enhancements

To support these complex features, the following technical components will be integrated:

* **Task Queues:** Implementation of a message broker (e.g., **Redis** with **Celery**) for handling asynchronous background tasks (sending emails/SMS, processing low-stock alerts) to maintain API speed.

* **Service Layer:** Refactoring the backend to introduce a clear **Service Layer** to isolate complex business logic (like payment processing and AI recommendations) from the API routes and database models.

* **External Service Configuration:** Secure handling of external API keys (Payment Gateway, SMS/Email services, NLP service) within the `.env` or a dedicated secrets manager.

## 8. 🛠️ Getting Started (Local Setup)

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/YourUsername/salon-management-system.git](https://github.com/YourUsername/salon-management-system.git)
    cd salon-management-system
    ```

2.  **Set up the environment and install dependencies:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Configure `.env` file:** Create and populate the `.env` file with your **PostgreSQL** database credentials and the **JWT Secret Key**.

4.  **Run Database Migrations:**

    ```bash
    alembic upgrade head
    ```

5.  **Start the server:**

    ```bash
    uvicorn app.main:app --reload
    ```

The server will be available at `http://localhost:8000`. Access the interactive documentation at `http://localhost:8000/docs`.

