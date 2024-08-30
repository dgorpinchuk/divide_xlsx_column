import pandas as pd

# Загрузите данные из Excel
file_path = '/Users/dgorpinchuk/Downloads/База_рассылки.xlsx'  # Укажите путь к вашему файлу
sheet_name = 'Данные'  # Укажите имя листа, если необходимо

# Чтение данных из Excel
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Предположим, что данные находятся в первом столбце (индекс 0)
data = df.iloc[:, 0]

# Задайте количество частей
num_parts = 3  # Укажите желаемое количество частей

# Разделите данные на указанное количество частей
part_size = len(data) // num_parts
parts = [data[i * part_size:(i + 1) * part_size] for i in range(num_parts)]

# Обработка остатка (если есть)
remaining_data = data[num_parts * part_size:]
if remaining_data.size > 0:
    parts[-1] = pd.concat([parts[-1], remaining_data], ignore_index=True)

# Сохраните каждую часть в отдельный файл
for i, part in enumerate(parts, start=1):
    new_file_path = f'Часть_{i}.xlsx'  # Укажите нужный формат и имя файла
    part_df = pd.DataFrame(part).reset_index(drop=True)  # Создание DataFrame для каждой части
    part_df.to_excel(new_file_path, index=False)
    print(f"Часть {i} успешно сохранена в {new_file_path}")
