from PIL import ImageGrab, ImageOps 
import pyautogui as py 
import numpy as np

def pressSpace():
    py.press("space")
#    py.keyUp("space")
    
def img():
#    box = (420,330, 450,332)
    box = (100,330, 170,332)
    image = ImageGrab.grab(box)
    image=ImageOps.grayscale(image)
    arr = np.array(image.getcolors())
#    print(arr[0])
    return(arr[0][1])
#    
def main():
    print("starting game")
    x=0
    while(1):
        if(img() != 247):
            pressSpace()
            x = x+1 
            print("---Jumping"+str(x)+"times")
                                
main()  
