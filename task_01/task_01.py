import pulp

# Ініціалізація проблеми лінійного програмування
model = pulp.LpProblem("Optimization_of_Production", pulp.LpMaximize)

# Змінні для кількості "Лимонаду" (x1) та "Фруктового соку" (x2)
x1 = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
x2 = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Цільова функція: максимізуємо загальну кількість продуктів
model += x1 + x2, "Total_Products"

# Обмеження на ресурси
model += 2*x1 + x2 <= 100, "Water_Constraint"
model += x1 <= 50, "Sugar_Constraint"
model += x1 <= 30, "Lemon_Juice_Constraint"
model += 2 * x2 <= 40, "Fruit_Puree_Constraint"

# Виконуємо оптимізацію
model.solve()

# Виведемо результати оптимізації
limjnade_count = pulp.value(x1)
fruit_juice_count = pulp.value(x2)
total_products = pulp.value(model.objective)

print(f"Кількість виробленого лимонаду: {limjnade_count}")
print(f"Кількість виробленого фруктового соку: {fruit_juice_count}")
print(f"Загальна кількість вироблених продуктів: {total_products}")