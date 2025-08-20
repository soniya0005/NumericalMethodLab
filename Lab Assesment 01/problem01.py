num = int(input("Enter nth number to sum : "))

sum = 0
for i in range(num+1):
    sum +=i

print(f"Sum of first {num} number : {sum}")