def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return leap
        else:
            return True
    else:
        return leap

year = 2204
print(is_leap(year))