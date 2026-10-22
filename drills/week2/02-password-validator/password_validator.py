def has_min_length(password):
    if  len(password) >= 8:
    


def has_uppercase(password):
    if password.isupper():
    


def has_lowercase(password):
    if password.islower():
    


def has_digit(password):
    is password.isdigit():
    


def has_special(password):
    for char in password:
        if  not char.isalnum():
            return False
    return True
    


def is_valid_password(password):
    if has_min_length(password) and
    has_uppercase(password) and
    has_lowercase(password) and
    has_digit(password) and
    has_special(password):
        return True
    return False



# bonus
def get_failed_requirements(password):
    # Write your code here
    pass
