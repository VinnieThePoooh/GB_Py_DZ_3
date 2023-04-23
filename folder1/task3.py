# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; 
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; 
# K – 5 очков;  
# J,X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость 
# введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

list_1_ochko = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
list_2_ochka = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
list_3_ochka = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
list_4_ochka = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
list_5_ochkov = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
list_8_ochkov = ['J', 'X', 'Ш', 'Э', 'Ю']
list_10_ochkov = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

list_slovo = input('Введите слово капсом через пробел: ').split()
count_ochkov = 0
for i in range(0, len(list_slovo)):
    if list_slovo[i] in list_1_ochko:
        count_ochkov += 1
    elif list_slovo[i] in list_2_ochka:
        count_ochkov += 2
    elif list_slovo[i] in list_3_ochka:
        count_ochkov += 3
    elif list_slovo[i] in list_4_ochka:
        count_ochkov += 4
    elif list_slovo[i] in list_5_ochkov:
        count_ochkov += 5
    elif list_slovo[i] in list_8_ochkov:
        count_ochkov += 8
    elif list_slovo[i] in list_10_ochkov:
        count_ochkov += 10
        
print(list_slovo)
print('Количетсво очков: ', count_ochkov)