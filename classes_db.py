import db_connection


class Base:
    @staticmethod
    def delete(query):
        return db_connection.Database.connect(query, 'delete')

    @staticmethod
    def update(search_id, column, new_data, table, search_id_column,):
        if new_data is int:
            query = f"""UPDATE {table} SET {column} = {new_data} WHERE {search_id_column} = {search_id};"""
        else:
            query = f"""UPDATE {table} SET {column} = '{new_data}' WHERE {search_id_column} = {search_id};"""
        return db_connection.Database.connect(query, 'update')

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return db_connection.Database.connect(query, 'select')


class Country(Base):
    def __init__(self, name):
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES('{self.name}');"""
        return db_connection.Database.connect(query, 'insert')


class City(Country):
    def __init__(self, country_id, name):
        super().__init__(name)
        self.country_id = country_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(country_id, name) VALUES({self.country_id}, '{self.name}');"""
        return db_connection.Database.connect(query, 'insert')


class Address(Base):
    def __init__(self, city_id, name):
        self.city_id = city_id
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO {table}(city_id, name) VALUES({self.city_id}, '{self.name}');"""
        return db_connection.Database.connect(query, 'insert')


class Locations(Base):
    def __init__(self, name, address_id):
        self.address_id = address_id
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO {table}(name, address_id) VALUES('{self.name}', {self.address_id});"""
        return db_connection.Database.connect(query, 'insert')


class Admin(Base):
    def __init__(self,first_name, last_name, password, status):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.status = status

    def insert(self, location_id, table):
        query = f"""INSERT INTO {table}(first_name, last_name, password, location_id, status) 
        VALUES('{self.first_name}', '{self.last_name}', '{self.password}', {location_id}, '{self.status}');"""
        return db_connection.Database.connect(query, 'insert')


class Employees(Admin):
    def __init__(self, first_name, last_name, password, status, location_id):
        super().__init__(first_name, last_name, password, status)
        self.location_id = location_id

    def insert(self, phone_number, address_id, table):
        query = f"""INSERT INTO {table}(first_name, last_name, password, phone_number, location_id, address_id, status) 
        VALUES('{self.first_name}', '{self.last_name}', '{self.password}', '{phone_number}', {self.location_id}, {address_id}, '{self.status}');"""
        return db_connection.Database.connect(query, 'insert')


class PaymentType(Base):
    def __init__(self, payment_type):
        self.payment_type = payment_type

    def insert(self, table):
        query = f"""INSERT INTO {table}(payment_type) VALUES('{self.payment_type}');"""
        return db_connection.Database.connect(query, 'insert')


class Payment(Base):
    def __init__(self, payment_type_id, payment_amount):
        self.payment_type_id = payment_type_id
        self.payment_amount = payment_amount

    def insert(self, table):
        query = f"""INSERT INTO {table}(payment_type_id, payment_amount) VALUES({self.payment_type_id}, {self.payment_amount});"""
        return db_connection.Database.connect(query, "insert")


class Category(Base):
    def __init__(self, title, description, expration_date):
        self.title = title
        self.description = description
        self.expration_date = expration_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(title, description, expration_date) VALUES('{self.title}', '{self.description}', '{self.expration_date}');"""
        return db_connection.Database.connect(query, "insert")


class Product(Base):
    def __init__(self, name, category_id, price, location_id, create_date):
        self.name = name
        self.category_id = category_id
        self.price = price
        self.location_id = location_id
        self.create_date = create_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(name, category_id, price, location_id, create_date) 
        VALUES('{self.name}', {self.category_id}, {self.price}, {self.location_id}, '{self.create_date}');"""
        return db_connection.Database.connect(query, "insert")


class OrderProduct(Base):
    def __init__(self, employee_id, product_id, payment_id, buying_date, product_count, total_price):
        self.employee_id = employee_id
        self.product_id = int(product_id)
        self.payment_id = int(payment_id)
        self.buying_date = buying_date
        self.product_count = int(product_count)
        self.total_price = float(total_price)

    def insert(self, table):
        query = f"""INSERT INTO {table}(employee_id, product_id, payment_id, buying_date, product_count, total_price) 
        VALUES({self.employee_id}, {self.product_id}, {self.payment_id}, '{self.buying_date}', {self.product_count}, {self.total_price});"""
        return db_connection.Database.connect(query, "insert")


class Customer(Base):
    def __init__(self, first_name, last_name, address_id, phone_number, order_product_id, payment_id):
        self.first_name = first_name
        self.last_name = last_name
        self.address_id = address_id
        self.phone_number = phone_number
        self.order_product_id = int(order_product_id)
        self.payment_id = int(payment_id)

    def insert(self, table):
        query = f"""INSERT INTO {table}(first_name, last_name, address_id, phone_number, order_product_id, payment_id) 
        VALUES('{self.first_name}', '{self.last_name}', {self.address_id}, '{self.phone_number}', {self.order_product_id}, {self.payment_id});"""
        return db_connection.Database.connect(query, "insert")


class ProductCustomer(Base):
    def __init__(self, product_id, customer_id):
        self.product_id = int(product_id)
        self.customer_id = int(customer_id)

    def insert(self, table):
        query = f"""INSERT INTO {table}(product_id, customer_id) 
        VALUES({self.product_id}, {self.customer_id});"""
        return db_connection.Database.connect(query, "insert")
