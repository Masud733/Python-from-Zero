import random
#randint() module for print random integer and uniform() module for float
random_integer = random.randint(1,10)
print(random_integer)
random_float = random.uniform(3.5,4.0)
print(random_float)
# Generating random numbers from a normal distribution using normalvariate() module
random_normal = random.normalvariate(1,5)
print(random_normal)

my_list = [10,20,30,40,50,60,70]
#choicede any random element
random_element = random.choice(my_list)
print("choice element randomly:",random_element)
#Takes a sequence and returns the sequence in a random order
my_list = [10,20,30,40,50]
random_shuffle = random.shuffle(my_list)
print("Print shuffle list:",random_shuffle)
#print any 3 ramdom sample element
random_sample = random.sample(my_list,3)
print("Print three random sample:",random_sample)
#Initialize the random number generator
seed_value = 42
random.seed(seed_value)
print(seed_value)



