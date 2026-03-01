import math

def probability_lower_bound(test_outcomes, deviation):
    d = len(test_outcomes)

    print(d)
    return 1-2*math.exp(-2*(deviation**2)*d)



print(probability_lower_bound([True, False] * 500, 0.05))
print("xiu gai4")
