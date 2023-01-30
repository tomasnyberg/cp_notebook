// Read lines from stdin using bufio
package main

import (
	"bufio"
	"fmt"
	"os"
	"math"
	// "strings"
)

func dfs(s string, m map[string]int) int {
	// if the length of s is 0
	if len(s) == 0 {
		return 0
	}
	if _, ok := m[s]; ok {
		return m[s]
	}
	results := make([]int, 0)
	// Create an array that holds pairs of two strings
	pairs := make([][]string, 0)
	// Append the first character of s and s without the first character to the array
	pairs = append(pairs, []string{s[:1], s[1:]})
	pairs = append(pairs, []string{s[len(s)-1:], s[:len(s)-1]})
	// Iterate through the array
	for _, pair := range pairs {
		alice := pair[0]
		remaining := pair[1]
		var a int
		var b int
		a = dfs(remaining[1:], m)
		b = dfs(remaining[:len(remaining)-1], m)
		// set the variable res to the maximum of a and b
		res := math.Max(float64(a), float64(b))
		if res != 0 {
			results = append(results, int(res))
		} else {
			if a >= 0{
				if alice[0] > remaining[0]{
					results = append(results, -1)
				} else if alice[0] < remaining[0] {
					results = append(results, 1)
				} else {
					results = append(results, 0)
				}
			} else {
				if alice[0] > remaining[len(remaining)-1]{
					results = append(results, -1)
				} else if alice[0] < remaining[len(remaining)-1] {
					results = append(results, 1)
				} else {
					results = append(results, 0)
				}
			}
		}
	}
	// return the minimum of the array results
	var answer = float64(results[0])
	for _, result := range results {
		answer = math.Min(answer, float64(result))
	}
	m[s] = int(answer)
	return int(answer)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	// read int from input to a variable
	fmt.Fscan(in, &n)
	for i := 0; i < n; i++ {
		// read one line from input to a variable s
		var s string
		fmt.Fscan(in, &s)
		// Create a hashmap from string to int
		var m = make(map[string]int)
		res := dfs(s, m)
		if res == 0 {
			fmt.Println("Draw")
		} else {
			fmt.Println("Alice")
		}
	}
}
