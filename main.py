from PIL import Image


def string_to_ascii(message: str) -> list:
    """
    Converts a string to a list of numbers corresponding to the ASCII table
    message: message to convert
    output: ascii_list: list of ints corresponding to each letter of the message in ASCII
    """
    ascii_list = []
    for character in message:
        ascii_list.append(ord(character))

    return ascii_list


def ascii_to_binary(ascii_message: list) -> list:
    """
    Converts a list of ASCII values to a list of binary strings
    ascii_message: list of numbers corresponding to a message in ASCII
    output: binary: list of binary strings
    """
    binary = []
    for line in ascii_message:
        binary.append(str(bin(line)))

    return binary


def ascii_to_string(ascii_message: list) -> str:
    """
    Input: a list containing each letter in ASCII
    Output: a string containing the message translated using the ASCII table
    """
    message = ""

    for i in ascii_message:
        message += chr(i)

    return message


def binstr_to_ascii(binary_message: list) -> list:
    """
    Input: a list containing each letter in binary
    Output: a list containing the message translated to ASCII
    """
    ascii_list = []
    for i in binary_message:
        ascii_list.append(int(i, 2))

    return ascii_list


def encode_special_characters(text: str) -> str:
    """
    Input: the message with accented characters
    Output: the same message but with codes instead of special characters
    """
    text = text.replace("é", "ecute")
    text = text.replace("è", "egrave")
    text = text.replace("ç", "ccedilla")
    text = text.replace("@", "arobase")
    text = text.replace("à", "agrave")
    text = text.replace("ê", "echapo")
    text = text.replace("â", "achapo")
    text = text.replace("î", "ichapo")
    text = text.replace("ô", "ochapo")
    return text


def decode_special_characters(text: str) -> str:
    """
    Input: the message with codes instead of special characters
    Output: the original message with special characters instead of character codes
    """
    text = text.replace("ecute", "é")
    text = text.replace("egrave", "è")
    text = text.replace("ccedilla", "ç")
    text = text.replace("arobase", "@")
    text = text.replace("agrave", "à")
    text = text.replace("echapo", "ê")
    text = text.replace("achapo", "â")
    text = text.replace("ichapo", "î")
    text = text.replace("ochapo", "ô")
    return text


# Shortcuts
def get_pixel_value(image, coord_x, coord_y) -> tuple:
    """
    Get the color of a pixel in an image (r, g, b)
    image: the image to modify
    coord_x: x coordinate of the pixel to modify
    coord_y: y coordinate of the pixel to modify
    output: returns a tuple (red, green, blue) of ASCII color values
    """
    red, green, blue, _ = image.getpixel((coord_x, coord_y))
    return red, green, blue


def to_nine_bits(binary_message: list) -> str:
    """
    Input: a list of strings containing the message in binary with different sizes
    Output: a string containing the entire message in binary with all characters expressed in 9 bits
    """
    for i in binary_message:  # Make all characters the same number of bits
        if len(i) != 9:
            a = i.zfill(9)
            binary_message[binary_message.index(i)] = a

    msg_bin = "".join(
        [str(k) for k in binary_message])  # Transform the list containing the different characters into a string
    msg_bin = msg_bin.replace("b", "0")  # Replace the default Python identifier with a 0
    return msg_bin


def change_pixel_value(image: Image.Image, coord_x: int, coord_y: int, red: int, green: int, blue: int) -> None:
    """
    Change the color of a pixel in an image
    image: the image to modify
    coord_x: x coordinate of the pixel to modify
    coord_y: y coordinate of the pixel to modify
    red: red value from 0 to 255 of the pixel to modify
    green: green value from 0 to 255 of the pixel to modify
    blue: blue value from 0 to 255 of the pixel to modify
    output: None
    """
    image.putpixel((coord_x, coord_y), (red, green, blue))
    return None


def encrypt(text: str, image: Image.Image) -> Image.Image:
    """
    Input: the text to steganograph and the image in which to steganograph the message
    Output: the image with the message and the size of the message steganographed
    Calls other functions to perform the necessary sequence of operations
    """
    text = encode_special_characters(text)
    ascii_message = string_to_ascii(text)
    binary_message = ascii_to_binary(ascii_message)
    msg_bin = to_nine_bits(binary_message)
    image = steganograph_size(image, msg_bin)

    if image is None:
        return None

    return steganograph(image, msg_bin)


def decrypt(image: Image.Image) -> str:
    """
    Input: the image with a steganographed code
    Output: the steganographed message in the image
    Calls other functions to perform the necessary sequence of operations
    """
    msg_len = desteganograph_size(image)
    message = desteganograph(image, msg_len)
    message = decode_special_characters(message)
    return message


# Verification (removable)
def verify_image_size(image: Image.Image, message_size: int) -> bool:
    """
    Verify that the message can fit in the image
    image: image to verify
    message_size: size of the message to verify
    output: boolean
            true: the message fits in the image
            false: the message does not fit in the image
    """

    width, height = image.size  # size of the image

    return message_size < width * height - width - 1


def steganograph_size(image, msg_bin: list):
    """
    Input: the image in which to include the size of the message and the message whose size to determine
    Output: the image with the size of the message steganographed on the first line
    Determine the size of the message and then write it in binary in the last values of the colors of each pixel
    """
    width, _ = image.size
    x, y, place = 0, 0, 0  # coordinates of the pixel x, y
    size = len(msg_bin)
    if verify_image_size(image, size) is False:
        print("error the given image is too small to include the given message")
        return None
    size = bin(size).replace("b", "0")
    size = size.zfill(width * 3)

    for _ in range(int(len(size) / 3)):
        # Get the color values of the pixel
        red, green, blue, _ = image.getpixel((x, y))
        # Transform the color values to binary to process them
        red, green, blue = bin(red), bin(green), bin(blue)

        red_list = [j for j in red]  # put in list to modify
        red_list[-1] = size[place]  # Apply modifications
        # Transform back to string
        red = "".join([str(k) for k in red_list])
        place += 1

        green_list = [j for j in green]  # put in list to modify
        green_list[-1] = size[place]  # Apply modifications
        # Transform back to string
        green = "".join([str(k) for k in green_list])
        place += 1

        blue_list = [j for j in blue]  # put in list to modify
        blue_list[-1] = size[place]  # Apply modifications
        # Transform back to string
        blue = "".join([str(k) for k in blue_list])
        place += 1

        red, green, blue = int(red, 2), int(green, 2), int(blue, 2)
        change_pixel_value(image, x, y, red, green, blue)
        x += 1

    return image


def desteganograph_size(image: Image.Image) -> int:
    """
    Decrypt the size of the message in an image
    image: image to decrypt
    output: size of the message in int
    """
    val = ""
    for x in range(image.size[0]):  # coordinates of the pixel x
        r, g, b = get_pixel_value(image, x, 0)  # red, green, blue ASCII values ranging from 0 to 255
        color_binary = ascii_to_binary([r, g, b])  # red, green, blue values in binary
        for color in color_binary:
            val += color[-1]  # get the last bit of the color
    message_size = int(val, 2)  # transform the binary message size to int
    return message_size // 3


# Steganography
def steganograph(image: Image.Image, msg_bin: list):
    """
    Input: the image in which to include the message and the message to include
    Output: the image with the message steganographed starting from the second line
    Write the message in binary in the last values of the colors of each pixel
    """
    width, height = image.size
    x, y, place = 0, 1, 0  # coordinates of the pixel x, y

    for _ in range(int(len(msg_bin) / 3)):
        # Get the color values of the pixel
        red, green, blue, _ = image.getpixel((x, y))
        # Transform the color values to binary to process them
        red, green, blue = bin(red), bin(green), bin(blue)

        red_list = [j for j in red]  # put in list to modify
        red_list[-1] = msg_bin[place]  # Apply modifications
        # Transform back to string
        red = "".join([str(k) for k in red_list])
        place += 1

        green_list = [j for j in green]  # put in list to modify
        green_list[-1] = msg_bin[place]  # Apply modifications
        # Transform back to string
        green = "".join([str(k) for k in green_list])
        place += 1

        blue_list = [j for j in blue]  # put in list to modify
        blue_list[-1] = msg_bin[place]  # Apply modifications
        # Transform back to string
        blue = "".join([str(k) for k in blue_list])
        place += 1

        red, green, blue = int(red, 2), int(green, 2), int(blue, 2)
        change_pixel_value(image, x, y, red, green, blue)
        x += 1
        if x == width - 1:
            y += 1
            x = 0
            if y == height - 1:
                break

    return image


def desteganograph(image: Image.Image, message_size: int) -> str:
    """
    Decrypt the message in an image
    image: image to decrypt
    message_size: size of the message to decrypt
    output: message in str
    """
    w, h = image.size
    bits_per_letter = 9  # number of bits per character
    x = 0  # coordinates of the pixel x
    y = 1  # coordinates of the pixel y
    bit_array = []
    byte_array = []
    for _ in range(message_size):
        r, g, b = get_pixel_value(image, x, y)  # red, green, blue ASCII values
        color_binary = ascii_to_binary([r, g, b])  # red, green, blue values in binary
        bit_array.append(color_binary[0][-1])  # add the red binary color to the array
        bit_array.append(color_binary[1][-1])  # add the green binary color to the array
        bit_array.append(color_binary[2][-1])  # add the blue binary color to the array

        x += 1  # add 1 to the x coordinates
        if x == w - 1:  # if x is at the edge of the image
            y += 1
            x = 0
            if y == h - 1:
                break
    temp = []
    for i in range(len(bit_array)):
        temp.append(bit_array[i])
        if (i + 1) % bits_per_letter == 0:
            byte_array.append(temp)  # group bits by character
            temp = []

    binary_list = []
    for byte in byte_array:
        val = ""
        for bit in byte:
            val += str(bit)
        binary_list.append(val)  # byte as a string

    ascii_list = binstr_to_ascii(binary_list)  # convert binary to ASCII
    letter_list = ascii_to_string(ascii_list)  # convert ASCII to string
    return "".join(letter_list)


if __name__ == "__main__":
    image_file: str = "default.png"
    output_file: str = "hidden.png"
    text: str = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim 
    veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate 
    velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
     cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
     est laborum.
    """

    img = Image.open(image_file)
    img = encrypt(text, img)
    img.save(output_file, "png")
    img = Image.open(output_file)
    print(decrypt(img))
