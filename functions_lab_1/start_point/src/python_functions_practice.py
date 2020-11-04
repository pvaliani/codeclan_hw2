
#first test function to return 10
def return_10():
    return 10

#second test function to add two integers
def add(num_1, num_2):
    num_3 = num_1 + num_2
    return num_3

#third test function to subtract two integers
def subtract(num_3, num_4):
    num_5 = num_3 - num_4
    return num_5

#fourth test function to multiply two integers
def multiply(num_6, num_7):
    num_8 = num_6 * num_7
    return num_8

#fifth test function to divide two integers
def divide(num_9, num_10):
    num_11 = num_9 / num_10
    return num_11


#sixth test function to return length of a string
def length_of_string(string):
    return len(string)

#seventh test function to join to strings
def join_string(string_1, string_2):
    string_1 = "Mary had a little lamb, "
    string_2 = "its fleece was white as snow"
    string_3 = string_1 + string_2
    return string_3

#eigthth test function to add two strings as converted ints
def add_string_as_number(string_4, string_5):
    return int(string_4) + int(string_5)

#ninth test function to convert number to full name of month - January
import datetime
#import datetime to utilise its date conversion properties
def number_to_full_month_name(month_number):
    datetime_object = datetime.datetime.strptime(str(month_number), "%m")
    month_name = datetime_object.strftime("%B")
    return month_name

#tenth test function to convert number to full name of month - March

def number_to_full_month_name(month_number):
    datetime_object = datetime.datetime.strptime(str(month_number), "%m")
    month_name = datetime_object.strftime("%B") #upper case B for long name month
    return month_name

#eleventh test function to convert number to full name of month - September

def number_to_full_month_name(month_number):
    datetime_object = datetime.datetime.strptime(str(month_number), "%m")
    month_name = datetime_object.strftime("%B")
    return month_name

#twelfth test function to convert number to short name of month - January

def number_to_short_month_name(month_number_2):
    datetime_object = datetime.datetime.strptime(str(month_number_2), "%m")
    month_name_2 = datetime_object.strftime("%b") #lower case b for shorthand month
    return month_name_2

#thirteenth test function to convert number to short name of month - April

def number_to_short_month_name(month_number_2):
    datetime_object = datetime.datetime.strptime(str(month_number_2), "%m")
    month_name_2 = datetime_object.strftime("%b") #lower case b for shorthand month
    return month_name_2

#fourteenth test function to convert number to short name of month - October

def number_to_short_month_name(month_number_2):
    datetime_object = datetime.datetime.strptime(str(month_number_2), "%m")
    month_name_2 = datetime_object.strftime("%b") #lower case b for shorthand month
    return month_name_2

# fifteenth test function to calculate volume of a cube given a side
def volume_of_cube(length_side):
    volume = length_side * length_side * length_side
    return volume

#sixteenth test function to reverse a string
def reverse_string(string):
    new_string = list(string)
    new_string.reverse()
    final_string = ''.join(new_string)
    return final_string

#seventeenth test function to convert farenheit to celcius 

def fahrenheit_to_celsius(fahrenheit):
    return ((fahrenheit-32) * 5)/9

