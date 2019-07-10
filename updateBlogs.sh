#!/bin/bash

curdir=$PWD
scriptdir=$(dirname ${BASH_SOURCE[0]-$0})
basedir=${scriptdir}/..

echo '====== Sync note from note repo ======'
cd $basedir/donno-repo && git pull
echo '====== Sync note success ======'

echo '====== Build static site from notes ======'
cp $basedir/donno-repo/t*.md $scriptdir/content
sed -i -e '3 c Category: Tech' -e '4 s/Created/Date/' $scriptdir/content/t*.md
cd $scriptdir && poetry run pelican content
echo '====== Build static site success ======'

echo 'Preview local website:'
echo 'Open http://localhost:8000 in your browser'
poetry run pelican --listen
read -p 'Publish to github? (y/n):' pubit

if [ $pubit != 'y' ]; then
  exit 0
fi

echo '====== Sync to github pages ======'
cd $basedir/leetschau.github.io
git pull
git rm -r *
cp -r $scriptdir/output/* .
git add -A
git commit -m 'update blogs'
git push
cd $curdir
echo '====== Sync to github pages success ======'
