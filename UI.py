import Model
import Logger


basefile = 'Base.txt'
main_base = Logger.import_base(basefile)
Logger.log_line(f'Запуск программы. Импортировано {len(main_base)} записей')


def base_append():
    Model.append_record(main_base)
    Logger.log_line(f'Добавлена запись: {main_base[-1]}')


def base_search():
    search = Model.find_record(main_base, input(
        'Введите значение для поиска => '))
    if len(search):
        print("\n".join(search))
        print('Поиск завершен.\n')
    else:
        print('Запись не найдена.\n')
    Logger.log_line(f'Поиск. Найдено: {len(search)} записей')


def base_exit():
    Logger.export_base(main_base, basefile)
    Logger.log_line(f'Выход. Экспортировано {len(main_base)} записей\n')
    print('Выход')
    exit()


def base_edit():
    c = Model.base_redaction(main_base, input('Введите критерий редактирования => '))
    if c > -1:
        Logger.log_line(f'Редактирование. Изменена запись {c}\n')
    print('Редактирование завершено.\n')


list_of_functions = [
    [base_exit, 'Выход'],
    [base_append, 'Добавление записи'],
    [base_search, 'Поиск записи'],
    [base_edit, 'Редактирование']
]
for num, item in enumerate(list_of_functions):
    print(num, item[1])

while True:
    a = int(input('Выберите вариант => \n'))
    if 0 <= a < len(list_of_functions):
        list_of_functions[a][0]()
