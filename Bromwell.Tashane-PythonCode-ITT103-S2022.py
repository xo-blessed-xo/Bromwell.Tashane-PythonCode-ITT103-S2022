# Author : Tashane Bromwell
# Date Created: April 24, 2022
# Course: ITT103
# Purpose: The purpose of this python program is to represent the pseudocode algorithm of the problem that was given for the assignment.

sp_class=0
while sp_class <6:                                                         # The program will loop as long as a class number 6 or greater is not entered. 
  sp_number=int(input('Enter sales person number here '))                  # Prompt user to input salesperson number as integer 
  sales_amount = int(input('Enter sales amount here '))                    # Prompt user to input sale class as integer
  sp_class  = int(input('Enter sales person class here '))                 # Prompt user to input sales amount as integer
  if sp_class == 1 and sales_amount <= 1000 :
      commission=(0.06 * sales_amount)                                     # Commission Calcualtion 
      print('The commission is $',commission)
  elif sp_class==1 and sales_amount <1000 and sales_amount <= 2000 :
      commission=(0.07 * sales_amount)
      print('The commission is $',commission)                              # Display commission 
  elif sp_class ==1 and sales_amount > 2000 :
      commission=(0.1 * sales_amount)
      print('The commission is $',commission)
  elif sp_class == 2 and sales_amount <= 1000 :
      commission=(0.04 * sales_amount)
      print('The commission is $',commission)
  elif sp_class == 2 and sales_amount > 2000 :
      commission=(0.06 * sales_amount)
      print('The commission is $',commission)
  elif sp_class == 3:
      commission=(0.045 * sales_amount)
      print('The commission is $',commission)
  else:
      print('The class input cannot be identitfied')
    
      

