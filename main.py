from model import *
import matplotlib.pyplot as plt

print('Enter p')
p = float(input())

print('Enter number of generations:')
num_generations = int(input())

counter = 1
x_vals = [0]
y_vals = [p]
for _ in range(num_generations):
    print('p =', p, 'q = ', 1-p)
    p = run(p, num_offspring=20000)
    x_vals.append(counter)
    counter += 1
    y_vals.append(p)

fig, ax = plt.subplots()

ax.plot(x_vals, y_vals, linewidth=2.0)
ax.plot(x_vals, [1- y for y in y_vals], linewidth=2.0)

plt.xlabel("Number of Generations")
plt.ylabel("Allele Frequency")
plt.legend(["p", "q"])
plt.ylim([0, 1])

plt.show()