# afr_lerp

Linearly interpolates each cell pair in 'map1_path' & 'map2_path' between 'lerp_start' and 'lerp_end', and outputs the result in 'output_path'.

Map files are text files in "tab separated variable" format. This format can be copy-pasted from and to Excel.

The top line of each tsv file is ignored and should be used as a comment.

There should be an empty new line at the bottom of each tsv file.
See "example_map.tsv".

Usage:
   ```python3 afr_lerp.py <map1_path> <map2_path> <output_path> <lerp_start> <lerp_end>```
