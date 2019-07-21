
import neuralNetwork as NNetwork


if __name__ == "__main__":
    input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3

    learning_rate = 0.5

    n = NNetwork.neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    q = n.query([1.0, 0.5, -1.5])

    print(q)