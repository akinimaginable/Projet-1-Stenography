# 007

A simple (not that simple when you start) project to hide messages in images using steganography.

## How it works

You define a message and pick an image to hide the message in.
The program will hide a message in an image by changing the least significant bit of the RGB values of each pixel. This way, the change is so small that the human eye can't notice it.


## How to use the CLI

1. Extract the zip file
2. Open the terminal and navigate to the folder where you extracted the files
3. Install the required libraries by running `pip install -r requirements.txt`
4. Run the command `python main.py`

## How to use the GUII

1. Extract the zip file
2. Open the terminal and navigate to the folder where you extracted the files
3. Install the required libraries by running `pip install -r requirements.txt`
4. Run the command `python gui.py`
