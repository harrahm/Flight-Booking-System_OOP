from flight import Flight 
from passenger import Passenger


#flights available

flight1 = Flight('BA123', 'LHR', 'JFK', 200, 200)
flight2 = Flight('TK007', 'STN', 'DAC', 500, 500)
flight3 = Flight('TK010', 'STN', 'IST', 500, 500)
flight4 = Flight('FR821', 'BCN', 'LGW', 300, 300)
flight5 = Flight("EK169", "LGW", "CDG", 150, 150)
flight6 = Flight("EZ456", "BER", "FCO", 200, 200)

#potential flyers
passenger1 = Passenger('1', 'Spongebob')
passenger2 = Passenger('2', 'Patrick')
passenger3 = Passenger('3', 'Sandy')
passenger4 = Passenger('4', 'Squidward')
passenger5 = Passenger('5', 'Plankton')



flight5.cancelBooking()
passenger3.getPassengerDetails()
