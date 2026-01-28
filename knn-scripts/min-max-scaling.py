def calculate_min_max_scaled(value, min, max):
    return (value - min) / (max - min)

# Calculate the Bill Length Normalisation
x1_bill_length = calculate_min_max_scaled(39.1, 30, 60)
print("x1 bill length " + str(x1_bill_length))

x2_bill_length = calculate_min_max_scaled(50.2, 30, 60)
print("x2 bill length " + str(x2_bill_length))

q_bill_length = calculate_min_max_scaled(39.5, 30, 60)
print("q bill length " + str(q_bill_length))
print()

# Calculate the Bill Depth Normalisation
x1_bill_depth = calculate_min_max_scaled(18.7, 10, 20)
print("x1 bill depth " + str(x1_bill_depth))

x2_bill_depth = calculate_min_max_scaled(14.3, 10, 20)
print("x2 bill depth " + str(x2_bill_depth))

q_bill_depth = calculate_min_max_scaled(17.4, 10, 20)
print("q bill depth " + str(q_bill_depth))
print()

# Calculate the Flipper Length Normalisation
x1_flipper_length = calculate_min_max_scaled(181, 170, 230)
print("x1 flipper length " + str(x1_flipper_length))

x2_flipper_length = calculate_min_max_scaled(218, 170, 230)
print("x2 flipper length " + str(x2_flipper_length))

q_flipper_length = calculate_min_max_scaled(186, 170, 230)
print("q flipper length " + str(q_flipper_length))
print()

# Calculate the Body Mass Normalisation
x1_body_mass = calculate_min_max_scaled(3750, 3000, 6000)
print("x1 body mass " + str(x1_body_mass))

x2_body_mass = calculate_min_max_scaled(5700, 3000, 6000)
print("x2 body mass " + str(x2_body_mass))

q_body_mass = calculate_min_max_scaled(3800, 3000, 6000)
print("q body mass " + str(q_body_mass))