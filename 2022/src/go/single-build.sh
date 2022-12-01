echo "Build + Run for day $1"
echo "======================================="
go build -o day$1/solution day$1/main.go && day$1/solution < ../../inputs/day$1.txt
echo "======================================="
echo ""
