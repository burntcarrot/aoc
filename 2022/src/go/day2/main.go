package main

import (
	"fmt"
	"strings"

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

func part1(lines []string) string {
	score := 0
	for _, line := range lines {
		sep := strings.Split(line, " ")
		opponent, me := sep[0], sep[1]
		if opponent == "A" {
			if me == "X" {
				score += 1 + 3
			} else if me == "Y" {
				score += 6 + 2
			} else {
				score += 3 + 0
			}
		} else if opponent == "B" {
			if me == "X" {
				score += 1 + 0
			} else if me == "Y" {
				score += 2 + 3
			} else {
				score += 6 + 3
			}
		} else {
			if me == "X" {
				score += 6 + 1
			} else if me == "Y" {
				score += 2 + 0
			} else {
				score += 3 + 3
			}
		}
	}

	print(score)
	return result
}

func part2(lines []string) string {
	score := 0
	for _, line := range lines {
		sep := strings.Split(line, " ")
		opponent, me := sep[0], sep[1]
		if opponent == "A" {
			if me == "X" {
				score += 3 + 0
			} else if me == "Y" {
				score += 1 + 3
			} else {
				score += 6 + 2
			}
		} else if opponent == "B" {
			if me == "X" {
				score += 1 + 0
			} else if me == "Y" {
				score += 2 + 3
			} else {
				score += 6 + 3
			}
		} else {
			if me == "X" {
				score += 2 + 0
			} else if me == "Y" {
				score += 3 + 3
			} else {
				score += 6 + 1
			}
		}
	}

	print(score)
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
