"""
# Take two int values from the user and print the greatest among them

int_1 = input('Enter first integer: ')
int_2 = input('Enter second integer: ')

if int_1 > int_2:
  print(f'{int_1} is greater than {int_2'})
else:
  print(f'{int_2} is greater than {int_1'})



# A student will not be allowed to sit in exam if his/ her attendance is less than 75%.
# take following input from the User
# number of classes held
# number of classes attended
# print percentage of classes attended
# is student allowed to sit for exams open
# modify the above question to allow student to sit if he/ she has a medical cause
# Ask user if he/ she has medical cause or not('Y' of 'N') and print accordingly

classes_held = int(input('Enter the number of classes held: '))
classes_attended = int(input('Enter the number of attended held: '))
percentage_of_classes_attendence = classes_attended/classes_held*100
print(percentage_of_classes_attendence, '%')


if percentage_of_classes_attendence >= 75 and percentage_of_classes_attendence <= 100:
  print('You are allowed to sit for exams.')
elif percentage_of_classes_attendence < 75 and percentage_of_classes_attendence > 0:
  print(input("Do you have a medical Cause, Y or N: "))
  if 'Y':
    print(str('You are allowed to sit for exams.'))
  elif 'N':
    print(str('You are not allowed to sit for exams.'))
  else:
    pass
else:
  pass


# A shop will give discount of 10% if the cost of the purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100, judge and print total cost for user

one_unit = int(100)
units_purchased = int(input("Enter units purchase: "))
quantity_purchased = one_unit * units_purchased
discount = int(quantity_purchased * 10/100)

if quantity_purchased > int(1000):
  print(quantity_purchased - discount)
elif quantity_purchased <= int(1000) and quantity_purchased > int(0):
  print(quantity_purchased)
else:
  pass



# Accept two int values from the user and return their product.
# If the product is greater than 1000, then return their sum

int_one = int(input('Enter the first integer: '))
int_two = int(input('Enter the second integer: '))
int_product = int_one * int_two
int_sum = int_one + int_two


if int_product < int(1000):
  print(int_product)
elif int_product > int(1000):
  print(int_sum)
else:
  pass




# given a list of ints, return True if first and last number of a list is same

int_list = list(input('Enter a list: '))

if int_list[0]==int_list[-1]:
  print(True)
else:
  print(False)
"""
