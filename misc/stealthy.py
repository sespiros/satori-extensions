import os

from hooker import hook

__name__ = 'stealthy'

@hook("post_close")
def stealth_open(satori_image, file_path, file_type):

	time_dict = (satori_image.get_attribute(file_path, 'times'))
	os.utime(
		file_path, (
			time_dict['atime'],
			time_dict['utime']
			),
		)
	satori_image.set_attribute(file_path, hex_digest, __name__, force_create=True)
