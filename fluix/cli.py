import argparse
from fluix.cmds.anim_cmd import run_animate
import os

def main():
    parser = argparse.ArgumentParser(prog='fluix', description=" Modular Python utilities for scientific post-processing: plotting, animations, and flow visualization.")
    subparsers = parser.add_subparsers(dest='command',required=True)

    ###############################
    #
    #       Animate
    #
    ###############################
    animate = subparsers.add_parser('animate', help='Create animations (gif/mp4) from images')
    animate.add_argument('--folder', required=True, type=str, help='Name of the folder with image frames. Important!!! The files in the directory require the following format :\n pic.0000.png \n pic.0001.png \n pic.0002.png \n ... \n pic.xxxx.png')
    animate.add_argument('--output', type=str, required=True, help='Output file (eg. out.mp4 or out.gif). Also takes the output directory as prefix.')
    animate.add_argument('--fps', type=int, default=30, help='Frames per second. Default is 30')
    animate.add_argument('--range', type=str, default=None, help='Frame ranges to use, in the form start:end (eg. 20:180)' )
    animate.add_argument('--quality', type=int, default=10, help='Render quality (1-10)')
    animate.add_argument('--codec', type=str, default='libx264', help="FFmpeg codec to use (eg. libx264)")
    animate.add_argument('--resize',
                         type=str,
                         choices = ["none", "max", "min"],
                         default="none",
                         help="Resize all the images to a certain dimension.\n"
                         "The value can be one of:\n"
                         "none - input images are untouched\n"
                         "max - input images are resized to the dimensions of the image having the maximum dimension\n"
                         "min - input images are resized to the dimensions of the image having the minimum dimension"
                         )


    ###############################
    #
    #       Image optim
    #
    ###############################
    opt = subparsers.add_parser("optimize", help="Auto optimize image or PDF")
    opt.add_argument("--input", required=True, help="Path to image or pdf. It autodetects based on the extension")
    opt.add_argument("--output", required=True, help="Output path and the name")
    opt.add_argument("--scale", type=float, default=1.0, help="Scale the image")
    opt.add_argument("--gray", action="store_true")
    opt.add_argument("--quality", type=int, default=85, help="JPEG/WebP quality (1-100)")
    opt.add_argument("--mode", choices=["hard"], help="Apply aggressive size reduction")

    args = parser.parse_args()
    if args.command == "animate":
        from fluix.cmds.anim_cmd import run_animate

        frame_range = None
        if args.range:
            try:
                start_str, end_str = args.range.split(":")
                start = int(start_str) if start_str else None
                end = int(end_str) if end_str else None
                frame_range = (start, end)
            except ValueError:
                print("Invalid --range format. Use start:end")
                exit()

        run_animate(
            folder=args.folder,
            output_path=args.output,
            fps=args.fps,
            frame_range=frame_range,
            resize=args.resize
        )

    elif args.command == "optimize":
        from fluix.cmds.optim_cmd import run_optimize

        run_optimize(
            input_path=args.input,
            output_path=args.output,
            scale=args.scale,
            grayscale=args.gray,
            mode=args.mode
        )
