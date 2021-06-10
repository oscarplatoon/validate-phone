import re
# Does a string contain a phone number?
def has_phone_number(input_string):
    pattern = "\d{3}-\d{3}-\d{4}"
    number = re.search(pattern,input_string)
    if number == None:
       return False
    return True
# Get a phone number back from a string
def get_phone_number(input_string):
    pattern = "\d{3}-\d{3}-\d{4}"
    number = re.search(pattern, input_string)
    if number == None:
        return None
    return number.group()
    

# Gets and returns all phone numbers from an inputed string
def get_all_phone_numbers(input_string):
    pattern = "\d{3}-\d{3}-\d{4}"
    phone_numbers = re.findall(pattern, input_string)
    return phone_numbers


# Hide all numbers in a phone number except the last 4 digits. An example of this looks like: XXX-XXX-1234
def hide_phone_numbers(input_string):
    pattern = "\d{3}.\d{3}"
    return re.sub(pattern, "XXX-XXX", input_string, count=0)


# Get the string of the phone number and format it for our pretend application. Ensure all of the phone numbers use dashes for delimiters.
# Example: 312-111-2222, 312.111.2222, (312) 111-2222 would all be 312-111-2222
def format_phone_number(input_string):
    pass
