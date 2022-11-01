def import_base(filename): # импорт информации из файла txt
    x = open(filename,'r',encoding='utf-8')
    return list(map(lambda x: x.rstrip('\n'), x.readlines()))

def log_line(str):
    with open('log.txt','a',encoding='utf-8') as f:
        f.write(f'{str} \n')

def export_base(main_base, filename):
    with open(filename,'w',encoding='utf-8') as f:
       for item in main_base:
        f.write(item+'\n')