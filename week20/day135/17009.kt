package com.example.d20240205


object `17009` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val req = mutableListOf<Int>()
        (0 until 6).forEach { _ ->
            req.add(input.readLine().toInt())
        }

        val resA = req[0]*3 + req[1]*2 + req[2]
        val resB = req[3]*3 + req[4]*2 + req[5]

        when {
            resA == resB -> println("T")
            resA > resB -> println("A")
            else -> println("B")
        }
    }
}