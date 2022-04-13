private const val BEVERAGE = "beer"

private const val ON_THE_WALL = "on the wall"

object BeerSong {
    fun verses(startBottles: Int, takeDown: Int): String {
        return (startBottles downTo takeDown).joinToString(separator = "\n") { oneVerse(it) }
    }

    private fun oneVerse(numberBottle: Int): String {
        return ("${bottleStatement(numberBottle)} $ON_THE_WALL, ${bottleStatement(numberBottle)}.\n" +
                "${takeStatement(numberBottle)}, ${bottleStatement(numberBottle - 1)} $ON_THE_WALL.\n")
            .replaceFirstChar(Char::titlecase)
    }

    private fun takeStatement(numberBottle: Int): String {
        return when (numberBottle) {
            0 -> "Go to the store and buy some more"
            1 -> "Take it down and pass it around"
            else -> "Take one down and pass it around"
        }
    }

    private fun bottleStatement(numberBottle: Int): String {
        return when (numberBottle) {
            -1 -> "99 bottles of $BEVERAGE"
            0 -> "no more bottles of $BEVERAGE"
            1 -> "1 bottle of $BEVERAGE"
            else -> "$numberBottle bottles of $BEVERAGE"
        }
    }
}
