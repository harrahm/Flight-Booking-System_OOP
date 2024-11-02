#Passenger: This class represents a passenger with attributes like passengerID, 
# name, passportNumber, contactDetails, and bookings (a list of Booking objects).
class Passenger(): 
    def __init__(self, passengerID, name):
        self.passengerID = passengerID
        self.name = name

    def getPassengerDetails(self):
        print(f'Passenger Details \nID: {self.passengerID} \nName: {self.name}')

    