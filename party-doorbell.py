import telnetlib # Needed to connect to fhem server for sensor triggers
import os        # Needed to execute aplay to play the sounds

HOST = "localhost" # We'll connect to this computer
PORT = 7072        # on fhem's default telnet port

tn = telnetlib.Telnet() # Create an instance of a telnet object
tn.open(HOST,PORT)      # Connect to the fhem server on this machine

tn.write("inform on\n") # fhem's command to spit out the data it gets

entranceSoundFile = None

while True:
	output = tn.read_until("\n") # When there's a carriage return from telnet, store the line that came in
	if "channel" in output:      # For any button press, process it:
		os.system('aplay doorbell.wav &')  #Play the doorbell.wav
		if "A0" in output:
			print "Button 1 Pressed."
			entranceSoundFile = "1.wav"
		if "AI" in output:
			print "Button 2 Pressed."
			entranceSoundFile = "2.wav"
		if "B0" in output:
			print "Button 3 Pressed."
			entranceSoundFile = "3.wav"
		if "BI" in output:
			print "Button 4 Pressed."
			entranceSoundFile = "4.wav"
	if "contact" in output:
		if "open" in output:
			print "Door opened."
			if entranceSoundFile is not None:
				print "I'll play: ", entranceSoundFile
				os.system('aplay ' + entranceSoundFile + ' &')
				entranceSoundFile = None
			else:
				print "No doorbell selected."
