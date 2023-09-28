def islower(c):    # checks for lowercase character
    """Returns True if c is lowercase.

    Returns False otherwise.
    """
    dec = ord(c)
    if dec >= 97 and dec <= 122:
        return True
    else:
        return False
