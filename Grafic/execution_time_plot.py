import matplotlib.pyplot as plt

matrix_sizes = [10, 100, 300, 500, 1000]
times_c = [2.058708, 4.1812102,30.4800838,130.3018438, 1564.582113]
times_java = [0.009, 2.595, 98.414, 283.447, 3717.596]
times_python = [0.130, 125.45, 3331.08, 16426.66, 146711.6247]

plt.figure(figsize=(10, 6))

plt.plot(matrix_sizes, times_c, label="C", marker='o', linewidth=2, markersize=8)
plt.plot(matrix_sizes, times_java, label="Java", marker='o', linewidth=2, markersize=8)
plt.plot(matrix_sizes, times_python, label="Python", marker='o', linewidth=2, markersize=8)

# Etiquetas de los ejes
plt.xlabel("Matrix size", fontsize=12)
plt.ylabel("Execution time (ms)", fontsize=12)
plt.title("Comparison execution time with different matrix size", fontsize=14)

plt.yscale('log')
plt.grid()
plt.xticks(matrix_sizes, fontsize=10)
plt.yticks(fontsize=10)

for i, size in enumerate(matrix_sizes):
    plt.text(size, times_c[i], f"{times_c[i]:.2f}", fontsize=10, ha='right')
    plt.text(size, times_java[i], f"{times_java[i]:.2f}", fontsize=10, ha='left')
    plt.text(size, times_python[i], f"{times_python[i]:.2f}", fontsize=10, ha='right')


plt.legend(fontsize=12)

plt.show()
