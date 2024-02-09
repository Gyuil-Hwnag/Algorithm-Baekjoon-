package com.example.d20240209

import kotlin.math.pow

object `28701` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val n = input.toInt()
        println(n.toSum())
        println(n.toSumPow())
        println(n.toPowSum())
    }

    private fun Int.toSum(): Int {
        var res = 0
        (0 .. this).forEach { res += it }
        return res
    }

    private fun Int.toSumPow(): Int = this.toSum().toDouble().pow(2).toInt()

    private fun Int.toPowSum(): Int {
        var res = 0.0
        (0 .. this).forEach {
            res += (it.toDouble().pow(3))
        }
        return res.toInt()
    }
}