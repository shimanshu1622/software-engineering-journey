'''
Create a class Movie with the following:

Attributes:
movie_name ->name of the movie
total_seats -> total seats available in the theatre
ticket_price -> price per ticket
booked_seats -> starts at 0

Methods:
book_ticket(num_tickets) books the given number of tickets. 
If enough seats are available, confirm the booking and show the total amount to pay. 
If not, show "Sorry, not enough seats available"

show_status() - displays movie name, seats available, and seats booked so far
'''


class Movie:
    def __init__(self,movie_name:str, total_seats:int, ticket_price:int):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_ticket(self,num_ticket):
        if self.total_seats < num_ticket:
            print("Sorry, not enough seats avilable\n")
        else:
            self.booked_seats += num_ticket
            self.total_seats -= num_ticket
            print(f"Your {num_ticket} ticket is Booked")
            print(f"Total amount to Pay: {num_ticket * self.ticket_price}\n")

    def show_status(self):
        print(f"Movie name is: {self.movie_name}")
        print(f"Total seats available are: {self.total_seats}")
        print(f"Total seats booked: {self.booked_seats}\n")

movie = Movie("Spiderman",100,399)
movie.show_status()

movie.book_ticket(65)

movie.show_status()

movie.book_ticket(50)

movie.show_status()

movie.book_ticket(25)

movie.show_status()