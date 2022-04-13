data class MatrixCoordinate(val row: Int, val col: Int)


class Matrix(aMatrix: List<List<Int>>) {

    val saddlePoints = potentialMaxRowSaddlePoints(aMatrix).intersect(potentialMinColumnSaddlePoints(aMatrix))

    fun getColumn(aMatrix: List<List<Int>>, indexColumn: Int): List<Int> = aMatrix.map { row -> row[indexColumn] }

    fun applyFunctionOnIndexes(aList: List<Int>, aFunction: (arrayValues: List<Int>) -> Int?): List<Int> =
        aList.mapIndexed { index, value -> if (value == aFunction(aList)) index else -1 }.filter { it != -1 }

    fun indexesOfMin(aColumn: List<Int>): List<Int> = applyFunctionOnIndexes(aColumn, List<Int>::minOrNull)

    fun indexesOfMax(aRow: List<Int>): List<Int> = applyFunctionOnIndexes(aRow, List<Int>::maxOrNull)

    fun potentialMaxRowSaddlePoints(aMatrix: List<List<Int>>): Set<MatrixCoordinate> {
        return aMatrix.mapIndexed { indexRow, row ->
            indexesOfMax(row).map { indexColumn ->
                MatrixCoordinate(
                    row = indexRow + 1,
                    col = indexColumn + 1
                )
            }
        }.flatten().toSet()
    }

    fun potentialMinColumnSaddlePoints(aMatrix: List<List<Int>>): Set<MatrixCoordinate> {
        return aMatrix[0].mapIndexed { indexCol, _ ->
            indexesOfMin(getColumn(aMatrix, indexCol)).map { indexRow ->
                MatrixCoordinate(
                    row = indexRow + 1,
                    col = indexCol + 1
                )
            }
        }.flatten().toSet()
    }


}


