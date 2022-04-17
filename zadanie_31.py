import random

print ("Podaj liczbe uczniow: ")
x = int(input())

correct = []
dict ={}

def read_file():
    with open("stolice.txt", "r") as f1:
        for line in f1:
            partitioned_line = line.partition(',')          # dziele linie na krotki, jako separator uzywam przecinka
            first_word_in_line = partitioned_line[0]        # przypisuje krotke z indeksem 0 do first_word_in_line
            second_word_in_line = partitioned_line[2]       # przypisuje krotke z indeksem 2 do second_word_in_line
            second_word_in_line = second_word_in_line[1:-1]     # usuwam spacje z poczatku i znak nowej lini z konca wyrazu
            el ={first_word_in_line:second_word_in_line}        #tworze element klucz:wartosc
            dict.update(el)                                     #dodaje el do slownika dict
def create_files(x):
    for i in range(x):
    # po przejsciu jednego pliku liste z praw.odpowiedziami dodaje do listy correct
      correct_file = []
      correct.append(correct_file)
      with open(f"test_{i+1}.txt", "w") as f2:
          rand_dict = random.sample(list(dict), len(dict))          #tworze rand_dict wypelniajac losowo panstwami z dict
          values = [dict[k] for k in rand_dict]                     # pod values zapisuje wartosci (stolice) z rand_dict
          for x in range(0, len(dict)):
            print(f"{x+1}. Jaka stolice ma panstwo: {rand_dict[0]}", file=f2)
            a = values[0]                           # pod a przypisuje stolice wybranego panstwa
            rand_dict = rand_dict[1:]
            values.remove(a)                     # usuwam z values wartosc a(zeby nie byla brana do losowych odpowiedzi)
            answers = random.sample(values, 3)     # tworze liste answers z 3 randomowymi odpowiedziami
            answers.append(a)                       # dodaje do answers poprawna odpowiedz

            random_answers = random.sample(answers, 4)
            # sprawdzam ktora odpowiedz jest prawidlowa i umieszczam ja w liscie correct_file
            if random_answers[0] == a:
                    correct_file.append('A')
            elif random_answers[1] == a:
                    correct_file.append('B')
            elif random_answers[2] == a:
                    correct_file.append('C')
            else:
                    correct_file.append('D')
            print(f"A. {random_answers[0]}", file=f2)
            print(f"B. {random_answers[1]}", file=f2)
            print(f"C. {random_answers[2]}", file=f2)
            print(f"D. {random_answers[3]}", file=f2)
            values.append(a)
def create_correct(correct, x):
    for i in range(x):
        with open(f"correct_test_{i+1}.txt", "w") as f3:
            for j in range(0, len(dict)):
                print(f"{j+1}.{correct[i][j]}", file = f3)  #przechodze po liscie zlozonej correct i wypisuje elementy do pliku




read_file()
create_files(x)
create_correct(correct,x)
