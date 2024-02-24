import database_korzinka


def main():
    ask = input("""
        1.country           7. payment_type
        2. city             8. payment
        3. address          9. category
        4. location         10. product
        5. admin            11. order_product
        6. employees        12. customer
                            13. product_customer
        
        >>>> """)

    if ask == '1':
        return database_korzinka.country()

    elif ask == '2':
        return database_korzinka.city()

    elif ask == '3':
        return database_korzinka.address()

    elif ask == '4':
        return database_korzinka.locations()

    elif ask == '5':
        return database_korzinka.admin()

    elif ask == '6':
        return database_korzinka.employees()

    elif ask == '7':
        return database_korzinka.payment_type()

    elif ask == '8':
        return database_korzinka.payment()

    elif ask == '9':
        return database_korzinka.category()

    elif ask == '10':
        return database_korzinka.product()

    elif ask == '11':
        return database_korzinka.order_product()

    elif ask == '12':
        return database_korzinka.customer()
    elif ask == '13':
        return database_korzinka.product_customer()
    else:
        print("ERROR")
        return main()


if __name__ == '__main__':
    main()