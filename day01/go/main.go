package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

// Using same logic from Python in Go.

func readInput(inputPath string) []string {
	content, err := os.ReadFile(inputPath)
	if err != nil {
		panic(err)
	}
	lines := strings.Split(strings.TrimSpace(string(content)), "\n")
	return lines
}

func partA(inputPath string) int {
	lines := readInput(inputPath)
	totalSum := 0

	for _, line := range lines {
		var firstDigit, lastDigit rune

		for _, char := range line {
			if unicode.IsDigit(char) {
				firstDigit = char
				break
			}
		}

		for _, char := range reverse(line) {
			if unicode.IsDigit(char) {
				lastDigit = char
				break
			}
		}

		totalSum += int(firstDigit-'0')*10 + int(lastDigit-'0')
	}

	return totalSum
}

func reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func testA() bool {
	return 142 == partA("test_input.txt")
}

func partB(inputPath string) int {
	numbers := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}

	lines := readInput(inputPath)
	totalSum := 0

	for _, line := range lines {
		var digits []int

		for i, char := range line {
			if unicode.IsDigit(char) {
				digits = append(digits, int(char-'0'))
			}

			for number, value := range numbers {
				if strings.HasPrefix(line[i:], number) {
					digits = append(digits, value)
				}
			}
		}

		totalSum += digits[0]*10 + digits[len(digits)-1]
	}

	return totalSum
}

func testB() bool {
	return 281 == partB("test_input2.txt")
}

func main() {
	fmt.Println("Test 1:", testA())
	fmt.Println("Day 01a:", partA("input.txt"))
	fmt.Println("Test 2:", testB())
	fmt.Println("Day 01b:", partB("input.txt"))
}
