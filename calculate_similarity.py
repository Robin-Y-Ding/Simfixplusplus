import math

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

def get_n_similar_loc(org_code, N):
    lines = open('buggy.token', 'r').readlines()
    file_output = open('similarity.score', 'w+')

    [file_output.write(str(calculate_edit_distance(org_code, line)+calculate_normalized_bow_distance(org_code, line))+'\n') for line in lines]

    file_output.close()

    score_lines = open('similarity.score', 'r').read().splitlines()
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

    print(final_list)

    file_output2 = open('similarcode.token', 'w+')
    [file_output2.write(lines[t[0]] + '\n') for t in final_list]

#This org_code should be the tokenized buggy code
org_code = "Calendar c = new GregorianCalendar ( mTimeZone ) ; \n"
get_n_similar_loc(org_code, 10)
