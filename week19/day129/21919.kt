package com.example.d20240120

object `21919` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val n = input.readLine().toInt()
        val nums = input.readLine().split(" ").map { it.toInt() }
        val primes = nums.toPrimeList()
        println(primes.toResult())
    }

    private fun List<Int>.toResult(): Int {
        val nums = this
        var res = nums.first()
        nums.forEach{ res = lcm(res, it) }
        return if (res == nums.first()) -1 else res
    }

    private fun lcm(a:Int, b:Int) = a * b / gcd(a, b)

    private fun gcd(a: Int, b: Int): Int = if (b != 0) gcd(b, a % b) else a

    private fun List<Int>.toPrimeList(): List<Int> {
        val req = mutableListOf<Int>()
        val nums = this
        nums.forEach { num ->
            if (num.isPrime()) req.add(num)
        }

        return req
    }

    private fun Int.isPrime(): Boolean {
        val num = this
        (2 until (num / 2) step 1).forEach {  n ->
            if (num % n == 0) return false
        }

        return true
    }
}