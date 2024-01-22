package com.example.d20240122


object `1359` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val (n, m, k) = input.split(" ").map { it.toInt() }
        println(Triple(n, m, k).toResult())
    }

    private fun Triple<Int, Int, Int>.toResult(): Double {
        var resTop = 0.0
        val (n, m, k) = this
        val resBottom = combination(n, m)
        for (i in k..m) {
            if (n - m < m - i) continue
            resTop += combination(m, i) * combination(n - m, m - i)
        }
        return resTop / resBottom
    }

    private fun combination(n: Int, c: Int): Double {
        var resTop = 1.0
        var resBottom = 1.0
        var top = n
        var bottom = c
        while (bottom > 0) {
            resTop *= top
            resBottom *= bottom
            top -= 1
            bottom -= 1
        }
        return resTop / resBottom
    }
}