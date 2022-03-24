country_list =[]

country_list.append("america")
country_list.append("japan")
country_list.append("russia")

print(country_list)

choice=0

def check_valid(element):
    if element in country_list:
        return True
    else:
        return False

while choice < 5: 
    print("Linked List Operations:")
    print("""
    1. Add element 
    2. Remove element
    3. Replace element 
    4. Search for element 
    5. Exit 
    """)
    choice=int(input("Your choice: "))
    if choice == 1:
        pos = int(input("Enter the element pos: "))
        element = input("Enter the element value: ")
        country_list.insert(pos,element)
        print("Element added successfully")
        
    elif choice == 2:
        print("Existing list: ", country_list)
        while True:  
            rem_element = input("Enter a valid element to be removed: ")
            status = check_valid(rem_element)
            if status == True:
                country_list.remove(rem_element)
                print("Entered element is valid and removed from the list")
                break
            else:
                print("Entered Element is not found. Please enter the valid input")
                continue
    elif choice == 3:
        print("Existing list: ", country_list)
        while True:
            rep_element = input("Enter the element to be replaced: ")
            status = check_valid(rep_element)
            if status == True:
                new_element = input("Enter the element to be added: ")
                idx = country_list.index(rep_element)
                country_list.remove(rep_element)
                country_list.insert(idx,new_element)
                print("New element is added to the list")
                break
            else:
                print("Entered input is invalid. Please retry")
                continue

    elif choice == 4 :
        while True:
            ser_element = input("Enter the element to be searched: ")
            status = check_valid(ser_element)
            if status == True:
                idx = country_list.index(ser_element)
                print(f"The element is found in position-{idx}")
                break
            else:
                print("Entered value is not present")
    else:
        break

print(f"Final list after the changes: {country_list}")      


    
'''
3 add  [america, japan, india ]
Linked List operations 
1 Add element 
2 Remove element
3 Replace element 
4 Search for element 
5 Exit 
Your choice : 1
Enter element : Russia 
At what posistion : 1 
List = [amer ..., russia] 
Linked List operations 
1 Add element 
2 Remove element
3 Replace element 
4 Search for element 
5 Exit 
your choice : 2
'''