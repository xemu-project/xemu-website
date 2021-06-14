#!/bin/bash -ex
if [[ ! -d dart-sass ]]; then
	echo "Downloading sass";
	SASS_URL=https://github.com/sass/dart-sass/releases/download/1.26.3/dart-sass-1.26.3-linux-x64.tar.gz
	wget $SASS_URL
	tar xf `basename $SASS_URL`
fi

if [[ ! -d bootstrap-4.4.1 ]]; then
	echo "Downloading bootstrap"
	BS_URL=https://github.com/twbs/bootstrap/archive/v4.4.1.zip
	wget $BS_URL
	unzip `basename $BS_URL`
fi

echo "Compiling stylesheets"
./dart-sass/sass theme.scss dist/theme.css

echo "Generating HTML pages"
./generate.py

cp resources/cover_front_default.png \
   resources/xbox_logo.png \
   resources/xbox_duke.png \
   dist
rm dist/theme.css.map

docker run --rm -v ${PWD}/docs:/docs squidfunk/mkdocs-material build
cp -r docs/site dist/docs
