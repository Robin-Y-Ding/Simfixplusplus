
with open("./corresponding_path.txt", "rt") as fin:
	with open("./new_paths.txt", "wt") as fout:
		for line in fin:
			line = line.replace('/zf8/sc2nf/CCRecom_exp/Defects4jProjectPatches/patches/', '/media/robin/external storage/Defects4JPatches/ProjectFiles/')
			line = line.replace('/zf8/sc2nf/CCRecom_exp/Bugs.jarProjectPatches/patches/', '/media/robin/external storage/Defects4JPatches/ProjectFiles/')
			line = line.replace('/parent/', '/child/')
			fout.write(line)

