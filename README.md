# Simfixplusplus
Simfix with Opennmt

# Update
Additional argument: 
--proj_tech=[similar|patch|all]
	Set the techniques to be applied to the buggy program.

# Code Changes
confix.common.config/Constant: line 38
	Add parameter PROJ_TECH to keep the user selected technique.

confix.main/Main:
	Take in the extra parameter

confix.main/Repair:
	Print the buggy code blocks required for Simfix++.
