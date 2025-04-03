import imageio.v3 as iio
import numpy as np
from scipy.ndimage import zoom
import os

import imageio.v3 as iio
import numpy as np
from scipy.ndimage import zoom
import os

def optimize_image(input_path, output_path, scale=1.0, grayscale=False, quality=25,
                   strip_alpha=False, quantize=None, strip_meta=False):
    ext = os.path.splitext(output_path)[-1][1:].lower()
    img = iio.imread(input_path)

    # Grayscale
    if grayscale and img.ndim == 3:
        img = img.mean(axis=2).astype(np.uint8)

    # Resize
    if scale < 1.0:
        if img.ndim == 3:
            img = zoom(img, (scale, scale, 1), order=1)
        else:
            img = zoom(img, (scale, scale), order=1)
        img = img.astype(np.uint8)

    # Strip alpha channel
    if strip_alpha and img.ndim == 3 and img.shape[-1] == 4:
        img = img[:, :, :3]

    # Prepare kwargs before using
    kwargs = {}
    if ext in ["jpg", "jpeg", "webp"]:
        kwargs["quality"] = quality

    # Set lossy format quality
    if ext in ["jpg", "jpeg", "webp"]:
        kwargs["quality"] = quality

    # I need to add quantize later. May be using Torch?

    iio.imwrite(output_path, img, **kwargs)
