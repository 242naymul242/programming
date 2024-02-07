import math  


number_of_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
# number_of_groups = number_of_students // group_size
# remaining_studetns = number_of_students % group_size
# if remaining_studetns != 0:
    # number_of_groups += 1
number_of_groups = math.ceil(number_of_students / group_size)
print(f"Number of groups formed: {number_of_groups}")