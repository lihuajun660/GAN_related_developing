import random
import numpy as np
from matplotlib import pyplot as plt

def create_new_fake_image(height = 1100, width = 1376, times = 0):
    img = np.zeros((height, width, 3),np.uint8)
    parti_num = random.randrange(25,45) 
    dpi = 96
    figsize = width / float(dpi), height / float(dpi)
    
    # Make some example data
    x = np.random.rand(parti_num)*width
    y = np.random.rand(parti_num)*height
    # Create a figure. Equal aspect so circles look circular
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    # Show the image
    ax.imshow(img, interpolation='nearest')

    # Now, loop through coord arrays, and create a circle at each x,y pair
    for xx,yy in zip(x,y):
        radius = random.uniform(2, 110)
        circ = plt.Circle((xx,yy),radius, color='white', fill=False)
        ax.add_patch(circ)    
    plt.xticks([]), plt.yticks([])
    plt.savefig(r"D:\huajun\Created_images\00"+ str(times) + ".png", dpi = dpi)
    # Show the image
    plt.close()
    
def loop(nums, h, w):
    for i in range(nums):
        create_new_fake_image(h, w, i)
    
if __name__ == "__main__":
    nums_of_images = 50
    height = 1100
    width = 1376
    loop(nums_of_images, height, width)
    
