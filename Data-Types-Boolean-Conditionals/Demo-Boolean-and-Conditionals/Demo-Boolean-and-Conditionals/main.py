# # Example 1
# is_raining = False
# is_hot = True
# print(is_raining)  # Outputs: False
# print(is_hot)  # Outputs: True




# # Example 2
# number = int(input("Enter a number: "))
# if number < 10:
#     print("The number is small")
# else:
#     print("The number is large")




# # Example 3
# coin = float(input("Insert your coin: (0.1/0.25/0.5/1): "))
# if coin == 0.1:
#     print("10c coin received!")
# elif coin == 0.25:
#     print("25c coin received!")
# elif coin == 0.5:
#     print("50c coin received!")
# elif coin == 1:
#     print("$1 coin received!")
# else:
#     print("Invalid coin!")
# height = int(input("Please enter your height (cm): "))
# if height > 120:
#     age = int(input("Please enter your age: "))
#     if age > 18:
#         print("Please pay $12")
#     elif 12 <= age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $5")
# else:
#     print("Sorry, you are below the height limit and cannot be admitted into this ride")




# # Example 4
# height = int(input("Please enter your height (cm): "))
# if height > 120:
#     age = int(input("Please enter your age: "))
#     total_cost = 0
#     if age > 18:
#         print("Adult tickets are $12")
#         total_cost += 12
#     elif 12 <= age <= 18:
#         print("Youth tickets are $7")
#         total_cost += 7
#     else:
#         print("Child tickets are $5")
#         total_cost += 5
#     wants_photo = input("Do you want a photo taken for $3? (Y or N): ")
#     wants_shirt = input("Do you want to purchase a shirt at $5? (Y or N): ")
#     if wants_photo == "Y":
#         total_cost += 3
#     if wants_shirt == "Y":
#         total_cost += 5
    
#     print(f"Your final bill is ${total_cost}")
# else:
#     print("Sorry, you are below the height limit and cannot be admitted into this ride")