import os
from fluix.core.optimize_image import optimize_image
from fluix.core.optimize_pdf import optimize_pdf  # you'll build this later

def run_optimize(input_path, output_path, scale=1.0, grayscale=False, mode=None, **kwargs):
    ext = os.path.splitext(input_path)[-1].lower()

    if ext in [".png", ".jpg", ".jpeg", ".bmp", ".webp", ".tiff"]:
        # Hey future, add batch processing to images later
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
        raise ValueError(f"Unsupported file type: {ext}")