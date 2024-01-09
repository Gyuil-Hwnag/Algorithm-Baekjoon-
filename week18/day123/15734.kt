package com.example

import kotlin.math.min

object `15734` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        val (left, right, all) = input.split(' ').map { it.toLong() }
        println(Triple(left, right, all).toResult())
    }

    private fun Triple<Long, Long, Long>.toResult(): Long {
        var leftPeople = first
        var rightPeople = second
        var allPeople = third
        while (allPeople > 0) {
            if (leftPeople < rightPeople) {
                leftPeople += 1
                allPeople -= 1
            } else if (rightPeople < leftPeople) {
                rightPeople += 1
                allPeople -= 1
            } else if (allPeople >= 2) {
                rightPeople += 1
                leftPeople += 1
                allPeople -= 2
            } else {
                return 2 * min(leftPeople, rightPeople)
            }
        }
        return 2 * min(leftPeople, rightPeople)
    }
}