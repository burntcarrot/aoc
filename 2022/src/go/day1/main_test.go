package main

import (
	"testing"

	"github.com/burntcarrot/aoc/2022/src/go/utils"
	"github.com/google/go-cmp/cmp"
)

func TestPart1(t *testing.T) {
	lines := utils.ReadFromFile("../../../test-inputs/day1.txt")
	got := part1(lines)
	expected := "24000\n"

	if !cmp.Equal(got, expected) {
		t.Errorf("got != expected; diff: %v\n", cmp.Diff(got, expected))
	}
}

func TestPart2(t *testing.T) {
	lines := utils.ReadFromFile("../../../test-inputs/day1.txt")
	got := part2(lines)
	expected := "24000\n45000\n"

	if !cmp.Equal(got, expected) {
		t.Errorf("got != expected; diff: %v\n", cmp.Diff(got, expected))
	}
}
