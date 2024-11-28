import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import gmean
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
import matplotlib.cm as cm

# 1. Створення масиву та розрахунки
array = np.random.randint(1, 100, size=50)
mean = np.mean(array)
geo_mean = gmean(array)
mode = stats.mode(array).mode[0]
median = np.median(array)
print(f"Середнє арифметичне: {mean}, Середнє геометричне: {geo_mean}, Мода: {mode}, Медіана: {median}")

# 2. Створення DataFrame та фільтрація
data = {
    'Команда': ['Команда A', 'Команда B', 'Команда C', 'Команда D'],
    'Очки': np.random.randint(50, 100, 4),
    'Матчі': np.random.randint(10, 20, 4),
    'Перемоги': np.random.randint(5, 10, 4),
}
df = pd.DataFrame(data)
filtered_df = df[df['Очки'] > 70]
print("Відфільтрована таблиця:\n", filtered_df)

# 3. Створення Series з пропусками
series1 = pd.Series([np.nan, 10, 20, np.nan, 30, 40])
series2 = pd.Series([5, np.nan, 15, 25, np.nan, 35])
series1_filled = series1.fillna(series1.mean())
series2_filled = series2.fillna(series2.mean())
print("Заповнені Series:\n", series1_filled, "\n", series2_filled)

# 4. Аналіз California Housing
california = fetch_california_housing(as_frame=True)
data = california.frame

# Гістограми атрибутів
for column in data.columns:
    plt.hist(data[column], bins=30, alpha=0.7)
    plt.title(f"Гістограма {column}")
    plt.xlabel(column)
    plt.ylabel("Частота")
    plt.show()

# Додавання нових атрибутів
data['TXPRM'] = data['MedInc'] / data['AveRooms']
data['TXLSTAT'] = data['MedInc'] / data['Population']

# 3D Діаграми розсіювання
from mpl_toolkits.mplot3d import Axes3D

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')
ax1.scatter(data['TXPRM'], data['MedHouseVal'], data['AveRooms'], c=data['MedInc'], cmap=cm.viridis)
ax1.set_title('Розсіювання TXPRM та MedHouseVal')
ax1.set_xlabel('TXPRM')
ax1.set_ylabel('MedHouseVal')
ax1.set_zlabel('AveRooms')

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.scatter(data['TXLSTAT'], data['MedHouseVal'], data['Population'], c=data['AveOccup'], cmap=cm.plasma)
ax2.set_title('Розсіювання TXLSTAT та MedHouseVal')
ax2.set_xlabel('TXLSTAT')
ax2.set_ylabel('MedHouseVal')
ax2.set_zlabel('Population')

plt.show()


