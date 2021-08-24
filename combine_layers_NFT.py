# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:51:06 2021

Author: @BlockBirdsNFT 
ETH wallet address: 0xEac00b45c7BB954D34DB75Ada1CC28aED5A53Efc

(modified from original BlockBirds script for images instead of gifs)
"""

from PIL import Image
import glob
import itertools


#this script works with pngs; layers (except for the background) should have transparency, 
#otherwise all images will stack over each other and only the last will show at the end

#"!!!" signals parts you should adjust to your own needs

#organizing your working directory:
    #each layer should be represented as a folder named "layer[number]-", starting from 0
    #within each layer folder, put all corresponding traits named "design[number].png", starting from 1

#!!! replace with the absolute path to your working directory (don't forget the final "/")
path = "C:/Users/user/Desktop/localwhaler/" #this is an example

#All good? Let's fooking do it!

#RUN THIS SECTION FIRST TO SEE THE AMOUNT OF IMAGES YOU'D GET WITH 
#THE AMOUNT OF LAYERS AND TRAITS YOU HAVE !!
#(if they are a lot (not hard getting to millions...), you might wanna remove some traits or layers)
#modify what you need first!

#---------------------------------------------------------------------------------

#this part lists all traits on each layer
leest=[]
for name in glob.glob(path+"layer*-/design*"):
    leest.append(name.partition("\\")[2])

#!!!...continue adding layers as as you wish, just keep adding numbers
layer0=[s for s in leest if "layer0" in str(s)]
layer0 = [sub.replace('layer0-\\', '') for sub in layer0] #background in example
layer1=[s for s in leest if "layer1" in str(s)]
layer1 = [sub.replace('layer1-\\', '') for sub in layer1] #head in example
layer2=[s for s in leest if "layer2" in str(s)]
layer2 = [sub.replace('layer2-\\', '') for sub in layer2] #eyes in example
#layer3=[s for s in leest if "layer3" in str(s)]
#layer3 = [sub.replace('layer3-\\', '') for sub in layer3] ... etc


#this part calculates the amount of results you'd get
combinations=list(itertools.product(layer0, layer1, layer2)) #!!! add all layers you'll use
print("You'll get "+str(len(combinations))+ " unique images")

#---------------------------------------------------------------------------------

#IF YOU'RE HAPPY WITH THE AMOUNT OF IMAGES EXPECTED, RUN THE FOLLOWING SECTION
#modify what you need first!

#this part composes and saves final images
for ele in range(len(combinations)):
    #!!!...continue adding layers as you wish. be sure to match the 
    #number of layer with "im" object and the number between brackets
    im0 = Image.open(path + "layer0-/"+combinations[ele][0])
    im1 = Image.open(path + "layer1-/"+combinations[ele][1])
    im2 = Image.open(path + "layer2-/"+combinations[ele][2])
    #im3 = Image.open(path + "layer3-/"+combinations[ele][3]) ... etc
    
    var = [im1, im2] #!!! add all layers you used, except for 0 
    for x in var:
        im0.alpha_composite(x) 
    im0.save(path+"finals"+str(ele)+".png")
    
#END (now you gotta manually select the final images you want FACK)