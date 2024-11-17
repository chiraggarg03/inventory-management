# Inventory Management System

This project demonstrates the real-time application of Open Database Connectivity (ODBC) in building a functional Inventory Management System (IMS). The IMS provides a seamless interface between a web-based frontend and a MySQL database backend using ODBC standards. It highlights the critical role of ODBC in ensuring database connectivity, compatibility, and real-time updates for effective inventory management.

## Objectives
1.	Demonstrate Database Integration: Utilize ODBC to connect the Flask-based backend with a MySQL database, showcasing how to implement real-time data operations like insertion, updates, and retrieval.
2.	Real-Time Synchronization: Ensure inventory data is updated and retrieved in real-time, enabling end-users to make data-driven decisions instantly.
3.	User-Friendly Interface: Provide an intuitive web-based frontend for users to manage product inventory efficiently, from adding new products to adjusting stock levels.
4.	Cross-Platform Support: Highlight how ODBC facilitates cross-platform database operations, making the system flexible and scalable.

## Key Features
### 1. MySQL Database Integration
  •	A MySQL database serves as the backend storage, storing product details like ID, name, description, quantity, price, and timestamps.
  •	Uses a schema with real-time timestamp updates to track changes to inventory.

### 2. Backend with Flask Framework
  •	Implements RESTful APIs for CRUD operations on the product inventory.
  •	Connects to the MySQL database using ODBC standards, ensuring real-time data interaction.
  •	Supports multiple endpoints:
    o	GET /products: Retrieves the entire product list.
    o	POST /products: Adds a new product to the inventory.
    o	POST /products/<product_id>/update-quantity: Adjusts the quantity of a specific product dynamically.

### 3. Frontend with HTML, CSS, and JavaScript
  •	Provides an intuitive interface for managing inventory.
  •	Displays inventory details in tabular form with low-stock indicators for better decision-making.
  •	Allows stock adjustments through increment/decrement buttons.

## Implementation of ODBC Connectivity
ODBC acts as the middleware between the Flask application and the MySQL database. It ensures:
  •	Standardization: Provides a consistent interface for interacting with the database.
  •	Real-Time Interaction: Facilitates real-time API responses for data retrieval and updates.
  •	Error Handling: Handles database-specific errors and ensures system reliability.
The database connection is initialized at runtime, allowing dynamic queries to be executed without compromising performance. The python mysql.connector library is used to provide the ODBC connectivity between the Flask application and the MySQL database.
