package com.example.d20240116

import java.util.*


object `3181` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val str = listOf("i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili")
        val req = input.split(' ')

        println(req.toResult(target = str))
    }

    private fun List<String>.toResult(target: List<String>): String {
        val req = this
        var r = req[0][0].toString()
        for (i in 1 until req.size) {
            if (req[i] in target) {
                continue
            }
            r += req[i][0]
        }
        return r.uppercase(Locale.getDefault())
    }
}