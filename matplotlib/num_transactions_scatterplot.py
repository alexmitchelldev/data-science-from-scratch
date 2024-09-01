from matplotlib import pyplot as plt

user_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
num_transactions = [287, 195, 168, 159, 157, 155, 144, 141, 141, 140]


plt.scatter(user_labels, num_transactions)
plt.axis([0, len(user_labels), 0, max(num_transactions)])
plt.ylabel('# transactions')
plt.xlabel('User')
plt.show()
