# second = int(input())
# hours = second // 60 // 60
# second2 = hours * 60 *60
# remaining_second = second - second2
# munit = remaining_second // 60
# second3 = munit * 60
# now_second = remaining_second - second3
# print(f"{hours}:{munit}:{now_second}")

seconds = int(input())
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print(f"{hours}:{minutes}:{seconds}")