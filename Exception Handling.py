def division(x, y):
    try:
        div = x/y
        print(f"{x}/{y} = {div}")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("Working on the division function.")


a = int(input("enter number 1: "))
b = int(input("enter number 2: "))

division(a, b)

division(10, 0)
