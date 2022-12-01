echo "Running linter for day $1"
echo "======================================="
{
    cd day$1 && golangci-lint run ./...
} || {
    echo "lint failed for day $1"
}
cd ..
echo "======================================="
echo ""
