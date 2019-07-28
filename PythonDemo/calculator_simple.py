#import numpy as np
import numpy as np
from sys import argv
import easygui


num1 = argv[1]
num2 = argv[2]
sum = int(num1) + int(num2)

print(sum)
easygui.msgbox( str(num1) + " + " + str(num2) + " = " + str(sum) ) 
