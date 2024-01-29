package com.example.d20240127

import java.util.*

object `3613` {

    private const val ERROR = "Error!"

    @JvmStatic
    fun main(args: Array<String>) {
        val input = System.`in`.bufferedReader().readLine()
        when (input.contains("_")) {
            true -> println(input.cToJava())
            false -> println(input.javaToC())
        }
    }

    private fun String.javaToC(): String {
        val res = StringBuilder()
        val req = this
        for (i in req.indices) {
            if (req[i].isUpperCase()) {
                if (i == 0) return ERROR
                else res.append("_${req[i].toLowerCase()}")
            } else {
                res.append(req[i].toLowerCase())
            }
        }

        return res.toString()
    }

    private fun String.cToJava(): String {
        val res = StringBuilder()
        val req = this
        if (req.contains("__") || req.startsWith('_') ||
                req.endsWith('_') ||
                !req.all { it.isLowerCase() || it == '_' }
        ) return ERROR

        req.split("_").forEachIndexed { index, word ->
            if (index == 0) res.append(word)
            else res.append(word.replaceFirstChar { if (it.isLowerCase()) it.titlecase(Locale.getDefault()) else it.toString() })
        }

        return res.toString()
    }
}