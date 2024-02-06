package com.example.d20240206


object `15992` {

    private const val MAX = 1001
    private const val DIVIDER = 1000000009

    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val t = input.readLine().toInt()
        val req = initList()

        (0 until t).forEach { _ ->
            val (n, m) = input.readLine().split(" ").map { it.toInt() }
            println(req.toResult(n = n, m = m))
        }
    }

    private fun Array<LongArray>.toResult(n: Int, m: Int): Long {
        return this[n][m]
    }

    private fun initList(): Array<LongArray> {
        val dp = Array(MAX) { LongArray(MAX) }
        dp[1][1] = 1

        dp[2][1] = 1
        dp[2][2] = 1

        dp[3][1] = 1
        dp[3][2] = 2
        dp[3][3] = 1

        for (i in 4 until MAX) {
            for (j in 1..i) {
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % DIVIDER
            }
        }
        return dp
    }
}
