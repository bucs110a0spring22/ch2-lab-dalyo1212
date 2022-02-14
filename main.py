import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 10
cost_per_class = cost_per_week/classes_per_week
print("This is how much you're paying for each class per week:", cost_per_class)
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))


#Part B
nums = [1,2,3,4,5]
random.choice(nums)
random_nums = random.choice(nums)
print("Random Number Generator:", random_nums)