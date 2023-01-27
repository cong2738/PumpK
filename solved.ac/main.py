from itertools import combinations_with_replacement as pm
ex_shape = pm([(0,0),(0,1),(0,2),(1,1)],4)
print(*ex_shape,sep='\n')