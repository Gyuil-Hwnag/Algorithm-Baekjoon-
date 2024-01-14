package com.example.d20240114


object `1448` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val n = input.readLine().toInt()
        val m = mutableListOf<Int>()
        (0 until n).forEach { _ ->
            m.add(input.readLine().toInt())
        }
        m.sortDescending()
        println(m.toList().toResult())
    }

    fun List<Int>.toResult(): Int {
        val req = this
        var res = -1
        for (i in 0 until req.size - 2) {
            if (req[i] < req[i + 1] + req[i + 2]) {
                res = req[i] + req[i + 1] + req[i + 2]
                break
            }
        }
        return res
    }
}