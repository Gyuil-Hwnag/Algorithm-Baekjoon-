package com.example.d20240123


object `1402` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val t = input.readLine().toInt()
        (0 until t).forEach { _ ->
            val (a, b) = input.readLine().split(" ").map { it.toInt() }
            println("yes")
        }
    }
}