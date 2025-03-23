#%% [markdown]
# # Image Augmentation
#
# In this first section, we define functions to augment images.
# The augmentation techniques include random rotation, horizontal flip, random cropping, brightness and contrast adjustments, and scaling.
#
# After running these cells, we can generate augmented images which will be saved into a new folder.

#%% [code]
import os
import random
from PIL import Image, ImageEnhance

def augment_image(image):
    # random rotation between -15 and 15 degrees
    angle = random.randint(-15, 15)
    image = image.rotate(angle, expand=True)

    # horizontal flip
    if random.random() > 0.5:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)

    # random cropping
    width, height = image.size
    new_width = int(width * random.uniform(0.8, 1.0))  # Crop width between 80% and 100%
    new_height = int(height * random.uniform(0.8, 1.0))  # Crop height between 80% and 100%

    # random position for cropping
    left = random.randint(0, width - new_width)
    top = random.randint(0, height - new_height)
    right = left + new_width
    bottom = top + new_height

    image = image.crop((left, top, right, bottom))

    # random brightness
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(random.uniform(0.5, 1.5))

    # contrast adjustment
    contrast_factors = [0.8, 1.0, 1.2]  # Lower, Normal, Higher
    contrast_factor = random.choice(contrast_factors)
    image = ImageEnhance.Contrast(image).enhance(contrast_factor)

    # scaling
    scale_factors = [0.8, 1.0, 1.2]  # Smaller, Normal, Larger
    scale_factor = random.choice(scale_factors)
    new_size = (int(image.width * scale_factor), int(image.height * scale_factor))
    image = image.resize(new_size, Image.ANTIALIAS)

    return image

def save_augmented_images(folder_path, output_folder, num_augmented_images=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]

    for img_name in images:
        img_path = os.path.join(folder_path, img_name)
        img = Image.open(img_path)
        for i in range(num_augmented_images):
            augmented_img = augment_image(img)
            augmented_img_name = f"{os.path.splitext(img_name)[0]}_augmented_{i}.jpg"
            augmented_img.save(os.path.join(output_folder, augmented_img_name))

# example of how we used this: 
# folder_path = 'DATASET/TRAIN/downdog'  # Path to the folder with original images
# output_folder = 'DATASET/TRAIN/downdog2'  # Path to save augmented images
# save_augmented_images(folder_path, output_folder, num_augmented_images=2)