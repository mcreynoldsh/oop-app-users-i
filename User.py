class User:
    def __init__(self, name, email_address, license_number):
        self.name= name
        self.email_address= email_address
        self.license_number= license_number



person = User("Tyler","tyler29@gmail.com",2345603)

person2 = User("Jane","janejane@gmail.com",3049585)
print( person.name)
print(person2.name)