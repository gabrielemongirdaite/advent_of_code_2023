from sympy import solve, symbols

t1, t2, t3 = symbols('t1'), symbols('t2'), symbols('t3')
p1, p2, p3 = symbols('p1'), symbols('p2'), symbols('p3')
v1, v2, v3 = symbols('v1'), symbols('v2'), symbols('v3')

equations = [385803404726014 - 192 * t1 - (p1 + t1 * v1), 386664184220541 - 149 * t1 - (p2 + t1 * v2),
             365612177547870 - 36 * t1 - (p3 + t1 * v3),
             67771006464582 + 280 * t2 - (p1 + t2 * v1), 193910554798739 + 136 * t2 - (p2 + t2 * v2),
             21517103663672 + 426 * t2 - (p3 + t2 * v3),
             334054450538558 + 84 * t3 - (p1 + t3 * v1), 356919582763697 - 25 * t3 - (p2 + t3 * v2),
             188448277532212 - 48 * t3 - (p3 + t3 * v3)]
solutions = solve(equations, t1, t2, t3, p1, p2, p3, v1, v2, v3, dict=True)
print(solutions[0][p1] + solutions[0][p2] + solutions[0][p3])
