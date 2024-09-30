class Person{
    var name: String = ""
    var age: Int = 0

    fun speak() {
        println("Hello")
    }
}

fun main() {
    val person = Person()
    person.name = "John"
    person.age = 30
    println(person.name)

}