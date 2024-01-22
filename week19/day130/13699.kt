package com.example.d20240122


object `13699` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val n = input.toInt()
        println(n.toResult())
    }

    private fun Int.toResult(): Long {
        val n = this
        val res = MutableList(n + 1) { 0L }
        res[0] = 1

        for (i in 1..n) {
            for (j in 0 until i) {
                res[i] += res[j] * res[i - j - 1]
            }
        }
        return res[n]
    }
}