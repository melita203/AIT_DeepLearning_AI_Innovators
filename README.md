# AIT_DeepLearning_AI_Innovators

Team: AI Innovators
- Caleb Kim, Melita Madhurza, Minji Woo

Project : Yoga Posture Classification and Grading

## Description :
With the growing popularity of home yoga, maintaining precise postures is essential to prevent injuries and maximize effectiveness. However, beginners often lack expert guidance.
This project aims to develop a yoga posture recognition model that can classify eight yoga poses from the static images. The long term goal is to extend this model for real time feedback and posture correction, helping users improve their alignment. The selected postures focus on back pain prevention and posture correction. 

## Data Preprocessing
We began by downloading a yoga pose dataset from Kaggle, which includes both training and testing images for five poses: Down Dog, Goddess, Plank, Tree, and Warrior II. However, the largest training set contained only 252 images, which was insufficient for robust model training. To address this, we applied data augmentation techniques such as rotation, horizontal flipping, cropping, brightness and contrast adjustments, and scaling/resizing. This process expanded our dataset significantly, generating eight unique images from each original image.

Next, we partitioned the augmented training dataset to create a validation set. We transferred around 10% of the expanded training dataset for this purpose.

With these steps completed, we finalized our comprehensive yoga pose dataset, making it ready for preprocessing and model training. The final dataset is available in this repository.

Now that we had the final dataset, our next step was preprocdessing. The Jupyter Notebook (`notebooks/data_preprocessing.ipynb`) performs the following steps:
1. Loads augmented images from `DATASET/TRAIN/`.
2. Resizes and normalizes images.
3. Constructs input (X) and output (Y) matrices.


## BlazePose Preprocessing
Once the final dataset was prepared, we extracted pose landmarks using **MediaPipe BlazePose**.
This step focused on representing each image with a 99-dimensional feature vector (x, y, z coordinates for 33 keypoints).

The preprocessing steps (in notebooks/data_preprocessing.ipynb) included:
- Loading images from DATASET/TRAIN/, DATASET/VALIDATION/, and DATASET/TEST/
- Running BlazePose landmark detection
- Constructing input matrices (X) and output labels (Y)
- Saving the processed data as .npy files for efficient loading

**Final processed dataset shapes:**
1. Train: (6119, 99)
2. Validation: (277, 99)
3. Test: (465, 99)

## Model Training and Evaluation
We built and compared two models:

### 1. Baseline Model (Logistic Regression)
- Trained on the BlazePose landmark features.
- Achieved a **Validation Accuracy** of **85.56%**.
- Provided a strong benchmark for comparison.

### 2. Deep Learning Model (Neural Network)
- 3 Dense layers with ReLU activations and Dropout regularization.
- Trained on the same BlazePose landmark features.
- Achieved:
  - **Validation Accuracy:** ~94%
  - **Test Accuracy:** ~97.63%

## Results
  | Model               | Validation Accuracy | Test Accuracy |
|---------------------|----------------------|---------------|
| Random Forest       | 85.56%               | N/A           |
| Neural Network (NN) | ~94%                 | 97.63%        |


