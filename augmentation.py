from PIL import Image, ImageEnhance, ImageOps
import os

def augment_image(img_path, output_folder):
    """
    Apply basic augmentations to an image and save them to the output folder.
    """
    try:
        # Open the image
        img = Image.open(img_path)
        
        print(f"Processing image: {img_path}")
        
        # Augmentation 1: Brightness enhancement
        enhancer = ImageEnhance.Brightness(img)
        bright_img = enhancer.enhance(1.5)  # Increase brightness by 1.5 times
        bright_img.save(os.path.join(output_folder, "bright_" + os.path.basename(img_path)))
        
        # Augmentation 2: Contrast enhancement
        enhancer = ImageEnhance.Contrast(img)
        contrast_img = enhancer.enhance(1.5)  # Increase contrast by 1.5 times
        contrast_img.save(os.path.join(output_folder, "contrast_" + os.path.basename(img_path)))
        
        # Augmentation 3: Image flip
        # flipped_img = ImageOps.mirror(img)
        # flipped_img.save(os.path.join(output_folder, "flipped_" + os.path.basename(img_path)))

        # Augmentation 4: Image rotation
        #rotated_img = img.rotate(45)  # Rotate image by 45 degrees
        #rotated_img.save(os.path.join(output_folder, "rotated_" + os.path.basename(img_path)))
    
    except Exception as e:
        print(f"Error processing {img_path}: {e}")

def main():
    # List of folders containing images
    base_folder = "D:/5 Protel mediapipe/data/"
    folders = [base_folder + str(i) for i in range(31)]  # This will create a list of folder paths from "0" to "30"

    for folder in folders:
        print(f"Checking folder: {folder}")

        output_folder = os.path.join(folder, "augmented")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for img_file in os.listdir(folder):
            print(f"Found file: {img_file}")

            if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(folder, img_file)
                augment_image(img_path, output_folder)

if __name__ == "__main__":
    main()
