import fitz
import os


def extract_images(pdf_path, output_folder):
    """
    Extract images from PDF and save them locally.

    Parameters:
        pdf_path (str): PDF file path
        output_folder (str): folder where images will be stored

    Returns:
        list: saved image paths
    """

    # Create folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)

    image_paths = []

    # Loop through each PDF page
    for page_num in range(len(doc)):

        page = doc[page_num]

        # Get all images from page
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):

            # Get image reference
            xref = img[0]

            # Extract actual image
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # Create unique image name
            image_name = f"page_{page_num+1}_{img_index}.{image_ext}"

            image_path = os.path.join(output_folder, image_name)

            # Save image
            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(image_path)

    doc.close()

    return image_paths