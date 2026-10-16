#1

films = ["film1","film2","film3"]
print(f"Первый фильм: {films[0]}")
print(f"Последний фильм: {films[-1]}")
films[1] = "filmnew"
films.append("filmappended")
print(f"Обновленный список: {films}")

#2

itemList = ["Хлеб","Молоко","Яйца"]
print(f"Ваши покупки: {itemList}")
itemList.append(input("Что хотите добавить? "))
print("Продукт добавлен!")
print(f"Список: {itemList}")
itemList.pop()
print("Последний продукт удалён!")
print(f"Итог: {itemList}")

#3

grades = [5,3,4]
print(f"Первая оценка: {grades[0]}")
grades[1] = 5
print(f"Третья оценка: {grades[2]}")
if grades[2] == 5:
  print("Отлично!")
else:
  print("Нужно подтянуть оценку!")
print(f"Все оценки: {grades}")

#4

student = ("Али",17,"Python")
print(f"Имя: {student[0]}")
print(f"Возраст: {student[1]}")
print(f"Курс: {student[2]}")
if student[1]  >= 18:
  print("Совершеннолетний")
else:
  print("Несовершеннолетний")

balances = [1000,2000,500]

#5

print(f"Ваш баланс: {balances[0]}")
balances[0] += int(input("Введите сумму пополнения: "))
print("Пополнение успешно!")
print(f"Новый баланс: {balances[0]} сом")
print(f"Все балансы: {balances}")
