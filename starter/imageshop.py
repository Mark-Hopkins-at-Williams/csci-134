from imageutil import read_image, read_image_as_grayscale, show_image


def letter_t():
    """Creates a small 5x5 black-and-white image of the letter T."""
    return [[255, 255, 255, 255, 255],
            [0, 0, 255, 0, 0],
            [0, 0, 255, 0, 0],
            [0, 0, 255, 0, 0],
            [0, 0, 255, 0, 0]]


def letter_c():
    """Creates a small 5x5 black-and-white image of the letter C."""
    return [[0, 255, 255, 255, 0],
            [255, 0, 0, 0, 255],
            [255, 0, 0, 0, 0],
            [255, 0, 0, 0, 255],
            [0, 255, 255, 255, 0]]


def green_c_on_red():
    """Creates a small 5x5 color image of a green C on a red background."""
    return [[[255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]],
            [[0, 255, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]],
            [[0, 255, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]],
            [[0, 255, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]],
            [[255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]]]


def williams_w():
    """Creates a small 5x5 color image of a purple W on a yellow background."""
    return [[[100, 0, 100], [180, 180, 0], [180, 180, 0], [180, 180, 0], [100, 0, 100]],
            [[100, 0, 100], [180, 180, 0], [100, 0, 100], [180, 180, 0], [100, 0, 100]],
            [[100, 0, 100], [180, 180, 0], [100, 0, 100], [180, 180, 0], [100, 0, 100]],
            [[100, 0, 100], [100, 0, 100], [100, 0, 100], [100, 0, 100], [100, 0, 100]],
            [[180, 180, 0], [100, 0, 100], [180, 180, 0], [100, 0, 100], [180, 180, 0]]]


def zeros(num_rows, num_cols):
    """
    Creates an all-black image with a specified number of rows and columns.
    In other words, this function creates a list of R lists, where R = num_rows. 
    Each sublist is a list of C zeros, where C = num_cols.
    
    >>> zeros(2, 3)
    [[0, 0, 0], [0, 0, 0]]
    >>> zeros(4, 2)
    [[0, 0], [0, 0], [0, 0], [0, 0]]
    """
    pass

def flip_horizontal(image):
    """
    Creates a new image corresponding to the original image, flipped 
    horizontally. This function should not modify the original image.
    
    >>> flip_horizontal([[1, 2, 3], [4, 5, 6]])
    [[3, 2, 1], [6, 5, 4]]

    >>> flip_horizontal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9]]
    """    
    pass


def flip_vertical(image):
    """
    Creates a new image corresponding to the original image, flipped 
    vertically. This function should not modify the original image.
    
    >>> flip_vertical([[1, 2, 3], [4, 5, 6]])
    [[4, 5, 6], [1, 2, 3]]
    >>> flip_vertical([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[9, 10, 11, 12], [5, 6, 7, 8], [1, 2, 3, 4]]
    """
    pass


def rotate_left(image):
    """
    Creates a new image corresponding to the original image, rotated 
    90 degrees left (counterclockwise). This function should not modify 
    the original image.
    
    >>> rotate_left([[1, 2, 3], [4, 5, 6]])
    [[3, 6], [2, 5], [1, 4]]
    >>> rotate_left([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[4, 8, 12], [3, 7, 11], [2, 6, 10], [1, 5, 9]]
    """
    pass


def green_screen(background, foreground):
    """
    Implements the "green screen" operation.

    To resulting image should be a new image with the same dimensions as 
    the background image. In order to create it, you need to go through the 
    pixels of the background and foreground images in parallel. If the 
    foreground pixel at a particular grid location is green (check this by 
    establishing whether the pixel's greenness is greater than 2 * its redness 
    and also greater than 2 * its blueness), then use the value of the 
    background pixel in the new image. Otherwise, use the value of the 
    foreground pixel.

    Note: The background and foreground images might not be same size. 
    Since the resulting image has the same dimensions as the background
    image, just use the value of the background pixel whenever there isn't
    a corresponding foreground pixel.
    
    >>> green_screen([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], [[[5, 12, 5], [5, 12, 10]], [[10, 12, 5], [4, 9, 4]]])
    [[[1, 2, 3], [5, 12, 10]], [[10, 12, 5], [10, 11, 12]]]

    Your extra doctests here
    """    
    rows = []
    for row in range(len(background)):
        new_row = []
        for col in range(len(background[0])):            
            if row < len(foreground) and col < len(foreground[0]):
                red, green, blue = foreground[row][col]
                if green > 2 * red and green > 2*blue:
                    new_row = new_row + [background[row][col]]
                else:
                    new_row = new_row + [foreground[row][col]]
            else:
                new_row = new_row + [background[row][col]]
        rows = rows + [new_row]
    pass

def convolve(image, kernel):
    """
    Convolves an image with a kernel (optional extension). This function should 
    return a new image that corresponds to the original image convolved using
    the specified weights (see the definition of convolution in the problem
    assignment). If the original image has dimension MxN, then the returned image
    should have dimension (M-2)x(N-2), because the pixels on the boundary of the
    original image do not have eight neighbors and thus cannot be processed.    

    >>> convolve([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    [[3480, 3930], [5280, 5730]]

    >>> convolve([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[0, 0, 0], [0, 2, 0], [0, 0, 0]])
    [[12, 14], [20, 22]]

    Your extra doctests here
    """
    pass
