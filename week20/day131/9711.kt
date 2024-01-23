package com.example.d20240123

import java.math.BigInteger
import kotlin.math.max

object `9711` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val t = input.readLine().toInt()
        val pList = mutableListOf<Int>()
        val qList = mutableListOf<BigInteger>()
        var maxNum = 0

        (0 until t).forEach { _ ->
            val (p, q) = input.readLine().split(" ")
            pList.add(p.toInt())
            qList.add(BigInteger(q))
            maxNum = max(maxNum.toDouble(), p.toDouble()).toInt()
        }

        val res = initNums(max = maxNum)
        (1 .. t).forEach { n ->
            println("Case #$n: ${res[pList[n - 1]].remainder(qList[n - 1])}")
        }
    }

    private fun initNums(max: Int): List<BigInteger> {
        val nums = MutableList(10001) { toBigInteger() }
        for (i in 3 .. max) {
            nums[i] = nums[i - 1].add(nums[i - 2])
        }
        return nums
    }

    private fun toBigInteger(n: Int = 1) = BigInteger(n.toString())
}