# Simfixplusplus
by Robin Ding and Joe Huang

## Setup
This section includes the basic setup to run Simfix++. More details can be found in the link provided.
- Ubuntu 16.04.2 LTS
- Oracle jdk1.7 (Using [Eclipse Mars](https://www.eclipse.org/mars/))
- [Defects4J](https://github.com/rjust/defects4j) and add DEFECTS4J_HOME="home_of_defects4j" to path
- Unzip `sbfl/data.zip` to `sbfl/data`
- Checkout the buggy verison of benchmark using defects4j command

### Suggest Setup
A faster way to set up Simfix++ after installing jdk1.7, Eclipse Mars, and sbfl/data on Ubuntu can be done by running the following scripts in `simfix-automatic-build`:
- ./pre-set.sh: this shell helps you fetch the code and resource.
- source source_me: This shell is derived from the official version of source_me, which aims to setup the environment.

After running them, defects4j should be downloaded inside the `simfix-automatic-build/d4j`. Make sure the buggy project is checkout before running Simfix++.

Example of [checking out a defects4j project](https://people.cs.umass.edu/~rjust/defects4j/html_doc/d4j/d4j-checkout.html):
```powershell
defects4j checkout -p Lang -v 1b -w /tmp/lang_1_buggy
```

## Run Simfix++
1. Build the project in Eclipse by import Simfix++ folder. `cofix.main.Main` is the entry of the program.
2. Add the arguments in Run->Run Configurations->Arguments
	* `--proj_home ` : the home of buggy program of benchmark. (`${buggy_program_path}` for the example)
	* `--proj_name` : the project name of buggy program of benchmark. (`chart` for the example)
	* `--bug_id` : the identifier of the buggy program. (`1` for the example)
	* `--proj_tech`: the technique of this fix, possible argument including `similar`, `patch`, and `all`. 

	example:  
	```powershell
  	--proj_home=/home/joe/simfixplusplus/simfix-automatic-build/d4j/projects 
	--proj_name=math 
	--bug_id=5
	--proj_tech=patch
  	```
	
## Evaluation results
After running the Simfix++, the console will print out the information about the current buggy project and ID, codes that will be used to replaced to original codes, and whether the project is successfuly fixed or not.


