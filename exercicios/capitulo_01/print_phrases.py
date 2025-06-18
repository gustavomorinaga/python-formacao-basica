# This code iterates through a list of phrases and prints each one to the console, pausing for 1 second between each print.

import time

phrases = ['Hello, World!', 'Python is great!', 'I love coding!', 'Keep learning!']

for phrase in phrases:
	print(phrase)  # Print each phrase in the list
	time.sleep(1)  # Pause for 1 second before printing the next phrase
