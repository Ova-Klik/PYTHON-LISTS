import random 

numbers = [random.randint(1,50) for number in range(1,11)]
print (numbers)



def length(my_list):
    count=0;
    for number in numbers:
        count+=1;
    return count;

count = length(numbers);   
print(count);




numbers = [1,0,3,0,5,0,7,0,9,1]

sum_of_even_position_element=0;
for number in range(0,length(numbers), 2):
    sum_of_even_position_element += numbers[number]; 

print(sum_of_even_position_element)




sum_of_odd_position_element=0;
for number in range(1,length(numbers), 2):
    sum_of_odd_position_element += numbers[number]; 

print(sum_of_odd_position_element)




product_of_every_third_position_element=1;
for number in range(2,length(numbers), 3):
    product_of_every_third_position_element *= numbers[number]; 

print(product_of_every_third_position_element)



total=0;
average=0;
for number in numbers:
    total += numbers[number]; 

average = total/length(numbers);
print(average);


largest = 0;
smallest = 0;

for number in numbers:

    if number>largest: largest=number;
    if number<smallest: smallest = number;
    
print(largest);
print(smallest);



string_list = ["eve", "var", "j"];


def string_processor(my_list):
    unique_string = "";
    count = 0;
    for string in string_list:
        count+=1;
        
        if len(string) >= 2 and string[0]== string[-1]:
            unique_string+=string;
        
    return [count,unique_string];


count, unique_string = string_processor(string_list);

print(count);
print(unique_string);


integers = [number for number in range (1,16)]

print(integers);


def add_every_third_element(my_list):
    
    product = 1;
    for number in range(2,length(numbers), 3):
        product *= numbers[number]; 
        
    return product
    





