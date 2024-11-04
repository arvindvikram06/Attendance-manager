import numpy as np
import os
from PIL import Image
import cv2
from datetime import datetime


def check_path_exists(path):
    """ Making sure the path exists else creating the path"""
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


def check_haarcascadefile():
    """ Checking for the Haarcascade-frontalface-default file"""
    exists = os.path.isfile(r"K:\PROJECTS\Face Recognition for Attendance Manager\ATTENDANCE-MANAGER-USING-FACE-RECOGNITION\main\static\asserts\haarcascade_frontalface_default.xml")
    if exists:
        return True
    else:
        print("The 'haarcascade_frontalface_default.xml' file is missing gg !")
        return False


def check_trained_file():
    """ Checking weather the Trained file exists """
    trainedFile = os.path.isfile("TrainingImageLabel\Trainner.yml")
    if trainedFile:
        return True
    else:
        print('TrainingImage Data is Missing, Please click on Save Profile to reset data!!')
        return False


# def get_last_inserted_id(db, YourModel):
#     """ For retrieving the last inserted student's ID in the database"""
#     # Query the last inserted ID in the table
#     last_inserted_id = db.session.query(YourModel.id).order_by(YourModel.id.desc()).first()
#     return last_inserted_id[0] if last_inserted_id else 0


def getImagesAndLabels(path):
    """ Getting the training images and the labels processed """
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        root = list(os.path.split(imagePath))
        # Split the root into id and image_count
        id = root[1].split('.')
        # Convert id and image_count to integers if needed
        id = int(id[0].strip())
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(id)
    return faces, Ids


def get_data_time():
    """ Getting the current data and time """
    return datetime.now().strftime("%H:%M, %d.%m.%Y")


def create_canvas_with_text(text):
    """ Creating a picture for displaying the registration done or attendance noted"""
    image_width, image_height = 640, 480
    # Create a white canvas
    canvas = np.ones((image_height, image_width, 3), dtype=np.uint8) * 255

    # Calculate the position to center the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = (image_width - text_size[0]) // 2
    text_y = (image_height + text_size[1]) // 2

    # Put the text on the canvas
    cv2.putText(canvas, text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness, cv2.LINE_AA)

    return canvas


def frame_processing(frame):
    """ Preprocessing the frames """
    ret, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    return frame


def checkIn_checkOut(check_in, check_out, id):
    """ Managing the check in and check out details """
    for i in check_in:
        if id == i[0]:
            print("index ===", check_in.index(i), "id ===", id)
            check_out.append(check_in.pop(check_in.index(i)))
    return check_in, check_out
