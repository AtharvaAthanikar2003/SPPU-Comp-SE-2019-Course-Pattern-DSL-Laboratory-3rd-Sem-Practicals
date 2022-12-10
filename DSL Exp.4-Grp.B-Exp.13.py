'''
Write a python program to maintain club members, sort on roll numbers in ascending
order. Write function “Ternary_Search” to search whether particular student is member
of club or not. Ternary search is modified binary search that divides array into 3 halves
instead of two.
'''

#task1
def accept_roll():        #accepting roll no
 roll_no = []
 print("Enter the number of students present in",b,"club: ")
 n= int(input())
 for i in range(n):
     roll_no.append(int(input("Enter Roll Number of Student: ")))
     i=i+1
 return roll_no
#-------------------------------------------------------------------------------------
#task2
def sort(roll_no):                  #sorting    
 for i in range(1,len(roll_no)):
     key = roll_no[i]
     k = i-1
     while k >= 0 and key < roll_no[k]:
         roll_no[k+1] = roll_no[k]
         k -= 1
         roll_no[k+1] = key
 return roll_no
#-------------------------------------------------------------------------------------
#task3
def NR_Ternary_Search(roll,roll_find):        #non recursive ternary search
 l = 0
 r = len(roll) - 1
 while l <= r:
     mid1 = l + (r - l) // 3        #mid1
     mid2 = l + 2 * (r - l) // 3     #mid2
     if roll_find == roll[l]:
         return l
     elif roll_find == roll[r]:
         return r
     elif roll_find < roll[l] or roll_find > roll[r]:
         return -1
     elif roll_find <= roll[mid1]:
         right = mid1
     elif roll_find > roll[mid1] and roll_find <= roll[mid2]:
         l= mid1 + 1
         r = mid2
     else:
         l = mid2 + 1
 return -1
#------------------------------------------------------------------------------------
unsorted_Roll = []
sorted_Roll = []
b=input("Enter club name: ")
print("------------------",b,"------------------")
f = 1
while f == 1:
 print("\n---------------------MENU---------------------")
 print("1. Accept Student Roll Numbers")
 print("2. Display the Roll Numbers of Student")
 print("3. Sort Roll Numbers from the list")
 print("4. Perform Non-Recursive Ternary Search")
 print("5. Exit\n")
#------------------------------------------------------------------------------------
 ch = int(input("Enter your choice from 1 to 5: "))
 if ch == 1:
    unsorted_Roll = accept_roll()
 elif ch == 2:
     print(unsorted_Roll)
 elif ch == 3:
     print("Roll numbers in asending order : \n")
     sorted_Roll = sort(unsorted_Roll)
     print(sorted_Roll)
 elif ch == 4:
     find_roll = int(input("Enter the Roll Number to be searched in club : "))
     i = NR_Ternary_Search(sorted_Roll,find_roll)
     if i != -1:
         print("The Roll Number",find_roll,"is found in club ")
     else:
         print("The Roll Number",find_roll,"is not found in club!!!")
 elif ch == 5:
     print("Thanks for using program!!")
     f=0
 else:
     print("Wrong choice!!!")
     f = 0

