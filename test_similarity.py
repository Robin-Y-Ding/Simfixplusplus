from apted import APTED, Config
import math
import subprocess


# Python3 program to conStruct a
# binary tree from the given String

# Helper class that allocates a new node
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# This funtcion is here just to test
def preOrder(node):
    if (node == None):
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)


# function to return the index of
# close parenthesis
def findIndex(Str, si, ei):
    if (si > ei):
        return -1

    # Inbuilt stack
    s = []
    for i in range(si, ei + 1):

        # if open parenthesis, push it
        if (Str[i] == '('):
            s.append(Str[i])

            # if close parenthesis
        elif (Str[i] == ')'):
            if (s[-1] == '('):
                s.pop(-1)

                # if stack is empty, this is
                # the required index
                if len(s) == 0:
                    return i
                    # if not found return -1
    return -1


# function to conStruct tree from String
def treeFromString(Str, si, ei):
    # Base case
    if (si > ei):
        return None

    # new root
    root = newNode(ord(Str[si]) - ord('0'))
    index = -1

    # if next char is '(' find the
    # index of its complement ')'
    if (si + 1 <= ei and Str[si + 1] == '('):
        index = findIndex(Str, si + 1, ei)

        # if index found
    if (index != -1):
        # call for left subtree
        root.left = treeFromString(Str, si + 2,
                                   index - 1)

        # call for right subtree
        root.right = treeFromString(Str, index + 2,
                                    ei - 1)
    return root









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

org_code = "if ( categoryKeys.length != this . startData [ NUMBER_CONSTANT ] . length ) { throw new IllegalArgumentException ( STRING_CONSTANT ) ; }\n"
cand_code = "if ( categoryKeys.length != this . startData [ NUMBER_CONSTANT ] . length ) { throw new IllegalArgumentException ( STRING_CONSTANT ) ; }"



class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
class CustomConfig(Config):
    def rename(self, node1, node2):
        """Compares attribute .value of trees"""
        return 1 if node1.data != node2.data else 0

    def children(self, node):
        """Get left and right children of binary tree"""
        return [x for x in (node.left, node.right) if x]

def get_tree_edit_distance(tree1, tree2, ):
    apted = APTED(tree1, tree2, CustomConfig())
    ed = apted.compute_edit_distance()
    return ed

def calculate_similarity_for_whole_file(org_code):
    fileinput = open('prev.token', 'r')
    file_output = open('similarity.score', 'w+')
    lines = fileinput.readlines()
    [file_output.write(str(calculate_edit_distance(org_code, line)+calculate_normalized_bow_distance(org_code, line))+'\n') for line in lines]


root = '{AST_ROOT_SC2NF{{(}{int}{)}{{(}{{{{(}{{value}{-}{{this}{.}{lowerBound}}}{)}}{/}{{(}{{{this}{.}{upperBound}}{-}{{this}{.}{lowerBound}}}{)}}}{*}{NUMBER_CONSTANT}}{)}}}}'
root2 = '{AST_ROOT_SC2NF{{{}{{super}{(}{paint}{,}{stroke}{,}{paint}{,}{stroke}{,}{alpha}{)}{;}}{{{{this}{.}{value}}{=}{value}}{;}}{}}}}'
#print(get_tree_edit_distance(root1, root2))
exe = 'python -m apted -t ' + root + ' ' + 'root2' + '-mv'


print(int(subprocess.check_output(['python', '-m', 'apted', '-t', root, root])))