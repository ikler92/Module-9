def all_variants(text):
    length = len(text)
    # Внешний цикл по длинам подпоследовательностей
    for size in range(1, length + 1):
        # Внутренний цикл по позициям, где начать подпоследовательность
        for start in range(length - size + 1):
            yield text[start:start + size]  # Генерируем подпоследовательность

# Пример вызова функции
a = all_variants("abc")
for i in a:
    print(i)



