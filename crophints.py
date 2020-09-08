import argparse
import io
import pathlib

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw, ImageColor
import subprocess
import fire

def get_crop_hints(path,ratios):
    """Detect crop hints on a single image and return the first result."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    crop_hints_params = types.CropHintsParams(aspect_ratios=ratios)
    image_context = types.ImageContext(crop_hints_params=crop_hints_params)

    response = client.crop_hints(image=image, image_context=image_context)
    hints = response.crop_hints_annotation.crop_hints

    # Get bounds for the first crop hint using an aspect ratio of 1.77.
    vertices = ( a.bounding_poly.vertices for a in hints )

    return vertices


def draw_hint(image_file,ratios=[1],template="{path.parent}/../cropped/{path.stem}-crophints.png"):
    """Draw a border around the image using the hints in the vector list."""
    vectsl = get_crop_hints(image_file,ratios)

    b = Image.open(image_file)
    back = b.convert("RGBA")

    for vects,col in zip(vectsl,('red','green','blue','yellow','purple','white')) :
        fore = Image.new('RGBA',back.size,(255,255,255,0))
        draw = ImageDraw.Draw(fore)
        bgc  = [a for a in ImageColor.getrgb(col)]
        bgc.append(50)
        draw.polygon([
            vects[0].x, vects[0].y,
            vects[1].x, vects[1].y,
            vects[2].x, vects[2].y,
            vects[3].x, vects[3].y],
            fill=tuple(bgc),
            outline=col)
        back.paste(fore,mask=fore)
    p=pathlib.Path(image_file)
    output_file=template.format(path=p)
    back.save(output_file,mode="RGBA")
    subprocess.run(["eog", "-f", output_file])


def crop_to_hint(image_file):
    """Crop the image using the hints in the vector list."""
    vects = get_crop_hint(image_file)

    im = Image.open(image_file)
    im2 = im.crop([vects[0].x, vects[0].y,
                  vects[2].x - 1, vects[2].y - 1])
    im2.save('output-crop.jpg', 'JPEG')


if __name__ == '__main__':
    fire.Fire(draw_hint)
