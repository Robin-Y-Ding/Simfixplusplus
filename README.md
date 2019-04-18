# Simfixplusplus
Simfix with Opennmt

## buggy.token
Tokenized java buggy code extracted from Defects4j projects history
## buggy_javasource.token
Buggy java source code extracted from Defects4j projects history
## patch.token
Tokenized java patch code extracted from Defects4j projects history
## patch_javasource.token
patched java source code extracted from Defects4j projects history
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
