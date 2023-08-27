
sum=0

# First way

for num in range(0,101,2):
    sum+=num
print(sum)

sum=0

# Second way
for num in range(1,101):
    if num%2==0:
        sum+=num
print(sum)