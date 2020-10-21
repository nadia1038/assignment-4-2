# Assignment : 05

# reverse those user's DNA whose age is greater than 18 and less than 25

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

for element in user_dna_sequence:
    if element[1]>18 and element[1]<25:
        print((element[2])[::-1])
