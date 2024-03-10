dict_files = {}
with open('1.txt', encoding='utf-8') as file:
    file_1 = file.read().split('\n')
    dict_files['1.txt'] = file_1

with open('2.txt', encoding='utf-8') as file:
    file_2 = file.read().split('\n')
    dict_files['2.txt'] = file_2

with open('3.txt', encoding='utf-8') as file:
    file_3 = file.read().split('\n')
    dict_files['3.txt'] = file_3

sorted_files = sorted(dict_files.items(), key=lambda x: x[1], reverse=True)
ind = {k:i+1 for i,k in enumerate(dict(sorted_files).keys())}

with open('sorted_files.txt', 'w', encoding='utf-8') as file:
    for key, value in dict(sorted_files).items():
        file.write(key+'\n')
        file.write(str(ind[key])+'\n')
        file.write('\n'.join(value)+'\n')