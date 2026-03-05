import matplotlib.pyplot as plt
temp = [0, 10, 20, 30, 37, 50, 60]
mg = [5, 10, 20, 40, 50, 25, 5]
plt.bar(temp, mg)
plt.xlabel('Temperature')
plt.ylabel('MG / min')
plt.title('Predicted Effect of Temperature on Amylase Activity')
plt.show()

