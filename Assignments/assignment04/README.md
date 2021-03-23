
## Assignment 4: Classification Benchmarks


**Using Logistic Regression and a Neural Network**

This assignment takes the form of 2 python scripts which should be called dirctly from the commandline. The data used is the MNIST data found on openml. 
This is a subset of the larger NIST file which contains 60,000 images of handwritten digits with 784 features. 
Information regarding this dataset can be found here: https://www.openml.org/d/554

Please note that the second script has been ammended to run on the digits dataset from sklearn to enable more user friendly computational times. 


__The Scripts and Data__ 

**lr-mnist.py**  This script uses multinomial logistic regression to classify images of handwritten digits into their correct digit group (0:9)


**nn-mnist.py**  This script employs a neural network to classify the same images of handwritten digits into their correct digit group (0:9)


The script pulls data from open online sources and so no additional data needs to be added into the script. 

Parameters can be set on the commandline using argpase arguments. Instructions of these can be found on each of these below. 

__Operating the scripts__

There are 3 steps to take to get your script up and running: 
Step 1: Clone the repository
Step 2: Create a virtual environment (cv101) 
Step 3: Run the 2 scripts using command line parameters 

(Output will be saved in a new folder called output_path


__1. Clone the repository__ 

The easiest way to access the files is to clone the repository from your commend line and move into Assignment04 as outlined below 

```bash
#clone repository into cds-visual-orlz
git clone https://github.com/Orlz/CDS_Visual_Analytics.git cds-visual-orlz

#Move into the correct file 
cd cds-visual-orlz/Assignments/assignment04
```

__2. Create the virtual environment__

You'll need to create a virtual environment which will allow you to run the script. This will require the requirements.txt file above 
To create the virtual environment you'll need to open your terminal and type the following code: 

```bash
bash create_vision_venv.sh
```
And then activate the environment by typing: 
```bash
$ source cv101/bin/activate
```


__3. Run the Script__

You have 2 scripts to run. Both contain some required and optional parameters to define. There are: 

Required: 
-s --split  This is the test split size. It should be a decimal between 0 - 1  (required for both scripts) 

_Optional for logistic regression model (lr-mnist.py)_
-f --filename   You are free to assign a filename to your output report. The default is "logistic_regression_report.csv"
-o --output_path   You are free to determine a new output location for your file. The default is called output_path 

_Optional for neural network model (nn-mnist.py)_
-f --filename       You are free to assign a filename to your output report. The default is "neural_network_report.csv"
-o --output_path    You are free to determine a new output location for your file. The default is called output_path
-l --layers         You can determine how many hidden layers your network will have. This is an integer number between 1:3. The default is set at 2. 
-e --epochs         You can change the number of epochs the network runs with. The default is set to 1000.  


Below is an example of the command line arguments for the logistic regression model with an 80:20 split: 

```bash
python3 lr-mnist.py -s 0.2 
```






