package com.example

import kotlin.math.pow


object `1864` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        while (true) {
            val str = input.readLine()
            if (str == "#") break
            println(str.toResult().sum().toInt())
        }
    }

    private fun String.toResult(): List<Float> {
        val str = this
        val numStr = str.map { it.toNums() }
        return numStr.mapIndexed { index, num ->
            num * 8.0f.pow(str.length - index - 1)
        }
    }

    private fun Char.toNums(): Float {
        return when (this) {
            '-' -> 0f
            '\\' -> 1f
            '(' -> 2f
            '@' -> 3f
            '?' -> 4f
            '>' -> 5f
            '&' -> 6f
            '%' -> 7f
            else -> (-1.0f)
        }
    }
}