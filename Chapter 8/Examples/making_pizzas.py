# First imported function from my own library
from make_pizza import make_pizza as mp
import make_pizza

pz_size = input('Pizza size: ')
mp(pz_size, 'Corn', 'Olives', 'Spicy Peppers', 'Pepperoni', 'Extra cheese')
