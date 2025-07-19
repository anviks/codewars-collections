/*
 * https://www.codewars.com/kata/52fb87703c1351ebd200081f
 */

package kata

import "strconv"

func WhatCentury(year string) string {
	yearNum, _ := strconv.Atoi(year)
	century := (yearNum-1)/100 + 1
	lastNumber := century % 10
	suffix := "th"

	if century < 10 || century > 20 {
		switch lastNumber {
		case 1:
			suffix = "st"
		case 2:
			suffix = "nd"
		case 3:
			suffix = "rd"
		}
	}

	return strconv.Itoa(century) + suffix
}
