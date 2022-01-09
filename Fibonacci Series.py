n_terms = int(input ("How many terms you want to print\n "))  
  
# First two terms  
a = 0  
b = 1  
count = 0  
  
# Now, we will check if the number of terms is valid or not  
if n_terms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")  
# if there is only one term, it will return a 
elif n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
    print(a)  
# Then we will generate Fibonacci sequence of number  
else:  
    print ("The fibonacci sequence of the numbers is:")  
while count < n_terms:  
    print(a)  
    nth = a + b  
    # At last, we will update values  
    a = b  
    b = nth  
    count += 1  