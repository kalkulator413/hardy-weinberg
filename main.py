from model import *
import matplotlib.pyplot as plt

print('Enter p')
p = float(input())

print('Enter number of generations:')
num_generations = int(input())

counter = 1
x_vals = [0]
p_vals = [p]
q_vals = [1-p]
for _ in range(num_generations):
    print('p =', p, 'q = ', 1-p)
    p = run(p, num_offspring=2000)
    x_vals.append(counter)
    counter += 1
    p_vals.append(p)
    q_vals.append(1-p)

fig, ax = plt.subplots()

ax.plot(x_vals, p_vals, linewidth=2.0)
ax.plot(x_vals, q_vals, linewidth=2.0)
ax.plot(x_vals, [p_vals[i]**2 + 2*p_vals[i]*q_vals[i] + q_vals[i]**2 for i in range(num_generations + 1)], 
    linewidth=6.0)

plt.xlabel("Number of Generations")
plt.ylabel("Allele Frequency")
plt.legend(["p", "q", 'p^2 + 2pq + q^2'])
plt.ylim([0, 1])
plt.xlim([0, num_generations + 1])

plt.show()