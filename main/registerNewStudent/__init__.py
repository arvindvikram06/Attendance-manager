import cv2
from ..functions import (check_haarcascadefile,
                         check_path_exists,
                         frame_processing,
                         create_canvas_with_text)


def video_capturing_for_registration(studentId):
    if check_haarcascadefile():
        """ Yielding the frames for the webcam video during registration"""
        check_path_exists("TrainingImage/")  # Check for the training image dir

        cam = cv2.VideoCapture(0)  # Initialization of the VideoCapture
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 800)  # Setting up the width of the captured video
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)  # Setting up the height of the captured video

        # Place the absolute path for the haarcascade_frontalface_default.xml file
        path = (r"K:\PROJECTS\Face Recognition for Attendance "
                r"Manager\ATTENDANCE-MANAGER-USING-FACE-RECOGNITION\main"
                r"\static\asserts\haarcascade_frontalface_default.xml")

        detector = cv2.CascadeClassifier(r"K:\PROJECTS\Face Recognition for Attendance "
                                         r"Manager\ATTENDANCE-MANAGER-USING-FACE-RECOGNITION"
                                         r"\main\static\asserts"
                                         r"\haarcascade_frontalface_default.xml")
        sampleNum = 0

        while True:
            ret, img = cam.read()  # Capturing the image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converting the image to a gray scale image
            faces = detector.detectMultiScale(gray, 1.3, 5)  # Detecting the faces

            if len(faces):  # To check weather the faces has any value
                x, y, w, h = faces[0]  # Taking a single face from detected faces
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Drawing rectangle around the face
                sampleNum = sampleNum + 1  # incrementing sample number

                cv2.imwrite("TrainingImage\ " + str(studentId) + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])  # Saving the sample images

            # Loading bar
            cv2.rectangle(img, (20, 20 + 100), (20 + 20, 120 - sampleNum), (255, 0, 0), -1)
            cv2.rectangle(img, (20, 20), (20 + 20, 20 + 100), (0, 255, 0), 2)

            frame = frame_processing(img)  # Preprocessing the image for the response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            if sampleNum > 100:
                print("Samples reached 100")
                break

        cam.release()
        cv2.destroyAllWindows()

        # Create a final frame with the text "Successfully Registered!"
        final_frame = create_canvas_with_text("Successfully Registered!")
        final_frame = frame_processing(final_frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + final_frame + b'\r\n')
