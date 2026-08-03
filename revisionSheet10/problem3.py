from random import randint

class Train:
    def __init__(self, t_no, src, dest):
        self.t_no = t_no
        self.src = src
        self.dest = dest

    def bookTicket(self):
        print(f"Ticket is Booked from {self.src} to {self.dest} in Train no.-> {self.t_no}")

    def status(self):
        print(f"Train is Running {self.t_no}")

    def fare(self):
        print(f"Fare for your journey from {self.src} to {self.dest} in Train no.-> {self.t_no} is : {randint(1,2000)}")



bullet_train = Train(12002, "New Delhi", "Bhopal")


bullet_train.bookTicket()
bullet_train.status()
bullet_train.fare()
