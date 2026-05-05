import fitz
import os
from PIL import Image
import io
import numpy as np


def is_logo_or_invalid(image_bytes):
    """
    Detect logo/header images
    """

    try:
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img_array = np.array(img)

        # Skip very small images
        if img.width < 250 or img.height < 150:
            return True

        # Mean brightness
        mean_pixel = img_array.mean()

        # Detect black-heavy images (UrbanRoof logo issue)
        black_pixels = np.sum(
            np.all(img_array < 40, axis=2)
        )

        total_pixels = img_array.shape[0] * img_array.shape[1]

        black_ratio = black_pixels / total_pixels

        # If image is mostly black → skip
        if black_ratio > 0.55:
            return True

        # Extra safeguard
        if mean_pixel < 50:
            return True

        return False

    except:
        return True


def extract_images(pdf_path, output_folder):
    """
    Extract only valid inspection images
    """

    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)

    image_mapping = {}

    for page_num in range(len(doc)):
        page = doc[page_num]

        images = page.get_images(full=True)

        page_images = []

        for img_index, img in enumerate(images):
            xref = img[0]

            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            ext = base_image["ext"]

            # Skip logo images
            if is_logo_or_invalid(image_bytes):
                continue

            image_name = f"page_{page_num+1}_{img_index}.{ext}"

            image_path = os.path.join(
                output_folder,
                image_name
            )

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            page_images.append(image_path)

        if page_images:
            image_mapping[page_num + 1] = page_images

    doc.close()

    return image_mapping