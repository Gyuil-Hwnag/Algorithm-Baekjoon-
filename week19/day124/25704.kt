package com.example.d20240110


object `25704` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val stamp = input.readLine().toInt()
        val price = input.readLine().toInt()

        val res = toResult(stamp = stamp, price = price)
        println(res)
    }

    private fun toResult(stamp: Int, price: Int): Int {
        val result = mutableListOf<Int>()
        result.add(price)
        if (stamp >= 5) result.add(price - 500)
        if (stamp >= 10) result.add((price * 0.9).toInt())
        if (stamp >= 15) result.add(price - 2000)
        if (stamp >= 20) result.add((price * 0.75).toInt())

        return if (result.min() < 0) 0 else result.min()
    }
}