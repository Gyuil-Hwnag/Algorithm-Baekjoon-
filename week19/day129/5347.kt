package com.example.d20240120


object `5347` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val (a, b) = input.split(" ").map { it.toInt() }
        println((a to b).toResult())
    }

    private fun Pair<Int, Int>.toResult(): Int = lcm(first, second)

    private fun lcm(a:Int, b:Int) = a * b / gcd(a, b)

    private fun gcd(a: Int, b: Int): Int = if (b != 0) gcd(b, a % b) else a
}