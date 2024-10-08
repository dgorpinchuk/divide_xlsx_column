# Скрипт для разделения таблицы Excel на части

## Описание

Очень удобно использовать, если у вас есть, к примеру файл со списком email адресов, который необходимо разбить на несколько

## Установка

Для работы скрипта требуется библиотека pandas. Убедитесь, что она установлена:

```bash
pip install pandas openpyxl
```


## Использование

Чтобы использовать скрипт, выполните следующие шаги:

1. Укажите путь к вашему Excel-файлу и имя листа, если это необходимо.
2. Задайте желаемое количество частей, на которые вы хотите разделить данные.
3. Запустите скрипт.

### Описание кода

▎Загрузите данные из Excel
```python
file_path = 'path_to_your_file.xlsx'  # Укажите путь к вашему файлу
sheet_name = 'Sheet1'  # Укажите имя листа, если необходимо
```

▎Чтение данных из Excel
```python
df = pd.read_excel(file_path, sheet_name=sheet_name)
```

▎Предположим, что данные находятся в первом столбце (индекс 0)
```python
data = df.iloc[:, 0]
```

▎Задайте количество частей
```python
num_parts = 4  # Укажите желаемое количество частей
```

▎Разделите данные на указанное количество частей
```python
part_size = len(data) // num_parts
parts = [data[i * part_size:(i + 1) * part_size] for i in range(num_parts)]
```

▎Обработка остатка (если есть)
```python
remaining_data = data[num_parts * part_size:]
if remaining_data.size > 0:
    parts[-1] = pd.concat([parts[-1], remaining_data], ignore_index=True)
```

▎Сохраните каждую часть в отдельный файл
```python
for i, part in enumerate(parts, start=1):
    new_file_path = f'output_part_{i}.xlsx'  # Укажите нужный формат и имя файла
    part_df = pd.DataFrame(part).reset_index(drop=True)  # Создание DataFrame для каждой части
    part_df.to_excel(new_file_path, index=False)
    print(f"Часть {i} успешно сохранена в {new_file_path}")
``` 
## Как это работает

1. Скрипт загружает данные из указанного Excel-файла и листа.
2. Данные извлекаются из первого столбца.
3. Пользователь задает количество частей, на которые нужно разделить данные.
4. Данные делятся на равные части, и остаток (если есть) добавляется к последней части.
5. Каждая часть сохраняется в отдельный Excel-файл с именем output_part_X.xlsx, где X — номер части.

## Заметки:
- Не забудьте заменить path_to_your_file.xlsx и другие переменные на актуальные.
- Вы можете добавить дополнительные секции по мере необходимости.
