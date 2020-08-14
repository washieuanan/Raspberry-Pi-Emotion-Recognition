# **Human Emotion Recognition with the Raspberry Pi**

This project aimed to use the PiCamera module for the Raspberry Pi to recognize human facial emotions. The model was built specifically for the project using the [FER2013 dataset](https://www.kaggle.com/ashishpatel26/facial-expression-recognitionferchallenge). The FER2013 dataset consists of over 30,000 images, all of which are formatted to be 48px * 48px grayscale images. For the Jupyter Notebook and the model itself, reference the ```machineLearning``` folder. 

Using the model, I wrote three classes with Tkinter to read in the image from the PiCamera and predict the emotion that one is feeling. Although this part of the project is not finished yet, depending on the emotion of one's face, the program will provide users with a playlist to listen to on Spotify. For the three scripts, reference ```predictor.py```in the ```machineLearning```folder, and ```photoApp.py``` and ```photoDriver.py```. 

## **How To Run The Application**

This script is ready to run on a desktop or laptop computer as well. After cloning the repository, please add a folder called ```output```. If you wish, you may call it another name (You will need to reference the folder's name later). 

Going to your terminal of choice, clone the repository into a directory of your choice. Then ```cd``` into the repository. Before you run the script, you need to install all necessary libraries. Run the following command to install all necessary libraries: ```pip install -r requirements.txt```. 

After installing all of the libraries, run the following command: ```python3 photoDriver.py --output [output_folder_name]```. Please note that ```[output_folder_name]``` is the name of the folder that you made to output all of your images. 

Note: When running the application, you may receive Tensorflow-GPU errors. Please do not worry about these errors. A GPU is not needed while running this application. 

## **How To Use The Application**

Note: Because of Tkinter's widget placement styles, the application must be opened to full window.
 

Once you open the application, you will see the live video stream and two buttons. The ***red*** button will be used to take the picture. Once you click the ***red*** button, a picture will be taken, pre-processed and be predicted on via the model. 

Then, click on the ***green*** button, the script will receive the emotion predicted and provide users with a Spotify playlist to listen to. 
