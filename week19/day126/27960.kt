package com.example.d20240115

import kotlin.math.pow


object `27960` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val (a, b) = input.split(' ').map { it.toInt() }
        println(Pair(a, b).toResult())
    }

    private fun Pair<Int, Int>.toResult(): Int {
        var a = first
        var b = second
        val req = listOf<Int>(1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
        val res = MutableList(10) { 0 }
        var result = 0

        for (i in req.size - 1 downTo 0) {
            if (a >= req[i]) {
                a -= req[i]
                res[i] += 1
            }
            if (b >= req[i]) {
                b -= req[i]
                res[i] += 1
            }

            if (res[i] == 1) result += ((2.0).pow(i)).toInt()
        }
        return result
    }
}