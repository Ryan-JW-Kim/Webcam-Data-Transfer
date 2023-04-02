from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import time


class FourPoints:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.x_same = x1 == x2
        self.y_same = y1 == y2

        self.zero_size = self.x_same or self.y_same

    def __str__(self) -> str:
        return(f"X1:{self.x1} X2:{self.x2} - Y1:{self.y1} Y2:{self.y2}  --  X:{self.x_same}  Y:{self.y_same}")
    
    def split_image(self, image_obj):
        return image_obj[int(self.x1): int(self.x2)][int(self.y1): int(self.y2)]


class Display:
    def __init__(self, path, as_pixels=False):
        self.path = path

        if as_pixels:
            self.mode = "Pixel Grid"
            self.y_groups = 5
            self.x_groups = 40

    def sub_image_size(self, width, height):

        while (width/self.x_groups) % 1 != 0.0:
            self.x_groups += 1
        
        while (height/self.y_groups) % 1 != 0.0:
            self.y_groups += 1

        myDict = {"Number of x groups": self.x_groups,
                  "Number of y groups": self.y_groups,
                  "Pixels per x group": width/self.x_groups,
                  "Pixels per y group": height/self.y_groups,
                  "Number of groups in image": self.x_groups * self.y_groups,
                  "Width": width,
                  "Height": height}
        
        return myDict

    def pixel_grid_generator(self):
        pass

    def launch(self):
        pass

    def test(self):
        testImage = img.imread(self.path)
        y, x, z = testImage.shape  
        dimension_dict = self.sub_image_size(x, y)
        x1, x2 = 0, None
        y1, y2 = 0, None

        sub_sections = []

        for _ in range(dimension_dict["Number of x groups"]):

            if x2 is None:
                x2 = dimension_dict["Pixels per x group"]
            
            else:
                x1 = x2
                x2 += dimension_dict["Pixels per x group"]

            for _ in range(dimension_dict["Number of y groups"]):
                if y2 is None:
                    y2 = dimension_dict["Pixels per y group"]
                
                else:
                    if y2 == dimension_dict["Height"]:
                        y1 = 0
                        y2 = dimension_dict["Pixels per y group"]
                    
                    else:
                        y1 = y2
                        y2 += dimension_dict["Pixels per y group"]
                
                obj = FourPoints(x1, x2, y1, y2)
                sub_sections.append(obj)
        
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)

        loaded = False
        for obj in sub_sections:
            if not obj.zero_size:
                sub = obj.split_image(testImage)
                if not loaded:
                    
                    # plt.imshow(sub)      
                    loaded = True

                else:
                    plt.set

        plt.show()    