package com.example.d20240118

import kotlin.math.pow
import kotlin.math.sqrt

object `1069` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val (x, y, d, t) = input.split(' ').map { it.toInt() }
        println(toResult(x = x, y = y, d = d, t = t))
    }

    private fun toResult(x: Int, y: Int, d: Int, t: Int): Int {
        val distance = sqrt(x.toDouble().pow(2) + y.toDouble().pow(2)).toInt()
        val res = if (distance >= d) {
            minOf(t * (distance / d) + distance % d, t * (distance / d) + t, distance)
        } else {
            minOf(t + (d - distance), 2 * t, distance)
        }
        return res
    }
}