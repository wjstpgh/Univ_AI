from constraint import *

problem=problem()
problem.addVariable('a', range(1,11)) //범위를 준다.
problem.addVariable('b', range(1,11,1))

problem,addConstraint(lambda a, b: a*3==b)//람다값을 준다
solutions=problem.getSolutions()

print(solutions)
