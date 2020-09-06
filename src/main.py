import shutil
import time
import sys
from PIL import Image
from pytube import YouTube
import cv2
import numpy as np
import tkinter as tk
import youtubeInterface


def calculateAverage(currentFrame):

    # Rather than RGB its BGR???
    # Populate arrays with all the Red, Green and Blue values for frame
    rArray = currentFrame[0:, 0:, 2]
    gArray = currentFrame[0:, 0:, 1]
    bArray = currentFrame[0:, 0:, 0]

    # Average the arrays
    rAverage = int(np.average(rArray))
    gAverage = int(np.average(gArray))
    bAverage = int(np.average(bArray))

    # Output the final color
    finalColor = (rAverage, gAverage, bAverage)
    return finalColor


def outputVideoAsFrames():

    # Read first frame and return whether it's there
    success, image = vidcap.read()
    count = 0

    # While there are still frames left
    while success:

        # Find average color of frame and fill in row
        frameColor = calculateAverage(image)
        for y in range(outputHeight):
            currentPixel = (count - 1, y)
            outputImage.putpixel(currentPixel, frameColor)

        # Move to next frame and increase frame count
        success, image = vidcap.read()
        count += 1


def main():
    # Variables (Video URL, output height and numpy options)
    np.set_printoptions(threshold=np.inf)
    videoURL = str(sys.argv[1])
    outputHeight = int(sys.argv[2])

    # Open video in link and download it
    video = YouTube(
        videoURL).streams.get_highest_resolution().download('../temp')
    videoPath = video.title()
    print(videoPath)

    # Start timer
    starttime = time.time()
    # Open VideoCapture and create a new image to output to
    vidcap = cv2.VideoCapture(videoPath)
    outputSize = (int(vidcap.get(7)), outputHeight)
    outputImage = Image.new('RGB', outputSize)

    # Use the VideoCapture to produce the image, save it and close
    outputVideoAsFrames()
    outputPath = '../output/' + YouTube(videoURL).title + '_output.png'
    outputImage.save(outputPath)
    vidcap.release()

    # Remove all temporary files
    shutil.rmtree("temp")

    # Stop timer and calculate final time
    endtime = time.time()
    totaltime = endtime - starttime
    print('Full output finished in %d seconds' % totaltime)


if __name__ == "__main__":
    main()
