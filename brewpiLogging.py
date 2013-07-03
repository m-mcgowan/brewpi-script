import sys
import time


def logMessage(message):
	print >> sys.stderr, time.strftime("%b %d %Y %H:%M:%S   ") + message

