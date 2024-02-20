package com.example.d20240220


object `2966` {

    private val adrianPattern by lazy { listOf<Char>('A', 'B', 'C') }
    private val brunoPattern by lazy { listOf<Char>('B', 'B', 'A', 'C') }
    private val goranPattern by lazy { listOf<Char>('C', 'C', 'A', 'A', 'B', 'B') }

    private var adrianRes = 0
    private var brunoRes = 0
    private var goranRes = 0

    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()

        val count = input.readLine().toInt()
        val problems = input.readLine()

        patternCheck(problems = problems, count = count)
        val topScore = getTopScore()
        println(topScore)
        topScore.toTopScorer()
    }

    private fun patternCheck(problems: String, count: Int) {
        for (index in 0 until count) {
            if (problems[index] == adrianPattern[index % 3]) adrianRes += 1
            if (problems[index] == brunoPattern[index % 4]) brunoRes += 1
            if (problems[index] == goranPattern[index % 6]) goranRes += 1
        }
    }

    private fun getTopScore(): Int = maxOf(adrianRes, brunoRes, goranRes)

    private fun Int.toTopScorer(): String {
        return when (this) {
            adrianRes -> "Adrian"
            brunoRes -> "Bruno"
            goranRes -> "Goran"
            else -> ""
        }
    }
}