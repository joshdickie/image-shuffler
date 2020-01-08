import random, string, os, math
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image

#window
root = Tk()
root.title("Random Image Grid Generator")
root.resizable(0, 0)


#################################### VARS ####################################
dir_path = os.path.dirname(os.path.realpath(__file__))
text_intro = ("This program takes a number of images of two distinct types, "
              "and randomly arranges a selection of them in a grid. Please "
              "ensure that the input images are placed in the appropriate "
              "folder, are named appropriately, and are the same size.")
text_matrix_number = "Number of matrices:"
text_image_type_a = "Number of images of type a to be selected:"
text_image_type_b = "Number of images of type b to be selected:"
images_a = [] #list of image type a paths
images_b = [] #list of image type b paths
images_total = [] #combined list of paths
padding = 10 #space between images on grid
image_x = 0 #how many pixels wide the images are
image_y = 0 #how many pixels high the images are
matrix_x_pix = 0 #how many pixels wide the matrix is
matrix_y_pix = 0 #how many pixels high the matrix is
matrix_x = 0 #how many images wide the matrix is
matrix_y = 0 #how many images high the matrix is

#Tkinter objects
number_of_matrices = StringVar()
number_of_images_a = StringVar()
number_of_images_b = StringVar()


################################### FUNCTS ###################################
def main():
    """
        generates a number (determined by the user) of randomized image
        matrices (of size determined by the user), and saves them to
        an "output" folder.
    """
    global matrix_x, matrix_y
    if inputs_valid():
        if number_of_images_b.get() != "": #check if images_b empty
            matrix_size = (int(number_of_images_a.get()) +
                           int(number_of_images_b.get()))
        else:
            matrix_size = int(number_of_images_a.get())

        size_prime, matrix_x, matrix_y = square_distribution(matrix_size)

        if size_prime:
            messagebox.showwarning("Grid can not be constructed", (
                                   "Error: grid of requested size can not be"
                                   "constructed (type a + type b is prime)"))
        else:
            generate_image_matrices()
            messagebox.showinfo("","done.")


def inputs_valid():
    """
        checks that all inputs are valid, including:
            - user entries
            - images
    """
    if entries_valid() and number_of_images_valid():
        return True
    else:
        return False


def entries_valid():
    """
        verifies that user iput is valid for:
            - Matrix size (x and y)
            - Number of matrices
    """
    if ((number_of_matrices.get()).isdigit() and
        (number_of_images_a.get()).isdigit() and
        ((number_of_images_b.get()).isdigit() or
         (number_of_images_b.get() is ""))):
            return True
    else:
        messagebox.showwarning("Invalid entries", (
                               "All input values must be "
                               "non-negative integers."))
        return False


def number_of_images_valid():
    """
        verifies that the number of images in the "type a" input folder is
        greater than or equal to number_of_images_a. Does the same for
        type b.
    """
    if number_of_images_a_valid() and number_of_images_b_valid():
        return True
    else:
        return False


def number_of_images_a_valid():
    """
        verifies that the number of images in the "type a" input folder is
        greater than or equal to number_of_images_a.
    """
    counter = 0
    with os.scandir(os.path.join(dir_path, "inputs", "type_a")) as filepaths:
        for path in filepaths:
            extension = os.path.splitext(path)[1].lower()
            if extension == ".png" or extension == ".jpg":
                counter += 1
    if counter >= int(number_of_images_a.get()):
        return True
    else:
        messagebox.showwarning("Invalid Image Inputs", (
                               "Not enough images of type a to create "
                               "requested grid."))
        return False


def number_of_images_b_valid():
    """
        verifies that the number of images in the "type b" input folder is
        greater than or equal to number_of_images_b.
    """
    counter = 0
    with os.scandir(os.path.join(dir_path, "inputs", "type_b")) as filepaths:
        for path in filepaths:
            extension = os.path.splitext(path)[1].lower()
            if extension == ".png" or extension == ".jpg":
                counter += 1
    if ((number_of_images_b.get() == "") or
        (counter >= int(number_of_images_b.get()))):
        return True
    else:
        messagebox.showwarning("Invalid Image Inputs", (
                               "Not enough images of type b to create "
                               "requested grid."))
        return False


def square_distribution(size):
    """
        Determines the "most square" x and y values which will make a grid of
        the specified size.

        args:
            size       - the size of the grid (int)

        returns:
            size_prime - True if size is prime (bool)
            x          - the x value of the most square distribution (int)
            y          - the y value of the most square distribution (int)
    """
    x = math.ceil(math.sqrt(size))
    while x < size:
        if size % x != 0:
            x += 1
        else:
            break
    y = size//x
    if x == size:
        size_prime = True
    else:
        size_prime = False
    return (size_prime, x, y)


def generate_image_matrices():
    """
        generates and saves the specified number of matrices, using the
        given input data.
    """
    for i in range(int(number_of_matrices.get())):
        clear_space()
        populate_image_lists()
        randomly_select_images()
        get_image_data()
        grid_frame = Image.new("RGB", (matrix_x_pix, matrix_y_pix), "white")
        image_index = 0
        for j in range(matrix_x):
            for k in range(matrix_y):
                img = Image.open(images_total[image_index])
                grid_frame.paste(img, (padding + (j * (padding + image_x)),
                                       padding + (k * (padding + image_y))))
                image_index += 1

        save_path = (os.path.join(dir_path, "outputs\\") +
                     number_of_images_a.get() + "a" +
                     number_of_images_b.get() + "b_img" + str(i) + ".png")
        grid_frame.save(save_path, "PNG")


def clear_space():
    """
        clears the workspace for a new run
    """
    global images_a, images_b, images_total
    images_a = []
    images_b = []
    images_total = []


def populate_image_lists():
    """
        populates images_a and images_b with the appropriate paths.
    """
    with os.scandir(os.path.join(dir_path, "inputs", "type_a")) as filepaths:
        for path in filepaths:
            extension = os.path.splitext(path)[1].lower()
            if extension == ".png" or extension == ".jpg":
                images_a.append(path.path)
    with os.scandir(os.path.join(dir_path, "inputs", "type_b")) as filepaths:
        for path in filepaths:
            extension = os.path.splitext(path)[1].lower()
            if extension == ".png" or extension == ".jpg":
                images_b.append(path.path)


def randomly_select_images():
    """
        combines images_a and images_b by randomly selecting the images    which
        will be used to generate the image grid, then shuffling the combined
        list.
    """
    global images_a, images_b, images_total
    images_a = random.sample(images_a, int(number_of_images_a.get()))
    if number_of_images_b.get() != "": #check if images_b empty
        images_b = random.sample(images_b, int(number_of_images_b.get()))
    else:
        images_b = []
    images_total = images_a + images_b
    random.shuffle(images_total)


def get_image_data():
    """
        gets relevant image data:
            - size (width and height) of images
            - size (width and height) of the grid
    """
    global image_x, image_y, matrix_x_pix, matrix_y_pix
    image_x, image_y = Image.open(images_total[0]).size
    matrix_x_pix = (matrix_x*image_x) + ((matrix_x + 1) * padding)
    matrix_y_pix = (matrix_y*image_y) + ((matrix_y + 1) * padding)


################################## GUI STUFF #################################

#Widgets
frame_intro = ttk.Frame(root, padding = 5, borderwidth = 2, relief = SUNKEN)
frame_inputs = ttk.Frame(root)
label_intro = ttk.Label(frame_intro, text = text_intro, justify = CENTER, wraplength = 450)
label_matrix_number = ttk.Label(frame_inputs, text = text_matrix_number, justify = RIGHT)
label_image_type_a = ttk.Label(frame_inputs, text = text_image_type_a, justify = RIGHT)
label_image_type_b = ttk.Label(frame_inputs, text = text_image_type_b, justify = RIGHT)
entry_matrix_number = ttk.Entry(frame_inputs, textvariable = number_of_matrices, width = 4)
entry_image_type_a = ttk.Entry(frame_inputs, textvariable = number_of_images_a, width = 4)
entry_image_type_b = ttk.Entry(frame_inputs, textvariable = number_of_images_b, width = 4)
button_go = ttk.Button(frame_inputs, text = "Go", command = main)

#Placement
frame_intro.grid(column = 1, row = 1, sticky = (N, S, E, W))
frame_inputs.grid(column = 1, row = 2, sticky = (N, S, E, W))
label_intro.grid(column = 1, row = 1, columnspan = 4, sticky = (N, S, E, W))
label_matrix_number.grid(column = 1, row = 3, sticky = E)
label_image_type_a.grid(column = 1, row = 4, sticky = E)
label_image_type_b.grid(column = 1, row = 5, sticky = E)
entry_matrix_number.grid(column = 2, row = 3)
entry_image_type_a.grid(column = 2, row = 4)
entry_image_type_b.grid(column = 2, row = 5)
button_go.grid(column = 5, row = 6)

#Main Loop
root.mainloop()
