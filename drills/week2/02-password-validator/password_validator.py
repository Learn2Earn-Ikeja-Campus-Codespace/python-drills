def has_min_length(password):
    if len(password) >= 8:
        return True
    return False


def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False
        


def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def has_special(password):
    for char in password:
        if not char.isalnum():
            return True
    return False


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
