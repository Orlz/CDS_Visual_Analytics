#!/usr/bin/env python

"""
===========================================================
Assignment 4: Neural Network Classification Benchmarks
===========================================================

Neural networks have allowed us to dive into the intricacies of deep learning and can provide one of the most accurate forms of classification. The model built in this script is a mere tip-toe into this field as it is simple (but effective!). 

The model uses the digits dataset from sklearn to classify digits into their correct numerical group (0:9) 
The output of the script is the evaluation metrics which are printed to the terminal.

This script will use argparse arguments to enable it to be run and the parameters ammended from the commandline.
It employs bonus challenge 1 (saving the output reports to an output file) and 2) determining number of hidden layers.
Instructions on how to use these can be found in the README.md file attached to this assignment. 

"""

"""
Import the Dependencies 

"""
#operating systems 
import os
import sys
sys.path.append(os.path.join(".."))

#command line functionality and pandas 
import argparse
import pandas as pd

# import utils 
from utils.neuralnetwork import NeuralNetwork

#Neural network dependencies from sklearn
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets
from sklearn import metrics


"""
Main Function with Argparse arguments

"""
def main():
    """
    Setting up our arguments with argparse
    """
    # initialise argument parser 
    ap = argparse.ArgumentParser()
    
    # Command line argument interface (i.e. define the arguments) 
    ap.add_argument("-s", "--split", required = True, help = "decimal between 0 - 1 indicating what the test split should be")
    ap.add_argument("-e", "--epochs", required = False, default = 1000, typ = int,
                    help = "Specify the number of epochs to run with. The default is set to 1000")
    ap.add_argument("-l", "--layers", required = False, default = 2, typ = int,
                    help = "Specify number of hidden layers. Maximum recommended = 3, default = 2")
    ap.add_argument("f", "--filename", required = False, default = "neural_network_report.csv",
                    help = "str indicating the filename of the output classification report")
    ap.add_argument("-o", "--output_path", required = True, help = "Path to output directory")
 
    # parse arguments (i.e. takes users input on the command line to make an args object which can be used in the script)  
    args = vars(ap.parse_args())
    
    
    """
    Assigning our arguments to variable names for the script
    """
   
    split = args["split"]
    epochs = args ["epochs"]
    layers = args["layers"]
    filename = args ["filename"]
    
    #output_path
    output_path = args["output_path"]
    
    #We want a default output path. Therefore, here we create one to save the metrics to (called output_path) 
    #The code says, "if an output path doesn't exist, please create one using os.mkdir()"
    if not os.path.exists(output_path):   
        os.mkdir(output_path) 
        
    
    """
    Fetching the digits dataset from sklearn and normalising it
    """
    
    # Load the data and ensure it is in the float format (instead of being an int) 
    digits = datasets.load_digits()
    data = digits.data.astype("float")
    
    # MinMax regularization (this ensures all numbers are between 0 - 1) 
    data = (data - data.min())/(data.max() - data.min())
    
    """
    Creating the train and test split 
    """
    #Create train and test sets based on the args "split" defined by the user (using sklearn train_test_split function)
    X_train, X_test, y_train, y_test = train_test_split(data, 
                                                  digits.target, 
                                                  test_size = split)
    
    """
    Convert the labels to binary representations (i.e. from integers to vectors)  
    """
    y_train = LabelBinarizer().fit_transform(y_train)
    y_test = LabelBinarizer().fit_transform(y_test)
    
    
    #Let the user know the training is about to begin 
    print("[INFO] We're about to start training the network...")
     
    """
    Adding the hidden layers functionality
    For this we can use an if else statement for up to 3 layers (beyond that doesn't make sense) 
    """
    
    #Then define the steps for each layer 
    if (layers==1):
        nn = NeuralNetwork([X_train.shape[1], 10])
    elif (len(layers)==2):
        nn = NeuralNetwork([X_train.shape[1], 16, 10])
    elif (len(layers)==3):
        nn = NeuralNetwork([X_train.shape[1], 32, 16, 10])
    else:
        nn = NeuralNetwork([X_train.shape[1], 16, 10])
        
   
    """
    Fitting and training the model
    """   
        
    #fit the model 
    print("[INFO] {}".format(nn))
    nn.fit(X_train, y_train, epochs=epochs)
    
    
    """
    Evaluating the model 
    """ 
    # Update the user on progress 
    print(["[INFO] Hang on, we're just evaluating how the neural network performed..."])
    
    #Create the predictions 
    predictions = nn.predict(X_test)
    predictions = predictions.argmax(axis=1)
    
    #Print the performance metrics to the screen
    print(classification_report(y_test.argmax(axis=1), predictions))
    
    
    """
    Creating a classification report 
    """ 
    #Create a dataframe of the metrics using pandas 
    nn_metrics = pd.DataFrame(metrics.classification_report(y_test.argmax(axis=1), predictions, output_dict=True))
   

    #Save the output to the output_path directory we created earlier. The file will be saved as a csv
    output_path = os.path.join("output_path", filename)
    nn_metrics.to_csv(output_path, index = False)
    
        
    #Then print to the terminal that this has been saved
    print("That's you complete - woohoo! The csv file and plots are in output directory.\n ") 
    

if __name__=="__main__":
    #execute main function
    main()
