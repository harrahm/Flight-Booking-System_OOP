class Flight():#class

    #class variables belong here and are attributes which are consistent amongst all objects e.g. all cars have 4 wheels or all humans 2 hands. the constructor variable will specify the skin/eye colour which varies from person to person
    

    def __init__(self, flightNumber, departurePort, arrivalPort, departureTime, arrivalTime, availableSeats, price):
        #these are constructor variables which help give an object unique attributes
        self.flightNumber = flightNumber
        self.departurePort = departurePort
        self.arrivalPort = arrivalPort
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.availableSeats = availableSeats
        self.price = price

    #methods:
    def bookSeat(self):
        if self.availableSeats > 0:
            self.availableSeats -= 1

        else:
            print('No more available seats!')


    def cancelBooking(self):
        self.availableSeats += 1


    def getFlightDetails(self): 
        print(f'Flight number:{self.flightNumber} \nDeparting from: {self.departurePort} at {self.departureTime}\nArriving to: {self.arrivalPort} at {self.arrivalTime}\nNumber of Available Seats: {self.availableSeats}')
        

    def getPrice(self, seatClass): #Returns the price based on the seat class (economy, business, first).
        if seatClass == 'First':
            self.price += 30
        
        elif seatClass == 'Business':
            self.price += 20
        
        elif seatClass == 'Economy':
            self.price += 15
        
        else:
            print('Invalid seat class')
        
        print(f'£{self.price}')