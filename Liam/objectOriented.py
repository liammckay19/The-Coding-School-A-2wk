class House:  # Object type
    def __init__(self, price=0, sqft=0, parking=False, address="", bath=0, bed=0):  # initialization method
        # Attributes  (starts with self. )
        self.price = price
        self.squareFeet = sqft
        self.parking = parking
        self.address = address
        self.bathrooms = bath
        self.bedrooms = bed
    
    # methods (functions inside of a class)
    def getPrice(self):
        return self.price
    
    def compareSqFt(self, obj_house):
        if type(obj_house) == type(House()):
            return self.squareFeet > obj_house.squareFeet
        else:
            return False
    
    def __str__(self):
        return "$" + str(self.price) + "\n" + str(self.squareFeet) + " sq. ft.\n"


def main():
    myHouse = House(1000000, 400, True, "500 Imnotastreet St. CA 9001", 1, 2)
    # instantiates an object, whose object type is House
    yourHouse = House(2000000, 800, False, "501 Imnotastreet St. CA 9001", 2, 2)
    obamasHouse = House(3000000, 1000, True, "502 Imnotastreet St. CA 9001", 4, 2)
    
    # I want to compare houses to each other. Make a one line statement to compare sq ft
    print(obamasHouse.compareSqFt(yourHouse))


if __name__ == '__main__':
    main()
