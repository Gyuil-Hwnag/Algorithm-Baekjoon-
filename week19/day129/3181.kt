package com.example.d20240120

import java.util.*

object `3181` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()

        val str = listOf("i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili")
        val b = input.split(" ")
        var r = b[0][0].toString()
        for (i in 1 until b.size) {
            if (b[i] in str) {
                continue
            }
            r += b[i][0]
        }
        println(r.uppercase(Locale.KOREA))
    }
}