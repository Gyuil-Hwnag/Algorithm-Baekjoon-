package com.example.d20240123

object `15991` {

    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val t = input.readLine().toInt()
        val res = initNums()

        (0 until t).forEach { _ ->
            val num = input.readLine().toInt()
            println(res[num])
        }
    }

    private fun initNums(): List<Long> {
        val res = mutableListOf<Long>(1, 1, 2, 2, 3, 3)
        for (i in 6..100000) {
            val num = ((res[i - 2] + res[i - 4] + res[i - 6]) % 1000000009)
            res.add(num)
        }
        return res
    }
}