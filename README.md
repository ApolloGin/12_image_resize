# 12_image_resize

## Synopsis

Script helps to resize image

## Quick start

 - Install all requirements from file `pip3 install -r requirements.txt`
 - Before you run script you need to now about it parameters
 ..1. Path to the source image. **Must be required**
 ..2. --Width - width of the result image
 ..3. --Height - height of the result image
 ..4. --Scale - how many times increse (>1) or decrese (<1) image
 ..5. --output - path to the result file

> Note: Unless specified width - height is considered so as to preserve aspect ratio. And vice versa. - If you specify the width and height - image would be exactly that as noted. Script displaed a warning in the console, if the proportions are not the same as the original image. If you specify the scale, the width and height can not be specified. Otherwise, no resizing occurs and the script breaks to clear error. If you do not specify the path to the final file, the result is put next to the script file.

..Now you can run image_resize.py with needed parameters

As a result of script would be image which is edited copy of the original image.

**Example**

`python3.5 image_resize.py source_image.jpg --width 100 --height 100 --output result_image.jpg`
