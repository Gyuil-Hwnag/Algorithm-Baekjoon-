package com.example.d20240118


object `2986` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val n = input.toInt()
        println(n.toResult())
    }

    private fun Int.toResult(): Int {
        var count = 0
        val n = this
        for (na in n -1 downTo 1) {
            count += 1
            if (n % na == 0) break
        }
        return count
    }
}