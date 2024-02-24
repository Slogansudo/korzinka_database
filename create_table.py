from db_connection import Database


def create_table():
    country = f""" CREATE TABLE country(country_id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        last_updated TIMESTAMP DEFAULT now());"""

    city = f""" CREATE TABLE city(city_id SERIAL PRIMARY KEY,
        country_id INT REFERENCES country(country_id),
        name VARCHAR(30) NOT NULL,
        last_update TIMESTAMP DEFAULT now());"""

    address = f""" CREATE TABLE address(address_id SERIAL PRIMARY KEY,
        city_id INT REFERENCES city(city_id),
        name VARCHAR(30) NOT NULL,
        last_update TIMESTAMP DEFAULT now());"""

    locations = f""" CREATE TABLE locations(location_id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        address_id INT REFERENCES address(address_id),
        last_update TIMESTAMP DEFAULT now());"""

    admin = f""" CREATE TABLE admin(admin_id SERIAL PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        password VARCHAR(30) NOT NULL,
        location_id INT REFERENCES locations(location_id),
        status VARCHAR(30) NOT NULL,
        last_update TIMESTAMP DEFAULT now());"""

    employees = f""" CREATE TABLE employees(employee_id SERIAL PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        password VARCHAR(30) NOT NULL,
        phone_number VARCHAR(30) NOT NULL,
        location_id INT REFERENCES locations(location_id),
        address_id INT REFERENCES address(address_id),
        status VARCHAR(30) NOT NULL,
        last_update TIMESTAMP DEFAULT now());"""

    payment_type = f""" CREATE TABLE payment_types(
        payment_type_id SERIAL PRIMARY KEY,
        payment_type VARCHAR(30) NOT NULL,
        last_update TIMESTAMP DEFAULT now());"""

    payment = f""" CREATE TABLE payment(payment_id SERIAL PRIMARY KEY,
        payment_type_id INT REFERENCES payment_types(payment_type_id),
        payment_amount INT NOT NULL,
        last_update TIMESTAMP DEFAULT now());"""

    category = f""" CREATE TABLE category(category_id SERIAL PRIMARY KEY,
        title VARCHAR(30) NOT NULL,
        description TEXT,
        expration_date DATE NOT NULL,
        last_update TIMESTAMP DEFAULT now());"""

    product = f""" CREATE TABLE product(product_id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        category_id INT REFERENCES category(category_id),
        price FLOAT NOT NULL,
        location_id INT REFERENCES locations(location_id),
        create_date DATE NOT NULL,
        last_update TIMESTAMP DEFAULT now());"""

    order_product = f""" CREATE TABLE order_product(order_product_id SERIAL PRIMARY KEY,
        employee_id INT REFERENCES employees(employee_id),
        product_id INT REFERENCES product(product_id),
        payment_id INT REFERENCES payment(payment_id),
        buying_date DATE NOT NULL,
        product_count INT NOT NULL,
        total_price FLOAT NOT NULL,
        last_update TIMESTAMP DEFAULT now());"""

    customer = f""" CREATE TABLE customer(customer_id SERIAL PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        address_id INT REFERENCES address(address_id),
        phone_number VARCHAR(13),
        order_product_id INT REFERENCES order_product(order_product_id),
        payment_id INT REFERENCES payment(payment_id),
        last_update TIMESTAMP DEFAULT now());"""

    product_customer = f""" CREATE TABLE product_customer(product_customer_id SERIAL PRIMARY KEY,
        product_id INT REFERENCES product(product_id),
        customer_id INT REFERENCES customer(customer_id),
        last_update TIMESTAMP DEFAULT now());"""
    data = {
        'country': country,
        'city': city,
        'address': address,
        'location': locations,
        'admin': admin,
        'employees': employees,
        'payment_type': payment_type,
        'payment': payment,
        'category': category,
        'product': product,
        'order_product': order_product,
        'customer': customer,
        'product_customer': product_customer
    }
    for i in data:
        print(f"{i} {Database.connect(data[i], 'create')}")






