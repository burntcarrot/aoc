echo "Test for day $1"
echo "======================================="
{
    cd day$1 && go test -v ./...
} || {
    echo "tests failed for day $1"
}
cd ..
echo "======================================="
echo ""
