import paddle 
import paddle.fluid as fluid
import numpy

def paddleAdd( valA, valB, type ):
    """
    利用paddlepaddle 计算valA, valB的和
    """
    a = fluid.layers.fill_constant(shape=[1], dtype=type, value=valA)
    b = fluid.layers.fill_constant(shape=[1], dtype=type, value=valB)
    z = a+b

    #create an Executor
    exe = fluid.Executor( fluid.CPUPlace() )

    #run
    ret = exe.run(fluid.default_main_program(), fetch_list=[z])

    return ret