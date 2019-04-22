import math
import os
import sys

def calculate_edit_distance(org_code, cand_code):
	"""
	The higher the score, the lower the similarity.
	Pay attention to \n symbol in the line
	"""
	org_parts = [part.strip() for part in org_code.split()]
	cand_parts = [part.strip() for part in cand_code.split()]

	def levenshteinDistance(s1, s2):
		if len(s1) > len(s2):
			s1, s2 = s2, s1

		distances = range(len(s1) + 1)
		for i2, c2 in enumerate(s2):
			distances_ = [i2 + 1]
			for i1, c1 in enumerate(s1):
				if c1 == c2:
					distances_.append(distances[i1])
				else:
					distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
			distances = distances_
		return distances[-1]

	return levenshteinDistance(org_parts, cand_parts)
	pass


def calculate_normalized_bow_distance(test_code, train_code):
	words = {}
	for word in test_code:
		if word not in words.keys():
			words[word] = [0, 0]
		words[word][0] += 1
	for word in train_code:
		if word not in words.keys():
			words[word] = [0, 0]
		words[word][1] += 1
	first_vector = []
	second_vector = []
	distance = 0
	for word in words.keys():
		distance += ((words[word][0] - words[word][1]) * (words[word][0] - words[word][1]))
	return math.sqrt(distance)


def get_similar_loc(org_code_file, N):
	
	if not os.path.isfile(org_code_file):
		raise ValueError("Cannot find buggy code!")

	N = int(N)
	org_code = open(org_code_file, "r").readline().strip()
	'''
	if len(line) > 1:
		print ("We only process one line bug for now.")
	'''
	#print (org_code)

	buggy_search_space = '/home/robin/Documents/buggy.token'
	patch_search_space = '/home/robin/Documents/patch.token'
	path_search_space = '/home/robin/Documents/corresponding_path.txt'
	patch_storage = "/tmp/PatchesForSimFix++"

	buggy_lines = open(buggy_search_space, 'r').readlines()
	fixed_lines = open(patch_search_space, 'r').readlines()
	file_path_lines = open(path_search_space, 'r').readlines()

	
	file_output = open('/tmp/similarity.score', 'w+')
	
	[file_output.write(str(calculate_edit_distance(org_code, line)+calculate_normalized_bow_distance(org_code, line))+'\n') for line in buggy_lines]
	file_output.close()

	score_lines = open('/tmp/similarity.score', 'r').read().splitlines()
	final_list = []
	linenum_score = list(enumerate(score_lines))

	# Get top N similar code: time complexity(N * sizeof(similarity.score))
	for i in range(0, N):
		min1 = (-1, '10000000')

		for j in range(len(linenum_score)):
			if float(linenum_score[j][1]) < float(min1[1]):
				min1 = linenum_score[j]

		linenum_score.remove(min1)
		final_list.append(min1)

	path_list = []
	[path_list.append(file_path_lines[t[0]]) for t in final_list]

	for path in path_list:
		if not os.path.isfile(path):
			#print ("Error: no such file!")
			continue
		else:
			if not os.path.exists(patch_storage):
				try:
					os.system('mkdir /tmp/PatchesForSimFix++')
				except Exception as e:
					print (e)
			else:
				cmd = "cp " + path + " " + patch_storage
				try:
					os.system(cmd)
				except Exception as e:
					print (e)

	return patch_storage


print (get_similar_loc(sys.argv[1], sys.argv[2]))

