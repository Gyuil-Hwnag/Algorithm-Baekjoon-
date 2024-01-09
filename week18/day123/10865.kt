package com.example


object `10865` {
    @JvmStatic
    fun main(args: Array<String>) {
        val reader = System.`in`.bufferedReader()
        val (n, m) = reader.readLine().split(' ').map { it.toInt() }
        val req = Array(n) { 0 }

        (0 until m).forEach { _ ->
            val (a, b) = reader.readLine().split(' ')
            req[a.toInt() - 1] += 1
            req[b.toInt() - 1] += 1
        }

        req.forEach {
            println(it)
        }
    }
}