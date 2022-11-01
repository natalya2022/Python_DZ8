base_struct = ['ФИО', 'Телефон', 'Должность', 'Оклад']

def append_record(main_base):  # добавление записи в список
    n=[]
    for key, item in enumerate(base_struct):
        n.append(input(f'Введите {item} => '))
    main_base.append(' || '.join(n))
    print('Запись внесена. Можно продолжить работу\n')


def find_record(main_base, x):  # поиск записей в списке
    a = []
    for item in main_base:
        if item.find(x) != -1:
            a.append(item)
    return a


def base_redaction(main_base, x):
    a = []
    for key1,item in enumerate(main_base):
        if item.find(x) != -1:
            a=item.split(' || ')
            break
    if not (len(a)):
        print('Запись не найдена. Можно продолжить работу\n')
        return -1
    print('Запись найдена. Режим редактирования.\nКлавишей Enter перейдите на нужное поле.\nИзмените и вновь нажмите Enter\n')
    for key, item in enumerate(base_struct):
        print(item,':', a[key], end = ' => ')
        b = input()
        if b:
            a[key] = b
    main_base[key1]=' || '.join(a)
    return key1

