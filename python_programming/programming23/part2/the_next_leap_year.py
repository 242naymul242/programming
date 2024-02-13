def is_leep_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False
        
year = int(input("Year: "))     
next_year = year
while True:
    next_year = next_year + 1
    if is_leep_year(next_year):
        print(f"The next leap year after {year} is {next_year}")
        break
    
