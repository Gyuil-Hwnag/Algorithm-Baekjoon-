package com.example.d20240131


object `17350` {

    private const val TARGET = "anj"
    private const val TRUE = "뭐야?"
    private const val FALSE = "뭐야;"

    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val n = input.readLine().toInt()
        var count = 0
        (0 until n).forEach { _ ->
            if (input.readLine().toResult()) count += 1
        }
        if (count == 0) println(TRUE) else println(FALSE)
    }

    private fun String.toResult(): Boolean = this == TARGET
}