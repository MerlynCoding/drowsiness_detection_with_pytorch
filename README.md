# Drowsiness Detection System

Welcome to the Drowsiness Detection System! This project aims to detect drowsiness using computer vision techniques. Here's how to get started:

## Installation

First, let's make sure we have all the necessary dependencies installed. Run the following command to install the required packages:

```bash
pip install -r requirements.txt
```

## Testing

After installing the requirements, let's test our camera and the detection system. Run the following commands to perform camera testing and detection testing:

```bash
python test_camera.py
python test_detection.py
```

## Image Sampling

Before training our model, we need to gather a sufficient number of image samples. Use the `take_photo_sample.py` script to capture images. You can adjust the `sample_total` parameter to specify how many samples you'd like to capture.

```bash
python take_photo_sample.py
```

## Annotation with LabelImg

Once we have our image samples, we need to annotate them. Open your command prompt and navigate to the project directory. Then, run the following command to launch LabelImg:

```bash
labelimg
```

Use LabelImg to draw bounding boxes around faces in the images and label them as either "drowsy" or "awake".

## Training

Now that we have annotated our images, we can proceed with training our model. Use the following command to train the model:

```bash
python train.py --img 320 --batch 16 --epochs 500 --data dataset.yml --weights yolov5s.pt --workers 2
```

## Testing Detection

After training, we can use the trained model to perform drowsiness detection. Run the `detection.py` script to test the detection capabilities:

```bash
python detection.py
```

That's it! You're now ready to detect drowsiness using the Drowsiness Detection System. Happy coding!

---

This README.md provides clear instructions for setting up the project, testing the camera and detection, sampling images, annotating them, training the model, and finally, testing the detection. It also incorporates grammatical improvements and strives to make the process engaging for the reader. Feel free to further customize it to suit your needs!
