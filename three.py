# Assignment : 03
# replace A by G in dna sequence of them whose age is greater than 20

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
##way1

for first_order in user_dna_sequence:
    if first_order[1] > 20:
        for second_order in first_order[2]:
            x = first_order[2].replace('A','G')
        print(x)
print('-------------------------')
    
#way2
                

array1 = []

for first_order in user_dna_sequence:
    if first_order[1] > 20:
        array1.append(first_order[2])

for first_order in array1:
    for second_order in first_order:
        x = first_order.replace('A','G')
    print(x)


            
