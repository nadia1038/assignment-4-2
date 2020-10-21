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

dna_elements = ["A", "T", "G", "C"]

# Assignment : 04
# replace T by C and G by A in dna sequence of them whose age is less than 20

##way1

for first_order in user_dna_sequence:
    if first_order[1] < 20:
        for second_order in first_order[2]:
            x = first_order[2].replace('T','C')
            y = x.replace('G','A')
        print(y)
print('----------------------------')
        

##way2

array1 = []

for first_order in user_dna_sequence:
    if first_order[1] < 20:
        array1.append(first_order[2])
print(array1)
print('----------------------------')

for first_order in array1:
    for second_order in first_order:
         x = first_order.replace('T','C')
         y = x.replace('G','A')
    print(y)

