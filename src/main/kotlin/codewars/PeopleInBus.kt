package codewars

fun people(busStops: Array<Pair<Int, Int>>) : Int {
    return busStops.sumOf { it.first - it.second }
}
