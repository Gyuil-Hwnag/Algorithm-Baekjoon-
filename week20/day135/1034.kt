package com.example.d20240205


object `1034` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val (n, m) = input.readLine().split(" ").map { it.toInt() }
        val req = mutableListOf<String>()
        for (i in 0 until n) {
            req.add(input.readLine())
        }

        val k = input.readLine().toInt()
        var maxCount = 0

        for (column in 0 until n) {
            var zeroCount = 0

            req[column].forEach {
                if (it == '0') zeroCount += 1
            }

            var lightCount = 0
            if (zeroCount <= k && zeroCount % 2 == k % 2) {
                for (column2 in 0 until n) {
                    if (req[column] == req[column2]) lightCount += 1
                }
            }

            maxCount = maxOf(maxCount, lightCount)
        }

        println(maxCount)
    }
}
