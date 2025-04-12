import os
from fluix.core.optimize_image import optimize_image
from fluix.core.optimize_pdf import optimize_pdf  # you'll build this later
from fluix.core.utils import msg
import mimetypes

def run_optimize(input_path: str,
                 output_path: str,
                 scale: float = 1.0,
                 grayscale: bool = False,
                 mode: str = "",
                 **kwargs):

    ext = os.path.splitext(input_path)[-1].lower()
    if ext == "" or ext == None:
        msg.error("No file extension found for the file")
        exit(-1)

    valid_img_mimetypes = [
            "image/png",
            "image/jpeg",
            "image/bmp",
            "image/webp",
            "image/tiff"
        ]

    valid_img_extensions = [
        ".png",
        ".jpg",
        ".jpeg",
        ".bmp",
        ".webp",
        ".tiff"
    ]

    if ext in valid_img_extensions:
        # TODO: Add batch processing to images later
        def get_img_size(path):
            return os.path.getsize(path)/(1024*1024) if os.path.exists(path) else 0
        size_before = get_img_size(input_path)

        if mode == "hard":
            print("Applying hard optimization mode...")
            if scale == 1.0:
                scale = 0.8
            extra = {
                "strip_alpha": True,
                "quantize": 64,
                "strip_meta": True
            }
        else:
            extra = {}

        optimize_image(input_path=input_path,output_path=output_path, scale=scale, grayscale=grayscale,**extra)

        size_after = get_img_size(output_path)
        print(f"Optimized the image {input_path} to {output_path}")
        print(f"File size: {size_before:.2f} MB → {size_after:.2f} MB")
        print(f"Reduced by: {size_before - size_after:.1f} MB")

    elif ext == ".pdf":
        optimize_pdf(input_path, output_path)
    else:
        msg.error(f"Unsupported file type: {ext}")
        exit(0)
