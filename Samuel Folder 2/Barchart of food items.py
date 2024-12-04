import matplotlib.pyplot as plt

Food_items = ['Mushroom', 'Pineapple', 'Prawns', 'Sausage', 'Spinach']
values = [0.176, 0.3, 0.086, 0.186, 0.3]

plt.barh(Food_items, values, color='brown')

plt.title('Barchart of food items')
plt.xlabel('Proportion of Total')

plt.show()














