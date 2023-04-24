def extract_nth_element(test_list, n):
    result = list(map(lambda x: (x[n]), test_list))
    return result


students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96),
            ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

print("Original list:")
print(students)

print(extract_nth_element(students, 0))

print(extract_nth_element(students, 2))
