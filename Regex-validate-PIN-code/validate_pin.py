import re

# For some reason first one doesn't see white spaces on codewars.com
# But it work right in console
# Second function passed smoothly


def validate_pin(pin):
    result = re.match("^\d{4}$|^\d{6}$", pin)
    return True if (result) else False


def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        result = re.match("^\d{4}$|^\d{6}$", pin)
        return True if (result) else False
    else:
        return False


print(validate_pin("1234"))
print(validate_pin("12345"))
print(validate_pin("123456"))
print(validate_pin("1234 "))
