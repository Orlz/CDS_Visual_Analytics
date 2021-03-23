#!/usr/bin/env python

"""
===========================================================
Assignment 4: Logistic Regression Classification Benchmarks
===========================================================

Classification is a key feature of visual analytics and continues to develop year on year. It has been used in many field from medical imaging (to help determine diagnosis) to business, to internet security, and beyond! 

This first script uses multinomial logistic regression to classify images of handwritten digits into the number category they belong to (between 0:9). The output of the script is the evaluation metrics which are printed to the terminal.

The script will use argparse arguments to enable it to be run and the parameters ammended from the commandline:

"""


"""
Import the Dependencies 

"""
#operating systems 
import os
import sys
sys.path.append(os.path.join(".."))

#command line functionality
import argparse

# import utils
import pandas as pd
import numpy as np
import utils.classifier_utils as clf_util

#Sklearn metrics  
from sklearn import metrics
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


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
    ap.add_argument("-o", "--output_path", required = True, help = "Path to output directory")
    ap.add_argument("f", "--filename", required = False, default = "logistic_regression_report.csv",
                    help = "str indicating the filename of the output classification report") 
    
    # parse arguments (i.e. takes users input on the command line to make an args object which can be used in the script)  
    args = vars(ap.parse_args())
    
    
    """
    Assigning our arguments to variable names for the script
    """
    #split  
    split = args["split"]
    
    #output_path
    output_path = args["output_path"]
    
    #We want a default output path. Therefore, here we create one to save the metrics to (called output_path) 
    #The code says, "if an output path doesn't exist, please create one using os.mkdir()"
    if not os.path.exists(output_path):   
        os.mkdir(output_path) 
        
    #Optional filename 
    filename = args["filename"]
        
         
    """
    Fetching the MNIST data from opemml 
    """
    #we call the data from an online directory called open_ml (X = pixel intensity values, y = digit category they belong to)  
    X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)    

    """
    Cleaning the data  
    """
    #Safety check: ensure the data is in a numpy array format
    X = np.array(X)
    y = np.array(y)
    
    """
    Creating the train and test split 
    """
    
    #Create train and test sets based on the args "split" defined by the user (using sklearn train_test_split function) 
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        random_state=33,
                                                        test_size= split ) #split will be a decimal between 0 - 1 
    
    #Scale the features to be between the scale of 0 to 1
    X_train_scaled = X_train/255.0
    X_test_scaled = X_test/255.0
    
        
    """
    Training the logistic regression model (model) 
    
    Note that we are building a multi-class or "multinomial" model as we need to classify beyond just binary inputs.
    
    This model uses the SAGA algorithm which works well when the no. of samples is significantly larger than the no. of features
    It is able to finely optimize non-smooth objective functions which is useful when we use the l1-penalty.
    """
    #This model uses the scikit-learn LogisticRegression function 
    model = LogisticRegression(penalty='none', 
                         tol=0.1, 
                         solver='saga',           
                         multi_class='multinomial').fit(X_train_scaled, y_train)
    
    
    """
    Calculating the accuracy  
    """
    #Print a message to let the user know the model is calculating 
    print("Classification is underway. It will just be a few moments")
    
    # Predict the accuracy of the test dataset using the trained model 
    y_pred = model.predict(X_test_scaled)
    
    #Then let the user know what accuracy the model is performing at 
    accuracy_score = accuracy_score(y_test, y_pred)
    print(f"This logistic regression model is classifying with an accuracy of {accuracy_score}.")

    """
    Create a classification report   
    """
    # Create a classification report using metrics from sklearn (make this a dataframe using pandas) 
    cm = pd.DataFrame(metrics.classification_report(y_test, y_pred, output_dict = True))

    # Print the classification report to the terminal
    print(cm)
    
    
    """
    Saving the classification report into the output path   
    """
    
    #We're saving our output path to the output_path directory we created earlier and saving the file as a csv
    output_path = os.path.join("output_path", filename)
    cm.to_csv(output_path, index = False)
    
    #Then print to the terminal that this has been saved
    print("That's you complete - woohoo! The csv file and plots are in output directory.\n ") 
    

#Close your main function 
if __name__=="__main__":
    #execute main function
    main()
