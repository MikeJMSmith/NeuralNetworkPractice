import logging
import numpy


logger = logging.getLogger(__name__)


# Neural Network class Definition
class neuralNetwork:

    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
        """
        Initialize the Neural Network
        """
        logger.info(">>> Initialzing nodes and learning rate")
        self.inodes = inputNodes
        self.hnodes = hiddenNodes
        self.onodes = outputNodes
        self.lr = learningRate

        logger.info(">>> Initialzing weight matrices")
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        
        pass
    
    def train(self):
        """
        train the Neural Network
        """
        pass

    def query(self):
        """
        query the neural network
        """
        pass