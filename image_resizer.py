
# Image Resizer
#
# Written by Vinay Williams
#
# Copyright 2016-2022 Vinay Williams
#
# All Rights Reserved by Vinay Williams including but not limited to redistribution, modification and resale. If use of this code is made please acknowledge the author's contribution. A general citation is Williams, V. (2016) Image Resizer Source Code (Version *Insert Version Number here* [Source Code].) 
#
# Started: 12th October 2016
#
# Purpose: Script to resize images which can be standalone or be repurposed in other code
#
# Changelog: 
#           v1.0.0 27th November 2016  : Add the plot capability to compare original and resized images
#           v1.0.1 13th August 2018    : Added ability to save images after processing
#           v1.0.2 30th February 2021  : Added ability to pick files and locations
#           v1.0.3 13th July 2022      : Added text to main function to be easier to use
#
# Functionality:
#   
#   Inputs:
#       imgs    - Either a list of images, list of paths of images or keyword "pick". Entering the keyword will open a file dialog to pick images
#       beight  - Height to resize images to 
#       width   - Width to resize images to
#       save    - Boolean flag to indicate whether to save images
#       plot    - Boolean flag to indicate whether to plot images. Note when the images are shown, press any key to close them
#
#   Outputs:
#       There are 2 possible outputs depending on the state of the save argument
#       
#       save = True     - Returns the path where the images were saved
#       save = False    - Returns a list which contains the images
#
# Functionality to be added:
#
#   - Move save argument to be either a boolean or string where the string can be a path to save to
#   - Add ability to change interpolation method
#   - Readd ability to save images with a modified original name when paths to the originals are passed in 

import cv2

def image_resizer(imgs, height, width, save = False, plot = False):
    
    if imgs == "pick":
        from tkinter import filedialog as fd
        from tkinter import Tk
        root = Tk()
        root.withdraw()
        imgs = fd.askopenfilenames()
   
    resized_imgs = [] 

    if isinstance(imgs[0], str):
        imgs2 = []
        for i in range(0,len(imgs)):
            imgs2.append(cv2.imread(imgs[i]))
        imgs = imgs2 
        del imgs2

    for img in imgs:
        image_resized = cv2.resize(img, (int(width), int(height)), interpolation= cv2.INTER_LINEAR)
        
        if plot == True:
            cv2.imshow("Original", image)
            cv2.imshow("Resized", image_resized)
            cv2.waitKey(0)
        
        resized_imgs.append(image_resized)

    if save == True:
        from tkinter import filedialog as fd 
        import os

        save_path = fd.askdirectory()
        os.chdir(save_path)

        for i in range(0,len(imgs)):
            #try:
            #    filename = os.path.splitext(os.path.basename(imgs[i]))[0]+"_resized_"+str(width)+"_"+str(height)+".png"
            #except
            #    filename = "Resized Image_"+str(i+1) +str(width)+"_"+str(height)+".png"
            filename = "Resized Image_"+str(i+1)+str(width)+"_"+str(height)+".png"
            cv2.imwrite(filename, resized_imgs[i])
        return save_path

    else:
        return resized_imgs

if __name__ == "__main__":
    print("Image Resizer\n\nRunning in file picker and saving mode\n")
    height = input("Resized height: ")
    width = input("\nResized width: ")
    print("\nResized file(s) located at: " + image_resizer("pick", height, width, save = True, plot = False))
    
