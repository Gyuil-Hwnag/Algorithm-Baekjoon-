package com.example.d20240122


object `20299` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val (n, m, s) = input.readLine().split(" ").map { it.toInt() }
        val req = mutableListOf<String>()
        (0 until n).forEach {
            req.add(input.readLine())
        }
        val (passTeams, passPeople) = req.toResult(params = (m to s))
        println(passTeams)
        println(passPeople)
    }

    private fun List<String>.toResult(params: Pair<Int, Int>): Pair<Int, String> {
        val teams = this
        val (m, s) = params
        var passTeam = 0
        val passPeople = mutableListOf<Int>()

        teams.forEach { team ->
            val checkTeam = team.split(" ").map { it.toInt() }
            if (checkTeam.sum() >= m && checkTeam.min() >= s) {
                passTeam += 1
                passPeople.addAll(checkTeam)
            }
        }

        return (passTeam to passPeople.joinToString(" "))
    }
}