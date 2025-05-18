# AIT_DeepLearning_AI_Innovators

Team: AI Innovators
- Caleb Kim, Melita Madhurza, Minji Woo

Project : Yoga Posture Classification and Grading

## Description :
With the growing popularity of home yoga, maintaining precise postures is essential to prevent injuries and maximize effectiveness. However, beginners often lack expert guidance.
This project aims to develop a yoga posture recognition model that can classify eight yoga poses from the static images. The long term goal is to extend this model for real time feedback and posture correction, helping users improve their alignment. The selected postures focus on back pain prevention and posture correction. 

## Data Preprocessing
We began by downloading a yoga pose dataset from Kaggle, which includes both training and testing images for five poses: Down Dog, Goddess, Plank, Tree, and Warrior II.
📂 **Dataset source**: [Kaggle Yoga Pose Dataset](https://www.kaggle.com/datasets/niharika41298/yoga-poses-dataset?resource=download)  

### 🔽 How to Get the Data:
1. Go to the [Kaggle Yoga Pose Dataset](https://www.kaggle.com/datasets/niharika41298/yoga-poses-dataset?resource=download) page.
2. Download and extract the dataset ZIP file.
3. Place the extracted folders in the following directory structure:

project-root/
│
├── DATASET/
│ ├── TRAIN/
│ │ ├── downdog/
│ │ ├── plank/
│ │ └── ... (other class folders)
│ └── TEST/
│ └── ...
├── dataaugmentation.py
└── ...

bash
Copy
Edit

### Running Image Augmentation:
To expand the dataset, use the `dataaugmentation.py` script. It applies a variety of transformations to each image, including:

- Random rotation
- Horizontal flip
- Random cropping
- Brightness adjustment
- Contrast enhancement
- Scaling/resizing

#### How to Use:
Open a Python script or notebook and run the following:

```python
from dataaugmentation import save_augmented_images

# Example usage:
folder_path = 'DATASET/TRAIN/downdog'  # Path to original images
output_folder = 'DATASET/TRAIN/downdog_augmented'  # Path to save augmented images

save_augmented_images(folder_path, output_folder, num_augmented_images=5)


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
| Logistic Regression       | 85.56%               | ~94%           |
| Neural Network (NN) | ~94%                 | 97.63%        |


