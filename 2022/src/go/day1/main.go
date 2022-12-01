package main

import (
	"fmt"
	"sort"
	"strconv"

	"github.com/burntcarrot/aoc/2022/src/go/utils"
)

// Using the result string as the medium for writing values helps in testing.
// We could capture stdout, but using a result string is easier for comparison.
var result string

func main() {
	lines := utils.ReadFromStdin()
	fmt.Println(part1(lines))
	clear()
	fmt.Println(part2(lines))
	clear()
}

func sortCalories(lines []string) []int {
	calories := make([]int, len(lines))
	index := 0

	for _, str := range lines {
		// if a blank string is encountered, increment the index
		// why? it acts as a way to move to the next elf
		if str == "" {
			index++
			continue
		}
		// else, convert calories to int and accumulate
		n, _ := strconv.Atoi(str)
		calories[index] += n
	}

	// sort the calories slice
	sort.Slice(calories, func(i, j int) bool {
		return calories[i] > calories[j]
	})

	return calories
}

func part1(lines []string) string {
	calories := sortCalories(lines)
	print(calories[0])
	return result
}

func part2(lines []string) string {
	calories := sortCalories(lines)
	print(calories[0] + calories[1] + calories[2])
	return result
}

// Reset the result string.
func clear() {
	result = ""
}

// "Print" to the result string.
func print(message any) {
	result += fmt.Sprintln(message)
}
