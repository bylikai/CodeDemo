import numpy as np
import scipy.special

#http://yann.lecun.com/exdb/mnist/
#
#http://www.pjreddie.com/media/files/mnist_train.csv
#http://www.pjreddie.com/media/files/mnist_test.csv

#https://raw.githubusercontent.com/makeyourownneuralnetwork/makeyourownneuralnetwork/master/mnist_dataset/mnist_train_100.csv
#https://raw.githubusercontent.com/makeyourownneuralnetwork/makeyourownneuralnetwork/master/mnist_dataset/mnist_test_10.csv

class neuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate

        #设置权重:
        #self.wih = np.random.rand(self.hnodes, self.inodes) - 0.5   # W_input_hidden = hidden_nodes * input_nodes
        #self.who = np.random.rand(self.onodes, self.hnodes) - 0.5   # W_hidden_output = hidden_nodes * output_nodes
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes) )
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        #激活函数
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    def train(self, inputs_list, targets_list ):
        #1.针对给定的训练样本计算输出
        #将inputs_list, targets_list 转换成2维数组
        inputs = np.array( inputs_list, ndmin=2).T
        targets = np.array( targets_list, ndmin=2).T

        #calculate signals into hidden layer
        hidden_inputs = np.dot( self.wih, inputs)

        #calculate the signals emerging from hidden layer 
        hidden_outputs = self.activation_function( hidden_inputs )

        #calculate singals into final output layer
        final_inputs = np.dot( self.who, hidden_outputs)

        #calculate the sinals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        #2. 基于所有计算输出与目标输出之间的误差，改进权重
        #1）计算误差： 
        #error is the (target-actual)
        output_errors = targets - final_outputs
        #hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = np.dot(self.who.T, output_errors)

        #2） 调整权重
        #update the weights for the links between the hidden and output layers
        self.who += self.lr * np.dot( (output_errors*final_outputs*(1.0-final_outputs)), np.transpose(hidden_outputs) )
        #update the weights for the links between the input and hidden layers
        self.wih += self.lr * np.dot( (hidden_errors*hidden_outputs*(1.0-hidden_outputs)), np.transpose(inputs) )

        pass

    def query(self, inputs_list):
        """
        查询神经网络
        """
        #将inputs_list转换成2维数组
        inputs = np.array( inputs_list, ndmin=2).T

        #calculate signals into hidden layer
        hidden_inputs = np.dot( self.wih, inputs)

        #calculate the signals emerging from hidden layer 
        hidden_outputs = self.activation_function( hidden_inputs )

        #calculate singals into final output layer
        final_inputs = np.dot( self.who, hidden_outputs)

        #calculate the sinals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs
    