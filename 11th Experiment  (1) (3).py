#Define overlap contains two variables list 1 and list 2.
def overlap(list1, list2):
    return set(list1).intersection(list2)

i=0
list1=[]
list2 = []
#assigning value to the variable to the list 1 
for i in range(3):
        inp1 = float(input("Enter number: "))
        list1.append(inp1)
#output of list 1
print("List 1 is: ", list1)
#assigning value to the variable to the list 2 
i=0                             
for i in range(3):
        inp2 = float(input("Enter number: "))
        list2.append(inp2)
print("List 2 is: \n",list2)
#calling define function
print(overlap(list1, list2))
#priting overlap 
print("Overlap is: ", overlap(list1, list2))
#using two random variables set 1 and set 2 to keep the values of list 1 and list 2.
set_1 = set(list1)
set_2 = set(list2)
#joining the lists 1 and 2
list2_items_not_in_list1 = list(set_2 - set_1)
#This will help us get the joined value of two lists 1 and 2.
combined_list = list1 + list2_items_not_in_list1
#priting the output for the joined value
print("Join is: ", combined_list)
