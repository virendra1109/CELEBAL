def is_leap(year):
    # First condition: Check if year is divisible by 4
    if year % 4 == 0:
        # Second condition: Check if year is divisible by 100
        if year % 100 == 0:
            # Third condition: Check if year is divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False