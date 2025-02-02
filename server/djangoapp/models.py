from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
# - Name
    name = models.CharField(null=False, max_length=30, default='')
# - Description
    description = models.CharField(max_length=500)
# - __str__ method to print a car make object
    def __str__(self):
        return "Name: " + self.name + ", " + \
               "Description" + self.description 

class CarModel(models.Model):
    CAR_TYPES = [
        ("SE", "Sedan"),
        ("SU", "SUV"),
        ("WA", "Wagon"),
        ("TR", "Truck")
    ]
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
    carMake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
# - Name
    name = models.CharField(null=False, max_length=30, default='')
# - Dealer id, used to refer a dealer created in cloudant database
    dealerId = models.IntegerField(null=False)
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
    carType = models.CharField(choices=CAR_TYPES, max_length=2)
# - Year (DateField)
    year = models.DateField(null=False)
# - __str__ method to print a car make object
    def __str__(self):
        return "Name: " + self.name + ", " + \
               "Type: " + self.carType + ", " + \
               "Year: " + self.year.strftime("%Y")

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        
        self.dealership = dealership
        
        self.name = name
        
        self.purchase = purchase
        
        self.review = review
       
        self.purchase_date = purchase_date
        
        self.car_make = car_make

        self.car_model = car_model

        self.car_year = car_year

        self.sentiment = sentiment

        self.id = id

    def __str__(self):
        return "Review name: " + self.name