#!/bin/bash -f
echo "======================================="
echo "Test"
echo "======================================="

files=$(ls $1)
for file in $files; do
        if [ -d "$file" ] && [ "$file" != "utils" ]; then
          echo "Running tests for $file"
          {
            cd "$file" && go test -v ./...
          } || {
            echo "tests failed for $file"
          }
          echo "======================================="
          echo ""
          cd ..
        fi
done

echo ""
