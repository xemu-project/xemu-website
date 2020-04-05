#!/bin/bash -ex
INPUT=$1
OUTPUT_RESIZED=`dirname $1`/cover_front_thumbnail_tmp.png
OUTPUT_COMPRESSED=`dirname $1`/cover_front_thumbnail.jpg
if [[ -e "$OUTPUT_COMPRESSED" ]]; then
	echo "$OUTPUT_COMPRESSED already exists"
	exit 0
fi
echo "CONVERTING $INPUT"
convert $INPUT -quality 100 -resize 256 -density 72x72 $OUTPUT_RESIZED
./guetzli/bin/Release/guetzli $OUTPUT_RESIZED $OUTPUT_COMPRESSED
rm $OUTPUT_RESIZED
