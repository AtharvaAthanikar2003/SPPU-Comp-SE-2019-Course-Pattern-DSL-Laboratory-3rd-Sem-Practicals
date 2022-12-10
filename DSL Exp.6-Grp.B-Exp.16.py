'''
Write a python program to store first year percentage of students in array. Write function
for sorting array of floating point numbers in ascending order using quick sort and display
top five scores.
'''

def accept_per():
    percent=[]
    n=int(input("Enter The Number Of Students:"))
    for i in range(n):
        print("Enter The Percentage of Student",i+1,":")
        per=float(input())
        if 0 <= per <= 100 :
            percent.append(per)
    return percent


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

  
    (array[i + 1], array[high]) = (array[high], array[i + 1])
  	
    return (i + 1)

def quick_sort(array,low,high):
    if low < high:
        pi = partition(array, low, high)
    		
        quick_sort(array, low, pi - 1)
    		
        quick_sort(array, pi + 1, high)
    return array

def top_five(list,n):
    print("Top 5 Maximum Percentages Are : ",list[n:n-6:-1])

unsorted_per = []
f = 1
while f == 1:
    print("\n---------------------MENU---------------------")
    print("1. Accept Student Perecentages")
    print("2. Sort Percentages with Quick Sort")
    print("3. Display Top Five Percentages")
    print("4. Exit\n")

#------------------------------------------------------------------------------------

    ch = int(input("Enter your choice from 1 to 4: "))
    if ch == 1:
        unsorted_per = accept_per()
    elif ch == 2:
        print("Percentages Sorted With Quick Sort : ")
        Qsorted_per = quick_sort(unsorted_per,0,len(unsorted_per)-1)
        print(Qsorted_per)
    elif ch == 3:
        top_five(Qsorted_per,len(unsorted_per))
    elif ch == 4:
        print("Thanks for using program!!")
        f=0
    else:
        print("Wrong choice!!!")
        f = 0

        
