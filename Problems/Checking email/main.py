def check_email(string):
    length_string = len(string)
    at = string.find('@')
    if length_string == len(string.replace(' ', '')):
        return string.find('.', at, length_string) > at + 1
    return False

    # Another solution 1
    # if '@' in string and ' ' not in string and '@.' not in string:
    #     return string.rfind('.') > string.find('@') + 1
    # return False
