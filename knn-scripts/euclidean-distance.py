import math

def euclidean_distance(x1, x2):
    if len(x1) != len(x2):
        raise ValueError("Vectors must have the same length")
    
    sum_squared_distance = 0
    for i in range(len(x1)):
        sum_squared_distance += (x1[i] - x2[i])**2
    return math.sqrt(sum_squared_distance)


x1 = [0.303, 0.870, 0.183, 0.250]
x2 = [0.673, 0.430, 0.800, 0.900]
q =  [0.317, 0.740, 0.267, 0.267]
ed_x1_q = euclidean_distance(x1,q)
ed_x2_q = euclidean_distance(x2,q)

print(f"Euclidean distance between x1 and q: {ed_x1_q:.3f}")
print(f"Euclidean distance between x2 and q: {ed_x2_q:.3f}")