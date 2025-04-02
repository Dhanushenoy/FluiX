import argparse
from fluix.cmds.anim_cmd import run_animate
import os

def main():
    parser = argparse.ArgumentParser(prog='pyfx')
    subparsers = parser.add_subparsers(dest='command')

    animate = subparsers.add_parser('animate', help='Create animations (gif/mp4) from images')
    animate.add_argument('--folder', type=str, help='Folder with image frames. If not given, current directory is taken. \n Important!!! Needs the following format :\n pic.0000.png \n pic.0001.png \n pic.0002.png \n ... \n pic.xxxx.png')
    animate.add_argument('--output', type=str, required=True, help='Output file (eg. out.mp4 or out.gif). Also takes the output directory as prefix.')
    animate.add_argument('--fps', type=int, default=30, help='Frames per second. Default is 30')
    animate.add_argument('--range', type=int, default=None, help='Frame ranges to use, in the form start:end (eg. 20:180)' )
    animate.add_argument('--quality', type=int, default=10, help='Render quality (1-10)')
    animate.add_argument('--codec', type=str, default='libx264', help="FFmpeg codec to use (eg. libx264)")

    args = parser.parse_args()
    frame_range = None
    if args.range:
        try:
            start_str, end_str = args.range.split(':')
            frame_range = (int(start_str), int(end_str))
        except ValueError:
            print("Invalid range format. Use start:end (e.g., 20:240)")
            return

    # Animate
    if args.command == 'animate':
        folder = args.folder or os.getcwd()
        run_animate(
            folder=folder,
            output_path=args.output,
            fps=args.fps,
            limit=args.limit,
            quality=args.quality,
            codec=args.codec
        )

