package com.example.d20240205

import kotlin.math.pow

object `16673` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val (c, k, p) = input.split(" ").map { it.toInt() }

        var res = 0
        for (i in 1..c) {
            res += (k * i) + p * (i.toDouble().pow(2).toInt())
        }

        println(res)
    }
}