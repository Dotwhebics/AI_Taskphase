# Neural Networks and CNNs


A neural network is an artificially built machine learning model which tries to mimic the biological idea of neurons. 

In a biological system neuron is a unit within the brain which holds some information. Neurons, millions in number, form connections which vary with experience and time during the lifetime of the individual to make changes in the way they function. 

Neural networks which form the backbone of AI work similarly. They are connected layer by layer and the connections have certain parameters called weigths which we shall talk about later. The weigths change over time and determine how strongly the neurons are connected and how receptive is one neuron to another.

Unlike the human nerves the overall architecture of the neurons is not randomly built and modified over time and experience. Neural networks have a well defined architecture right from the beginning.

Learning is the process that involves making chages in the effectiveness of the connections within the existing architecture describing how sensitive any pair of neurons is. 

Neural networks have layers, which can be considered as any intermediate step between the input and result. The input and result also form seperate layers.

## How it works?

The input, say a number written by hand is broken down in chunks. In our case the chinks are pixels. These are fed to the input layer. Each pixel has a value between 0 and 1 which represents the "activation" of that pixel. Activation is basically a number that gives the magnitude that neuron contributes towards deciding a certain output.

As data moves through the connections to the successive layers a certain task is performed by each layer that in turn influences the output in some way. We call this forward propagation.

The model we are attempting to perfect has a predefined architecture of layers and connection. We require each of the connections to have a certain "strength" as not all connections are of the same importace. Let the importance of a connection between 2 neurons in 2 different layers be represented by a number that we shall call "weight". The strong connections must have a postive value of slightly larger magnitude compared to say a weak connection with small negative value. Initially, all these connections have random values.

### 1. Forward Propagation

In the process of forward propagation, we add all the weighted contributions that the previous layer makes to a particular neuron. An extra constant called the bias is added to this. Value of the weighed sum may only be of significance beyond a threshold value. The bias is basically the negative of that threshold value. 

Once this is done we clip any value we get after the computation to a fixed range using a specific function. For example, the sigmoid function clips the values between 0 and 1. The clipping function is called the activation function. The output of this function in turn becomes the activation of the currect neuron. 

This process occurs in all neurons in this layer to get individual activation values. 
The exact process ocurrs layer to layer eventually working on determining the output. 

### 2. Backward Propagation

It must be understood that initially what the model outputs is completely random and it is with the process of training that we aspire to make this network to fulfill the alloted task. A clear analogy with the human learning process can be seen here. Learning with experience and repetition, making small corrections in the journey towards perfection which is almost never attained.

The process of learning involves performing small corrections to the value of the parameters (the connection weights and the biases) iteratively.

First, we define a cost funtion which serves the purpose of determining how far is the prediction from the actual values (error). To find the optimal value of the parameters, we need to ensure the minimisation of this cost function.

This minimisation is achived by changing the parameters in small steps. Gradient Descent is the process that stands up to this task. In gradient decent we make small step changes in the parameter values. The changes are proportional to the negative slope of the cost function with respect to a change in one parameter. Thus we are "descending" to the minima of the cost function.

The partial derivative w.r.t to each weight and bias is calculated for this purpose.

As is clear, we are moving backwards from the output layer hence this process is backward propagation.

> Forward propagation and backward propagation take place alternatively for a fixed number of iterations.


## Convolutional Neural Networks (CovNets)

Convolution is a mathmatical filter that works on two functions to convert them to a third function. Convolution is carried out by the activation function we talked of.

A convolutional neural network, a multilayer network, is aimed at attempting to perform specifc tasks the way human vision peforms them. Like, identification of a handwritten number even though hand writing may vary significantly, or identifying an object.

Convolutional neural networks are applied to pattern recognition in images.

Convolutional neural networks work the way described above.

## Sources :

> 3Blue1Brown Youtube channel's neural networks playlist

> https://en.wikipedia.org/wiki/Neural_network

> https://en.wikipedia.org/wiki/Convolution

> https://www.digitalvidya.com/blog/types-of-neural-networks/