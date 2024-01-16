package com.example.d20240116

object `6376` {
    @JvmStatic
    fun main(args: Array<String>) {
        println("n e")
        println("- -----------")
        println("0 1")
        println("1 2")
        println("2 2.5")
        var result = 2.5
        (3 .. 9).forEach {
            val res = it.calculateE()
            result += res
            println(String.format("%.0f %.9f", it.toDouble(), result))
        }

    }

    private fun Int.calculateE(): Double {
        var res = 1.0
        val target = this
        (1..target).forEach {
            res *= it
        }
        return 1 / res
    }
}