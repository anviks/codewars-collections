package random

fun main() {
    val firstName = "John"
    val lastName = "Doe!"
    println("My name is $firstName $lastName")

    val sus = if (1 > 0) "baka" else "Waltuh"

    var cars = noStreamNeeded()

    when (sus) {
        "Waltuh" -> println("hi")
        "baka" -> println("hi lol")
        else -> println("suc")
    }

    ranges(cars)

    var carOb = Car("Audi", "A7", 2017)


}

private fun ranges(cars: ArrayList<String>) {
    for (x in cars) {
        continue
    }

    for (chars in 'a'..'x') {
        continue
    }

    for (nums in (5..15).step(3)) {
        println(nums)
    }

    var lmao = 5..23
    lmao.step(3)
}

private fun noStreamNeeded(): ArrayList<String> {
    val carsArray = arrayOf("Volvo", "BMW", "Ford", "Mazda")
    println(carsArray[0])
    var cars = arrayListOf("Volvo", "BMW", "Ford", "Mazda")

    println("Cars: ${cars.joinToString()}")
    cars = cars.filter { it.length > 3 } as ArrayList<String>
    println("Cars: ${cars.joinToString()}")

    println("Ford in Cars: ${"Ford" in cars}")

    val carLengths = cars.map { it.length }
    println("CarLengths: $carLengths")

    val carLength = carLengths.reduce { num1, num2 -> num1 + num2 }
    println("Total: $carLength")

    return cars
}

fun concat1(s1: String, s2: String): String {
    return s1 + s2
}

fun concat2(s1: String, s2: String): String = s1 + s2

fun concat3(s1: String, s2: String) = s1 + s2
