package com.example.d20240206


object `8394` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val n = input.toInt()
        val res = MutableList(size = n + 1) { 0 }
        res[0] = 1
        res[1] = 1

        for (i in 2..n) {
            res[i] = (res[i - 1] + res[i - 2]) % 10
        }
        println(res[n])
    }
}