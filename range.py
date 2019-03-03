import random
range(5) #[0, 1, 2, 3, 4]
range(3) #[0, 1, 2]
for i in range(3):
	r = random.randint(1,1000)
	print(r) #generate random number from 1-1000 range for three times

range(2, 5) # [2, 3, 4]
range(2, 10, 3) # begin with 3, step is 3, the end is near 10, [2, 5, 8]