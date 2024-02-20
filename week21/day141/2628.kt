package com.example.d20240220


object `2628` {

    private val input by lazy { System.`in`.bufferedReader() }

    private val widths by lazy { mutableListOf<Int>(0) }
    private val heights by lazy { mutableListOf<Int>(0) }

    @JvmStatic
    fun main(args: Array<String>) {
        initWidthHeights()
        setWidthHeights()
        sortedWidthHeights()
        val result = getResults()
        println(result)
    }

    private fun initWidthHeights() {
        val (width, height) = input.readLine().split(" ").map { it.toInt() }
        widths.add(width)
        heights.add(height)
    }

    private fun setWidthHeights() {
        val count = input.readLine().toInt()
        for (i in 0 until count) {
            val (direction, point) = input.readLine().split(" ").map { it.toInt() }
            if (direction == 1) {
                widths.add(point)
            } else {
                heights.add(point)
            }
        }
    }

    private fun sortedWidthHeights() {
        widths.sort()
        heights.sort()
    }

    private fun getResults(): Int {
        val diffWidth = mutableListOf<Int>()
        val diffHeights = mutableListOf<Int>()

        for (index in 0 until widths.size - 1) {
            diffWidth.add((widths[index + 1] - widths[index]))
        }

        for (index in 0 until heights.size - 1) {
            diffHeights.add((heights[index + 1] - heights[index]))
        }

        return diffWidth.max() * diffHeights.max()
    }
}