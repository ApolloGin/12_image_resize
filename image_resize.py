from PIL import Image
import argparse
import os


def resize_image(
        path_to_original, path_to_result, 
        width=None, height=None, scale=None):
    message = ''
    im = Image.open(path_to_original)
    try:
        new_size = get_new_size(im.size, width, height, scale)
    except Exception as e:
        message = repr(e)
    else:
        if not proportions_are_met(im.size, new_size):
            message = 'WARNING!!! New file will be created, '\
                'but image proportions are violated'
        out = im.resize(new_size)
        if not path_to_result:
            directory, full_filename = os.path.split(path_to_original)
            name, extension = os.path.splitext(full_filename)
            path_to_result = '{0}/{1}__{2}x{3}{4}'.format(
                directory,
                name,
                new_size[0],
                new_size[1],
                extension
            )
        out.save(path_to_result)
        return message + '\nFile created successfully'
    return message + '\nFile is not created.'


def get_new_size(size, width=None, height=None, scale=None):
    if scale:
        if width is not None or height is not None:
            raise ValueError('When scale is defined,'\
                ' width and height should not be determined'
            )
            return None
        return tuple(map(lambda x: int(x*scale), size))
    if width is None and height is None:
        return size
    if width is None and height is not None:
        return (size[0] * height // size[1], height)
    if width is not None and height is None:
        return (width, size[1] * width // size[0])
    return (width, height)


def proportions_are_met(size1, size2):
    return abs(size1[0] / size1[1] - size2[0] / size2[1]) == 0

    
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the source image')
    parser.add_argument('-w', '--width',
        type=int,
        help='width of the resulting image'
    )
    parser.add_argument('-ht', '--height',
        type=int,
        help='height of the resulting image'
    )
    parser.add_argument('-s', '--scale',
        type=float,
        help='how many times increse (>1) or decrese (<1) image'
    )
    parser.add_argument('-o', '--output',
        help='path to the result file'
    )
    args = parser.parse_args()
    return {
        'input': args.input,
        'width': args.width,
        'height': args.height,
        'scale': args.scale,
        'output': args.output
    }


if __name__ == '__main__':
    arguments = get_arguments()
    print(resize_image(
        arguments['input'],
        arguments['output'],
        arguments['width'],
        arguments['height'],
        arguments['scale']
    ))