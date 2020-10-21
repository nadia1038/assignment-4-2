# Assignment : 06

# Find the users whose DNA ends with A


user_dna_sequence = [
[
"Roksana Kozlova", 18, "GTTAGCCGACTTGGCXCTTT"
],
[
"Roza Kiseleva", 19, "ATTTGGCGAATTGGCCTTT"
],
[
"Kliment Volkov", 27, "ATTTGACCAATTGZGCAAA"
],
[
"Afanas Morozov", 22, "ATTTGACCGATTNGGCAA"
],
]

for element in (user_dna_sequence):
    if (element[2])[-1] == 'A':
        print(element[0])
print('---------------------------------')

# Assignment : 07
# Find the users whose DNA ends with T

for element in (user_dna_sequence):
    if (element[2])[-1] == 'T':
        print(element[0])
print('---------------------------------')

# Assignment : 08
# Find the users whose DNA ends with G

for element in(user_dna_sequence):
    if (element[2])[-1] == 'G':
        print(element[0])
    else:
        print("no user found")
