
# Edge Detection
Download and save the image at the link below:

https://upload.wikimedia.org/wikipedia/commons/f/f4/%22We_Hold_These_Truths%22_at_Jefferson_Memorial_IMG_4729.JPG

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

## Recommended edge inputs for ROI of attached image 
x1 = 1400
y1 = 890 

x2 = 2900
y2 = 2800 
    
