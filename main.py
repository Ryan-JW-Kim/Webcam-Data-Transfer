import matplotlib.pyplot as plt
from analysis import Analysis
from display import Display
from reader import Reader
import threading


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()

if __name__ != "__main__":

    analytics = Analysis()
    analytics.start_time()

    path_to_image = "dog.jpg"
    
    # Create Display Image object
    display = Display(path_to_image, as_pixels=True)

    # Created Read Image object
    # reader = Reader()

    # Launch Reader thread
    # read_thread = threading.Thread(target=reader.launch)
    # read_thread.start()

    # Launch Display thread
    # display_thread = threading.Thread(target=display.launch)
    # display_thread.start()
    # display.launch()
    obj = display.test()
    plt.imshow(obj)

    # Wait till threads successfull execute
    # read_thread.join()
    # display_thread.join()
    analytics.end_time()

    # Display Reader Output
    # reader.display_result()

    # Print input/output comparision
    analytics.report()
