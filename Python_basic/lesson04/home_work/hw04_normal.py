import re, random

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# вариант 1 с RE
# выводит все символы нижнего регистра, обрамляющие символы верхнего регистра, с выдеделением пар обрамления
ptrn = re.compile('([a-z]+)[A-Z]+([a-z]+)')
print('***вариант 1 с RE***\n', ptrn.findall(line))

# вариант 2 без RE
# выводит все символы нижнего регистра подряд, обрамляющие символы верхнего регистра, без выдеделения пар
def find_substrs(string, find_substr):
    substrs = []
    enter = string
    while enter:
        result = find_substr(enter)
        if result:
            substr, idx = result
            if substr:
                substrs.append(substr)
            if idx == None:
                enter = ''
            enter = enter[idx:]
        else:
            break
    return substrs

def find_substr(string):
    start_idx, end_idx = None, None
    for idx, item in enumerate(string):
        if start_idx == None:
            if item.islower():
                start_idx = idx
        else:
            if item.isupper():
                end_idx = idx
                last_idx = idx + 1
                return string[start_idx:end_idx], last_idx
    if end_idx == None:
        return string[start_idx:], None

print('***вариант 2 без RE***\n', find_substrs(line, find_substr))


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# вариант 1 с RE
# выводит символы верхнего регистра, обрамленные двумя символами нижнего регистра с каждой стороны, 
# НЕ учитывает случаи, когда начальное обрамление уже было использовано как конечное обрамлениие в предыдущей группе  
ptrn = re.compile('[a-z]{2}([A-Z]+)[a-z]{2}')
print('***вариант 1 с RE***\n', ptrn.findall(line_2))

# вариант 2 без RE
# выводит все символы верхнего регистра, обрамленные двумя символами нижнего регистра с каждой стороны, учитывая все случаи
def find_substrs_2(string, find_substr_2):
    substrs = []
    enter = string
    while enter:
        result = find_substr_2(enter)
        if result:
#             print(result)
            substr, idx = result
            if substr and idx != None:
                substrs.append(substr)
            if idx == None:
                enter = ''
            enter = enter[idx:]
        else:
            break
    return substrs

def find_substr_2(string):
    start_idx, end_idx = None, None
    count_upper = 0
    count_lower_start = 0
    count_lower_end = 0
    for idx, item in enumerate(string):
        if item.islower():
            if count_upper == 0:
                count_lower_start += 1
            else:
                count_lower_start = 0
                count_lower_end += 1
                if count_lower_end >= 2:
                    end_idx = idx - 1
                    last_idx = idx - 1 
#                     print(idx, item, start_idx, end_idx, last_idx)
                    return string[start_idx:end_idx], last_idx
        if item.isupper():
            if count_lower_end == 1:
                count_lower_end = 0
                count_upper = 0
                start_idx = None
            if count_lower_start == 1:
                count_lower_start = 0
                count_upper = 0
                start_idx = None
            if count_lower_start >= 2:
                count_upper += 1
                if start_idx == None:
                    start_idx = idx
    if end_idx == None:
        return string[start_idx:], None

print('***вариант 2 без RE***\n', find_substrs_2(line_2, find_substr_2))

       

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

file_name = 'Numbers.txt'
with open(file_name, 'w') as f:
    f.write(str(random.randint(10**2499, 10**2500)))
    
ptrn = re.compile('[0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+')
# [0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+
with open(file_name, 'r') as f:
    for line in f:
        list_numbers = ptrn.findall(line)
len_numbers = 0
for idx, string in enumerate(list_numbers):
    if len(string) > len_numbers:
        idx_numbers = idx
        len_numbers = len(string) 
print(list_numbers[idx_numbers])
# print(list_numbers)

