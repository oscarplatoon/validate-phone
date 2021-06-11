import re
# Does a string contain a phone number?
def has_phone_number(input_string):
    if re.search('\d{3}-\d{3}-\d{4}',input_string) == None:
        return False
    else:
        return True

# Get a phone number back from a string
def get_phone_number(input_string):
    out = re.findall('\d{3}-\d{3}-\d{4}',input_string)
    if out == []: return None
    else: return out[0]
    


# Gets and returns all phone numbers from an inputed string
def get_all_phone_numbers(input_string):
    return re.findall('\d{3}-\d{3}-\d{4}',input_string)
    


# Hide all numbers in a phone number except the last 4 digits. An example of this looks like: XXX-XXX-1234
def hide_phone_numbers(input_string):
    return re.sub('\d{3}-\d{3}-','XXX-XXX-',input_string)


# Get the string of the phone number and format it for our pretend application. Ensure all of the phone numbers use dashes for delimiters.
# Example: 312-111-2222, 312.111.2222, (312) 111-2222 would all be 312-111-2222
def format_phone_number(input_string):
    out = re.sub('[^\d,]*','',input_string)
    final = []
    for x in out.split(','):
        final.append(x[0:3]+'-'+x[3:6]+'-'+x[6:])
    return(', '.join(final))
