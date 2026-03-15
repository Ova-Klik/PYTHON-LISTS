import random 

numbers=[]

for index in range(10):
    numbers.append(random.randint(1,50))
    
print (f"A random list: {numbers}")
  

numbers=[]
for index in range(10):
    numbers+=[random.randint(1,50)]
    
print (f"Another random list: {numbers}")


numbers=[random.randint(1,50) for index in range(10)]
print (f"And another random list: {numbers}")


#-------------------------------------------------------------------------------

def get_length_of_list(the_list):
    count=0
    for element in the_list:
        count+=1
    return count

#-------------------------------------------------------------------------------    
    
def get_sum_of_element_in_list(the_list):
    sum_of_element=0
    for element in the_list:
        sum_of_element+=element
    return sum_of_element

sum_of_element=get_sum_of_element_in_list(numbers)
print (sum_of_element)

#-------------------------------------------------------------------------------

def get_sum_of_element_even_positions(the_list):
    
    sum_of_element_even_positions=0
    length=get_length_of_list(the_list)
    
    for index in range(1,length,2):
       
        sum_of_element_even_positions+=the_list[index]
    
    return sum_of_element_even_positions
    
numbers=[1,2,3,4,5,6,7,8,9,0]

sum_of_element_even_positions=get_sum_of_element_even_positions(numbers)

print (f"The sum of elements at even position: {sum_of_element_even_positions}")

#-------------------------------------------------------------------------------

def get_sum_of_element_odd_positions(the_list):
    
    sum_of_element_odd_positions=0
    length=get_length_of_list(the_list)
    
    for index in range(0,length,2):
           
            sum_of_element_odd_positions+=the_list[index]
           
    
    return sum_of_element_odd_positions
    
numbers=[1,2,3,4,5,6,7,8,9,10]

sum_of_element_odd_positions=get_sum_of_element_odd_positions(numbers)

print (f"The sum of elements at odd position: {sum_of_element_odd_positions}")



#-------------------------------------------------------------------------------



def get_product_of_element_at_third_positions(the_list):
    
    product_of_third_positions=1
    length=get_length_of_list(the_list)
    
    for index in range(0,length,3):
           
        product_of_third_positions*=the_list[index]
    
    return product_of_third_positions
    
numbers=[1,2,3,4,5,6,7,8,9,6]

product_of_element_at_third_positions=get_product_of_element_at_third_positions(numbers)

print (f"The product of third positions : {product_of_element_at_third_positions}")

    
    
#-------------------------------------------------------------------------------


def get_average_of_all_elements(the_list):
    
    length = get_length_of_list(the_list)
    sum_of_elements = get_sum_of_element_in_list(the_list)
    average_of_all_elements = sum_of_elements/length
    
    return average_of_all_elements
    
numbers=[1,2,3,4,5,6,7,8,9,6]

average_of_all_elements=get_average_of_all_elements(numbers)

print (f"The average of all elements : {average_of_all_elements}")


 #-------------------------------------------------------------------------------   


def get_largest_of_all_elements(the_list):
    
    largest=the_list[0]
    
    for number in the_list:
    
        if number > largest: largest =number

    return largest
    
numbers=[1,2,3,4,5,6,7,8,9,6]

largest_of_all_elements=get_largest_of_all_elements(numbers)

print (f"The largest of all elements : {largest_of_all_elements}")

#-------------------------------------------------------------------------------


def get_smallest_of_all_elements(the_list):
    
    smallest=the_list[0]
    
    for number in the_list:
    
        if number < smallest: smallest =number
    
    return smallest
    
numbers=[1,2,3,4,5,6,7,8,9,6]

smallest_of_all_elements=get_smallest_of_all_elements(numbers)

print (f"The smallest of all elements : {smallest_of_all_elements}")

#-------------------------------------------------------------------------------

def count_number_of_strings_in_a_list_of_strings(the_list):
    
    count=0

    for string in the_list:
        count+=1
        length_of_string=get_length_of_list(string)
        if string[0]==string[-1] and length_of_string>2: 
        
            return (string,count)
            
    
strings=["me","a","wolf","what","london", "alpha"]
string,count=count_number_of_strings_in_a_list_of_strings(strings)

print (f"The length of the list: {count}")
print(f"The string with length above 2 and that has it's first letter equal to the last: '{string}'") 


#-------------------------------------------------------------------------------

def display_sequential_list_of_integers(the_list):
    
    
    for integer in the_list:
    
        print(integer, end=" ")
    print()
            
    
integers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
display_sequential_list_of_integers(integers)



#-------------------------------------------------------------------------------


def add_every_third_element(the_list):
    
    length=get_length_of_list(the_list)
    sum_of_third_element=0
    
    for index in range (2,len(the_list),3):
   
       sum_of_third_element+=the_list[index]
       
    return sum_of_third_element
            
    
sum_of_third_element=add_every_third_element(integers)
print(f"The sum of every third element: {sum_of_third_element}") 

#-------------------------------------------------------------------------------


def add_first_middle_and_last_element(the_list):
    
    length=get_length_of_list(the_list)
    
    first_element = the_list[0]
    
    if length%2==0: 
        middle_position1 = length//2-1
        middle_position2 = length//2
        middle_position = the_list[middle_position1] + the_list[middle_position2]
        
    else: middle_position = the_list[length//2]
    
    last_element = the_list[-1]
               
    return first_element + middle_position + last_element
            
    
sum_first_middle_last_element=add_first_middle_and_last_element(integers)
print(f"The sum_first_middle_last_element: {sum_first_middle_last_element}")
