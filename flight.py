class Flight():#class

    #class variables belong here and are attributes which are consistent amongst all objects e.g. all cars have 4 wheels or all humans 2 hands. the constructor variable will specify the skin/eye colour which varies from person to person

    def __init__(self, flightNumber, departurePort, arrivalPort, availableSeats, max_seats): #constructor of the class - defines all the attributes of the class
        #these are constructor variables which help give an object unique attributes
        self.flightNumber = flightNumber
        self.departurePort = departurePort
        self.arrivalPort = arrivalPort
        self.availableSeats = availableSeats
        self.max_seats = max_seats

    #methods:
    def bookSeat(self):
        if self.availableSeats > 0:
            self.availableSeats -= 1

        else:
            print('No more available seats!')


    def cancelBooking(self):
        if self.availableSeats < self.max_seats:
            self.availableSeats += 1

        else:
            print('There are no more seats to cancel!')


    def getFlightDetails(self): 
        print(f'Flight number:{self.flightNumber} \nDeparting from: {self.departurePort} \nArriving to: {self.arrivalPort}\nNumber of Available Seats: {self.availableSeats}')
        