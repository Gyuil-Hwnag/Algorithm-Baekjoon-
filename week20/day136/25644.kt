package com.example.d20240206


object `25644` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val n = input.readLine().toInt()
        val req = input.readLine().split(" ").map { it.toInt() }
        var (maxi, res) = (0 to 0)

        for (i in n-1 downTo 0) {
            maxi = maxOf(maxi, req[i])
            res = maxOf(res, (maxi - req[i]))
        }

        println(res)
    }
}