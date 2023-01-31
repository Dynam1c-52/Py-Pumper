import os

location = input("Enter the file path to pump: ")

pump = int(input("Enter the number of megabytes to pump file: "))

max = pump * 1024 * 1024

with open(location, 'ab') as f:
 
    f.write(b'\0' * max)

weight = os.path.getsize(location)

print("Pumped file")
