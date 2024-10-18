import matplotlib.pyplot as plt
import numpy as np


sizes = [10, 100, 300, 500, 1000]
python_memory = [4, 520, 3052, 8880, 40952]
java_memory = [218, 775, 2039, 3787, 8658]
c_memory = [1186.4, 1377.6, 3243.2, 7004, 24668.8]


bar_width = 0.25
index = np.arange(len(sizes))


plt.figure(figsize=(10, 6))
plt.bar(index, python_memory, bar_width, label='Python')
plt.bar(index + bar_width, java_memory, bar_width, label='Java')
plt.bar(index + 2 * bar_width, c_memory, bar_width, label='C')


plt.xlabel('Matrix Size')
plt.ylabel('Memory Usage (KB)')
plt.title('Memory Usage Comparison Between Python, Java, and C')
plt.xticks(index + bar_width, sizes)


plt.ylim(0, 45000)
plt.yticks(np.arange(0, 45001, 5000))

plt.legend()


plt.tight_layout()
plt.show()
