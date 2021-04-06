"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Matthew Savin
Date:   01/23/2021
"""

import introcs

APIKEY = "eOJaamPj6YeQY5ItpnhIxY20RX52nWCOsxivbmQqyrce"

def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str
    assert introcs.count_str(s, " ")
    
    space = introcs.find_str(s, " ")
    word = s[ :space]
    return word


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str
    assert introcs.count_str(s, " ")
    
    space = introcs.find_str(s, " ")
    word = s[space + 1: ]
    return word


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert type(s) == str
    assert introcs.count_str(s, '\"') >=2
    
    first_quote = introcs.find_str(s, '"') + 1
    second_quote = introcs.find_str(s, '"', first_quote)
    return s[first_quote : second_quote]


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
    On the other hand if the json is 

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str
    
    start_src = introcs.find_str(json,'"src":')+6
    src_string = json[start_src:]
    return first_inside_quotes(src_string)


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is 

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str
    
    start_dst = introcs.find_str(json,'"dst":')+6
    dst_string = json[start_dst:]
    return first_inside_quotes(dst_string)


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message 
    'Source currency code is invalid'). On the other hand if the json is 

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str
    
    start_error = introcs.find_str(json,'"error":')+8
    end_error = json[start_error:]
    return len(end_error) > 4


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response 
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src 
    and dst currencies, respectively. If the query is invalid, both src-amount and 
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert type(src) == str and src != ''
    assert type(dst) == str and dst != ''
    assert type(amt) == float, int
    
    var1 = 'https://ecpyfac.ecornell.com/python/currency/fixed?src='+str(src)+\
    '&dst='+str(dst)+'&amt='+str(amt)+'&key=eOJaamPj6YeQY5ItpnhIxY20RX52nWCOsxivbmQqyrce'
    var2 = introcs.urlread(var1)
    return var2


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    assert introcs.isalpha(currency)
    
    #Call service_response, hard code dst and the amount. ('Isolate the src')
    a = service_response(currency,'EUR', 2.5)
    #Call has_error. We are evaluating the service_response here.
    b = has_error(a)
    #Has_error is going to return false if it is a valid currency. Use boolean opperator to return the opposite. 
    return not (b)


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency 
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert type(src) == str
    assert introcs.isalpha(src)
    assert type(dst) == str
    assert introcs.isalpha(dst)
    assert type(amt) == float, int
    
    #call the service_response and assign it to variable.
    a = service_response(src, dst, amt)
    #isolate the dst and assign it to variable.
    b = get_dst(a)
    #in "1.772814 Euros". Use the before_space function to isolate just the numbers.
    c = before_space(b)
    #return it as a float.
    return float(c)

    


    