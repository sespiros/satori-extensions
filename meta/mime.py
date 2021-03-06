import binascii
import magic

from hooker import hook

__name__ = 'mime'
magic_obj = magic.Magic(flags=magic.MAGIC_MIME_TYPE)


@hook("imager.with_open")
def mime_file(satori_image, file_path, file_type, fd):
    fd.seek(0)
    chunk = fd.read(512)
    mime = magic_obj.id_buffer(chunk)
    satori_image.set_attribute(file_path, mime, __name__, force_create=True)



@hook("imager.on_end")
def clean_magic():
    magic_obj.close()
