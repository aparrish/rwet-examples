from textblob import TextBlob
import sys

# stdin's read() method just reads in all of standard input as a string;
text = sys.stdin.read().decode('ascii', errors="replace")
blob = TextBlob(text)

for sentence in blob.sentences:
	if len(sentence.words) <= 5:
		print sentence.replace("\n", " ")

