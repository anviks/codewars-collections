/*
 * https://www.codewars.com/kata/52fb87703c1351ebd200081f
 */

// TODO: replace with your own tests (TDD). An example to get you started is included below.
// Ginkgo BDD Testing Framework <http://onsi.github.io/ginkgo/>
// Gomega Matcher Library <http://onsi.github.io/gomega/>

package kata_test

import (
	. "codewarsGo/src/solutions/6kyu/what_century_is_it"
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestWhatCenturyIsIt(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "WhatCenturyIsIt Suite")
}

func dotest(y, expected string) {
	Expect(WhatCentury(y)).To(Equal(expected), "With year = \"%s\"", y)
}

var _ = Describe("Tests", func() {
	It("Sample tests", func() {
		dotest("2011", "21st")
		dotest("2154", "22nd")
		dotest("2259", "23rd")
		dotest("1234", "13th")
		dotest("1023", "11th")
	})
})
