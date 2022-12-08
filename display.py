from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img

class Display:
    def __init__(self, path, as_pixels=False):
        self.path = path

        if as_pixels:
            self.mode = "Pixel Grid"
            self.grid_size = (5,5) # Width, Height ratio per frame

    def pixel_grid_generator(self):

        im = img.imread(self.path)
        # pixels = list(img.getdata())
        # width, height = img.size

        yield im

    def launch(self):
        
        # fig = plt.figure()
        # ax = fig.add_subplot(111)
        # plt.ion()
        # plt.show()

        if self.mode == "Pixel Grid":
            for frame in self.pixel_grid_generator():
                # img = ax.imshow(frame)
                # plt.draw()
                plt.imshow(frame)
    
    def test(self):
        testImage = img.imread(self.path)
        return testImage