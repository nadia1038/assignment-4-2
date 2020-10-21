# Assignment : 01
# filter dna: remove invalid elements from all the DNA


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

#way1 : using one nested loop

for first_order in user_dna_sequence:
    for second_order in first_order[2]:
        if second_order not in dna_elements:
            x =first_order[2].replace(second_order,'')
            print(x)
print('------------------------------------------------------------')

#way2 : using two nested loops

array1 = []
array2 = []


for first_order in user_dna_sequence:
    for second_order in first_order[2]:
        if second_order not in dna_elements:
            array1.append(first_order[2])
            array2.append(second_order)
            
for element1 in array1:
    for element2 in element1:
        if element2  in array2:
            x = element1.replace(element2,'')
            print(x)



