"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    seat = ['A','B','C','D']
    for letter in range(number):
        yield seat[letter%4]



def generate_seats(number):
    row= 1
    count = 0
    while count < number:
        if row == 13:
            row += 1
            continue
        for letter in ['A','B','C','D']:
            if count>=number:
                break
            yield f"{row}{letter}"
            count += 1
        row += 1
        
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

def assign_seats(passengers):
    seats = generate_seats(len(passengers))
    return {passenger: next(seats) for passenger in passengers}


def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        code = f"{seat}{flight_id}"
        yield code + '0' * (12 - len(code))

