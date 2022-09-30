class Phone:
    def __int__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f" is calling {phone_number} ")


iphone = Phone
samsung = Phone

print(iphone.brand)