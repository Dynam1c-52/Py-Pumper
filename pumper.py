import os
location = input("Enter the file path to pump: ")
pump = int(input("Enter the number of megabytes to pump file: "))

increase_bytes = pump * 1024 * 1024

with open(location, 'ab') as f:
 
    f.write(b'\0' * increase_bytes)

file_size = os.path.getsize(location)

print("Pumped file")
