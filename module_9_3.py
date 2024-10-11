first = ['Strings', 'Student', 'Cumputers']
second = ['Строка', "Урбан", "Компьютер"]

first_result = (len(i) - len(j) for i, j in zip(first, second) if i != j)
print(list(first_result))

second_result = (len(first[i]) >= len(second[i]) for i in range(min(len(first), len(second))))
print(list(second_result))