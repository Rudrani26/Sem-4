import matplotlib.pyplot as plt
import numpy as np

men_Mean = (22, 30, 33, 30, 26)
women_Mean = (25, 32, 30, 35, 29)
men_Std = (4, 3, 4, 1, 5)
women_Std = (3, 5, 2, 3, 3)

index = np.arange(5)
barwidth = 0.4

plt.bar(index, men_Mean, yerr=men_Std, color='yellow', label="Men")
plt.bar(index, women_Mean, bottom=men_Mean, yerr=women_Std,
        color='purple', label="Women")

plt.xticks(index, ('Group1', 'Group2', 'Group3', 'Group4', 'Group5'))
plt.xlabel("Groups")
plt.ylabel("Mean score of Men and Women")

plt.legend()
plt.show()
