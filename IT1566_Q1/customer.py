class Customer:
    def __init__(self, name, email, mobile_number):
        self.__name = name
        self.__email = email
        self.__mobile_number = mobile_number

    def get_customer_info(self):
        return 'Name: ' + self.__name + ', Email: ' + self.__email + \
               ', Mobile Number: ' + self.__mobile_number


c = Customer("Keat Kean", "lee_keat_kean@nyp.edu.sg", "88888888")
print(c.get_customer_info())
