import os
import glob
import re

def makepvd(pattern, output):
    files = sorted(glob.glob(pattern))
    if not files:
        print(f"[FluiX] No files matching pattern : {pattern}")
        return
    
    common_prefix = os.path.commonpath(files)
    rel_files = [os.path.relpath(f, start=os.path.dirname(output)) for f in files]

    # Extract timestep numbers from filenames
    timestep_list = []
    for f in rel_files:
        match = re.search(r'(\d+)', os.path.basename(f))
        if match:
            timestep = int(match.group(1))
            timestep_list.append(timestep)
        else:
            timestep_list.append(0)  # fallback if no number

    header = """<VTKFile type="Collection" version="0.1" byte_order="LittleEndian">
  <Collection>"""
    
    footer = """  </Collection>
</VTKFile>"""

    datasets = ""
    for f, timestep in zip(rel_files, timestep_list):
        datasets += f'    <DataSet timestep="{timestep}" group="" part="0" file="{f}"/>\n'

    with open(output, 'w') as f:
        f.write(header + "\n")
        f.write(datasets)
        f.write(footer)

    print(f"[FluiX] Generated {output} with {len(files)} files.")
