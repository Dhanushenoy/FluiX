# pyfx/animate.py

import os
import imageio.v2 as imageio
from typing import Optional

def images_to_video(
    input_dir: str,
    output_path: str,
    fps: int = 30,
    extensions: tuple = ('.png', '.jpg', '.jpeg', '.gif'),
    codec: str = 'libx264',
    quality: int = 10,
    frame_range: tuple = None
):
    image_files = [f for f in os.listdir(input_dir) if f.endswith(extensions)]

    try:
        image_files = sorted(image_files, key=lambda x: int(x.split('.')[1]))
    except Exception:
        image_files.sort()

    if frame_range:
        start, end = frame_range
        image_files = image_files[start:end]

    images = [imageio.imread(os.path.join(input_dir, fname)) for fname in image_files]

    if output_path.lower().endswith('.gif'):
        imageio.mimsave(output_path, images, fps=fps)
    else:
        writer = imageio.get_writer(
            output_path,
            fps=fps,
            codec=codec,
            quality=quality,
            ffmpeg_log_level='error',
            pixelformat='yuv420p'
        )
        for image in images:
            writer.append_data(image)
        writer.close()

    print(f"[pyFX] Saved animation to {output_path}")