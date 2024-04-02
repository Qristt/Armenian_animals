![woman-programmer-software-web-development-computer-girl-work-script-coding-programming_352905-203](https://github.com/Qristt/Armenian_animals/assets/154927704/0e1b45c5-20a0-4252-9539-7b6426eb91f6)

## Classification model - animals of the red book of Armenia



#

### Table of Contents

- [Task Description](#task-description)
- [Tech Stack](#tech-stack)
- [Approach Overview](#approach-overview)
- [Work Progress](#work-progress)
- [Deliverables](#deliverables)
#

### Task Description

The goal of the task was to create a model that would predict what animal was given a picture. The images used to create this model were obtained from websites. The goal of the model was to accurately determine the name of the animal. It was very important for the model to perform the prediction well, considering that the data provided is a small part of the whole.

---


### Tech Stack

<img align="left" alt="Java" width="30px" style="padding-right:20px;" src="https://github.com/GorPiliposyan/subway-ticket-barrier-state-detection/blob/main/Images/Python-logo-notext.svg"/>
<img align="left" alt="Java" width="30px" style="padding-right:20px;" src="https://github.com/GorPiliposyan/subway-ticket-barrier-state-detection/blob/main/Images/PyTorch_logo_icon.svg"/>
<img align="left" alt="Java" width="100px" style="padding-right:20px;" src="https://github.com/GorPiliposyan/subway-ticket-barrier-state-detection/blob/main/Images/UltralyticsYOLO_full_blue.svg"/>
<img align="left" alt="Java" width="30px" style="padding-right:20px;" src="https://github.com/GorPiliposyan/subway-ticket-barrier-state-detection/blob/main/Images/OpenCV_Logo.svg"/>
<br />

#

- **Python**
- **PyTorch**
- **Ultralytics YOLOv8**
- **OpenCV**

#

### Work Progress

-  I have collected pictures of 5 animals registered in the Red Book of Armenia: seagull, leopard, mouflon, otter, chaytakis.
-  Split the train val test folders and clean them of duplicate images
-  The images are augmented and then training is done with Yolov8x.
-  We create a model that learns to guess animals using the pictures of the training folder, and then the model makes a guess with the pictures of the validation folder, and according to the results of the 
   run folder, it becomes clear how accurate the prediction was. If there are errors, we perform augmentation and training again
-  The model works in jupyter notebook, the installs are done with anaconda
-  The Utils folder is designed to make train/val/test, rename_all_files and similar tasks easier.
-  The images as well as the augmented images are located in the dataset folder
-  The Runs folder is already the training result


#


### Approach Overview

- **Model Preparation Jupyter Notebook:** The process of creating the classification model was detailed in the `Model.ipynb` notebook. This notebook includes comprehensive steps for data preparation, model training, and evaluation. Comments throughout the notebook elaborate on key decisions and metrics supporting the model's adequacy.



#

### Web App

**Web application coming very soon!**

#


### Deliverables

**Main files:**
- `Model.ipynb`: Python code file, our model. Detailed Jupyter Notebook showcasing in detail the model creation process with relevant comments and a discussion section in the end.`.
- `yolov8x_cls_custom.pt`: Ultralytics YOLOv8 custom trained 'yolov8x-cls.pt' model weights file. Necessary to run `model_run.py` file.

**Extra files:**
- `utils`: Folder with some helper functions I have used for "model_preparation.ipynb"
- `animals`: Dataset folder with the original and augmented images, split into train/val/test folders. (test images only in original folder)
- `runs`: Folder with training images.

