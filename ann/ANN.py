#! bin/bash/python3
import math
import random
import _pickle as pickle
from numpy import dot

class ANN:
    network = []
    inputs = []
    targets = []

    def sigmoid(self, t):
        """
        Sigmoid function
        """
        return 1 / (1 + math.exp(-t))

    def neuron_output(self, weights, inputs):
        """
        Calculates the output for an individual neuron
        """
        return self.sigmoid(dot(weights, inputs))

    def feed_forward(self, network, input_vector):
        """
        Performs feed forward operation for input fitting.
        """
        outputs = []

        for layer in network:
            input_with_bias = input_vector + [1]
            output = [self.neuron_output(neuron, input_with_bias) for neuron in layer]
            outputs.append(output)
            input_vector = output

        return outputs

    def back_propogate(self, network, input_vector, targets):
        """
        Performs back propogation for network training.
        """
        hidden_outputs, outputs = self.feed_forward(network, input_vector)
        output_deltas = [output * (1 - output) * (output - target)
                         for output, target in zip(outputs, targets)]

        for i, output_neuron in enumerate(network[-1]):
            for j, hidden_output in enumerate(hidden_outputs + [1]):
                output_neuron[j] -= output_deltas[i] * hidden_output
            network[-1][i] = output_neuron

        hidden_deltas = [hidden_output * (1 - hidden_output) *
                         dot(output_deltas, [n[i] for n in network[-1]])
                         for i, hidden_output in enumerate(hidden_outputs)]

        for i, hidden_neuron in enumerate(network[0]):
            for j, inpt in enumerate(input_vector + [1]):
                hidden_neuron[j] -= hidden_deltas[i] * inpt
            network[0][i] = hidden_neuron

        self.network = network

    def build(self, input_size=10, num_hidden=3, output_size=10):
        """
        Creates a randomized neural network. 
        input_size is the number of inputs
        num_hidden is the number of neurons in the hidden layer
        output_size is the number of outputs.
        """
        random.seed(0)

        hidden_layer = [[random.random() for _ in range(input_size + 1)]
                        for _ in range(num_hidden)]

        output_layer = [[random.random() for _ in range(num_hidden + 1)]
                        for _ in range(output_size)]

        self.network = [hidden_layer, output_layer]

    def train(self, iterations=1000):
        """
        Trains the neural network. 
        Before using train, the build method should have been run and 
        the inputs and targets properties should have been set.
        """
        for _ in range(iterations):
            for input_vector, target_vector in zip(self.inputs, self.targets):
                self.back_propogate(self.network, input_vector, target_vector)

    def fit(self, inpt, threshold=False, truncate=3):
        """
        Tests inputs in current neural network. 
        If threshold is True, it will output 1s for any output at least 60% of the highest output. 
        Truncate will round the decimal to the number of digits passed in. Pass -1 for no rounding.
        """
        output = self.feed_forward(self.network, inpt)[-1]

        if truncate > -1:
            fmtstr = '.' + str(truncate) + 'f'
            output = [float(format(out, fmtstr)) for out in output]

        if threshold:
            highest = max(output)
            output = [1 if out >= highest * .6 else 0 for out in output]

        return output

    def save(self, file_prefix=''):
        """
        Saves the self.network, self.inputs, and self.targets objects into respective .p files.
        file_prefix will add a prefix to the filename.
        """
        for i, file in enumerate(['network.p', 'inputs.p', 'targets.p']):
            cf = file_prefix + file
            f = open(cf, 'wb')
            obj = [self.network, self.inputs, self.targets][i]
            pickle.dump(obj, f)
            f.close()

    def restore(self, file_prefix=''):
        """
        Loads the self.network, self.inputs, and self.targets objects from their respective .p files.
        file_prefix will add a prefix to the filename.
        """
        network_file = file_prefix + 'network.p'
        nf = open(network_file, 'rb')
        self.network = pickle.load(nf)
        nf.close()

        inputs_file = file_prefix + 'inputs.p'
        inf = open(inputs_file, 'rb')
        self.inputs = pickle.load(inf)
        inf.close()

        targets_file = file_prefix + 'targets.p'
        tf = open(targets_file, 'rb')
        self.targets = pickle.load(tf)
        tf.close()