my_numbers = []
numbers_full = []


def get_numbers(my_numbers):
    print("Wpisz 6 liczb: ")
    for i in range(6):
        my_numbers.append(int(input()))


#funkcja zwracajaca liczbe linii w pliku
def count_lines():
    lines = 0
    with open("dl.txt", "r") as f0:
        for line in f0:
            lines += 1
        return lines

lines = count_lines()
def open_file():
    with open("dl.txt", "r") as f1:
        for line in f1:
            partitioned_line = line.split(' ')      # dziele linie na czesci
            dwa = partitioned_line[2]               # wybieram czesc z numerami
            dwa = dwa[:-1]                          # usuwam znak nowej linii
            numbers=dwa.split(',')                  # oddzielam kazdy numer od siebie
            for i in range(6):                      # rzutuje numery ze string na int
                numbers[i] = int(numbers[i])
            numbers_full.append(numbers)            #dodaje liste numbers, do listy numbers_full


def count_func(my_numbers, numbers_full, lines):
    total_3 = 0
    total_4 = 0
    total_5 = 0
    total_6 = 0
    A = set(my_numbers)
    for i in range(lines):
        B = set(numbers_full[i])
        C = A.intersection(B)
        if len(C) == 3:
            total_3 += 1
        elif len(C) == 4:
            total_4 += 1
        elif len(C) == 5:
            total_5 += 1
        elif len(C) == 6:
            total_6 +=1

    print("Ilosc udanych trafien: ")
    print("trzy:",total_3)
    print("cztery:",total_4)
    print("piec:",total_5)
    print("szesc:",total_6)


get_numbers(my_numbers)
open_file()
count_func(my_numbers, numbers_full, lines)