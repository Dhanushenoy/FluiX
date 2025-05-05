import os
from fluix.core.animate import images_to_video

def run_animate(folder: str,
                output_path: str,
                fps: int = 30,
                frame_range = None,
                quality: int = 10,
                codec: str = 'libx264',
                resize: str = "none"):
    print("Animating your frames....")
    images_to_video(
        input_dir=folder,
        output_path=output_path,
        fps=fps,
        frame_range=frame_range,
        quality=quality,
        codec=codec,
        resize=resize
    )
