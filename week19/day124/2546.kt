package com.example.d20240110


object `2546` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val t = input.readLine().toInt()
        (0 until t).forEach {  _ ->
            println(input.readLine().toInt().toResult())
        }
    }

    private fun Int.toResult(): Int {
        var count = 1
        var res = 1
        val finish = this
        while (count < finish) {
            res = 2 * res + 1
            count += 1
        }
        return res
    }
}