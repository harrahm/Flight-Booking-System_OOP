#Passenger: This class represents a passenger with attributes like passengerID, 
# name, passportNumber, contactDetails, and bookings (a list of Booking objects).
class Passenger: 
    def __init__(self, passengerID, name, passportNumber, contactDetails, bookings):
        self.passengerID = passengerID
        self.name = name
        self.passportNumber = passportNumber
        self.contactDetails = contactDetails
        self.bookings = bookings

    