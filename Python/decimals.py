import decimal

value1 = decimal.Decimal(3.1459)
print(value1)
print(value1.as_tuple())

value2 = decimal.Decimal("69.80085")
print(value2)
print(value2.as_tuple())


def round(x):
    remainder = x.remainder_near(decimal.Decimal('0.10'))
    if abs(remainder) == decimal.Decimal(0.05):
        return x
    else:
        return x - remainder


for x in range(10, 20):
    y = decimal.Decimal(x)/decimal.Decimal('1E2')
    print("", round(y))


print(round(decimal.Decimal(0.69)))

decimal.getcontext().prec = 5
decimal.getcontext().rounding = decimal.ROUND_CEILING
print(decimal.Decimal(20)/decimal.Decimal(6))

decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_FLOOR
print(decimal.Decimal(20)/decimal.Decimal(6))

decimal.getcontext().prec = 1
decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
print(decimal.Decimal(10)/decimal.Decimal(6))
