import matplotlib.pyplot as plt

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.title("Comparison of Maths and Science scores")

plt.scatter(marks_range, math_marks, label='Math', color='brown')
plt.scatter(marks_range, science_marks, label='Science', color='purple')

plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")

plt.legend()
plt.show()
