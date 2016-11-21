from PIL import Image
import numpy as np

# Convert PIL image to 200x200 array normalised to -0.5 to 0.5 rage.
def image_2_array(filename):
    # PIL image pil_img
    pil_img=Image.open(filename)
    pil_arr=np.array(pil_img)
    pil_max = np.amax(np.absolute(pil_arr))
    pil_min = np.amin(np.absolute(pil_arr))
    #print ("Max/min:"+ str(pil_max)+"/"+str(pil_min))
    if pil_max == 0:
        return pil_img,pil_arr
    pil_scaled_arr = (pil_arr / pil_max) - 0.5
    return pil_img, pil_scaled_arr

# Invert normalised PIL image
def invert_array(arr):
    #print(arr.shape)
    #print(arr[100][50:60])
    inverted_arr = arr * (-1)
    #print(inverted_arr[100][50:60])
    return inverted_arr
    
# Convert normalized array to PIL image
def array_2_image(arr):
    MAX = 255
    arr_scaled = (arr + 0.5) * MAX
    arr_max = np.amax(arr_scaled)
    arr_min = np.amin(arr_scaled)
    #print ("Array Max/min:"+ str(arr_max)+"/"+str(arr_min))
    im = Image.fromarray(arr_scaled)
    return im