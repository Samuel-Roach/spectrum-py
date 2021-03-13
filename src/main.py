import shutil
import time
import sys
from PIL import Image
from pytube import YouTube
import cv2
import numpy as np
import os
import argparse


def calculate_average(current_frame):

    # Rather than RGB its BGR???
    # Populate arrays with all the Red, Green and Blue values for frame
    r_array = current_frame[0:, 0:, 2]
    g_array = current_frame[0:, 0:, 1]
    b_array = current_frame[0:, 0:, 0]

    # Average the arrays
    r_average = int(np.average(r_array))
    g_average = int(np.average(g_array))
    b_average = int(np.average(b_array))

    # Output the final colorz
    final_color = (r_average, g_average, b_average)
    return final_color


def output_video_as_frames(vidcap, output_height, output_image):

    # Read first frame and return whether it's there
    success, image = vidcap.read()
    count = 0

    # While there are still frames left
    while success:

        # Find average color of frame and fill in row
        frame_color = calculate_average(image)
        for y in range(output_height):
            current_pixel = (count - 1, y)
            output_image.putpixel(current_pixel, frame_color)

        # Move to next frame and increase frame count
        success, image = vidcap.read()
        count += 1


def argument_handler(argv):
    parser = argparse.ArgumentParser(description="Generate image data from videos")


def main():
    # Variables (Video URL, output height and numpy options)
    np.set_printoptions(threshold=np.inf)
    video_url = str(sys.argv[1])
    output_height = int(sys.argv[2])

    # Open video in link and download it
    temp_path = os.path.join(os.path.dirname(
        os.path.dirname(__file__)), "temp")
    video = YouTube(
        video_url).streams.get_highest_resolution().download(temp_path)
    video_path = video.title()
    print(video_path)

    # Start timer
    start_time = time.time()
    # Open VideoCapture and create a new image to output to
    vidcap = cv2.VideoCapture(video_path)
    output_size = (int(vidcap.get(7)), output_height)
    output_image = Image.new('RGB', output_size)

    # Use the VideoCapture to produce the image, save it and close
    output_video_as_frames(vidcap, output_height, output_image)
    output_path = os.path.join(os.path.dirname(os.path.dirname(
        __file__)), "output", YouTube(video_url).title + "_output.png")
    f = open(output_path, 'x')
    f.close()
    output_image.save(output_path)
    vidcap.release()

    # Remove all temporary files
    shutil.rmtree(temp_path)

    # Stop timer and calculate final time
    end_time = time.time()
    total_time = end_time - start_time
    print('Full output finished in %d seconds' % total_time)


if __name__ == "__main__":
    main()
