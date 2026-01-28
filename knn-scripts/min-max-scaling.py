def calculate_min_max_scaled(value, min, max):
    return (value - min) / (max - min)

min = int(input("Enter min value: "))
max = int(input("Enter max value: "))
value = int(input("Enter feature value: "))

print(f"Min-Max Scaled value = {calculate_min_max_scaled(value, min, max):.3f}")