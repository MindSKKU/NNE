#-*- coding: utf-8 -*-
import numpy as np
import random
import os
import matplotlib.pyplot as plt
from collections import OrderedDict
from utils import numerical_gradient

def softmax(x):
    
    """
    Softmax 함수를 생성하라.
    NaN가 생성되지 않도록 구현 할 것(오버플로우 방지)
    Batch size(N)을 고려하여 구현하라
    
    Inputs : 
        - x : (N,D) 차원의 벡터
    
    Output : 
        - softmax_output : (N,D) 차원의 Softmax 결과
    
    
    Make Softmax function.
    Be careful not to make NaN.(preventing overflow)
    Implement considering Batch size(N).
    
    Inputs : 
        - x : vector with dimension (N,D)
    
    Output : 
        - softmax_output : Softmax result with dimension (N,D)
    
    """
    
    softmax_output = None
    
    #########################################################################################################
    #------------------------------------------WRITE YOUR CODE----------------------------------------------#
    
    #-----------------------------------------END OF YOUR CODE----------------------------------------------#
    #########################################################################################################
    
    return softmax_output




def cross_entropy_loss(score, target, weights, regularization):
    
    """
    cross_entropy_loss 함수를 생성하라.
    delta를 이용하여 log값의 input으로 0이 들어가지 않도록 대처하라
    Batch size(N)을 고려하여 구현하라.
    Weights를 이용한 L2 Regularization을 고려하여 구현하라
    L2 Regularization은 0.5를 곱하여 계산하라 (미분 할 때 계산적 이점)
    
    Inputs : 
        - score : (N, D) 차원의 벡터
        - target : (N, D) 차원의 벡터 (One-hot encoding)
        - weights : N개의 Weight 벡터
        - regularization : regularization를 결정하는 0과 1사이의 수
    
    Output : 
        - loss : scalar인 loss 값
    
    
    Make cross_entropy_loss function.
    Let 0 not to be an input to log using delta.
    Implement considering Batch size(N).
    Implement considering L2 Regularization using Weights.
    Calculate L2 Regularization with multiplying 0.5. (advantage when differentiating)
    
    Inputs : 
        - score : vector with dimension (N, D)
        - target : vector with dimension (N, D) (One-hot encoding)
        - weights : N number of Weight vectors
        - regularization : a number between 0 to 1, which sets regularization
    
    Output : 
        - loss : loss value which is a scalar    
    """
    
    delta = 1e-9
    batch_size = target.shape[0]
    data_loss = 0
    reg_loss = 0
    loss = None
    
    #########################################################################################################
    #------------------------------------------WRITE YOUR CODE----------------------------------------------#
    
    #-----------------------------------------END OF YOUR CODE----------------------------------------------#
    #########################################################################################################
    
    loss = data_loss + reg_loss
    
    return loss
    

    

class OutputLayer:
    
    """
    Softmax를 이용한 Cross-entropy loss를 계산하는 Ouput Layer class를 생성하라.
    앞서 생성한 softmax() 및 cross_entropy_loss를 이용하여 구현 할 것
    forward, backward의 계산과정을 생각하여 구현할 것
    backpropagation에서 softmax의 output과 target label의 정보가 이용됨을 유념하여 구현할 것
    
    forward() : 
        - x : (N,D) 차원의 벡터
        - y : (N, # of Label) 차원의 벡터 
        - return : softmax loss
    
    backward() : 
        - dout : backpropagation으로 오는 delta 값, output layer 이므로 delta = 1
        - return : dx
    
    
    Make Ouput Layer class which calculates Cross-entropy loss, using Softmax.
    Use Softmax() and cross_entropy_loss, which are previously made.
    Consider the calculating process of forward, backward.
    Be careful that output of softmax and target label are used in backpropagation.
    
    forward() : 
        - x : vector with dimension (N,D)
        - y : vector with dimension (N, # of Label) 
        - return : softmax loss
    
    backward() : 
        - dout : delta from backpropagation, delta = 1 as it is output layer
        - return : dx    
    """
    
    def __init__(self, weights, regularization):
        self.loss = None           # loss value
        self.output_softmax = None # Output of softmax
        self.target_label = None   # Target label (one-hot vector)
        self.weights = weights
        self.regularization = regularization
        
    def forward(self, x, y):
    
        #########################################################################################################
        #------------------------------------------WRITE YOUR CODE----------------------------------------------#

        #-----------------------------------------END OF YOUR CODE----------------------------------------------#
        #########################################################################################################
    
        return self.loss
    
    def backward(self, dout=1):
        
        bt_size = self.target_label.shape[0]
        dx = None
        
        #########################################################################################################
        #------------------------------------------WRITE YOUR CODE----------------------------------------------#
        
        
        #-----------------------------------------END OF YOUR CODE----------------------------------------------#
        #########################################################################################################
        
        return dx
    
    
class ReLU:
    
    """
    ReLU를 구현하라
    forward, backward의 계산과정을 생각하여 구현할 것
    backpropagation에서 forward 과정에서 사용 된 mask 정보가 사용됨을 유념하여 구현할 것
    
    forward() : 
        - x : (N,D) 차원의 벡터
        - return : ReLU output
    
    backward() : 
        - dout : backpropagation으로 오는 delta 값
        - return : dx
    
    
    Implement RELU.
    Consider the calculating process of forward, backward.
    Be careful that mask information used in forward process is utilized in backpropagation.
    
    forward() : 
        - x : vector with dimension (N,D)
        - return : ReLU output
    
    backward() : 
        - dout : delta from backpropagation
        - return : dx    
    
    """
    
    def __init__(self):
        
        self.mask = None
        
    def forward(self, x):
        
        self.out = None
    
        #########################################################################################################
        #------------------------------------------WRITE YOUR CODE----------------------------------------------#

        #-----------------------------------------END OF YOUR CODE----------------------------------------------#
        #########################################################################################################
    
        return out
    
    def backward(self, dout):
    
        dx = None
        
        #########################################################################################################
        #------------------------------------------WRITE YOUR CODE----------------------------------------------#

        #-----------------------------------------END OF YOUR CODE----------------------------------------------#
        #########################################################################################################
        
        return dx
    
class Sigmoid:
    
    """
    Sigmoid 구현하라
    forward, backward의 계산과정을 생각하여 구현할 것
    backpropagation 과정에서 forward 과정에서 나온 계산 결과가 사용됨을 유념하여 구현할 것
    
    forward() : 
        - x : (N,D) 차원의 벡터
        - return : ReLU output
    
    backward() : 
        - dout : backpropagation으로 오는 delta 값
        - return : dx
    
    
    Implement Sigmoid.
    Consider the calculating process of forward, backward.
    Be careful that the results from forward process is utilized in backpropagation.
    
    forward() : 
        - x : vector with dimension (N,D)
        - return : ReLU output
    
    backward() : 
        - dout : delta from backpropagation
        - return : dx    
    
    """
    
    def __init__(self):
        self.out = None
        
    def forward(self, x):
    
        #########################################################################################################
        #------------------------------------------WRITE YOUR CODE----------------------------------------------#

        #-----------------------------------------END OF YOUR CODE----------------------------------------------#
        #########################################################################################################
    
        return out
    
    def backward(self, dout):
        
        dx = None
        
        #########################################################################################################
        #------------------------------------------WRITE YOUR CODE----------------------------------------------#

        #-----------------------------------------END OF YOUR CODE----------------------------------------------#
        #########################################################################################################
        
        return dx
    
    
    
class Affine:
    
    """
    Affine 계층을 구현하라
    Affine 계층이란 Y = np.dot(X, W) + B (X는 입력, W는 가중치, B는 바이어스)와 같은 한 뉴런의 가중치합을 계산하는 것
    forward, backward의 계산과정을 생각하여 구현할 것
    Batch size(N)을 고려하여 구현할 것
    Backward 과정에서 W,b 그리고 x 까지 모두 사용됨을 유의하여 구현할 것
    
    forward() : 
        - x : (N,D) 차원의 벡터
        - return : Affine output
    
    backward() : 
        - dout : backpropagation의 결과로 오는 delta 값
        - return : dx
    
    
    Implement Affine layer.
    Affine layer is calculating one neuron's weighted sum like Y = np.dot(X, W) + B (X: input, W: weight, B: bias)
    Consider the the calculating process of forward, backward.
    Consider the Batch size(N).
    Be careful that W,b, and x are used in Backward.
    
    forward() : 
        - x : vector with dimension (N,D)
        - return : Affine output
    
    backward() : 
        - dout : delta from backpropagation
        - return : dx    
    
    """
    
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None
        
    def forward(self, x):
        
        out = None
    
        #########################################################################################################
        #------------------------------------------WRITE YOUR CODE----------------------------------------------#

        #-----------------------------------------END OF YOUR CODE----------------------------------------------#
        #########################################################################################################
    
        return out
    
    def backward(self, dout):
        
        dx = None
        
        #########################################################################################################
        #------------------------------------------WRITE YOUR CODE----------------------------------------------#

        #-----------------------------------------END OF YOUR CODE----------------------------------------------#
        #########################################################################################################
        
        return dx
    
    
    
    
from collections import OrderedDict
class TwoLayerNet:
    
    """

    __init__() : 
        - Weight 및 bias를 initialization 하는 함수
        - Initialization 된 Weight와 bias를 이용하여 계층을 생성하는 함수
    
    predict() : 
        - Input data(x)에 대해서 Neural network의 forward propagtion을 수행하는 함수
        
    loss() : 
        - Input data(x)에 대해서 Neural network의 forward propagtion을 수행한 결과를 이용하여 Loss를 계산하는 함수
        
    accuracy() :
        - Input data(x)의 결과와 True label(y)을 이용하여 Accuracy를 구하는 함수
        
    numerical_gradient() :
        - Input data(x)와 True label(y)을 이용하여 Numerical_gradient를 구하는 함수
        - Backpropagation 방법과의 비교를 위해 사용
        
    gradient():
        - Input data(x)와 True label(y)을 이용하여 Backpropagation을 수행하는 함수
        
    
    
    __init__() : 
        - A function initializing Weight and bias
        - A function making layers with initialized Weight and bias
        
    predict() : 
        - A function performing forward propagation in neural network with input data(x)

    loss() : 
        - A function calculating Loss using the results from forward propagation of Neural network with input data(x)
        
    accuracy() :
        - A function obtaining Accuracy using the results from input data(x) and True label(y)
        
    numerical_gradient() :
        - A function obtaining Numerical_gradient using Input data(x) and True label(y)
        - Utilized to compare with backpropagation
        
    gradient():
        - A function performing Backpropagation using Input data(x) and True label(y)
    
    """

    def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01, regularization = 0.0):

        # 가중치 초기화
        # Weight initialization
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size) 
        self.params['b2'] = np.zeros(output_size)

        self.weights = {}
        self.weights['W1'] = self.params['W1']
        self.weights['W2'] = self.params['W2']
        
        self.reg = regularization

        # 계층 생성
        # Layer generation
        self.layers = OrderedDict() # infromation about OrderedDict (https://pymotw.com/2/collections/ordereddict.html)
        
        #########################################################################################################
        # TwoLayerNet을 구현하라                                                                                 
        # Neural Network의 구조는 다음과 같이 구현할 것                                                           
        # [ Input => Fully Connected => ReLU => Fully Connected(OutputLayer) ]
        # 구현시 위 과정에서 생성한 Class(Affine, ReLU)들 및 Weight initialization 과정에서 생성한 weight를 이용하여 구현할 것
        
        # Implement TwoLayerNet.
        # Implement Neural Network structure as follow
        # [ Input => Fully Connected => ReLU => Fully Connected(OutputLayer) ]
        # Implement using previously made Class(Affine, ReLU) and weights from Weight initialization
        #########################################################################################################
        #------------------------------------------WRITE YOUR CODE----------------------------------------------#
        # self.layers['Affine1'] = None
        # self.layers['Relu1'] = None
        # self.layers['Affine2'] = None

        #-----------------------------------------END OF YOUR CODE----------------------------------------------#
        #########################################################################################################
        self.lastLayer = OutputLayer(self.weights, self.reg)

    def predict(self, x):

        for layer in self.layers.values():
            x = layer.forward(x)
            
        return x

    def loss(self, x, y):
        score = self.predict(x)
        return self.lastLayer.forward(score, y)

    

    def accuracy(self, x, y):

        score = self.predict(x)
        score = np.argmax(score, axis=1)
        if y.ndim != 1 : y = np.argmax(y, axis=1)
        accuracy = np.sum(score == y) / float(x.shape[0])

        return accuracy

    def numerical_gradient(self, x, y):

        loss_W = lambda W: self.loss(x, y)

        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
        
        if self.reg != 0.0:
                       
            #########################################################################################################
            # Gradient를 구할 때 Regularization에 대한 부분을 구현하라
            # Implement Regularization part when obtaining Gradient
            #########################################################################################################
            #------------------------------------------WRITE YOUR CODE----------------------------------------------#
            
            pass #erase this when writing your code

            #-----------------------------------------END OF YOUR CODE----------------------------------------------#
            #########################################################################################################
            
        return grads

        

    def gradient(self, x, y):

        # forward
        self.loss(x, y)

        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)
        layers = list(self.layers.values())
        layers.reverse()

        for layer in layers:
            dout = layer.backward(dout)

        grads = {}
        grads['W1'], grads['b1'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W2'], grads['b2'] = self.layers['Affine2'].dW, self.layers['Affine2'].db
        
        if self.reg != 0.0:
            
            #########################################################################################################
            # 각 Weight 및 bias의 Gradient를 구할 때 Regularization에 의한 영향을 구현하라
            # Implement the impact of Regularization when obtaining each Gradient of Weight and bias.
            #########################################################################################################
            #------------------------------------------WRITE YOUR CODE----------------------------------------------#
            
            pass #erase this when writing your code

            #-----------------------------------------END OF YOUR CODE----------------------------------------------#
            #########################################################################################################

        return grads
    
    
    
    
    
class ThreeLayerNet:
    
    """

    __init__() : 
        - Weight 및 bias를 initialization 하는 함수
        - Initialization 된 Weight와 bias를 이용하여 계층을 생성하는 함수
    
    predict() : 
        - Input data(x)에 대해서 Neural network의 forward propagtion을 수행하는 함수
        
    loss() : 
        - Input data(x)에 대해서 Neural network의 forward propagtion을 수행한 결과를 이용하여 Loss를 계산하는 함수
        
    accuracy() :
        - Input data(x)의 결과와 True label(y)을 이용하여 Accuracy를 구하는 함수
        
    numerical_gradient() :
        - Input data(x)와 True label(y)을 이용하여 Numerical_gradient를 구하는 함수
        - Backpropagation 방법과의 비교를 위해 사용
    gradient():
        - Input data(x)와 True label(y)을 이용하여 Backpropagation을 수행하는 함수
        
    
    
    __init__() : 
        - A function initializing Weight and bias
        - A function making layers using initialized Weight and bias
    
    predict() : 
        - A function performing forward propagation of Neural network with Input data(x)
        
    loss() : 
        - A function calculating Loss using the results from forward propagation of Neural network with input data(x)
        
    accuracy() :
        - A function obtaining Accuracy using the results from input data(x) and True label(y)
        
    numerical_gradient() :
        - A function obtaining Numerical_gradient using Input data(x) and True label(y)
        - Utilized to compare with backpropagation
        
    gradient():
        - A function performing Backpropagation using Input data(x) and True label(y)    
    
    """

    def __init__(self, input_size, hidden_size1, hidden_size2, output_size, weight_init_std = 0.01, regularization = 0.0):

        
        #########################################################################################################
        # TwoLayerNet을 응용하여 ThreeLayerNet 구현하라
        # Neural Network의 구조는 다음과 같이 구현할 것
        #[ Input => Fully Connected => ReLU => Fully Connected => ReLU => Fully Connected(OutputLayer) ]
        #구현시 위 과정에서 생성한 Class를 이용하여 구현할 것
        #* Hidden Layer가 증가함에 따라 바꿔야하는 요소들(Weight 및 bias 추가, Hidden Layer의 weight 수, Weight update 등)을
        #충분히 고려하여 구현할 것 *
        # Hidden Layer의 변수로 hidden_size1, hidden_size2를 사용할 것
        
        
        # Implement ThreeLayerNet applying TwoLayerNet
        # Implement Neural Network structure as follow:
        #[ Input => Fully Connected => ReLU => Fully Connected => ReLU => Fully Connected(OutputLayer) ]
        # Implement using the Class previously made
        # * Consider the elements to be changed as Hidden Layer increase (e.g. addition of Weight and bias, number of weight in Hidden Layers, 
        #  Weight update) *
        # Use hidden_size1 and hidden_size2 as variables of Hidden Layer
        #########################################################################################################
        #########################################################################################################
        #------------------------------------------WRITE YOUR CODE----------------------------------------------#
        
        #-----------------------------------------END OF YOUR CODE----------------------------------------------#
        #########################################################################################################

        return 
    
    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
            
        return x

    def loss(self, x, y):        
        score = self.predict(x)
        
        return self.lastLayer.forward(score, y)

    

    def accuracy(self, x, y):
        score = self.predict(x)
        score = np.argmax(score, axis=1)
        if y.ndim != 1 : y = np.argmax(y, axis=1)
        accuracy = np.sum(score == y) / float(x.shape[0])

        return accuracy

        

    def gradient(self, x, y):
        # forward
        self.loss(x, y)
        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)
        layers = list(self.layers.values())
        layers.reverse()

        for layer in layers:
            dout = layer.backward(dout)

        grads = {}
        #########################################################################################################
        # 각 Weight 및 bias의 Gradient를 구하는 부분을 구현하라
        # Implement the part obtaining Gradient of each Weight and bias
        #########################################################################################################
        #------------------------------------------WRITE YOUR CODE----------------------------------------------#

        #-----------------------------------------END OF YOUR CODE----------------------------------------------#
        #########################################################################################################

        return grads
    
    
    
    
