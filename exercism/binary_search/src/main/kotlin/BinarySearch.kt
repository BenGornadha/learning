object BinarySearch {

    fun search(list: List<Int>, item: Int): Int {
        fun dichotomySearch(startIdx: Int, endIdx: Int): Int {

            val middleIndex = ((endIdx - startIdx) / 2) + startIdx
            if (startIdx == endIdx && startIdx == middleIndex && list[middleIndex] != item) throw NoSuchElementException()
            return when {
                (list[middleIndex] > item) -> dichotomySearch(startIdx = startIdx, endIdx = middleIndex)
                (list[middleIndex] < item) -> dichotomySearch(startIdx = middleIndex + 1, endIdx = endIdx)
                else -> middleIndex
            }

        }
        if (list.isEmpty()) throw NoSuchElementException()
        return dichotomySearch(0, list.size - 1)

    }
}
