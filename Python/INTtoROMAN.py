class solution:
    def intToroman(self, num):
        val = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD",
                  "C", "XC", "L", "XL",
                  "X", "IX", "V", "VI", "I"]

        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += symbol[i]
                num -= val[i]
            i += 1
        return roman_num


print(solution().intToroman(18))
print(solution().intToroman(26))
