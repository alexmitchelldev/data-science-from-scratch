from matplotlib import pyplot as plt

playstation = [40, 23, 17]
xbox = [35, 30, 11]
switch = [25, 30, 33]

sales = [i for i, _ in enumerate(playstation)]

plt.plot(sales, playstation, 'b-', label='Playstation')
plt.plot(sales, xbox, 'g-', label='Xbox')
plt.plot(sales, switch, 'r-', label='Switch')

plt.legend(loc=9)
plt.xlabel('Year')
plt.ylabel('Sales in millions')
plt.axis([-0.1, 2.1, 10, 50])
plt.xticks([0, 1, 2], ['2020', '2021', '2022'])
plt.title('Video game console sales')

plt.show()
