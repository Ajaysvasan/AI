import pandas as pd
import math
import numpy as np

# Load dataset
data = pd.read_csv("3-dataset.csv")

# Extract features (excluding the target column)
features = [feat for feat in data.columns if feat != "answer"]

# Define a class for the tree node
class Node:
    def __init__(self):
        self.children = []
        self.value = ""
        self.isLeaf = False
        self.pred = ""

# Calculate entropy
def entropy(examples):
    pos = len(examples[examples["answer"] == "yes"])
    neg = len(examples[examples["answer"] == "no"])
    total = pos + neg
    if total == 0 or pos == 0 or neg == 0:
        return 0.0
    p = pos / total
    n = neg / total
    return -(p * math.log2(p) + n * math.log2(n))

# Calculate information gain
def info_gain(examples, attr):
    uniq = np.unique(examples[attr])
    gain = entropy(examples)  # Calculate entropy of the full dataset
    for u in uniq:
        subdata = examples[examples[attr] == u]
        sub_e = entropy(subdata)
        gain -= (len(subdata) / len(examples)) * sub_e
    return gain

# ID3 algorithm to build the decision tree
def ID3(examples, attrs):
    root = Node()
    # If all examples belong to the same class, return a leaf node
    if len(np.unique(examples["answer"])) == 1:
        root.isLeaf = True
        root.pred = np.unique(examples["answer"])[0]
        return root
    # If no attributes are left, return a leaf node with the most common class
    if not attrs:
        root.isLeaf = True
        root.pred = examples["answer"].mode()[0]
        return root

    # Find the attribute with the maximum information gain
    max_gain = -1
    max_feat = None
    for feature in attrs:
        gain = info_gain(examples, feature)
        if gain > max_gain:
            max_gain = gain
            max_feat = feature

    root.value = max_feat
    uniq = np.unique(examples[max_feat])

    # Split the dataset and recursively build child nodes
    for u in uniq:
        subdata = examples[examples[max_feat] == u]
        if subdata.empty:
            # Handle the case where a branch ends with no examples
            newNode = Node()
            newNode.isLeaf = True
            newNode.pred = examples["answer"].mode()[0]
            root.children.append(newNode)
        else:
            new_attrs = attrs.copy()
            new_attrs.remove(max_feat)
            child = ID3(subdata, new_attrs)
            dummyNode = Node()
            dummyNode.value = u
            dummyNode.children.append(child)
            root.children.append(dummyNode)

    return root

# Print the decision tree
def printTree(root: Node, depth=0):
    print("\t" * depth, end="")
    print(root.value, end="")
    if root.isLeaf:
        print(f" -> {root.pred}")
        return
    print()
    for child in root.children:
        printTree(child, depth + 1)

# Build the decision tree and print it
root = ID3(data, features)
printTree(root)
