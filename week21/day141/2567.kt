package com.example.d20240220


/** TODO : 시간초 & 메모리 비교 **/

/**
 * lazy 와 1개의 기능 == 1개의 함수
 * 메모리 : 24444 KB
 * 시간 : 204 ms
 **/
object `2567` {

    private val input by lazy { System.`in`.bufferedReader() }
    private val area by lazy { MutableList(101) { MutableList(101) { 0 } } }

    private val dx by lazy { listOf(-1, 0, 1, 0) }
    private val dy by lazy { listOf(0, 1, 0, -1) }

    private val t by lazy { input.readLine().toInt() }
    private var res = 0

    @JvmStatic
    fun main(args: Array<String>) {
        initArea()
        toResult()
        printResult()
    }

    private fun initArea() {
        for (count in 0 until t) {
            val (x, y) = input.readLine().split(" ").map { it.toInt() }
            for (xx in x until x + 10) {
                for (yy in y until y + 10) {
                    area[xx][yy] = 1
                }
            }
        }
    }

    private fun toResult() {
        for (xx in 0 until 101) {
            for (yy in 0 until 101) {
                if (area[xx][yy] == 1) {
                    var count = 0
                    for (k in 0 until 4) {
                        if (area[xx + dx[k]][yy + dy[k]] == 1) count += 1
                    }

                    when (count) {
                        3 -> res += 1
                        2 -> res += 2
                        else -> {}
                    }
                }
            }
        }
    }

    private fun printResult() = println(res)
}

/**
 * main 함수안에 전부 넣기
 * 메모리 : 24756 KB
 * 시간 : 168 ms
 **/
object `2567allInMain` {

    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val area = MutableList(101) { MutableList(101) { 0 } }
        val t = input.readLine().toInt()
        val dx = listOf(-1, 0, 1, 0)
        val dy = listOf(0, 1, 0, -1)
        var res = 0

        for (count in 0 until t) {
            val (x, y) = input.readLine().split(" ").map { it.toInt() }
            for (xx in x until x + 10) {
                for (yy in y until y + 10) {
                    area[xx][yy] = 1
                }
            }
        }

        for (xx in 0 until 101) {
            for (yy in 0 until 101) {
                if (area[xx][yy] == 1) {
                    var count = 0
                    for (k in 0 until 4) {
                        if (area[xx + dx[k]][yy + dy[k]] == 1) count += 1
                    }

                    when (count) {
                        3 -> res += 1
                        2 -> res += 2
                        else -> {}
                    }
                }
            }
        }

        println(res)
    }
}