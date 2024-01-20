package com.example.d20240120

import kotlin.math.pow


object `13706` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        input.toInt().toResult()
    }

    private fun Int.toResult() {
        val n = this
        var low = 1
        var high = n
        while (true) {
            val mid = (low + high) / 2
            when {
                (mid.toDouble().pow(2) == n.toDouble()) -> {
                    println(mid)
                    break
                }
                (mid.toDouble().pow(2) > n.toDouble()) -> high = mid - 1
                (mid.toDouble().pow(2) < n.toDouble()) -> low = mid + 1
            }
        }
    }
}
