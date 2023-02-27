import io
import random
import random as rnd

path = "C:/train.txt"

count_normal = 0
count_bad = 0
arr1 = []
arr2 = []
sort = io.open("C:/train_sorted.txt", "w", encoding='utf-8')
final = io.open("C:/train_final.txt", "w", encoding='utf-8')
with io.open(path, encoding='utf-8') as file:
    for line in file:
        normal_line = line.replace(",", "")
        arr2 = normal_line.split()
        arr2.pop(0)
        if arr2[0] == "__label__OBSCENITY" or arr2[1] == "__label__OBSCENITY":
            continue
        if arr2[0] == "__label__NORMAL":
            arr2.pop(0)
            arr2[-1] = arr2[-1] + '",'
            arr2.append("0.0")
            count_normal += 1
        elif arr2[0] == "__label__THREAT" or arr2[0] == "__label__INSULT":
            arr2.pop(0)
            arr2[-1] = arr2[-1] + '",'
            arr2.append("1.0")
            count_bad += 1
        if arr2[0] == "__label__THREAT" or arr2[0] == "__label__INSULT":
            arr2.pop(0)
        cont = arr2[0]
        cont = '"' + cont
        arr2[0] = cont
        arr2.append("\n")
        newline = " ".join(arr2)
        sort.write(newline)
        """arr1.append(newline)"""

print(arr1)
print(arr2)

arr1.clear()
arr2.clear()
count_max = 0

with io.open("C:/train_sorted.txt", "r", encoding='utf-8') as file:
    for line in file:
        newline = line.split()
        if newline[-1] == "0.0" and count_max < 60000:
            samp_line = (" ".join(newline[0: -1]))
            samp_line += "0.0"
            arr1.append(samp_line)
            count_max += 1
        elif newline[-1] == "1.0":
            samp_line = (" ".join(newline[0: -1]))
            samp_line += "1.0"
            arr2.append(samp_line)

print(len(arr1))
print(len(arr2))
newarray = arr1 + arr2
random.shuffle(newarray)
print(len(newarray))
for element in newarray:
    final.write(element + "\n")

print(len(arr1))
print(len(arr2))
print(len(newarray))

