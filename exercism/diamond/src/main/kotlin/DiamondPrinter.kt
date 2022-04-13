private const val WHITE_SPACE = " "

class DiamondPrinter {

    fun printToList(aLetter: Char): List<String> {
        val diamondLetters = ('A' until aLetter) + (aLetter downTo 'A')
        return diamondLetters.map { letter ->
            createRow(currentLetter = letter, halfLengthRow = positionInAlphabet(aLetter))
        }
    }

    private fun createRow(currentLetter: Char, halfLengthRow: Int) : String {

        val leftPosition = halfLengthRow - positionInAlphabet(currentLetter)
        val rightPosition = halfLengthRow + positionInAlphabet(currentLetter)
        return StringBuilder().apply {
            repeat(halfLengthRow * 2 + 1) { append(WHITE_SPACE) }
            setCharAt(leftPosition, currentLetter)
            setCharAt(rightPosition, currentLetter)
        }.toString()
    }

    private fun positionInAlphabet(aLetter: Char) = aLetter - 'A'

}
