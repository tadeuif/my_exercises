first_input = input()
second_input = input()

first_array = first_input.split()
second_array = second_input.split()

code_a = int(first_array[0])
code_b = int(second_array[0])

units_a = int(first_array[1])
units_b = int(second_array[1])

price_a = float(first_array[2])
price_b = float(second_array[2])

total_a = float(price_a * units_a)
total_b = float(price_b * units_b)

print("VALOR A PAGAR: R$ %.2f" % (total_a + total_b))