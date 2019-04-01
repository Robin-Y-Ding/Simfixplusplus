#/bin/bash

# NOTE: this script is designed for simple running:
#       one fault can be tested at one time.
#       For more powerful running options pls visit
#       our project homepage at 
#       https://github.com/xgdsmileboy/SimFix.git
#
# simfix-del.jar : corresponds to SimFix-D in the paper
# simfix-all.jar : corresponds to SimFix-A in the paper
# simfix.jar     : corresponds to SimFix in the paper (our approach)
# 
# modify HERE as need
#
jar_file=simfix.jar

check_evn() {
    echo '|------------------------------------------------------|'
    echo '|-------------checking necessary software--------------|'
    echo '|------------------------------------------------------|'

    if ! [ -x "$(command -v perl)" ]; then
        echo 'Error : perl not found!'
        echo 'Please install perl first by typing: sudo apt-get install perl'
        exit 1
    else
        echo 'Find perl:'$(command -v perl)
    fi

    if ! [ -x "$(command -v git)" ]; then
        echo 'Error : git not found!'
        echo 'Please install git first by typing: sudo apt-get install git'
        exit 1
    else
        echo 'Find git:'$(command -v git)
    fi

    if ! [ -x "$(command -v svn)" ]; then
        echo 'Error : svn not found!'
        echo 'Please install svn first by typing: sudo apt-get install subversion'
        exit 1
    else
        echo 'Find svn:'$(command -v svn)
    fi
}

check_evn

# pls do not revise below
BASE=$(pwd)
proj_home=$BASE/d4j/projects
# default example
proj_name=math
bug_id=5

echo '|------------------------------------------------------|'
echo '|             set current testing project              |'
echo '|             Example 1 : ./run.sh chart 1             |'
echo '|             Example 2 : ./run.sh math 1              |'
echo '|------------------------------------------------------|'
if [ $# -eq 2 ]; then
    proj_name=$1
    bug_id=$2
    echo "TEST : " $proj_name'_'$bug_id
else
    echo "Default : " $proj_name'_'$bug_id
fi

echo '|------------------------------------------------------|'
echo '|         checkout project from the Internet           |'
echo '|------------------------------------------------------|'

if [ ! -d $proj_home/$proj_name ]; then
    echo 'Create directory : ' $proj_home'/'$proj_name
    mkdir $proj_home/$proj_name
else
    rm -rf $proj_home/$proj_name/*
fi

Proj_name=$(echo "$proj_name" | sed "s/.*/\u&/")
proj_bug=${proj_name}'_'$bug_id'_'buggy

one_bug=$proj_home/$proj_name/$proj_bug

defects4j checkout -p $Proj_name -v ${bug_id}b -w $one_bug 2>/dev/null

if [ ! -d $one_bug ]; then
    echo 'Download '$proj_name'-'$bug_id' Failed! Please check!'
echo 'You may not run: source source_me' 
    exit 1
else
    echo 'Save '$proj_name'-'$bug_id' to '$one_bug
fi

echo '|------------------------------------------------------|'
echo '|                     run simfix                       |'
echo '|------------------------------------------------------|'

cd $BASE/runnable
java -jar $jar_file --proj_home=$proj_home --proj_name=$proj_name --bug_id=$bug_id

if [ ! -d $proj_home/$proj_name ]; then
    echo 'Should not happen'
else
    rm -rf $proj_home/$proj_name
fi

echo '|------------------------------------------------------|'
echo '|------------------------Finish------------------------|'
echo '  Summary:'
echo '   * log file:'
echo '      ./runnable/log/'$proj_name'/'$bug_id'.txt'
echo '   * patch folder (if success):'
echo '      ./runnable/patch/'$proj_name'/'$bug_id       


