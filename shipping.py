weight = float(input("What is the weight of the package? : "))
premium_ground_cost = 120


if weight <= 2:
    cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
    cost_ground = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
    cost_ground = weight * 4.00 + 20
elif weight > 10:
    cost_ground = weight * 4.75 + 20

print("Ground Shipping :"+ str(cost_ground) +" EUR")

print("Premium Shipping : " + str(premium_ground_cost)+" EUR")

if weight <= 2:
    cost = weight * 4.5 + 0.00
elif weight > 2 and weight <= 6:
    cost = weight * 9.00 + 0.00
elif weight > 6 and weight <= 10:
    cost = weight * 12.00 + 0.00
elif weight > 10:
    cost = weight * 14.25 + 0.00
print("Drone Shipping :"+ str(cost) +" EUR")




