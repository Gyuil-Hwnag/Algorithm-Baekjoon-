package com.example.d20240110


object `29699` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val req = input.toLong()
        println(req.toResult())
    }

    private fun Long.toResult(): Char {
        val index = ((this - 1) % 14).toInt()
        val str = "WelcomeToSMUPC"
        return str[index]
    }
}