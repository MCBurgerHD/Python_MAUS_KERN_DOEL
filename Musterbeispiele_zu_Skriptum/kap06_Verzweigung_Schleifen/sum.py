# Python code to demonstrate the working of  
# sum() 
   
numbers = [1,2,3,4,5,1,4,5] 
  
# start parameter is not provided start = 0
Sum = sum(numbers) 
print(Sum) 
  
# start = 10 
Sum = sum(numbers, 10) 
print(Sum) 

numbers = [x for x in range(1, 1001)]
print(numbers[0], numbers[999])
Sum = sum(numbers)
print(Sum)
