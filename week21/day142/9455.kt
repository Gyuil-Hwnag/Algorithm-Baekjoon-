package com.example


object `9455` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val t = input.readLine().toInt()

        for (i in 0 until t) {
            val (m, n) = input.readLine().split(" ").map { it.toInt() }
            val area = mutableListOf<List<Int>>()
            for (j in 0 until m) {
                area.add(input.readLine().split(" ").map { it.toInt() })
            }
            println(area.toResult())
        }
    }

    private fun List<List<Int>>.toResult(): Int {
        val area = this.map { it.toMutableList() }.toMutableList()
        var res = 0
        var count = 0
        while (count >= 0) {
            for (i in area.size - 2 downTo 0) {
                for (j in 0 until  area[i].size) {
                    if (area[i][j] == 1 && area[i + 1][j] == 0) {
                        area[i + 1][j] = 1
                        area[i][j] = 0
                        count += 1
                        res += 1
                    }
                }
            }
            count = when (count) {
                0 -> -1
                else -> 0
            }
        }

        return res
    }
}