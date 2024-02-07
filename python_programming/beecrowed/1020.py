day = int(input())
year = day // 365
remaining_day = day - year * 365 
month = remaining_day // 30
day1 = month * 30
now_day = remaining_day - day1
print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{now_day} dia(s)")