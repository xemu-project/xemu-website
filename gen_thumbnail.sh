#!/bin/bash -ex
INPUT=$1
OUTPUT_COMPRESSED=`dirname $1`/cover_front_thumbnail.jpg
if [[ -e "$OUTPUT_COMPRESSED" ]]; then
	echo "$OUTPUT_COMPRESSED already exists"
	exit 0
fi
echo "CONVERTING $INPUT"
convert $INPUT -quality 85 -resize 256 -density 72x72 $OUTPUT_COMPRESSED
