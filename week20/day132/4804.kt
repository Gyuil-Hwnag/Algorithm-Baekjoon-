package com.example.d20240127


object `4804` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val req = input.split(" ").map { it.toInt() }
        req.toResult()
    }

    private fun List<Int>.toResult() {
        var a = this[0]
        var b = this[1]
        var c = this[2]
        var d = this[3]
        while (true) {
            if (a == 0 && b == 0 && c == 0 && d == 0) break
            var res = 0
            while (a != b || b != c || c != d) {
                val tempA = a
                a = kotlin.math.abs(a - b)
                b = kotlin.math.abs(b - c)
                c = kotlin.math.abs(c - d)
                d = kotlin.math.abs(d - tempA)
                res += 1
            }
            println(res)
        }
    }
}