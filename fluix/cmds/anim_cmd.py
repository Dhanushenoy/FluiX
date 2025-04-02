import os
from fluix.core.animate import images_to_video

def run_animate(folder, output_path, fps=30, frame_range=None, quality=10, codec='libx264'):
    print("Animating your frames....")
    images_to_video(
        input_dir=folder,
        output_path=output_path,
        fps=fps,
        frame_range=frame_range,
        quality=quality,
        codec=codec
    )