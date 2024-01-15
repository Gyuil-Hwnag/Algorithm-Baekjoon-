package com.example.d20240114


object `1016` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val (minN, maxX) = input.split(' ').map { it.toInt() }
        println(Pair(minN, maxX).toResult())
    }

    private fun Pair<Int, Int>.toResult(): Int {
        val minN = first
        val maxX = second
        val req = mutableListOf<Int>()
        val nums = MutableList(maxX - minN + 1) { 1 }

        for (i in 2 .. Math.sqrt(maxX.toDouble()).toInt()) {
            req.add(i * i)
        }

        for (r in req) {
            var num = minN / r * r
            while (num < maxX + 1) {
                if (num - minN >= 0) nums[num - minN] = 0
                num += r
            }
        }
        return nums.sum()
    }
}