package com.example.d20240212


object `13414` {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val (k, l) = input.readLine().split(" ").map { it.toInt() }
        val students = mutableListOf<String>()
        for (i in 0 until l) {
            students.add(input.readLine())
        }

        students.toReadyQueue(k).forEach {
            println(it)
        }
    }

    private fun List<String>.toReadyQueue(maxSize: Int): List<String> {
        val ready = this
        val queue = LinkedHashSet<String>()

        ready.forEach {
            val student = it
            if (queue.contains(student)) queue.remove(student)
            queue.add(student)
        }

        return if (queue.size > maxSize) queue.toList().slice(0 until maxSize) else queue.toList()
    }
}