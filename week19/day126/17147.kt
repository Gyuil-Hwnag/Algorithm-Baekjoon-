package com.example.d20240115


object `17147` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val (n, m) = input.split(' ').map { it.toInt() }
        println(Pair(n, m).toResult())
    }

    private fun Pair<Int, Int>.toResult(): Int {
        var n = first
        val m = second
        var res = n
        while (n > 0) {
            res += (n / m)
            n /= m
        }
        return res
    }
}