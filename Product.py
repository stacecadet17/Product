class Product(object):
    def __init__(self, price, name, weight, brand, status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self):
        self.price = (.09 * self.price) + self.price
        return self
    def Return(self):
        if (self.status == "defective"):
            self.price = 0
        elif(self.status == "for sale"):
            self.price = self.price
        elif(self.status == "used"):
            self.price = self.price - (.20 * self.price)
        return self
    def display_info(self):
        print "Price is" + " " + str(self.price) + " " + "dollars"
        print self.name + ""
        print str(self.weight) + "lbs"
        print self.brand + ""
        print self.status + ""
        return self

product1 = Product(100, "crossbody bag", 2, "Kate Spade", "defective")
product2 = Product(1000, "Suede Pumps", 2, "Christian Louboutin", "for sale")

product1.Return().display_info()
product2.sell().display_info()
