import main
import classes_db


def country():
    ask = input("""country page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        name = input("Enter country name: ")
        datas = classes_db.Country(name)
        print(datas.insert('country'))
        return country()
    elif ask == "2":
        search_column = input("insert search column name: ")
        if search_column == "country_id":
            data = int(input('insert country id: '))
            query = f"""DELETE FROM country WHERE {search_column} = {data};"""
        elif search_column == "name":
            data = input("insert country name: ")
            query = f"""DELETE FROM country WHERE {search_column} = '{data}';"""
        elif search_column == "last_update":
            data = input('insert last update: ')
            query = f"""DELETE FROM country WHERE {search_column} = '{data}';"""
        else:
            print("invalid input")
            return country()
        print(classes_db.Country.delete(query))
        return country()
    elif ask == "3":
        country_id = input("insert country id: ")
        column = input("insert search column name: ")
        if column == "country_id":
            new_data = int(input('insert new_country id: '))
        else:
            new_data = input('insert new_data: ')
        print(classes_db.Country.update(country_id, column, new_data, 'country', 'country_id'))
        return country()
    elif ask == '4':
        data_x = classes_db.Country.select('country')
        for i in data_x:
            print(i)
        return country()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return country()


def city():
    ask = input("""city page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        country_id = int(input("insert country id: "))
        name = input("insert city name: ")
        data_z = classes_db.City(country_id, name)
        print(data_z.insert('city'))
        return city()
    elif ask == "2":
        search_column = input("insert search column name: ")
        if search_column == "city_id" or search_column == "country_id":
            search_data = int(input("insert search data: "))
            query = f"""DELETE FROM city WHERE {search_column}={search_data};"""
        else:
            search_data = input("insert search data: ")
            query = f"""UPDATE city SET {search_column}='{search_data}';"""
        print(classes_db.City.delete(query))
        return city()
    elif ask == "3":
        search_id = input("insert city_id: ")
        column = input("insert search column name: ")
        if column == "city_id" or column == "country_id":
            new_data = int(input("insert new data: "))
        else:
            new_data = input("insert new data: ")
        print(classes_db.City.update(search_id, column, new_data, 'city', 'city_id'))
        return city()
    elif ask == '4':
        data_x = classes_db.City.select('city')
        for i in data_x:
            print(i)
        return city()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return city()


def address():
    ask = input("""address page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        city_id = int(input("insert city_id: "))
        name = input("insert name: ")
        data_y = classes_db.Address(city_id, name)
        print(data_y.insert('address'))
        return address()
    elif ask == "2":
        search_column = input("insert search column name: ")
        if search_column == "city_id" or search_column == "address_id":
            search_data = int(input("insert search data: "))
            query = f"""DELETE FROM address WHERE {search_column} = {search_data};"""
        else:
            search_data = input("insert search data: ")
            query = f"""DELETE FROM address WHERE {search_column}='{search_data}';"""
        print(classes_db.Address.delete(query))
        return address()
    elif ask == "3":
        search_id = input("insert address_id: ")
        search_column = input("insert search column name: ")
        if search_column == "city_id" or search_column == "address_id":
            new_data = int(input("insert new data: "))
        else:
            new_data = input("insert new data: ")
        print(classes_db.Address.update(search_id, search_column,new_data, 'address', 'address_id'))
        return address()
    elif ask == '4':
        data_x = classes_db.Address.select('address')
        for i in data_x:
            print(i)
        return address()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return address()


def locations():
    ask = input("""locations page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        name = input("insert new name: ")
        address_id = int(input("insert address id: "))
        data_x = classes_db.Locations(name, address_id)
        print(data_x.insert('locations'))
        return locations()
    elif ask == "2":
        search_column = input("insert search column name: ")
        if search_column == "address_id" or search_column == "location_id":
            search_data = int(input("insert search data: "))
            query = f"""DELETE FROM locations WHERE {search_column}={search_data};"""
        else:
            search_data = input("insert search data: ")
            query = f"""UPDATE locations SET {search_column}='{search_data}';"""
        print(classes_db.Locations.delete(query))
        return locations()
    elif ask == "3":
        search_id = input("insert location_id: ")
        column = input("insert search column name: ")
        if column == "location_id" or column == "address_id":
            new_data = int(input("insert new data: "))
        else:
            new_data = input("insert new data: ")
        print(classes_db.Locations.update(search_id, column, new_data, 'locations', 'location_id'))
        return locations()
    elif ask == '4':
        data_x = classes_db.Locations.select('locations')
        for i in data_x:
            print(i)
        return locations()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return location()


def admin():
    ask = input("""locations page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == '1':
        first_name = input("insert first name: ")
        last_name = input("insert last_name: ")
        password = input("insert password: ")
        location_id = int(input("insert location_id: "))
        data_y = classes_db.Admin(first_name, last_name, password, status='admin')
        print(data_y.insert(location_id, 'admin'))
        return admin()
    elif ask == '2':
        column = input("insert search column name: ")
        if column == "location_id" or column == "admin_id":
            search_data = int(input("insert search data: "))
            query = f"""DELETE FROM admin WHERE {column}={search_data};"""
        else:
            search_data = input("insert search data: ")
            query = f"""DELETE FROM admin WHERE {column}='{search_data}';"""
        print(classes_db.Admin.delete(query))
    elif ask == '3':
        search_id = int(input("insert admin_id: "))
        column = input("insert search column name: ")
        if column == "location_id" or column == "admin_id":
            new_data = int(input('insert new data: '))
        else:
            new_data = input("insert new data: ")
        print(classes_db.Admin.update(search_id, column, new_data, 'admin', 'admin_id'))
        return admin()
    elif ask == '4':
        data_x = classes_db.Admin.select('admin')
        for i in data_x:
            print(i)
        return admin()
    elif ask == '5':
        return main.main()
    else:
        print("invalid")
        return admin()


def employees():
    ask = input("""employees page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        first_name = input('insert first name: ')
        last_name = input('insert last_name: ')
        password = input('insert password: ')
        phone_number = input('insert phone number: ')
        location_id = int(input('insert location_id: '))
        address_id = input('insert address_id: ')
        status = input('insert status: ')
        data_y = classes_db.Employees(first_name, last_name, password, status, location_id)
        print(data_y.insert(phone_number, address_id, 'employees'))
        return employees()
    elif ask == "2":
        column =input('insert search column name: ')
        if column == 'employee_id' or column == 'location_id':
            search_data = int(input('insert search data: '))
            query = f"""DELETE FROM employees WHERE {column}={search_data};"""
        else:
            search_data = input('insert search data: ')
            query = f"""DELETE FROM employees WHERE {column}='{search_data}';"""
        print(classes_db.Employees.delete(query))
        return employees()
    elif ask == "3":
        search_id = int(input('insert employees_id: '))
        column = input('insert search column name for updated: ')
        if column == 'employee_id' or column == 'location_id':
            new_data = int(input('insert new data: '))
        else:
            new_data = input('insert new data: ')
        print(classes_db.Employees.update(search_id, column, new_data, 'employees', 'employee_id'))
        return employees()
    elif ask == '4':
        data_x = classes_db.Employees.select('employees')
        for i in data_x:
            print(i)
        return employees()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return employees()


def payment_type():
    ask = input("""payment_type page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        payment_typ = input('insert payment type(card or cash): ')
        data = classes_db.PaymentType(payment_typ)
        print(data.insert('payment_types'))
        return payment_type()
    elif ask == "2":
        column = input('insert search_column: ')
        if column == 'payment_type_id':
            search_data = int(input('insert search data: '))
            query = f"""DELETE FROM payment_types WHERE {column}={search_data};"""
        else:
            search_data = input('insert search data: ')
            query = f"""DELETE FROM payment_types WHERE {column}='{search_data}';"""
        print(classes_db.PaymentType.delete(query))
        return payment_type()

    elif ask == "3":
        search_id = int(input('insert payment_type_id:'))
        column = input('insert search_column: ')
        if column == 'payment_type_id':
            new_data = int(input('insert new data: '))
        else:
            new_data = input('insert new data: ')
        print(classes_db.PaymentType.update(search_id, column, new_data, 'payment_types', 'payment_type_id'))
        return payment_type()
    elif ask == '4':
        data_x = classes_db.PaymentType.select('payment_types')
        for i in data_x:
            print(i)
        return payment_type()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return payment_type()


def payment():
    ask = input("""payment page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        payment_type_id = int(input('insert payment_type_id:'))
        payment_amount = int(input('insert payment_amount:'))
        data_y = classes_db.Payment(payment_type_id, payment_amount)
        print(data_y.insert('payment'))
        return payment()
    elif ask == "2":
        column = input('insert search column: ')
        search_data = int(input('insert search data: '))
        query = f"""DELETE FROM payment WHERE {column}={search_data};"""
        print(classes_db.Payment.delete(query))
        return payment()
    elif ask == "3":
        search_id = int(input("insert payment_id: "))
        column = input('insert search column: ')
        new_data = int(input('insert new_data: '))
        print(classes_db.Payment.update(search_id, column, new_data, 'payment', 'payment_id'))
        return payment()
    elif ask == '4':
        data_x = classes_db.Payment.select('payment')
        for i in data_x:
            print(i)
        return payment()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return payment()


def category():
    ask = input("""category page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        title = input('insert title: ')
        description = input('insert description: ')
        expration_date = input('insert expiration date: ')
        data_y = classes_db.Category(title, description, expration_date)
        print(data_y.insert('category'))
        return category()
    elif ask == "2":
        column = input('insert column name: ')
        if column == "category_id":
            search_data = int(input('insert search data: '))
            query = f"""DELETE FROM category WHERE {column}={search_data};"""
        else:
            search_data = input('insert search data: ')
            query = f"""DELETE FROM category WHERE {column}='{search_data}';"""
        print(classes_db.Category.delete(query))
        return category()
    elif ask == "3":
        search_id = int(input('insert category id: '))
        column = input('insert search column: ')
        if column == "category_id":
            new_data = int(input('insert new data: '))
        else:
            new_data = input('insert new data: ')
        print(classes_db.Category.update(search_id, column, new_data, 'category', 'category_id'))
        return category()
    elif ask == '4':
        data_x = classes_db.Category.select('category')
        for i in data_x:
            print(i)
        return category()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return category()


def product():
    ask = input("""product page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        name = input('insert product name: ')
        category_id = int(input('insert category_id: '))
        price = float(input('insert price: '))
        location_id = int(input('insert location id: '))
        create_date = input('insert create date: ')
        data_y = classes_db.Product(name, category_id, price, location_id, create_date)
        print(data_y.insert('product'))
        return product()
    elif ask == "2":
        column = input('insert search_column name : ')
        if column == 'category_id' or column == 'product_id' or column == 'location_id':
            search_data = int(input('insert search data: '))
            query = f"""DELETE FROM product WHERE {column}={search_data};"""
        else:
            search_data = input('insert search data: ')
            query = f"""DELETE FROM product WHERE {column}='{search_data}';"""
        print(classes_db.Product.delete(query))
        return product()
    elif ask == "3":
        search_id = input('insert product_id: ')
        column = input('insert search_column name : ')
        if column == 'product_id' or column == 'location_id' or column == 'category_id':
            new_data = int(input('insert new data: '))
        else:
            new_data = input('insert new data: ')
        print(classes_db.Product.update(search_id, column, new_data, 'product', 'product_id'))
        return product()
    elif ask == '4':
        DATA_X = classes_db.Product.select('product')
        for i in DATA_X:
            print(i)
        return product()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return product()


def order_product():
    ask = input("""order_product page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        employee_id = int(input('insert employee id: '))
        product_id = int(input('insert product id: '))
        payment_id = int(input('insert payment id: '))
        buying_date = input('insert buying date: ')
        product_count = int(input('insert product count: '))
        total_price = float(input('insert total price: '))
        data_y = classes_db.OrderProduct(employee_id, product_id, payment_id, buying_date, product_count, total_price)
        print(data_y.insert('order_product'))
        return order_product()
    elif ask == "2":
        column = input('insert column name: ')
        if column == 'order_product_id' or column == 'employee_id' or column == 'product_id' or column == 'payment_id' or column == 'product_count':
            search_data = int(input('insert search data: '))
            query =f"""DELETE FROM order_product WHERE {column}={search_data};"""
        else:
            search_data = input('insert search data: ')
            query =f"""DELETE FROM order_product WHERE {column}='{search_data}';"""
        print(classes_db.OrderProduct.delete(query))
        return order_product()
    elif ask == "3":
        search_id = int(input('insert order_product_id: '))
        column = input('insert seach column name: ')
        if column == 'buying_date':
            search_data = input('insert search data: ')
        else:
            search_data = int(input('insert search data: '))
        print(classes_db.OrderProduct.update(search_id, column, search_data, 'order_product', 'order_product_id'))
        return order_product()
    elif ask == '4':
        data_x = classes_db.OrderProduct.select('order_product')
        for i in data_x:
            print(i)
        return order_product()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return order_product()


def customer():
    ask = input("""customer page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        first_name = input('insert first name: ')
        last_name = input('insert last_name: ')
        address_id = int(input('insert address_id: '))
        phone_number = input('insert phone_number: ')
        order_product_id = int(input('insert order_product_id:'))
        payment_id = int(input('insert payment_id: '))
        data_y = classes_db.Customer(first_name, last_name, address_id, phone_number, order_product_id, payment_id)
        print(data_y.insert('customer'))
        return customer()
    elif ask == "2":
        column = input('insert column name: ')
        if column == 'first_name' or column == 'last_name' or column == 'phone_number':
            data = input('insert search data: ')
            query = f"""DELETE FROM customer WHERE {column}='{data}';"""
        else:
            data = int(input('insert search data: '))
            query = f"""DELETE FROM customer WHERE {column}={data};"""
        print(classes_db.Customer.delete(query))
        return customer()
    elif ask == "3":
        search_id = int(input('insert customer_id : '))
        column = input('insert seach column name: ')
        if column == 'first_name' or column == 'last_name' or column == 'phone_number':
            data = input('insert new data: ')
        else:
            data = int(input('insert new data: '))
        print(classes_db.Customer.update(search_id, column, data, 'customer', 'customer_id'))
        return customer()
    elif ask == '4':
        data = classes_db.Customer.select('customer')
        for i in data:
            print(i)
        return customer()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return customer()


def product_customer():
    ask = input("""product_customer page
        1. INSERT
        2. DELETE
        3. UPDATE
        4. SELECT
        5. BACK
        >>>> """)
    if ask == "1":
        product_id = int(input('insert product_id: '))
        customer_id = int(input('insert customer id: '))
        data = classes_db.ProductCustomer(product_id, customer_id)
        print(data.insert('product_customer'))
        return product_customer()
    elif ask == "2":
        column = input('insert column name : ')
        data = int(input('insert new data: '))
        query = f"""DELETE FROM product_customer WHERE {column} = {data};"""
        print(classes_db.ProductCustomer.delete(query))
        return product_customer()
    elif ask == "3":
        search_id = int(input('insert product customer id: '))
        column = input('insert column name : ')
        new_data = int(input('insert new data: '))
        print(classes_db.ProductCustomer.update(search_id, column, new_data, 'product_customer', 'product_customer_id'))
        return product_customer()
    elif ask == '4':
        data = classes_db.ProductCustomer.select('product_customer')
        for i in data:
            print(i)
        return product_customer()
    elif ask == '5':
        return main.main()
    else:
        print("ERROR")
        return product_customer()