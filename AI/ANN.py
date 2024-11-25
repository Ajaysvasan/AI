import numpy as np

# Dataset
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

# Normalize inputs and outputs
X = X / np.amax(X, axis=0)  # Normalize input
y = y / 100  # Normalize output

# Sigmoid Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)

# Hyperparameters
epoch = 1000  # Increased iterations
lr = 0.1  # Learning rate

# Network architecture
inputlayer_neurons = X.shape[1]  # Number of features
hiddenlayer_neurons = 3  # Number of hidden layer neurons
output_neurons = 1  # Number of output neurons

# Weight and bias initialization
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))  # Weights for hidden layer
bh = np.random.uniform(size=(1, hiddenlayer_neurons))  # Bias for hidden layer
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))  # Weights for output layer
bout = np.random.uniform(size=(1, output_neurons))  # Bias for output layer

# Training the network
for i in range(epoch):
    # Forward Propagation
    hinp1 = np.dot(X, wh) + bh
    hlayer_act = sigmoid(hinp1)
    outinp1 = np.dot(hlayer_act, wout) + bout
    output = sigmoid(outinp1)

    # Error calculation
    EO = y - output  # Error at output
    loss = np.mean(np.square(EO))  # Mean Squared Error

    # Backpropagation
    outgrad = derivatives_sigmoid(output)  # Gradient for output layer
    d_output = EO * outgrad
    EH = d_output.dot(wout.T)  # Error at hidden layer
    hiddengrad = derivatives_sigmoid(hlayer_act)  # Gradient for hidden layer
    d_hiddenlayer = EH * hiddengrad

    # Updating weights and biases
    wout += hlayer_act.T.dot(d_output) * lr
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    wh += X.T.dot(d_hiddenlayer) * lr
    bh += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr

    # Logging progress
    if (i + 1) % 100 == 0 or i == 0:  # Log every 100 epochs
        print(f"Epoch {i+1}/{epoch}")
        print(f"Loss: {loss:.6f}")

# Final Outputs
print("\nFinal Results:")
print("Input:\n", X)
print("Actual Output:\n", y)
print("Predicted Output:\n", output)
