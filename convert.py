#!/usb/bin/python
import argparse
import tempfile
from subprocess import call
import sys

WIDTH=768
HEIGHT=972

def produce_png(file, width, height):
	size = max(width, height)
	resulting_file = '%s.png' % file
	#tmp = tempfile.gettempdir()
	tmp = '.'
	return_code = call(['qlmanage', '-t', '-o', tmp,  '-s %s' % size, file])
	if (return_code == 0):
		adjust_png(resulting_file, width,height)
	

def adjust_png(file, width, height):
	resulting_file = file.replace('.svg', '')
	shave = (max(width, height) - min(width, height)) / 2
	if (width > height):
		# shave from tops
		shave_geometry = "0x%s!" % shave
	else:
		shave_geometry = "%sx0!" % shave
	return_code = call(['convert', '-shave', shave_geometry, file, resulting_file])


def main(argv):
	parser = argparse.ArgumentParser(description='Processes SVG.')
	parser.add_argument('-g', '--geometry', dest='geometry', default='%sx%s' % (WIDTH, HEIGHT),
			help='Geometry in width x height')
	parser.add_argument('files', metavar='FILE', nargs='+', help='Name of SVG file.')

	args = parser.parse_args(argv)

	width, height = args.geometry.upper().split('X')
	width, height = int(width),int(height)

	for f in args.files:
		produce_png(f, width, height) 


if __name__ == "__main__":
	main(sys.argv[1:])
