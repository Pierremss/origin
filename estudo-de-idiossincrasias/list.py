#the goal is to creat a list and then creat others two list based on th first one
#i will use range() 

vetor1 = list(range(1, 21)) #this will create a list with the numbers from 1 to 20
print(vetor1) 

vetor2 = [x  for x in vetor1 if x % 2 == 0] #this will create a list with the even numbers from the first list
print (vetor2)

vetor3 = [x**2 for x in vetor1] #this will creat a list with the squares of the numbers from the first list
print(vetor3)
