import Calculator

test1 = "(a+b)*)c -d)"
test2 = "(a+b(*(c -d)"
test3 = ")a+b(*(c-d)"
test4 = "a+b*c-d"
test5 = "(a+b)*(c -d)"

c = Calculator.Calculator()

print(c.matched_expression(test1))
print(c.matched_expression(test2))
print(c.matched_expression(test3))
print(c.matched_expression(test4))
print(c.matched_expression(test5))

