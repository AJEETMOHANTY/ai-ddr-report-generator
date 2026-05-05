import fitz
import os


def extract_images(pdf_path, output_folder):
    """
    Extract meaningful images from PDF.

    Filters out:
    - logos
    - tiny icons
    - decorative elements

    Keeps:
    - inspection photos
    - thermal images
    """

    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)

    image_paths = []

    for page_num in range(len(doc)):
        page = doc[page_num]

        images = page.get_images(full=True)

        for img_index, img in enumerate(images):

            xref = img[0]

            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # Get image dimensions
            width = base_image.get("width", 0)
            height = base_image.get("height", 0)

            # Skip very small images (logos/icons)
            if width < 200 or height < 200:
                print(
                    f"Skipping small image on page {page_num+1}"
                )
                continue

            image_name = (
                f"page_{page_num+1}_{img_index}.{image_ext}"
            )

            image_path = os.path.join(
                output_folder,
                image_name
            )

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(image_path)

    doc.close()

    return image_paths