#!/bin/bash -f
echo "======================================="
echo "Build + Run"
echo "======================================="

files=$(ls $1)
for file in $files; do
        if [ -d "$file" ] && [ "$file" != "utils" ]; then
          echo "Building and running $file"
          go build -o "$file"/solution "$file"/main.go && "$file"/solution < ../../inputs/"$file".txt
          echo "======================================="
          echo ""
        fi
done

echo ""
