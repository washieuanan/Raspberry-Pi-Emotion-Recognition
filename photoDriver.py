from __future__ import print_function
from photoApp import PhotoApp
from imutils.video import WebcamVideoStream
import argparse
import time

ap = argparse.ArgumentParser()
ap.add_argument(
    "-o",
    "--output",
    required=True,
    help="Path to output directory to store the pictures",
)
args = vars(ap.parse_args())


print("[INFO] Getting the camera ready...")

vs = WebcamVideoStream(src=0).start()
time.sleep(2.0)

pba = PhotoApp(vs, args["output"])
pba.root.mainloop()
