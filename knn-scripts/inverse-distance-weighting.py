# A method that calculates the IDW for a given distance
def inverse_distance_weight(weight):
    return 1 / weight

over_total_weight = 0
under_total_weight = 0

x1 = 1.5
x1_inverse_weight = inverse_distance_weight(x1)
print(f"x1 inverse distance-weight: {x1_inverse_weight:.3f}")
over_total_weight+=x1_inverse_weight

x3 = 1.8
x3_inverse_weight = inverse_distance_weight(x3)
print(f"x3 inverse distance-weight: {x3_inverse_weight:.3f}")
over_total_weight+=x3_inverse_weight

x5 = 2.2
x5_inverse_weight = inverse_distance_weight(x5)
print(f"x5 inverse distance-weight: {x5_inverse_weight:.3f}")
under_total_weight+=x5_inverse_weight

x7 = 2.4
x7_inverse_weight = inverse_distance_weight(x7)
print(f"x7 inverse distance-weight: {x7_inverse_weight:.3f}")
under_total_weight+=x7_inverse_weight


print(f"Over total weighted vote : {over_total_weight:.3f}")
print(f"Under total weighted vote : {under_total_weight:.3f}")