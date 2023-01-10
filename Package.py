class Package:
    def __init__(self, id, address, city, state, zip_code, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.start_time = None
        self.delivered_time = None
        self.is_delivered = False

    def __str__(self):
        return "ID: %s, Address: %s, City: %s, State: %s, \n" \
               "Zip Code: %s, Deadline Time: %s, Weight: %s, \n" \
               "Status: %s, Start Time: %s, Delivery Time: %s\n" % (self.id, self.address, self.city,
                                                       self.state, self.zip_code, self.deadline,
                                                       self.weight, self.status, self.start_time, self.delivered_time)

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