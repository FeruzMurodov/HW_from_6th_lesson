first_el = int(input("Введите первый элемент: "))
diff = int(input("Введите разность: "))
count_element = int(input("Введите кол-во элементов: "))

print(result := [first_el + i * diff for i in range(count_element)])