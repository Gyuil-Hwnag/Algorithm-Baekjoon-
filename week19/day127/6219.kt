package com.example.d20240116

import kotlin.math.pow


object `6219` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()

        val (a, b, d) = input.split(' ').map { it.toInt() }
        val req = mutableListOf<String>()

        (a .. b).forEach { num ->
            if (num.isPrime()) req.add(num.toString())
        }

        println(req.toResult(target = d.toString()))
    }

    private fun List<String>.toResult(target: String): Int {
        var res = 0
        val numbers = this
        numbers.forEach { num ->
            if (num.contains(target)) res += 1
        }
        return res
    }

    private fun Int.isPrime(): Boolean {
        val num = this
        for (n in 2 .. num.toDouble().pow(0.5).toInt() step 1) {
            if (num % n == 0) return false
        }
        return true
    }
}