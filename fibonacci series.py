# Program to display the Fibonacci sequence

nterms = int(input("How many terms= "))
n1, n2 = 0, 1       #Initial two terms
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:   # if there is only one term, return n1
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:               # generate fibonacci sequence
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1