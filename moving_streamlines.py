# -*- coding: utf-8 -*-
"""
Created on Tue May 02 21:27:26 2017

@author: Kelly Kochanski
03-May-2017
Example from this code: www.youtube.com/watch?v=h1dlnW1lmgc
Inspiration: NASA Perpetual Ocean, www.youtube.com/watch?v=CCmTY0PKGDs
Tested on VisIT 2.10

Script to create moving streamlines in VisIT.
 - Randomly seed a box (dimensions specified inside set_stream_length) with short streamlines
 - Save a series of images showing the streamlines growing over time.
 - As streamlines approach the maximum length, their opacity decreases and they gradually fade out before being replaced with new, smaller streamlines.

Set user parameters and number of streamlines in main()
Create or modify the function savePNG() with correct output directories, file format, etc

Color table : recommend fade from neutral to bright to and optionally back to neutral color
Example uses lilac [136 136 178] to off-white [253 248 255] to grey [82 82 82]
"""


def set_stream_length(streamtime, seed, options):
	(max_streamtime, boxExtents, colorTable, nStreamlines) = options
	print 'setting stream length'
	opacity = max( min(max_streamtime - max_streamtime/2, 1), 0)
	StreamlineAtts = StreamlineAttributes()
	StreamlineAtts.sourceType = StreamlineAtts.SpecifiedBox  # SpecifiedPoint, 	SpecifiedPointList, SpecifiedLine, SpecifiedCircle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection
	StreamlineAtts.pointSource = (0, 0, 0)
	StreamlineAtts.lineStart = (0, 0, 0)
	StreamlineAtts.lineEnd = (1, 0, 0)
	StreamlineAtts.planeOrigin = (0, 0, 0)
	StreamlineAtts.planeNormal = (0, 0, 1)
	StreamlineAtts.planeUpAxis = (0, 1, 0)
	StreamlineAtts.radius = 1
	StreamlineAtts.sphereOrigin = (0, 0, 0)
	StreamlineAtts.boxExtents = boxExtents
	StreamlineAtts.useWholeBox = 0
	StreamlineAtts.pointList = (0, 0, 0, 1, 0, 0, 0, 1, 0)
	StreamlineAtts.sampleDensity0 = 20
	StreamlineAtts.sampleDensity1 = 20
	StreamlineAtts.sampleDensity2 = 1
	StreamlineAtts.coloringMethod = StreamlineAtts.ColorByTime  # Solid, ColorBySpeed, 	ColorByVorticity, ColorByLength, ColorByTime, ColorBySeedPointID, ColorByVariable, 	ColorByCorrelationDistance, ColorByNumberDomainsVisited
	StreamlineAtts.colorTableName = colorTable
	StreamlineAtts.singleColor = (0, 0, 0, 255)
	StreamlineAtts.legendFlag = 0
	StreamlineAtts.lightingFlag = 0
	StreamlineAtts.integrationDirection = StreamlineAtts.Forward  # Forward, Backward, Both
	StreamlineAtts.maxSteps = 100
	StreamlineAtts.terminateByDistance = 0
	StreamlineAtts.termDistance = 2
	StreamlineAtts.terminateByTime = 1
	StreamlineAtts.termTime = streamtime
	StreamlineAtts.maxStepLength = 0.1
	StreamlineAtts.limitMaximumTimestep = 1
	StreamlineAtts.maxTimeStep = 0.1
	StreamlineAtts.relTol = 0.0001
	StreamlineAtts.absTolSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	StreamlineAtts.absTolAbsolute = 1e-06
	StreamlineAtts.absTolBBox = 1e-06
	StreamlineAtts.fieldType = StreamlineAtts.Default  # Default, FlashField, M3DC12DField, M3DC13DField, Nek5000Field, NIMRODField
	StreamlineAtts.fieldConstant = 1
	StreamlineAtts.velocitySource = (0, 0, 0)
	StreamlineAtts.integrationType = StreamlineAtts.DormandPrince  # Euler, Leapfrog, DormandPrince, AdamsBashforth, RK4, M3DC12DIntegrator
	StreamlineAtts.parallelizationAlgorithmType = StreamlineAtts.VisItSelects  # LoadOnDemand, ParallelStaticDomains, MasterSlave, VisItSelects
	StreamlineAtts.maxProcessCount = 10
	StreamlineAtts.maxDomainCacheSize = 3
	StreamlineAtts.workGroupSize = 32
	StreamlineAtts.pathlines = 0
	StreamlineAtts.pathlinesOverrideStartingTimeFlag = 0
	StreamlineAtts.pathlinesOverrideStartingTime = 0
	StreamlineAtts.pathlinesPeriod = 0
	StreamlineAtts.pathlinesCMFE = StreamlineAtts.POS_CMFE  # CONN_CMFE, POS_CMFE
	StreamlineAtts.coordinateSystem = StreamlineAtts.AsIs  # AsIs, CylindricalToCartesian, CartesianToCylindrical
	StreamlineAtts.phiScalingFlag = 0
	StreamlineAtts.phiScaling = 1
	StreamlineAtts.coloringVariable = "windMag"
	StreamlineAtts.legendMinFlag = 1
	StreamlineAtts.legendMaxFlag = 0
	StreamlineAtts.legendMin = 0
	StreamlineAtts.legendMax = 0.4
	StreamlineAtts.displayBegin = 0
	StreamlineAtts.displayEnd = 1
	StreamlineAtts.displayBeginFlag = 0
	StreamlineAtts.displayEndFlag = 0
	StreamlineAtts.referenceTypeForDisplay = StreamlineAtts.Distance  # Distance, Time, Step
	StreamlineAtts.displayMethod = StreamlineAtts.Lines  # Lines, Tubes, Ribbons
	StreamlineAtts.tubeSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	StreamlineAtts.tubeRadiusAbsolute = 0.125
	StreamlineAtts.tubeRadiusBBox = 0.0001
	StreamlineAtts.ribbonWidthSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	StreamlineAtts.ribbonWidthAbsolute = 0.125
	StreamlineAtts.ribbonWidthBBox = 0.01
	StreamlineAtts.lineWidth = 1
	StreamlineAtts.showSeeds = 0
	StreamlineAtts.seedRadiusSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	StreamlineAtts.seedRadiusAbsolute = 1
	StreamlineAtts.seedRadiusBBox = 0.015
	StreamlineAtts.showHeads = 0
	StreamlineAtts.headDisplayType = StreamlineAtts.Sphere  # Sphere, Cone
	StreamlineAtts.headRadiusSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	StreamlineAtts.headRadiusAbsolute = 0.25
	StreamlineAtts.headRadiusBBox = 0.02
	StreamlineAtts.headHeightRatio = 2
	StreamlineAtts.opacityType = StreamlineAtts.Constant  # FullyOpaque, Constant, Ramp, VariableRange
	StreamlineAtts.opacityVariable = "windMag"
	StreamlineAtts.opacity = opacity
	StreamlineAtts.opacityVarMin = 0
	StreamlineAtts.opacityVarMax = 5
	StreamlineAtts.opacityVarMinFlag = 1
	StreamlineAtts.opacityVarMaxFlag = 1
	StreamlineAtts.tubeDisplayDensity = 10
	StreamlineAtts.geomDisplayQuality = StreamlineAtts.Medium  # Low, Medium, High, Super
	StreamlineAtts.sampleDistance0 = 10
	StreamlineAtts.sampleDistance1 = 10
	StreamlineAtts.sampleDistance2 = 10
	StreamlineAtts.fillInterior = 1
	StreamlineAtts.randomSamples = 1
	StreamlineAtts.randomSeed = seed
	StreamlineAtts.numberOfRandomSamples = nStreamlines
	StreamlineAtts.forceNodeCenteredData = 0
	StreamlineAtts.issueTerminationWarnings = 1
	StreamlineAtts.issueStiffnessWarnings = 1
	StreamlineAtts.issueCriticalPointsWarnings = 1
	StreamlineAtts.criticalPointThreshold = 0.001
	StreamlineAtts.varyTubeRadius = StreamlineAtts.Scalar  # None, Scalar
	StreamlineAtts.varyTubeRadiusFactor = 10
	StreamlineAtts.varyTubeRadiusVariable = "windMag"
	StreamlineAtts.correlationDistanceAngTol = 5
	StreamlineAtts.correlationDistanceMinDistAbsolute = 1
	StreamlineAtts.correlationDistanceMinDistBBox = 0.005
	StreamlineAtts.correlationDistanceMinDistType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	StreamlineAtts.selection = ""
	SetPlotOptions(StreamlineAtts)

def savePNG():
	SaveWindowAtts = SaveWindowAttributes()
	SaveWindowAtts.outputToCurrentDirectory = 1
	SaveWindowAtts.outputDirectory = "."
	SaveWindowAtts.fileName = "visit"
	SaveWindowAtts.family = 1
	SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
	SaveWindowAtts.width = 1024
	SaveWindowAtts.height = 1024
	SaveWindowAtts.screenCapture = 0
	SaveWindowAtts.saveTiled = 0
	SaveWindowAtts.quality = 80
	SaveWindowAtts.progressive = 0
	SaveWindowAtts.binary = 0
	SaveWindowAtts.stereo = 0
	SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
	SaveWindowAtts.forceMerge = 0
	SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, 	EqualWidthHeight, ScreenProportions
	SaveWindowAtts.advancedMultiWindowSave = 0
	SetSaveWindowAttributes(SaveWindowAtts)
	SaveWindow()
	SaveWindowAtts = SaveWindowAttributes()
	SaveWindowAtts.outputToCurrentDirectory = 0
	SaveWindowAtts.outputDirectory = "/projects/scivizclass/Submissions/keko1352/Project/Streamlines/Antarctica"
	SaveWindowAtts.fileName = "wind_plates_201007_plates"
	SaveWindowAtts.family = 1
	SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
	SaveWindowAtts.width = 1024
	SaveWindowAtts.height = 1024
	SaveWindowAtts.screenCapture = 0
	SaveWindowAtts.saveTiled = 0
	SaveWindowAtts.quality = 80
	SaveWindowAtts.progressive = 0
	SaveWindowAtts.binary = 0
	SaveWindowAtts.stereo = 0
	SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
	SaveWindowAtts.forceMerge = 0
	SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
	SaveWindowAtts.advancedMultiWindowSave = 0
	SetSaveWindowAttributes(SaveWindowAtts)
	SaveWindow()

def main():
	# User-set parameters
	max_streamtime = 1.7 # maximum length in time of any streamline
	box_extents = (0, 360, -90, -40, 28, 29) # Streamlines are only generated in this region. Format: (minx, maxx, miny, maxy, minz, maxz)
	colorTable = "windagain" # String specifying name of color table.
	nFrames = 200 # number of frames to be generated
	steplength = 0.05 # increase in streamline integration time between frames
	streamlengths = [0,  0.283, 0.567, 0.85] # Initial lengths of streamlines. Require 1 entry per streamline plot. Recommend: output of numpy.linspace(0, max_streamtime, number of plots)
	nStreamlines = 650 # number of streamlines generated in each streamline plot

	# User must add the desired number of streamline plots
	# and must manually add an equal number of "SetActivePlots" commands with the correct plot numbers
	# Each streamline plot needs a different seed to generate different random distributions o streamlines.
	
	AddPlot("Streamline", "wind", 1, 0)
	AddPlot("Streamline", "wind", 1, 0)
	AddPlot("Streamline", "wind", 1, 0)
	AddPlot("Streamline", "wind", 1, 0)

	streamline_options = (max_streamtime, box_extents, colorTable, nStreamlines)

	for n in range(nFrames):
		streamlengths = [length + steplength for length in streamlengths]
		streamlengths = [length % max_streamtime for length in streamlengths]
		
		# VisIT numbers plots sequentially from 0
		# Example: if you have five background plots, and want four sets of streamlines,
		#  the streamline plots will be labelled 5 through 8.
		# Each plot has a unique random seed (numbers 11-14 in this example)
		#  and a unique index in the streamlengths vector (0 onwards).
		SetActivePlots((8, 5))
		SetActivePlots(5)
		set_stream_length(streamlengths[0], 11, streamline_options)
		SetActivePlots((5,6))
		SetActivePlots(6)
		set_stream_length(streamlengths[1], 12, streamline_options)
		SetActivePlots((6,7))
		SetActivePlots(7)
		set_stream_length(streamlengths[2], 13, streamline_options)
		SetActivePlots((7,8))
		SetActivePlots(8)
		set_stream_length(streamlengths[3], 14, streamline_options)
		
		DrawPlots()
		savePNG()

main()
		
