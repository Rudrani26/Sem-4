import matplotlib.pyplot as plt

progLang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(progLang, popularity, color=[
    'green', 'red', 'blue', 'yellow', 'cyan', 'orange'])
plt.title("Popularity of programming languages")
plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.grid(which='major', linewidth=0.5, linestyle='-', color='red')
plt.grid(which='minor', linewidth=0.5, linestyle=':', color='black')
plt.minorticks_on()
plt.show()
