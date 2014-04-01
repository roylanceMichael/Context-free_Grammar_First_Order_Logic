# Mike Roylance - roylance.michael@gmail.com
import sys
import nltk

def main():
	# const variables
	sem = "SEM"
	sentence = "I had a lunch"

	# create the parseResult builder
	parser = nltk.load_parser('file:grammar.fcfg', trace=0)

	# read in the example sentences
	tokenizedSent = nltk.word_tokenize(sentence)
	trees = parser.nbest_parse(tokenizedSent)

	if len(trees) > 0:
		#print trees[0].node[sem].simplify()
		print trees[0]

if __name__ == '__main__':
        main()