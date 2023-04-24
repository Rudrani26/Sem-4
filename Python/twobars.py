import matplotlib.pyplot as plt
import numpy as np

men_Mean = (22, 30, 33, 30, 26)
women_Mean = (25, 32, 30, 35, 29)

index = np.arange(5)
barwidth = 0.4

plt.bar(index, men_Mean, barwidth,  color='yellow', label="Men")
plt.bar(index+barwidth, women_Mean, barwidth, color='purple', label="Women")

plt.xticks(index, ('M1', 'M2', 'M3', 'M4', 'M5'))
plt.xlabel("Gender")
plt.ylabel("Mean score of Men and Women")

plt.legend()
plt.show()
