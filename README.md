![logo](https://github.com/Qristt/Armenian_animals/assets/154927704/d746d695-eb91-4839-b2c3-f632283de362)

## Armenian animals Classification Model





#

### Table of Contents

- [Task Description](#task-description)
- [Tech Stack](#tech-stack)
- [Approach Overview](#approach-overview)
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


<img src="./Images/supervised_learning_flowchart.png" style="width: 700px; height:600px;">
