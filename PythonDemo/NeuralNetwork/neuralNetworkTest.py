
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import neuralNetwork as NNetwork

def test_neural():
    input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3

    learning_rate = 0.5

    n = NNetwork.neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    q = n.query([1.0, 0.5, -1.5])

    print(q)
    pass

def test_mnist_train1():
    input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3

    learning_rate = 0.5

    n = NNetwork.neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    q = n.query([1.0, 0.5, -1.5])

    print(q)

    data_file = open("mnist_train_100.csv", "r")
    data_list = data_file.readlines()
    data_file.close()

    # print(data_list)

    all_values = data_list[0].split(',')
    print(len(all_values))  # 785,   784 = 28*28

    # 将数据的范围从0~255 转换为0.01~1.00, 防止0导致人为造成权重更新失败
    scaled_input = np.asfarray(all_values[1:]) / 255.0 * 0.99 + 0.01
    print(scaled_input)

    # see all_values[1:] of string array as float array
    image_array = np.asfarray(all_values[1:]).reshape((28, 28))

    onodes = 10
    targets = np.zeros(onodes) + 0.01
    targets[int(all_values[0])] = 0.99
    print(targets)

    plt.imshow(image_array, cmap='Greys', interpolation='None')
    plt.show()
    print("@OK")
    pass

def test_mnist_train2( mnist_train_file, mnist_test_file ):
    input_nodes = 784
    hidden_nodes = 100
    output_nodes = 10
    learning_rate = 0.3

    n = NNetwork.neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    train_data_file = open(mnist_train_file, "r")  #train_data_file = open("mnist_train_100.csv", "r")
    train_data_list = train_data_file.readlines()
    train_data_file.close()

    for record in train_data_list:
        all_values = record.split(',')
        inputs = np.asfarray(all_values[1:]) / 255.0 * 0.99 + 0.01

        targets = np.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99

        n.train(inputs, targets)
        pass

    test_mnist_test2(n, mnist_test_file )

    pass

def test_mnist_test1( n, mnist_test_file ):
    test_data_file = open(mnist_test_file, "r") #test_data_file = open("mnist_test_10.csv", "r")
    test_data_list = test_data_file.readlines()
    test_data_file.close()

    all_values = test_data_list[0].split(',')
    print(all_values[0])

    image_array = np.asfarray(all_values[1:]).reshape((28, 28))
    plt.imshow(image_array, cmap='Greys', interpolation='None')
    plt.show()
    res = n.query( np.asfarray(all_values[1:]) / 255.0 * 0.99 + 0.01 )

    print(all_values[0], end=' ')
    print("mnist as ")
    print(res)

    pass


def test_mnist_test2(n, mnist_test_file ):
    test_data_file = open(mnist_test_file, "r") #test_data_file = open("mnist_test_10.csv", "r")
    test_data_list = test_data_file.readlines()
    test_data_file.close()

    scorecard = []

    for record in test_data_list:
        # split the record by , commas
        all_values = record.split(',')
        # correct answer is first value
        correct_label = int(all_values[0])
        print(correct_label, "correct label")

        #scale ans shift the inputs, and query the network
        inputs = np.asfarray(all_values[1:]) / 255.0 * 0.99 + 0.01
        outputs = n.query(inputs)

        # the index of the highest value corresponds to the label,
        label = np.argmax(outputs)
        print(label, "network 's answer")

        # append correct or incorrect to list
        if (label == correct_label):
            scorecard.append(1)
        else:
            scorecard.append(0)
        print()
        pass
    scorecard_array = np.asarray(scorecard)
    print("performance = ", scorecard_array.sum() / scorecard_array.size )

    print("@test_mnist_test2@")
    pass


if __name__ == "__main__":
    #test_neural()

    #test_mnist_train1()

    #test_mnist_train2( "mnist_train_100.csv", "mnist_test_10.csv" )

    basepath = "F:/"  # change basepath for your file system.
    test_mnist_train2(basepath+"mnist_train.csv", basepath+"mnist_test.csv")

    pass

