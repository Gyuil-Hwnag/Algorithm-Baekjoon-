package com.example.d20240114


object `1681` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val (n, l) = input.split(' ').map { it.toInt() }
        println(result(n = n, num = l))
    }

    private fun result(n: Int, num: Int): Int {
        var people = n
        var res = 1
        while (true) {
            if (!res.toString().contains(num.toString())) people -= 1
            if (people == 0) break
            res += 1
        }

        return res
    }
}