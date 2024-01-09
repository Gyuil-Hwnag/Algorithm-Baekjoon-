package com.example

object `28352` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val res = input.toLong().factorial()
        println(res)
    }

    private fun Long.factorial(): Long {
        var count = this
        var res: Long = 1
        while (count > 1) {
            res *= count
            count -= 1
        }
        return res / 604800
    }
}