"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Matthew Savin
Date:   1/23/2021
"""

import currency

# Get the src value
get_src = input('3-letter code for original currency: ')

# Get the dst value
get_dst = input('3-letter code for the new currency: ')

# Get the amt value
get_amt = input('Amount of the original currency: ')
float_amt = float(get_amt)

# Get exchange amount by calling exchange function
exchange_function = currency.exchange(src = get_src, dst = get_dst, amt = float_amt)

# Print the output and combine each segment together using concatination.
print('You can exchange'+' '+str(float_amt)+' '+str(get_src)+ ' for '+ str(round(exchange_function, 3))+' '+str(get_dst)+'.')

