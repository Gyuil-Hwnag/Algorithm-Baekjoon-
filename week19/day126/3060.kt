package com.example.d20240115

object `3060` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val t = input.readLine().toInt()
        (0 until t).forEach { _ ->
            val meal = input.readLine().toDouble()
            val pigs = input.readLine().split(' ').map { it.toDouble() }
            println(Pair(meal, pigs.sum()).toResult())
        }
    }

    private fun Pair<Double, Double>.toResult(): Int {
        var res = 1
        val meals = first
        var totalPigs = second
        while (meals >= totalPigs) {
            res += 1
            totalPigs *= 4
        }
        return res
    }
}