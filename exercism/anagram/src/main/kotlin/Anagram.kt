class Anagram(private val word: String) {

    fun match(potentialAnagrams: Collection<String>): Set<String> =
        potentialAnagrams
            .filter { aPotentialAnagram -> aPotentialAnagram isAnagramOf word }
            .toSet()

    private infix fun String.isAnagramOf(aPotentialAnagram: String) =
        this hasSameLettersAs aPotentialAnagram && this isDifferentOf aPotentialAnagram

    private infix fun String.hasSameLettersAs(aPotentialAnagram: String) =
        frequencyLetterFor(aWord = this) == frequencyLetterFor(aWord = aPotentialAnagram)

    private infix fun String.isDifferentOf(anotherWord: String) = !anotherWord.equals(this, ignoreCase = true)

    private fun frequencyLetterFor(aWord: String): Map<Char, List<Char>> =
        aWord.lowercase().groupBy { it }
}

