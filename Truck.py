class Truck:
    def __init__(self, capacity, speed, load, packages, address, depart_time):
        self.capacity=capacity
        self.speed=speed
        self.load=load
        self.packages=packages
        self.mileage=0
        self.address=address
        self.depart_time=depart_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages, self.mileage,
                                               self.address, self.depart_time)

