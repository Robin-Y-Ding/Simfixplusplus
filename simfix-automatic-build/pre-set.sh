#/bin/bash

BASE=$(pwd)

mkdir d4j
cd d4j
mkdir projects
git clone https://github.com/rjust/defects4j.git
cd defects4j
git checkout fee5ddf020
cd $BASE

mkdir jvm
cd jvm 
wget http://cdn-files.evildayz.com/mirror/java/jdk_7u79/jdk-7u79-linux-x64.tar.gz
cd $BASE

git clone https://github.com/xgdsmileboy/SimFix.git runnable
cd runnable/sbfl
unzip "*.zip"
cd ..
mv ./final/simfix.jar .
mv ./final/simfix-all.jar .
mv ./final/simfix-del.jar .
cd $BASE
