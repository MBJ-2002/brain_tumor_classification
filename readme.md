# Brain Tumor Classification

Dataset Used : [Brain Tumor Images](https://www.kaggle.com/datasets/murtozalikhon/brain-tumor-multimodal-image-ct-and-mri)

## Overview:
 - Dataset has two classes **Healthy** and **Tumor**
 - Healthy MRI has 2000 Images
 - Tumor MRI has 3000 Images

### CNN Model Currently trained on only MRI images
 - I had done splitting of dataset with the split.py due to errors but I highly recommend to use inbuilt functions from TensorFlow or Torch to prepare image data


### CNN Metrics:
 - Dataset has two classes **Healthy** and **Tumor**
 - Healthy MRI has 2000 Images
 - Tumor MRI has 3000 Images
 - Precision for Healthy Class : 0.97
 - Precision for Tumor Class : 0.99 
 - It might look like overfitting but on looking confusion matrix it looks good
 - Average Inference Time : 20-30ms depending on hardware
 - Runs on CPU, to run on GPU need TensorFlow GPU version that is available on Linux

 ### ResNet Metric:
 - Precision for Healthy Class : 0.92
 - Precision for Tumor Class : 0.98 
 - Average Test Accuracy : 95%
 - Validation Accuracy: 0.94
 - Overall Much better than CNN
 - Model Size ~ 203MB
 - ResNet Model: [Download](https://drive.google.com/file/d/1d3RNUViKOgNtoirVpXupwx348e_c4bDP/view?usp=sharing)
 - Move the downloaded model to models folder and then test

### How to use custom images to test:
 - First load model from models folder
 - Simply pass the path to image in the function `predict(img_path)`
