package random

open class Car(private val brand: String, val model: String, private var year: Int) {
    fun drive() {
        println("Wrooom!")
    }

    fun getBrand(): String {
        return brand
    }

    companion object {
        fun getStatic(): String {
            return "Lolxd"
        }
    }

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Car) return false

        if (brand != other.brand) return false
        if (model != other.model) return false
        if (year != other.year) return false

        return true
    }

    override fun hashCode(): Int {
        var result = brand.hashCode()
        result = 31 * result + model.hashCode()
        result = 31 * result + year
        return result
    }

    override fun toString(): String {
        return "random.Car(brand='$brand', model='$model', year=$year)"
    }
}
