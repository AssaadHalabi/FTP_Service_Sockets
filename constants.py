# Assaad El Halabi, 201907829, Globals and templates. I am the sole creator of this beautiful project

from string import Template

FILEDIR = './files'


SUCCESSFUL_PUT_TEMPLATE = Template('$filename has been uploaded successfully.')
SUCCESSFUL_CHANGE_TEMPLATE = Template('$filename has been changed into $new_filename.')
SUCCESSFUL_GET_TEMPLATE = Template('$filename has been downloaded successfully.')
