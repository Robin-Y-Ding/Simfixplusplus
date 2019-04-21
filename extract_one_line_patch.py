import csv
import os

def read_oneline_bug_info(file):
	csv_info = list()

	with open(file, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			csv_info.append(row)
	csvfile.close()
	return csv_info


def create_directory(csv_info):

	proj_home_path = "/home/robin/Documents/Simfixplusplus/simfix-automatic-build/d4j/projects"
	for row in csv_info:
		proj_name = row[0]
		bug_id = row[1]
	
		path1 = proj_home_path + "/" + proj_name.lower()
		path2 = proj_home_path + "/" + proj_name.lower() + "/" + proj_name.lower() + "_" + bug_id \
				+ "_" + "fixed"
		
		#print (path1)
		#print (path2)

		
		if not os.path.exists(path2):
			if not os.path.exists(path1):
				try:  
					os.mkdir(path1)
				except OSError:  
					print ("Creation of the directory %s failed" % path1)
			else:
				try:  
					os.mkdir(path2)
				except OSError:  
					print ("Creation of the directory %s failed" % path2)


def checkout_fixed_file(csv_info):

	proj_home_path = "/home/robin/Documents/Simfixplusplus/simfix-automatic-build/d4j/projects"
	#defects4j checkout -p Lang -v 1b -w /tmp/lang_1_buggy
	for row in csv_info:
		proj_name = row[0]
		bug_id = row[1]
		path2 = proj_home_path + "/" + proj_name.lower() + "/" + proj_name.lower() + "_" + bug_id \
				+ "_" + "fixed"
		checkout_command = "defects4j checkout -p " + proj_name + " -v " + bug_id + "f" + " -w " + path2

		
		if len(os.listdir(path2)) == 0:
			os.system(checkout_command)
		

def generate_one_line_fixed_file(csv_info):
	file_output = open("./one_line_patch.txt", "w+")
	proj_home_path = "/home/robin/Documents/Simfixplusplus/simfix-automatic-build/d4j/projects"
	for row in csv_info:
		proj_name = row[0]
		bug_id = row[1]
		detail_path = row[2]
		line_number = row[3]
		path2 = proj_home_path + "/" + proj_name.lower() + "/" + proj_name.lower() + "_" + bug_id \
				+ "_" + "fixed"
		
		fixed_file_path = path2 + "/" + detail_path
		
		file_input=open(fixed_file_path)
		lines=file_input.readlines()
		new_line = lines[int(line_number) - 1].strip() + "\n"
		file_output.write(new_line)

	file_input.close()
	file_output.close()




file = "/home/robin/Documents/sequencer/src/Defects4J_Experiment/Defects4J_oneLiner_metadata.csv"

#read_oneline_bug_info(file)
#print(os.path.exists("/home/robin/Documents/Simfixplusplus/simfix-automatic-build/d4j/projects/math/math_5_buggy"))

csv_info = read_oneline_bug_info(file)
#create_directory(csv_info)
#checkout_fixed_file(csv_info)
generate_one_line_fixed_file(csv_info)