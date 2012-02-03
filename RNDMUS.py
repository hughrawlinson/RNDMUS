# RNDMUS
# A granular audio mashup generator
# Copyright Code O'Clock, 2012

import wave
import random

def process(inputFile,outputFile,grainLength,sampLength):
	"""Processes the mashup and saves based on input parameters
	inputFile: The file to process
	outputFile: The file to save the processed audio to
	grainLength: The length of a grain in milliseconds
	clipLength: The length of the output file in milliseconds"""
	#define input file, output file, instantiate a dataset
	location = wave.open(inputFile, 'r')
	destination = wave.open(outputFile, 'w')
	dataset = []
		
	#set ouptut file's parameters
	destination.setnchannels(location.getnchannels())
	destination.setframerate(location.getframerate())
	destination.setsampwidth(location.getsampwidth())

	#define clipLength and sampleLength
	clipLengthInSamps = location.getframerate() * sampLength / 1000
	grainLengthInSamps = location.getframerate() * grainLength / 1000
	
	if (clipLengthInSamps % grainLengthInSamps != 0):
		clipLengthInSamps = clipLengthInSamps - (clipLengthInSamps % grainLengthInSamps) + grainLengthInSamps
		
	#loop through file, getting sampLength clips and appending them to dataset
	for i in range(1, (clipLengthInSamps/grainLengthInSamps)):
		location.setpos(random.randint(0, location.getnframes() - clipLengthInSamps))
		dataval = location.readframes(grainLengthInSamps)
		dataset.append(dataval)

	#join dataset and write to destination
	valuestr = ''.join(dataset)
	destination.writeframesraw(valuestr)
		
if __name__ == "__main__":
    import sys
    process(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    
		