from __future__ import print_function
from PIL import Image, ImageTk
import tkinter as tki
import threading
import datetime
import imutils
import cv2
import os
import numpy as np
import webbrowser
import matplotlib

matplotlib.use("Agg")
from machineLearning.predictor import Predictor


class PhotoApp:
    def __init__(self, vs, outputPath):
        self.vs = vs
        self.outputPath = outputPath
        self.frame = None
        self.thread = None
        self.stopEvent = None

        self.root = tki.Tk()
        self.panel = None
        self.root.geometry("500x500")

        btn = tki.Button(
            self.root, text="Take a picture!", bg="red", command=self.runOnPress
        )
        btn.place(relx=0.0, rely=0.5, relheight=0.3, relwidth=1.0)

        listen_on_spotify = tki.PhotoImage(
            file=r"C:\Users\washi\Desktop\Coding\raspberry_pi_emotion_detection\snapshot\assets\spotify.png"
        )

        self.linkVar = tki.StringVar()
        self.linkVar.set("Open in Spotify")

        self.link = tki.Label(self.root, textvariable=self.linkVar, bg="green")

        self.link.place(relx=0.0, rely=0.7, relheight=0.3, relwidth=1.0)
        self.link.bind("<Button-1>", lambda e: self.urlOpener())

        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.start()

        self.root.wm_title("Emotion Reccomender")
        self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)

    def videoLoop(self):
        try:
            # keep looping over frames until we are instructed to stop
            while not self.stopEvent.is_set():
                # grab the frame from the video stream and resize it to
                # have a maximum width of 300 pixels
                self.frame = self.vs.read()
                self.frame = imutils.resize(self.frame, width=350, height=350)

                # OpenCV represents images in BGR order; however PIL
                # represents images in RGB order, so we need to swap
                # the channels, then convert to PIL and ImageTk format
                image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)

                # if the panel is not None, we need to initialize it
                if self.panel is None:
                    self.panel = tki.Label(image=image)
                    self.panel.image = image
                    self.panel.place(relx=0.42, rely=0.0)

                # otherwise, simply update the panel
                else:
                    self.panel.configure(image=image)
                    self.panel.image = image

        except RuntimeError:
            print("[INFO] caught an error")

    def takeSnapshot(self):
        # Takes a picture
        ts = datetime.datetime.now()
        self.filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
        p = os.path.sep.join((self.outputPath, self.filename))
        # save the file
        cv2.imwrite(p, self.frame.copy())
        print("[INFO] saved {}".format(self.filename))

    def onClose(self):
        # set the stop event, cleanup the camera, and allow the rest of
        # the quit process to continue
        print("[INFO] closing...")
        self.stopEvent.set()
        self.vs.stop()
        self.root.quit()

    def getPrediction(self):
        # Get the prediction of the image
        src = "output/" + self.filename
        print(src)
        img = Predictor().resize(src=src)
        predictor = Predictor().predict(img)

        return predictor

    def runOnPress(self):
        # Callback function to take a picture, and get the link for the spotify playlist
        self.takeSnapshot()
        print("[INFO] PREDICTING")

    def urlOpener(self):
        self.emotion = self.getPrediction()
        print("INFO:", self.emotion)
        self.emotionLink = r" "

        if self.emotion == 0:
            self.emotionLink = r"https://open.spotify.com/playlist/4OQq1cgV9FJ35t5YCCvB9r?si=UiAwCmb3TAyfM0J6cuYQww"

        elif self.emotion == 1:
            self.emotionLink = r"https://open.spotify.com/playlist/4OQq1cgV9FJ35t5YCCvB9r?si=UiAwCmb3TAyfM0J6cuYQww"

        elif self.emotion == 2:
            self.emotionLink = r"https://open.spotify.com/playlist/5XYWhZiosQfvoPIY7PvBvK?si=pxGPj4c9QvGhH76BbMk5lA"

        webbrowser.open_new(self.emotionLink)

