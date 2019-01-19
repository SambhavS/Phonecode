# Phonecode problem; finished in 1 hour and 6 minutes
DIGITS = "1234567890"
to_digit = {'a': '5', 'c': '6', 'b': '7', 'e': '0', 'd': '3', 'g': '9', 'f': '4',
			'i': '6', 'h': '9', 'k': '7', 'j': '1', 'm': '5', 'l': '8', 'o': '8',
			'n': '1', 'q': '1', 'p': '8', 's': '3', 'r': '2', 'u': '7', 't': '4',
			'w': '2', 'v': '6', 'y': '3', 'x': '2', 'z': '9'}

def numify(word): 
	return "".join(to_digit[letter.lower()] for letter in word if letter.lower() in to_digit.keys())

def get_words(num, match_words):
	if not num:
		return []
	answer = []
	partitions = [(num[0:i+1], num[i+1:]) for i in range(len(num))]
	for fst, rest in partitions:
		if fst in match_words:
			words = match_words[fst]
			rest_answers = get_words(rest, match_words)
			for word in words:
				if rest:
					for rest_answer in rest_answers:
						answer.append("{} {}".format(word, rest_answer))
				else:
					answer.append(word)
	if not answer:
		if len(num) == 1:
			return [num[0]]
		other_words = get_words(num[1:], match_words)
		return ["{} {}".format(num[0], word) for word in other_words]
	return answer

def main(all_nums, all_words):
	match_words = {}
	for word in all_words:
		num = numify(word)
		if num not in match_words:
			match_words[num] = set()
		match_words[num].add(word)
	answer = []
	for og_num in all_nums:
		num = "".join(d for d in og_num if d in DIGITS)
		valid_words = []
		words = get_words(num, match_words)
		for word in words:
			tokens = word.split()
			valid = True
			for i in range(len(tokens)-1):
				if tokens[i] in DIGITS and tokens[i+1] in DIGITS:
					valid = False
			if valid:
				valid_words.append(word)
		for word in valid_words:
			answer.append("{}: {}".format(og_num, word))
	return answer

def test_run():
	all_nums = [i.strip() for i in open("input.txt").readlines()]
	all_words = [i.strip() for i in open("dict.txt").readlines()]
	correct_lines = [i.strip() for i in open("expected.txt").readlines()]
	answer = list(sorted(main(all_nums, all_words)))
	correct = list(sorted(correct_lines))
	# Test run
	matches = len([1 for a, c in zip(answer, correct) if a == c])		
	print("Matching entries: {}/{}".format(matches, len(correct)))

test_run()