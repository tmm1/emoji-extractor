# stolen from
# https://github.com/tmm1/emoji-extractor/blob/master/emoji_extractor.rb stolen
# largely from http://www.ruby-forum.com/topic/140784

import struct
import io
import os
import re

n = 0
prev = None


def extract_chunk(font_file, output):
    lenword = font_file.read(4)
    length = struct.unpack('>I', lenword)[0]
    the_type = font_file.read(4)
    data = font_file.read(length) if length > 0 else ""
    crc = font_file.read(4)
    if length < 0 or not chr(the_type[0]).isalpha():
        return None, None
    # if not validate_crc(the_type + data, crc):
    #     return None
    output.write(lenword)
    output.write(the_type)
    if data:
        output.write(data)
    output.write(crc)
    return [the_type, data]


def extract_png(font_file):  # sourcery skip: raise-specific-error
    global prev
    global n

    print(n)
    buf = io.BytesIO()
    hdr = font_file.read(8)
    if hdr[:4] != b'\x89PNG':
        raise Exception("Not a PNG File")
    if hdr[4:8] != b'\r\n\x1a\n':
        raise Exception("file not in binary mode")
    buf.write(hdr)
    print(buf.read())

    height, width = 0, 0

    while True:
        chunk_type, chunk_data = extract_chunk(font_file, buf)
        if chunk_type == b'IHDR':  # 'IHDR'
            height, width = struct.unpack('>II', chunk_data[:8])
            print(f"h: {height}, w: {width}")
        if chunk_type is None or chunk_type == b'IEND':
            break

    folder = f"eimages/{height}x{width}"
    if not os.path.exists(folder):
        os.makedirs(folder)

    if prev != folder:
        n = 0
        prev = folder
    n += 1
    buf.seek(0)
    with open(f"{folder}/{n}.png", "wb") as ofp:
        ofp.write(buf.getvalue())


# sourcery skip: raise-specific-error
with open('AppleColorEmoji-160px.ttc', 'rb') as ttf:
    ttf_data = ttf.read()

    pos = 0
    while True:
        match = re.search(b'\211PNG', ttf_data[pos:])
        if match is None:
            raise Exception("no PNG found")
        pos += match.start() + 1
        ttf.seek(pos - 1)

        extract_png(ttf)
