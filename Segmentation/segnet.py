import jetson.inference
import jetson.utils

import argparse
import sys

from segnet_utils import *

parser = argparse.ArgumentParser(description="Segment a live camera stream using an semantic segmentation DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.segNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="fcn-resnet18-voc", help="pre-trained model to load, see below for options")
parser.add_argument("--filter-mode", type=str, default="linear", choices=["point", "linear"], help="filtering mode used during visualization, options are:\n  'point' or 'linear' (default: 'linear')")
parser.add_argument("--visualize", type=str, default="overlay,mask", help="Visualization options (can be 'overlay' 'mask' 'overlay,mask'")
parser.add_argument("--ignore-class", type=str, default="void", help="optional name of class to ignore in the visualization results (default: 'void')")
parser.add_argument("--alpha", type=float, default=150.0, help="alpha blending value to use during overlay, between 0.0 and 255.0 (default: 150.0)")
parser.add_argument("--stats", action="store_true", help="compute statistics about segmentation mask class output")

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)
count = 0

net = jetson.inference.segNet(opt.network, sys.argv)

net.SetOverlayAlpha(opt.alpha)

buffers = segmentationBuffers(net, opt)

input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)

while True:
	img_input = input.Capture()

	buffers.Alloc(img_input.shape, img_input.format)

	net.Process(img_input, ignore_class=opt.ignore_class)



	if buffers.overlay:
		net.Overlay(buffers.overlay, filter_mode=opt.filter_mode)

	if buffers.mask:
		net.Mask(buffers.mask, filter_mode=opt.filter_mode)
		mask = buffers.mask
		mask_np = jetson.utils.cudaToNumpy(mask)

		
	if buffers.composite:
		jetson.utils.cudaOverlay(buffers.overlay, buffers.composite, 0, 0)
		jetson.utils.cudaOverlay(buffers.mask, buffers.composite, buffers.overlay.width, 0)

	output.Render(buffers.output)

	output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))

	jetson.utils.cudaDeviceSynchronize()
	net.PrintProfilerTimes()

	if opt.stats:
		buffers.ComputeStats()
    
	if not input.IsStreaming() or not output.IsStreaming():
		break
