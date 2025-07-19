/*
 * https://www.codewars.com/kata/59f08f89a5e129c543000069
 */

package kata_test

import (
	. "codewarsGo/src/solutions/6kyu/string_array_duplicates"
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestStringArrayDuplicates(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "StringArrayDuplicates Suite")
}

func dotest(s, exp []string) {
	var ans = Dup(s)
	Expect(ans).To(Equal(exp))
}

var _ = Describe("Example tests", func() {
	It("It should work for basic tests", func() {
		dotest([]string{"ccooddddddewwwaaaaarrrrsssss", "piccaninny", "hubbubbubboo"}, []string{"codewars", "picaniny", "hubububo"})
		dotest([]string{"abracadabra", "allottee", "assessee"}, []string{"abracadabra", "alote", "asese"})
		dotest([]string{"kelless", "keenness"}, []string{"keles", "kenes"})
	})
})
