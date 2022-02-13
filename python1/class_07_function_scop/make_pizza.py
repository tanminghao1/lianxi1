# 导入模块：import 模块名，会导入模块内所有的函数，类
import pizza
pizza.make_pizza('5','葱花','胡椒')
pizza.make_pizza('8','香菜','花生','葱花')
# 导入特定的函数，导入模块内特定的函数,通过用逗号隔开函数名
from d3_from_import import fun_1,fun_2
# 可以直接调用函数，无需模块名.函数名
fun_1()
fun_2()
from pizza import make_pizza
make_pizza('10','香菜')

# 导入模块中的所有函数
from pizza import *
make_pizza('10')

# 使用as给模块指定别名
import pizza as p
p.make_pizza('10','辣椒粉')