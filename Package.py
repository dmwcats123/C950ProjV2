# create class to hold packages
class Package:
    def __init__(self, id, state, city, deadline, zip_code,  weight, address, status):
        self.start_time = None
        self.delivered_time = None
        self.is_delivered = False
        self.id = id
        self.state = state
        self.city = city
        self.deadline = deadline
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
        self.address = address


    def __str__(self):
        return "ID: %s, Address: %s, City: %s, State: %s, " \
               "Zip Code: %s, Deadline Time: %s, Weight: %s, " \
               "Status: %s, Start Time: %s, Delivery Time: %s" % (self.id, self.address, self.city,
                                                       self.state, self.zip_code, self.deadline,
                                                       self.weight, self.status, self.start_time, self.delivered_time)

# Checks if a status is delivered at a specified time.
    def check_delivered(self, current_time):
        if self.delivered_time < current_time:
            self.status = "Delivered"
            self.is_delivered = True
        elif self.delivered_time > current_time:
            self.status = "On the way"
            self.is_delivered = False
        else:
            self.status = "At Hub"
            self.is_delivered = True