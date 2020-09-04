
import sys

def load_map(filename: str):  # returns row-major 2-dim array or floats e.g. 'map: [float][float]'

    with open(filename) as file:
        lines = file.readlines()[1:]  # chop off the first (comment) line
        rows = [None] * 20
        l = 0
        while l < len(lines)-1:
            rows[l] = [None] * 20
            line = lines[l]
            cells = line.split("\t")
            c = 0
            while c < len(cells):
                cell = float(cells[c])
                rows[l][c] = cell
                c += 1
            l += 1
    return rows

def lerp(map1, map2, a, b):

    out = [None] * 20
    r = 0
    while r < 20:
        out[r] = [None] * 20
        s = a + ((b - a) * (float(r)/float(20)))
        c = 0
        while c < 20:
            out[r][c] = map1[r][c] + ((map2[r][c] - map1[r][c]) * s)
            c += 1
        r += 1
    return out

def write_to_disk(map, filename):

    out = ""
    r = 0
    while r < 20:
        c = 0
        while c < 20:
            out += str(round(map[r][c], 2))
            if c != 20:
                out += "\t"
            c += 1
        out += "\n"
        r += 1

    with open(filename, "w") as file:
        file.write(out)

def main(map1_path, map2_path, lerped_path, a, b):

    map1 = load_map(map1_path)
    map2 = load_map(map2_path)
    lerped = lerp(map1, map2, float(a), float(b))

    write_to_disk(lerped, lerped_path)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
