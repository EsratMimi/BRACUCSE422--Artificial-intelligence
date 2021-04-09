import numpy as np
output=np.genfromtxt('Question.txt',delimiter=' ',skip_header=0,filling_values=000,
                     dtype='float')
print(output)
