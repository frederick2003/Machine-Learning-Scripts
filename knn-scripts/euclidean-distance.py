import math

def euclidean_distance(x1, x2):
    if len(x1) != len(x2):
        raise ValueError("Vectors must have the same length")
    
    sum_squared_distance = 0
    for i in range(len(x1)):
        sum_squared_distance += (x1[i] - x2[i])**2
    return math.sqrt(sum_squared_distance)


x1 = [0.05, 0.646]
x2 = [0.4, 0.364]
ed_x1_x2 = euclidean_distance(x1,x2)

print(f"Euclidean distance between x1 and x2: {ed_x1_x2:.3f}")