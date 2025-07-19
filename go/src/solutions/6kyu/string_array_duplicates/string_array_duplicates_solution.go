/*
 * https://www.codewars.com/kata/59f08f89a5e129c543000069
 */

package kata

import (
	"bytes"
)

func Dup(arr []string) []string {
	result := []string{}

	for _, str := range arr {
		buff := bytes.NewBufferString("")
		var lastChar byte
		for j := range str {
			if str[j] != lastChar {
				lastChar = str[j]
				buff.WriteByte(lastChar)
			}
		}
		result = append(result, buff.String())
	}

	return result
}
