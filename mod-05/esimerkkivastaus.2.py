numbers = []

new_number = input("Anna luku tai paina Enter ohjelman lopettamiseksi: ")

if new_number =="":
    print("Et antanut yhtään lukua vaan lopetit ohjelman saman tien.")
else:
    while new_number != "":
        numbers.append(int(new_number))
        new_number = input("Anna luku tai paina Eneter ohjelman lopettamiseksi: ")
    numbers.sort(reverse=True)
    print(numbers[0:6])


