import javalang
import sys

def main(argv):
	file_lines = open(argv[0], "r").readlines()
	tokenized_file = open(argv[1], "w")

	for line in file_lines:
		tokens_string = ""
		try:
			tokens = list(javalang.tokenizer.tokenize(line))
			for token in tokens:
					tokens_string = tokens_string + token.value + " "
		except:
			sys.stderr.write("Tokenization failed\n")
			sys.exit(1)

		
		tokenized_file.write(tokens_string + '\n')
		
	tokenized_file.close()
	sys.exit(0)


if __name__=="__main__":
	main(sys.argv[1:])
