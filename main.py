# Mike Roylance - roylance.michael@gmail.com
import sys
import nltk

def test_I_had_a_lunch():
	# arrange
	tlp = nltk.LogicParser()

	whatIwant = r''

	np = r'\P.P(john)'
	vp = r'(\X x.X(\y.drink(x,y)))'
	det = r'(\P Q.exists x.(P(x) & Q(x)))'
	np1 = r'(\x.soda(x))'

	detNp1 = str((tlp.parse(det + np1)).simplify())
	print detNp1
	vpDetNp1 = str((tlp.parse(np + vp + det + np1)).simplify())
	print vpDetNp1

def main():
	# const variables
	sem = "SEM"
	sentence = "I had a delicious lunch"

	# create the parseResult builder
	parser = nltk.load_parser('file:grammar.fcfg', trace=0)

	# read in the example sentences
	tokenizedSent = nltk.word_tokenize(sentence)
	trees = parser.nbest_parse(tokenizedSent)

	if len(trees) > 0:
		print trees[0].node[sem].simplify()
		# print trees[0]

if __name__ == '__main__':
        main()
        # test_I_had_a_lunch()