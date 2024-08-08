/*
 * https://www.codewars.com/kumite/66b146349574c9ea3dfafd0a?sel=66b146349574c9ea3dfafd0a
 */

package me.anviks.codewars.translations._5kyu.a_chain_adding_function

class add(val value: Int = 0) {
    operator fun invoke(n: Int): add {
        return add(value + n)
    }

    override fun equals(other: Any?): Boolean {
        return when (other) {
            is Int -> value == other
            is add -> value == other.value
            else -> false
        }
    }

    operator fun plus(n: Int): Int {
        return value + n
    }

    override fun hashCode(): Int {
        return value
    }
}
