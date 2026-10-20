import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# 1. Загрузка данных (замени 'data.csv' на свой файл)
# df = pd.read_csv('data.csv')

# Для примера создадим синтетические данные (например, для зависимости цены от комнат)
np.random.seed(42)
X = np.random.randint(1, 6, size=(100, 1))  # Количество комнат (от 1 до 5)
y = 30 + 15 * X.flatten() + np.random.normal(0, 5, 100) # Цена жилья

# 2. Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Прогнозирование на тестовых данных
y_pred = model.predict(X_test)

# 5. Оценка качества модели
print(f"Коэффициент детерминации (R2): {r2_score(y_test, y_pred):.4f}")
print(f"Среднеквадратичная ошибка (MSE): {mean_squared_error(y_test, y_pred):.4f}")
print(f"Средняя абсолютная ошибка (MAE): {mean_absolute_error(y_test, y_pred):.4f}")
print(f"Коэффициент (наклон): {model.coef_[0]}")
print(f"Свободный член (интерсепт): {model.intercept_}")

# 6. Визуализация результатов
plt.scatter(X_test, y_test, color='blue', label='Реальные данные')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Линия регрессии')
plt.xlabel('Независимый признак')
plt.ylabel('Целевая переменная')
plt.legend()
plt.show()