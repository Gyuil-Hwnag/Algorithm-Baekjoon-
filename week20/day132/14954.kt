package com.example.d20240127


object `14954` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val result = input.toInt().isHappyNumber()
        when(result) {
            true -> println("HAPPY")
            false -> println("UNHAPPY")
        }
    }

    private fun Int.isHappyNumber(): Boolean {
        var number = this
        while (number != 1) {
            var res = 0
            number.toString().forEach {
                res += (it.toInteger() * it.toInteger())
            }
            when (res) {
                1 -> return true
                4 -> break
                else -> number = res
            }
        }
        return false
    }

    private fun Char.toInteger(): Int = Character.getNumericValue(this)
}