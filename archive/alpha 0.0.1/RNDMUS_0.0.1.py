#!/usr/bin/python
import sys, wave, random

def out(a):
	a = a.upper()
	print("|| " + a + " ||")

#RNDMUS
#An audio file masher script
#Copyright Hugh Rawlinson, 2012

FileLocation = sys.argv[1]
FileDestination = sys.argv[2]

lenPerCycleMs = 50

def go(destination, location, tenMsLen):
	dataset = []
	
	destination.setnchannels(location.getnchannels())
	destination.setframerate(location.getframerate())
	destination.setsampwidth(location.getsampwidth())
	
	nframes = location.getnframes()
	thirtySec = (location.getframerate() * 30)/tenMsLen + 50
	
	for i in range(1, thirtySec):
		location.setpos(random.randint(0,nframes - tenMsLen))
		dataval = location.readframes(tenMsLen)
		dataset.append(dataval)
		
	valuestr = ''.join(dataset)
	destination.writeframesraw(valuestr)
	

message = "RNDMUS by Raw Software"
out(message)

message = "RNDMUS will now mash up "
out(message)

location = wave.open(FileLocation, 'r')
destination = wave.open(FileDestination, 'w')

#fr =  location.getframerate()

#message = "Framerate is " . fr
#out(message)

a = 0.005

if (location.getframerate() == 48000):
	framesPerCycle = int(48000 * a)

elif (location.getframerate() == 44100):
	framesPerCycle = int(44100 * a)

else:
	message = "RNDMUS does not support sample rates other than 48k and 44.1k. Yet."
	out(message)
	
print framesPerCycle
	
go(destination, location, framesPerCycle)

destination.close()
location.close()

message = "done"

out(message)