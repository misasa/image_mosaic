# python package -- image_mosaic

A series of image utilities.  Use this ImageMosaic to crop, rotate, or
enlarge bitmap images.  This package was developed as [python package
-- opencvtool](https://gitlab.misasa.okayama-u.ac.jp/pythonpackage/opencvtool)
until 2018-08.

See [gem package -- vstool](https://gitlab.misasa.okayama-u.ac.jp/gems/vstool/tree/master) that refers to this package.
See [gem package -- opencvtool](https://gitlab.misasa.okayama-u.ac.jp/gems/opencvtool/tree/master) that refers to this package.


# Dependency

## [opencv](http://opencv.org/downloads.html "download and DOS> copy C:\opencv\build\python\2.7\x86\cv2.pyd C:\Python27\Lib\site-packages")


# Installation

Install it as Administrator as:

    ADMIN.CMD> pip install git+https://github.com/misasa/image_mosaic.git

    ADMIN.CMD> pip list
    ADMIN.CMD> pip uninstall opencvtool
    $ wget https://github.com/misasa/image_mosaic/archive/master.zip
    ADMIN.CMD> pip install master.zip

Successful installation is confirmed by:

    CMD> image-warp --help

# Commands

Commands are summarized as:

| command             | description                                                               | note |
| ------------------- | ------------------------------------------------------------------------- | ---- |
| affine_from_points  | No description available                                                  |      |
| blend-image         | Blend two images using alpha blend techniques                             |      |
| crop_image          | No description available                                                  |      |
| h_from_points       | No description available                                                  |      |
| haffine_from_params | No description available                                                  |      |
| haffine_from_points | No description available                                                  |      |
| image-get-affine    | Calculate affine_ij2vs, affine_xy2vs, and anchors_xy                      |      |
| image-warp-clicks   | Transform imagefile by matching three coordinates                         |      |
| image-warp          | Transform imagefile based on Affine matrix stored in imageometry file.    |      |
| image_in_image      | No description available                                                  |      |
| make_tiles          | No description available                                                  |      |
| transform_image     | No description available                                                  |      |
| transform_points    | No description available                                                  |      |
| warp_image          | Transform an image based on parameters of angle, magnification, and shift |      |


# Usage

See online document with option `--help`.
