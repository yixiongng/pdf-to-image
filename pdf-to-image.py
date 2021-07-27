from pdf2image import *
import argparse
import os
import timeit
start = timeit.default_timer()
ap = argparse.ArgumentParser()
ap.add_argument("--pdf", required=True,
	help="path to input image that we'll align to template")
args = vars(ap.parse_args())

pages=convert_from_path(args["pdf"])
base=os.path.basename(args["pdf"])
imgname = os.path.splitext(base)[0]
parent_path = "./"
directory = imgname
path = os.path.join(parent_path, imgname)
os.mkdir(path)
for index, page in enumerate(pages):
	page.save(path + "/" + imgname + '_' + str(index) + '.jpg', 'JPEG')

stop = timeit.default_timer()

print('Time: ', stop - start)  
