import re
# Does a string contain a phone number?
def has_phone_number(input_string):
    phone_number = r"[\d]{3}-[\d]{3}-[\d]{4}" 
    has_number = re.search(phone_number, input_string)
    if has_number == None:
        return False
    return True

# Get a phone number back from a string
def get_phone_number(input_string):
    phone_number = r"[\d]{3}-[\d]{3}-[\d]{4}" 
    has_number = re.search(phone_number, input_string)
    if has_number == None:
        return has_number
    return has_number.group()


# Gets and returns all phone numbers from an inputed string
def get_all_phone_numbers(input_string):
    phone_number = r"[\d]{3}-[\d]{3}-[\d]{4}" 
    return re.findall(phone_number, input_string)


# Hide all numbers in a phone number except the last 4 digits. An example of this looks like: XXX-XXX-1234
def hide_phone_numbers(input_string):
    return re.sub(r"\d{3}.\d{3}", "XXX-XXX", input_string, count = 0)


# Get the string of the phone number and format it for our pretend application. Ensure all of the phone numbers use dashes for delimiters.
# Example: 312-111-2222, 312.111.2222, (312) 111-2222 would all be 312-111-2222
def format_phone_number(input_string):
    return re.sub(r"(\(?(\d{3})\.?-?\)?\s?(\d{3})\.?-?(\d{4}))", r"\2-\3-\4", input_string, count = 0)
