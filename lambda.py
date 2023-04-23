# -------------------------------------------------------

# r = lambda a : a + 15
# print(r(10))

# r = lambda x, y : x * y
# print(r(12, 4))

# -------------------------------------------------------

# is_num = lambda q: q.replace('.','',1).isdigit()

# print("\nPrint checking numbers:")
# is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)

# -------------------------------------------------------

weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day) == 6 else '', weekdays)
for d in days:
    print(d)
