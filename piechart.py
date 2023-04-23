import matplotlib.pyplot as plt

progLang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.title("Popularity of programming languages",
          bbox={'facecolor': '0.8', 'pad': 5})

plt.pie(popularity, explode=(0.1, 0, 0, 0, 0, 0), labels=progLang,
        colors=('r', 'g', 'b', 'y', 'c', 'pink'), shadow=True, autopct='%1.1f%%')

plt.legend()
plt.show()
