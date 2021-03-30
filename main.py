even_numbers = 0
odd_numbers = 0
to_input = int(input("how many numbers to input? "))

for i in range(to_input):
  number = str(input("enter a number: "))
  if int(number) % 2 == 0:
    print(number + " is an even number")
    even_numbers += 1
  if int(number) % 2 == 1:
    print(number + " is an odd number")
    odd_numbers += 1
print("done, you entered" )
print(str(even_numbers) + " even numbers")
print(str(odd_numbers) + " odd numbers")
