package com.example.d20240212

import java.text.SimpleDateFormat


object `5635` {

    private const val DATE_FORMAT = "yyyyMMdd"

    data class People(val name: String, val birthDay: Long)

    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader()
        val t = input.readLine().toInt()
        val peoples = mutableListOf<People>()

        (0 until t).forEach { _ ->
            val (name, day, month, year) = input.readLine().split(" ")
            val date = year + month.toFormatUnderTen() + day.toFormatUnderTen()
            val birthDay = SimpleDateFormat(DATE_FORMAT).parse(date).toInstant().toEpochMilli()
            peoples.add(People(name = name, birthDay = birthDay))
        }

        peoples.sortBy { it.birthDay }
        println(peoples.last().name)
        println(peoples.first().name)
    }

    private fun String.toFormatUnderTen(): String = if (this.toInt() < 10) "0${this}" else this
}

