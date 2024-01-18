package com.example.d20240118


object `9471` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val t = input.readLine().toInt()
        (0 until t).forEach {  _ ->
            val (n , m) = input.readLine().split(' ').map { it.toInt() }
            println((n to m).toResult())
        }
    }

    private fun Pair<Int, Int>.toResult(): String {
        val n = first
        val m = second.toFisano()
        return "$n $m"
    }

    private fun Int.toFisano(): Int {
        val num = this
        var result = 1
        var left = 1
        var right = 2
        while (true) {
            if (left % num == 1 && right % num == 1) break
            result += 1
            val temp = left
            left = right
            right = (temp + right) % num
        }
        return result
    }
}