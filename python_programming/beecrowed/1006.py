a = float(input())
b = float(input())
c = float(input())
a_weight = 2
b_weight = 3
c_weight = 5
total_weight = a_weight + b_weight + c_weight
weighted_sum = a * a_weight + b * b_weight + c * c_weight
avarage = weighted_sum / total_weight
print(f"MEDIA = {avarage:.1f}")