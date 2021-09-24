"""
    Хранилище данных. Ключ-значение.
"""
import argparse
import json
import os
import tempfile

# указываем путь к нашему файлу-хранилищу
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

# если файл не создан, создаем новый
if not os.path.isfile(storage_path):
    os.system(f"touch {storage_path}")
    print("done!")

# with open(storage_path, 'r') as file:
#     for line in file:
#         print(line)

# обработка параметров выполнения команды
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

# был передан аргумент --key
if args.key:

    # был передан аргумент --value
    if args.value:
        # создаем буффер
        buf = {}
        # открываем файл на чтение
        with open(storage_path, 'r') as file:
            # передаем данные файла в буффер
            buf = file.read()
            # проверяем находятся ли данные в буффере
            if buf != '':
                # десериализуем данные из файла в словарь
                buf = json.loads(buf)
                # если ключ присутствует в словаре переписываем
                if args.key in buf.keys():
                    buf[args.key] = args.value
                # если ключа нет обновляем словарь новой парой ключ-значение
                else:
                    buf.update({args.key: args.value})
            # если данных нет создаем словарь
            else:
                buf = {args.key: args.value}
        # записываем данные из буффера в файл
        with open(storage_path, 'w') as file:
            file.write(json.dumps(buf))
        print(f"Данные добавлены!")

    # если не передан аргумент --value
    elif args.value is None:
        # открываем файл на чтение
        with open(storage_path, 'r') as file:
            buf = file.read()
            if buf != '':
                buf = json.loads(buf)
                # если в файле есть переданный ключ выводим
                # хранимые по нему данные
                if args.key in buf.keys():
                    print(buf[args.key])
                else:
                    print(None)
            else:
                print(None)

# если параметры команды не переданы выводим все содержимое словаря
else:
    with open(storage_path, 'r') as file:
        buf = file.read()
        if buf != '':
            buf = json.loads(buf)
            for key, value in buf.items():
                print(f"{key}: {value}")
