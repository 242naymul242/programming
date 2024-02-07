input1 = input().split()
input2 = input().split()

product1_number_of_units = int(input1[1])
product1_unit_price = float(input1[2])
product1_sub_total_price = product1_number_of_units * product1_unit_price

product2_number_of_units = int(input2[1])
product2_unit_price = float(input2[2])
product2_sub_total_price = product2_number_of_units * product2_unit_price

total_price = product1_sub_total_price + product2_sub_total_price
print(f"VALOR A PAGAR: R$ {total_price:.2f}")  