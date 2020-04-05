#!/bin/bash -ex
# exit 0
cd dist
cssmin > theme.css.min < theme.css
mv theme.css.min theme.css
rm -rf .git
git init .
git remote add origin git@github.com:mborgerson/xemu-website.git
echo "xemu.app" > CNAME
git add .
git commit -m "Update site"
git branch -m gh-pages
git push -f origin gh-pages
