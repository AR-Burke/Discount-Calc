########################
#
# Python Lab 2
# Class Section: CS 135
# Name: Aria Burke
# Insturctor: Qiping Yan
# Assignment Lab #2
# Submission Date : 2/10/2023
# comments: none
# 
########################

amount = int(input("Enter Number of packages Sold: "))
price = 99
discount = 0

if 10<=amount<=19:
    discount = amount*price*(10/100)
elif 20<=amount<=49:
    discount = amount*price*(20/100)
elif 50<=amount<=99:
    discount = amount*price*(30/100)
elif 100<=amount:
    discount = amount*price*(40/100)
print('The discount amount is:',discount)
total_amount = price*amount
total_amount = total_amount-discount
print('The total amount after the discount is:', total_amount)