# -*- coding: utf-8 -*-

import os
from hooker import hook

__name__ = 'ntfs-streams'

@hook("imager.pre_open")
def find_streams(satori_image, file_path, file_type, os_context):

    if file_type == 'U' or file_type == 'F':
        command = "dir " + file_path + " /r"
        stdout = os.popen(command).read()

        stream_dict = parse_cmd(stdout)

        satori_image.set_attribute(file_path, stream_dict, __name__, force_create=True)

def parse_cmd(stdout):

    lines = stdout.splitlines()[5:-2]

    ret = {}
    for row in lines:
        try:
            filename = row.split()[-1]
        except IndexError:
            # print(row)
            continue

        if ":" not in filename:
            continue
        fname, alt_stream, stream_type = filename.split(":")
        ret[alt_stream] = stream_type

    return ret
