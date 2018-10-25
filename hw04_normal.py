import re, random

# �������-1:
# ������� ������� � ������ ��������, ������� ��������� ������
# 1 ��� ����� �������� � ������� ��������.
# �.�. �� ������ "mtMmEZUOmcq" ����� �������� ['mt', 'm', 'mcq']
# ������ ������ ����� ���������: � ������� re � ���.

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

# ������� 1 � RE
# ������� ��� ������� ������� ��������, ����������� ������� �������� ��������, � ������������ ��� ����������
ptrn = re.compile('([a-z]+)[A-Z]+([a-z]+)')
print('***������� 1 � RE***\n', ptrn.findall(line))

# ������� 2 ��� RE
# ������� ��� ������� ������� �������� ������, ����������� ������� �������� ��������, ��� ����������� ���
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

print('***������� 2 ��� RE***\n', find_substrs(line, find_substr))


# �������-2:
# ������� ������� � ������� ��������, ����� �� ������� ���������
# ��� ������� � ������ ��������, � ������ - ��� ������� � ������� ��������.
# �.�. �� ������ 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# ����� �������� ������ �����: ['AY', 'NOGI', 'P']
# ������ ������ ����� ���������: � ������� re � ���.

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

# ������� 1 � RE
# ������� ������� �������� ��������, ����������� ����� ��������� ������� �������� � ������ �������, 
# �� ��������� ������, ����� ��������� ���������� ��� ���� ������������ ��� �������� ����������� � ���������� ������  
ptrn = re.compile('[a-z]{2}([A-Z]+)[a-z]{2}')
print('***������� 1 � RE***\n', ptrn.findall(line_2))

# ������� 2 ��� RE
# ������� ��� ������� �������� ��������, ����������� ����� ��������� ������� �������� � ������ �������, �������� ��� ������
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

print('***������� 2 ��� RE***\n', find_substrs_2(line_2, find_substr_2))

       

# �������-3:
# �������� ������, ����������� ��������� ���� (�������������� ������� ��� �����)
# ������������� ������ �������, � ���������� � ����� ������ ����
# 2500-������� ������������ �����.
# ������� � �������� ����� ������� ������������������ ���������� ����
# � ��������������� �����.

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

