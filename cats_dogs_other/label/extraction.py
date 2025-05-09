from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

import fitz
from fitz import Pixmap


def convert_pixmap_to_rgb(pixmap) -> Pixmap:
    """Convert to rgb in order to write on png"""
    # check if it is already on rgb
    if pixmap.n < 4:
        return pixmap
    else:
        return fitz.Pixmap(fitz.csRGB, pixmap)


@dataclass
class ExtractImagesResult:
    number_files_input: int
    number_images_output: int


def extract_images(pdfs_directory_path: str, images_directory_path: str) -> ExtractImagesResult:
    pdfs = [p for p in Path(pdfs_directory_path).iterdir() if p.is_file()]
    Path(images_directory_path).mkdir(parents=True, exist_ok=True)
    number_images_output = 0
    for pdf_path in pdfs:
        with open(pdf_path, "rb") as pdf_stream:
            pdf_bytes = pdf_stream.read()
        with fitz.open(stream=pdf_bytes, filetype="pdf") as document:
            number_pages = len(document)
            for index in range(number_pages):
                images = document.get_page_images(index)
                for index_image, image in enumerate(images):
                    xref = image[0]
                    image_pix = fitz.Pixmap(document, xref)
                    image_bytes_io = BytesIO(convert_pixmap_to_rgb(image_pix).tobytes())
                    filename = f"{pdf_path.stem}_page{index}_index{index_image}.png"
                    number_images_output += 1
                    with open(Path(images_directory_path) / filename, "wb") as file_stream:
                        file_stream.write(image_bytes_io.getbuffer())

    return ExtractImagesResult(
        number_files_input=len(pdfs),
        number_images_output=number_images_output
    )
