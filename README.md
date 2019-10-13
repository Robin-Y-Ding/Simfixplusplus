# Simfixplusplus
by Robin Ding (yd2447@columbia.edu) and Joe Huang (jch2220@columbia.edu)

This is a course project for the excellent research-based course, COMS6156 Topics in Software Engineering, given by [Prof. Gail Kaiser](http://www.cs.columbia.edu/~kaiser/) in Columbia University. This project is done under the supervision of [Prof. Baishakhi Ray](http://rayb.info/) and [Prof. Gail Kaiser](http://www.cs.columbia.edu/~kaiser/), and we appreciate the advise and help from Saikat Chakraborty.

We give our tool a name of “SimFix++” because the tool is developed based on the SimFix tool. The original tool please refer here: https://github.com/xgdsmileboy/SimFix. Their excellent paper can be referred here: https://xgdsmileboy.github.io/files/paper/simfix-issta18.pdf. Our project is just for research and fun, and we thank SimFix team for their significant contribution to automated program repair field.

![Simfix++ Diagram](https://github.com/Robin-Y-Ding/Simfixplusplus/blob/master/simfixpp_diagram.png)


## Description
We expanded the functionality of SimFix by taking the commit history of current project into consideration. Originally, SimFix uses exsiting patches offline to capture the most frequent bug-fixing patterns and use these patterns to shrink the search space when they search for similar code snippets in current codebase. Rather than focusing on similar "code snippets" in current repository, we directly search for the similar "bug" code in the project's commit history, and we use the patches of this similar bug as guidance to fix the real bug.

Specifically, our work flow is as follows:
1. Calculating the similarity (Structure similarity and Edit Distance) between current buggy code and the buggy code in commit history of the same project.
2. Pick the top-k similar bugs from the commit history and extract their corresponding patches as candidates.
3. Following the design of original SimFix, we slightly modify the candidates (e.g. variable mapping) to make them fit into the current buggy context.
4. Generate candidate patches and validate them.

## Results
We design and implement our new features as additional functionality of original SimFix, which means the project SimFix++ maintains all the power inherited from SimFix.

In addition, we extended the power to FOUR new bugs in Defects4J dataset. New means SimFix cannot fix these bugs as stated in the ISSTA'18 paper.

Additional fixes (4):

* chart: 8
* closure: 92, 93
* lang: 26


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


