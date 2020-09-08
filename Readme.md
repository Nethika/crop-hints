# Google Vision Crop Hints

This python3 example is derived from the example code provided [by Google](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/cloud-client/crop_hints/crop_hints.py). 

```
  crophints.py --image-file IMAGE_FILE [--ratios RATIOS] [--template TEMPLATE]

  RATIOS is a python array of rational numbers that represents width 
         divided by height (1.5 for a 3:2 landscape image).

  TEMPLATE is a python template that can contain expressions like 
           `{path.stem}` derived from the path of the IMAGE_FILE. 
           For the full range of attributes, please refer to the 
           PurePath object documentation at 
           https://docs.python.org/3/library/pathlib.html#methods-and-properties.
```

Please see the [Makefile](./Makefile) for examples on how to process a batch of images


## Installing 

You have to get credentials (Google offers a handy JSON file) here: https://console.developers.google.com/apis/credentials. The
JSON file needs to be referenced in the GOOGLE_APPLICATION_CREDENTIALS environment variable.

[Python dependencies](requirements.txt) can be installed using `pip install -r requirements.txt`.

## Look who's allways in the crop

The red crop is 1:1 (square), the blue is 9:16 (portrait, mobile phone), the green 16:9 (landscape, computer).

| as taken | mirrored |
|---|---|
| ![](cropped/merkel-hoch-crophints.png) | ![](cropped/merkel-spiegel-crophints.png) |

