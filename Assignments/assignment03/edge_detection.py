#!/usr/bin/env python

"""
Assignment 3: Edge Detection 

Edge detection is the beginning step in teaching computers how to read and interpret image. Using edge detection we can fnd specific information within an image and analyse this. This assignment tests our ability to find and define edges in an image with many engraved letters. The script completes 4 tasks: 

For a given image
  1. Find the ROI on the image and draw a rectangle around it   (save as image_with_ROI.jpg)  
  2. Using this ROI, crop the image to only include the ROI   (save as image_cropped.jpg) 
  3. Use canny edge detection techniques to identify every letter in the image image_letters.jpg) 
  4. Draw green contours around each letter  (save image as  
  
We are using argparse and have 3 input parameters which need defined in the command line:
    image_path: str <path-to-image>
    roi: : x1 y1 x2 y2, the coordinate points defining the top-left and bottom-right corner of ROI (to draw a rectangle) 
    output_path: str <path-to-output-file>
    
Example of command line input:
    edge_detection.py --image_path <path-to-image> --roi x1 y1 x2 y2 --output_path <path-to-output-file>

Output:
    - image_with_ROI.jpg: image from task 1 (ROI identified with a green rectange) 
    - image_cropped.jpg: image from task 2 (the cropped ROI image) 
    - image_letters.jpg: cropped image with contoured letters
    
Worked example of how command line code would look: 
$ python edge_detection.py --image_path ../../data/img/weholdtruths.jpeg --roi 10 10 50 50 --output_path output/
    
    
"""

# import dependencies of script 
#operating systems 
import os
import sys
sys.path.append(os.path.join(".."))

#Image processing 
import cv2
import numpy as np

#display 
from utils.imutils import jimshow
import matplotlib.pyplot as plt
import matplotlib as mpl

#Command line functionality
import argparse


# main function: 
def main():
    
 ##Argparse set-up: this helps us to find the path and image using the command line 
    
    # initialise argparse 
    ap = argparse.ArgumentParser()
    
    # create the input parameters defined above (required = True means user must input these to use script) 
    ap.add_argument("-i", "--image_path", required = True, help = "Path to image")
    ap.add_argument("-r", "--roi", required = True, help = "Points of ROI in image", nargs='+')   #nargs helps control no. inputs
    ap.add_argument("-o", "--output_path", required = True, help = "Path to output directory")
    
    # parse arguments
    args = vars(ap.parse_args())
    
    
 ## Read in the image

    # connect the image_path variable to the defined image path from the command line 
    image_path = args["image_path"]
    
    # read in the image
    image = cv2.imread(image_path)
    
    
 ## Create the output path 
    # if an output path doesn't exist, we need to create one by the following 
    output_path = args["output_path"]   # connecting output_path variable to the command line output path 
    if not os.path.exists(output_path):   #If this output path doesn't exist,
        os.mkdir(output_path)             # Then create one called output_path 
    
 ## Draw the ROI (Task 1) 
    
    # First we connect the ROI variable to the 4 defined numbers in the command line 
    ROI = args["roi"]
    
    # define top left corner using first 2 roi inputs (x1, y1), and bottom right corner using last 2 roi inputs (x2, y2) 
    top_left_corner = (int(ROI[0]), int(ROI[1]))   
    bottom_right_corner = (int(ROI[2]), int(ROI[3]))
    
    # draw a green rectangle as ROI ontop of the image
    ROI_image = cv2.rectangle(image.copy(), top_left_corner, bottom_right_corner, (0,255,0), (2)) #calling the green channel
    
    # save image with ROI
    cv2.imwrite(os.path.join(output_path, "image_with_ROI.jpg"), ROI_image) #Output saved as image_with_ROI.jpg
    
 ## Crop the image to include only the ROI (Task 2) 
    
    # crop image based on roi points (this can be read as cropped image = image[startY:endY, startX:endX] ) 
    cropped_image = image[top_left_corner[1]:bottom_right_corner[1], top_left_corner[0]:bottom_right_corner[0]] 
    
    # save cropped image to the output path 
    cv2.imwrite(os.path.join(output_path, "image_cropped.jpg"), cropped_image)
    
 ## Image Processing - canny edge detection  (Task 3) 
    
    # We blur the image to remove high freq.edges (we'll use gaussian blurring with a (9x9) kernal and 0 for the default sigma) 
    blurred_image = cv2.GaussianBlur(cropped_image, (7,7), 0)
    
    # We then apply thresholding to make the image black & white (this helps to segment foreground and background)
    # This can be read as (cv2.threshold(image, threshold_value, colour, method )) threshold = 110, colour = white (255)
    (_, binary_image) = cv2.threshold(blurred_image, 110, 255, cv2.THRESH_BINARY)
    
    # apply cv2's canny edge detection (We've manually set the parameters) 
    canny_image = cv2.Canny(binary_image, 60, 150)
    
    
    
 ## Draw the contours (Task 4) 
    
    # finding contours
    #This can be read as:  cv2.findContours(image_copy, contour_retrieval_mode, contour_approximation_method)
    (contours, _) = cv2.findContours(canny_image.copy(), 
                                     cv2.RETR_EXTERNAL, 
                                     cv2.CHAIN_APPROX_SIMPLE)
    
    # drawing contours on cropped image with thickness of 2 (using copy of cropped image) 
    letters_image = cv2.drawContours(cropped_image.copy(), contours, -1, (0,255,0), 2)
    
    # Saving the final image 
    cv2.imwrite(os.path.join(output_path, "image_letters.jpg"), letters_image)
    
    #Let the user know it's complete 
    print(f"\nThat's you finishe - woohoo! The images are saved in {output_path}.")
    
# complete the main function script    
if __name__=="__main__":
    main()
