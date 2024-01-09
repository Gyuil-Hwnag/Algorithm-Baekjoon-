package com.example


object `29790` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val (solveCount, level, maxLevel) = input.split(' ').map { it.toLong() }
        println(Triple(solveCount, level, maxLevel).toResult())
    }

    private fun Triple<Long, Long, Long>.toResult(): String {
        val solveNumber = first
        val level = second
        val maxLevel = third
        return when {
            solveNumber >= 1000 && (level >= 8000 || maxLevel >= 260) -> "Very Good"
            solveNumber >= 1000 -> "Good"
            else -> "Bad"
        }
    }
}