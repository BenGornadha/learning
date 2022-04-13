import org.junit.Test
import java.util.Collections.emptySet
import kotlin.test.assertEquals


class MatrixTest {

    @Test
    fun  `index of min for matrix with only one column`() {
        val aMatrix = Matrix(listOf(emptyList()))
        val inputMatrix = listOf(listOf(5),listOf(1),listOf(4))

        val res2 = aMatrix.potentialMinColumnSaddlePoints(inputMatrix)
        
        assertEquals(setOf(MatrixCoordinate(row = 2, col = 1)), res2)
    
    }

    @Test
    fun `getColumn should return the right values for different index columns one row`(){
        val aMatrix = Matrix(listOf(emptyList()))
        val inputMatrix = listOf(listOf(5,1,4))
        val res=aMatrix.getColumn(inputMatrix,0)
        assertEquals(listOf(5),res)
        val res1=aMatrix.getColumn(inputMatrix,1)
        assertEquals(listOf(1),res1)
        val res2=aMatrix.getColumn(inputMatrix,2)
        assertEquals(listOf(4),res2)

    }

    @Test
    fun `getColumn should return the right values for different index columns multiple rows`(){
        val aMatrix = Matrix(listOf(emptyList()))
        val inputMatrix = listOf(listOf(5,1,4),listOf(1,2,3))
        val res=aMatrix.getColumn(inputMatrix,0)
        assertEquals(listOf(5,1),res)
        val res1=aMatrix.getColumn(inputMatrix,1)
        assertEquals(listOf(1,2),res1)
        val res2=aMatrix.getColumn(inputMatrix,2)
        assertEquals(listOf(4,3),res2)

    }

    @Test
    fun  `index of min for matrix with only one row`() {
        val aMatrix = Matrix(listOf(emptyList()))
        val inputMatrix = listOf(listOf(5,1,4))

        
        val res3 = aMatrix.potentialMinColumnSaddlePoints(inputMatrix)
        assertEquals(setOf(MatrixCoordinate(row = 1, col =1 ),MatrixCoordinate(row = 1, col =2 ),MatrixCoordinate(row = 1, col =3)), res3)
    }

    @Test
    fun `index of max value for list `() {

        val inputMatrix = listOf(listOf(1, 8, 4))
        val aMatrix = Matrix(listOf(emptyList()))

        val res2 = aMatrix.potentialMaxRowSaddlePoints(inputMatrix)
        assertEquals(setOf(MatrixCoordinate(row = 1, col = 2)), res2)
    }


    @Test
    fun `Min indexes of column`() {

        val inputList = listOf(1, 8, 4)
        val aMatrix = Matrix(listOf(emptyList()))
        val res = aMatrix.indexesOfMin(aColumn = inputList)
        assertEquals(listOf(0), res)
    }

    @Test
    fun `Multiple min value for a column`() {
        val inputList = listOf(1, 1, 4)
        val aMatrix = Matrix(listOf(emptyList()))
        val res2 = aMatrix.indexesOfMin(aColumn = inputList)
        assertEquals(listOf(0, 1), res2)


    }

    @Test
    fun `min index of empty column`() {
        val inputList = emptyList<Int>()
        val aMatrix = Matrix(listOf(emptyList()))
        val res2 = aMatrix.indexesOfMin(aColumn = inputList)
        assertEquals(emptyList(), res2)
    }

    @Test
    fun `Max indexes Of row`() {

        val aMatrix = Matrix(listOf(emptyList()))
        val res3 = aMatrix.indexesOfMax(listOf(9, 8, 7))

        assertEquals(listOf(0), res3)
    }

    @Test
    fun `Mutliples max indexes Of row`() {
        val aMatrix = Matrix(listOf(emptyList()))
        val res3 = aMatrix.indexesOfMax(listOf(9, 9, 1))

        assertEquals(listOf(0, 1), res3)
    }

    @Test
    fun `Max indexes Of empty row`() {
        val aMatrix = Matrix(listOf(emptyList()))
        val inputList = emptyList<Int>()
        val res3 = aMatrix.indexesOfMax(inputList)
        assertEquals(emptyList(), res3)
    }

    @Test
    fun `single saddle point`() =
        assertSaddlePointsEqual(
            Matrix(
                listOf(
                    listOf(9, 8, 7),
                    listOf(5, 3, 2),
                    listOf(6, 6, 7)
                )
            ),
            setOf(
                MatrixCoordinate(2, 1)
            )
        )

    @Test
    fun `no saddle points for empty matrix`() =
        assertSaddlePointsEqual(
            Matrix(listOf(emptyList())),
            emptySet()
        )

    @Test
    fun `no saddle points for nonempty matrix`() =
        assertSaddlePointsEqual(
            Matrix(
                listOf(
                    listOf(1, 2, 3),
                    listOf(3, 1, 2),
                    listOf(2, 3, 1)
                )
            ),
            emptySet()
        )

    @Test
    fun `multiple saddle points in a column`() =
        assertSaddlePointsEqual(
            Matrix(
                listOf(
                    listOf(4, 5, 4),
                    listOf(3, 5, 5),
                    listOf(1, 5, 4)
                )
            ),
            setOf(
                MatrixCoordinate(1, 2),
                MatrixCoordinate(2, 2),
                MatrixCoordinate(3, 2)
            )
        )

    @Test
    fun `multiple saddle points in a row`() =
        assertSaddlePointsEqual(
            Matrix(
                listOf(
                    listOf(6, 7, 8),
                    listOf(5, 5, 5),
                    listOf(7, 5, 6)
                )
            ),
            setOf(
                MatrixCoordinate(2, 1),
                MatrixCoordinate(2, 2),
                MatrixCoordinate(2, 3)
            )
        )

    @Test
    fun `saddle point in bottom right corner`() =
        assertSaddlePointsEqual(
            Matrix(
                listOf(
                    listOf(8, 7, 9),
                    listOf(6, 7, 6),
                    listOf(3, 2, 5)
                )
            ),
            setOf(
                MatrixCoordinate(3, 3)
            )
        )

    @Test
    fun `saddle points in a single column matrix`() =
        assertSaddlePointsEqual(
            Matrix(
                listOf(
                    listOf(2),
                    listOf(1),
                    listOf(4),
                    listOf(1)
                )
            ),
            setOf(
                MatrixCoordinate(2, 1),
                MatrixCoordinate(4, 1)
            )
        )

    @Test
    fun `saddle points in a single row matrix`() =
        assertSaddlePointsEqual(
            Matrix(
                listOf(
                    listOf(2, 5, 3, 5)
                )
            ),
            setOf(
                MatrixCoordinate(1, 2),
                MatrixCoordinate(1, 4)
            )
        )
}

private fun assertSaddlePointsEqual(matrix: Matrix, coordinates: Set<MatrixCoordinate>) =
    assertEquals(coordinates, matrix.saddlePoints)

