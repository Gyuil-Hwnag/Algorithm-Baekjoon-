package com.example.d20240120

import kotlin.math.pow
import kotlin.math.sqrt

object `9421` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val req = input.toInt().toPrimes()
        req.forEach {
            it.toResult()
        }
    }

    private fun Int.toResult() {
        val nums = mutableListOf<Int>()
        var num = this
        while (true) {
            var res = 0
            num.toString().forEach { n ->
                res += n.toString().toDouble().pow(2).toInt()
            }
            if (res in nums) break
            if (res == 1) {
                println(this)
                break
            }
            nums.add(res)
            num = res
        }
    }

    private fun Int.toPrimes(): List<Int> {
        val nums = mutableListOf<Int>()
        val n = this
        (2 .. n).forEach { num ->
            if (num.isPrime()) nums.add(num)
        }
        return nums
    }

    private fun Int.isPrime(): Boolean {
        val num = this
        (2 .. sqrt(num.toDouble()).toInt()).forEach { n ->
            if (num % n == 0) return false
        }
        return true
    }
}