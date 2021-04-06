"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Matthew Savin
Date:   1/23/2021
"""

import introcs
import currency

def test_before_space():
    
    """Test procedure for before_space"""
    
    result = currency.before_space('Matthew Savin')
    introcs.assert_equals('Matthew', result)
    
    result = currency.before_space('Matthew Walker Savin')
    introcs.assert_equals('Matthew', result)
    
    result = currency.before_space(' Matthew')
    introcs.assert_equals('', result)
    
    result = currency.before_space('Hello  Matthew')
    introcs.assert_equals('Hello', result)
    
    print("Testing before_space.")
    
    
def test_after_space():
    
    """Test procedure for after_space_space"""
    
    result = currency.after_space('Matthew Savin')
    introcs.assert_equals('Savin', result)
    
    result = currency.after_space('Matthew Walker Savin')
    introcs.assert_equals('Walker Savin', result)
    
    result = currency.after_space('Matthew ')
    introcs.assert_equals('', result)
    
    result = currency.after_space('Hello  Matthew')
    introcs.assert_equals(' Matthew', result)
    
    print("Testing after_space.")
    
    
def test_first_inside_quotes():
    
    """Test procedure for first_inside_quotes"""
    
    result = currency.first_inside_quotes('"Matthew Savin"')
    introcs.assert_equals('Matthew Savin', result)
    
    result = currency.first_inside_quotes('Matthew "Savin"')
    introcs.assert_equals('Savin', result)
    
    result = currency.first_inside_quotes('"Matthew""Savin"')
    introcs.assert_equals('Matthew', result) 
    
    result = currency.first_inside_quotes('"""Matthew Savin"')
    introcs.assert_equals('', result)
    
    print("Testing first_inside_quotes.")
    
    
def test_get_src():
    
    """Test procedure for get_src"""
    
    result = currency.get_src('{"success": true, "src": "2 United States Dollars",'+
                              ' "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)
    
    result = currency.get_src('{"success":false,"src":"","dst":"",'+
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)
    
    result = currency.get_src('{"success": true, "src":"2 United States Dollars",'+
                              ' "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)
    
    result = currency.get_src('{"success": false,"src": "","dst": "",'+
                              '"error": "Source currency code is invalid."}')
    introcs.assert_equals('', result)
    
    print("Testing get_src.")
    
    
def test_get_dst():
    
    """Test procedure for get_dst"""
    
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars",'+
                              ' "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)
    
    result = currency.get_dst('{"success":false,"src":"","dst":"",'+
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)
    
    result = currency.get_dst('{"success":true, "src":"2 United States Dollars",'+
                              ' "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros', result)
    
    result = currency.get_dst('{"success": false,"src":"","dst": "",'+
                              '"error": "Source currency code is invalid."}')
    introcs.assert_equals('', result)
    
    print("Testing get_dst.")
    

def test_has_error():
    
    """Test procedure for has_error"""
    
    result = currency.has_error('{"success":false,"src":"","dst":"",'+
                                '"error":"Source currency code is invalid."}')
    introcs.assert_true(result)
    
    result = currency.has_error('{"success": true, "src": "2 United States Dollars",'+
                                ' "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(result)
    
    result = currency.has_error('{"success":true, "src":"2 United States Dollars",'+
                                ' "dst":"1.772814 Euros", "error":""}')
    introcs.assert_false(result)
    
    result = currency.has_error('{"success": false,"src": "","dst": "",'+
                                '"error": "Source currency code is invalid."}')
    introcs.assert_true(result)
    
    print("Testing has_error.")
    
    
def test_service_response():
    
    """Test procedure for service_response"""
    
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars",'+
                          ' "dst": "2.2160175 Euros", "error": ""}', currency.service_response('USD','EUR',2.5))
    
    introcs.assert_equals('{"success": true, "src": "-2.5 United States Dollars",'+
                          ' "dst": "-2.2160175 Euros", "error": ""}', currency.service_response('USD','EUR',-2.5))

    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error":'+
                          ' "The rate for currency EOR is not present."}', currency.service_response('USD', 'EOR', 0.0))
    
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error":'+
                          ' "The rate for currency UAD is not present."}', currency.service_response('UAD', 'EUR', 0.0))
    
    print("Testing service_response.")
    
    
def test_iscurrency():
    
    """Test procedure for iscurrency"""
    
    introcs.assert_true(currency.iscurrency('USD'))
    
    introcs.assert_false(currency.iscurrency('EOR'))
    
    print("Testing iscurrency.")
    
    
def test_exchange():
    
    """Test procedure for exchange"""

    result = currency.exchange('USD','EUR',2.5)
    introcs.assert_floats_equal(2.2160175, result)

    result = currency.exchange('USD','EUR',-2.5)
    introcs.assert_floats_equal(-2.2160175, result)
    
    print("Testing exchange.")
    
    
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()

print("All tests completed successfully.")