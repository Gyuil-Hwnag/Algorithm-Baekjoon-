package com.example


object `23804` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val req = input.toInt()
        req.toResult()
    }

    private fun Int.toResult() {
        val count = this
        Pair(count, 5 * count).toPrint()
        Pair(3 * count, count).toPrint()
        Pair(count, 5 * count).toPrint()
    }

    private fun Pair<Int, Int>.toPrint() {
        val str = "@"
        val nextLine = "\n"
        (0 until first).forEach { _ ->
            (0 until second).forEach { _ ->
                print(str)
            }
            print(nextLine)
        }
    }
}