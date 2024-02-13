package com.example.d20240212

import kotlin.math.pow


object `11576` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val (a, b) = input.readLine().split(" ").map { it.toInt() }
        val m = input.readLine().toInt()
        val nums = input.readLine().split(" ").map { it.toInt() }

        val tens = nums.reversed().toTenBinary(binary = a)
        val res = tens.toBinary(binary = b)

        println(res.reversed().joinToString(" "))
    }

    private fun List<Int>.toTenBinary(binary: Int): Int {
        var res = 0
        for (index in indices) {
            val multiply = binary.toDouble().pow(index).toInt()
            res += (this[index] * multiply)
        }
        return res
    }

    private fun Int.toBinary(binary: Int): List<Int> {
        val res = mutableListOf<Int>()
        var num = this
        while (num != 0) {
            res.add((num % binary))
            num /= binary
        }
        return res
    }
}