import shutil
import time
import sys
from PIL import Image
from pytube import YouTube
import cv2
import numpy as np

# Variables (Video URL, output height and numpy options)
np.set_printoptions(threshold=np.inf)
VIDEO_URL = str(sys.argv[1])
OUTPUT_HEIGHT = int(sys.argv[2])

# Open video in link and download it
VIDEO = YouTube(VIDEO_URL).streams.get_highest_resolution().download('./temp')
VIDEO_PATH = VIDEO.title()
print(VIDEO_PATH)

# Start timer
START_TIME = time.time()

def download_youtube_url(youtube_url):
    try:
        youtube_video = YouTube(youtube_url).streams.get_highest_resolution().download('./temp')
    except Exception as e:
        print('Could not download youtube video')
        raise

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

    # Output the final color
    final_color = (r_average, g_average, b_average)
    return final_color


def output_video_as_frames():

    # Read first frame and return whether it's there
    success, image = VIDCAP.read()
    count = 0

    # While there are still frames left
    while success:

        # Find average color of frame and fill in row
        frame_color = calculate_average(image)
        for y in range(OUTPUT_HEIGHT):
            current_pixel = (count - 1, y)
            OUTPUT_IMAGE.putpixel(current_pixel, frame_color)

        # Move to next frame and increase frame count
        success, image = VIDCAP.read()
        count += 1


# Open VideoCapture and create a new image to output to
VIDCAP = cv2.VideoCapture(VIDEO_PATH)
OUTPUT_SIZE = (int(VIDCAP.get(7)), OUTPUT_HEIGHT)
OUTPUT_IMAGE = Image.new('RGB', OUTPUT_SIZE)

# Use the VideoCapture to produce the image, save it and close
output_video_as_frames()
OUTPUT_PATH = './output/' + YouTube(VIDEO_URL).title + '_output.png'
OUTPUT_IMAGE.save(OUTPUT_PATH)
VIDCAP.release()

# Remove all temporary files
shutil.rmtree("temp")

# Stop timer and calculate final time
END_TIME = time.time()
TOTAL_TIME = END_TIME - START_TIME

print('Full output finished in %d seconds' % TOTAL_TIME)
