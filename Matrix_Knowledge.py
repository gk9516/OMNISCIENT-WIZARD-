Explanation = {
	"Diagonal_Matrix_False": 

	"""Given Matrix is a SQUARE MATRIX. Hence it might also possibly be a DIAGONAL MATRIX. 
For a matrix to be a DIAGONAL  MATRIX, all other elements other than its MAIN DIAGONAL must have ZERO value.

Here we clearly see that NOT all of its NON MAIN DIAGONAL elements are zero.
Hence it is NOT a DIAGONAL MATRIX""",

	"Diagonal_Matrix_True":

	"""Given Matrix is a SQUARE MATRIX. Hence it might also possibly be a DIAGONAL MATRIX. 
For a matrix to be a DIAGONAL  MATRIX, all other elements other than its MAIN DIAGONAL must have ZERO value.

Here we clearly see that all of its NON MAIN DIAGONAL elements are ZERO.
Hence it is a DIAGONAL MATRIX""",

	"Diagonal_Matrix_Not_Square": 

	"""Given Matrix is NOT a SQUARE MATRIX. A RECTANGULAR MATRIX CANNOT be a DIAGONAL MATRIX. """,

	"Square_False":

	"""In this Matrix, Number of Rows is NOT EQUAL to Number of Coloumns.
Therefore the given matrix of order {}x{} is NOT a SQUARE MATRIX but instead, a RECTANGULAR MATRIX""",

	"Square_True":

	"""In this Matrix, Number of Rows is EQUAL to Number of Coloumns.
Therefore the given matrix is a SQUARE MATRIX of order {}x{}""",

    "Scalar_True": 

    """The Given Matrix is a Diagonal Matrix. If all of the MAIN DIAGONAL elements are EQUAL, then it will be a SCALAR MATRIX.

Clearly, all of the MAIN DIAGONAL elements have the SAME value of {}.
Therefore the given Matrix is a SCALAR MATRIX of magnitude {} and order {}""",

    "Scalar_False": 

    """The Given Matrix is a Diagonal Matrix. If all of the MAIN DIAGONAL elements are EQUAL, then it will be a SCALAR MATRIX.

But, NOT all of the MAIN DIAGONAL elements have the SAME value.
Therefore the given Matrix is NOT a SCALAR MATRIX""",

    "Scalar_Matrix_Not_Diagonal":

    """For a Matrix to be SCALAR MATRIX, the Matrix must first be a proper DIAGONAL MATRIX.

Given matrix is clearly NOT a diagonal matrix.
Hence the given Matrix is NOT a SCALAR MATRIX""",

    "Identity_True":

    """For a Matrix to be IDENTITY MATRIX, all its MAIN DIAGONAL elements must have the SAME value ONE
and all other NON MAIN DIAGONAL elements must be ZERO. In other words, Identity Matrix is in fact a SCALAR MATRIX of magnitude ONE.

Given Matrix is a SCALAR MATRIX of Magnitude ONE. 
Therefore the given Matrix is an IDENTITY MATRIX of order {} """,

    "Identity_False":

    """For a Matrix to be IDENTITY MATRIX, all its MAIN DIAGONAL elements must have the SAME value ONE
and all other NON MAIN DIAGONAL elements must be ZERO. In other words, Identity Matrix is in fact a SCALAR MATRIX of magnitude ONE.

Given Matrix is a SCALAR MATRIX,
BUT its Magnitude is {}. 
Therefore the given Matrix is NOT an IDENTITY MATRIX""",

    "Identity_Matrix_Not_Scalar": 

    """For a Matrix to be IDENTITY MATRIX, all its MAIN DIAGONAL elements must have the SAME value ONE
and all other NON MAIN DIAGONAL elements must be ZERO.

Clearly the given Matrix does not meet the requirements.
Therefore the given Matrix is NOT an IDENTITY MATRIX.""",

    "Null_False": 

    """For a Matrix to be a NULL MATRIX (or) ZERO MATRIX, all its elements must have a value of ZERO.

Clearly, NOT all of the elements have its value equal to ZERO.
Hence the given Matrix is NOT a NULL MATRIX""",

    "Null_True": 

    """For a Matrix to be a NULL MATRIX (or) ZERO MATRIX, all its elements must have a value of ZERO.

Clearly,all of the elements have its value EQUAL to ZERO.
Hence the given Matrix is a NULL MATRIX""",

    "Operation_Scalar_Addition":

    """Scalar Addition involves the addition of a scalar value to each of the Matrix's elements.

Given Matrix:-
{}
Performing Scalar Addition of {} to the given matrix,
{}
Therefore we get 
{}""",
    
    "Operation_Scalar_Multiplication":

    """Scalar Multiplication involves the multiplication of a scalar value to each of the Matrix's elements.

Given Matrix:-
{}
Performing Scalar multiplication of {} to the given matrix,
{}
Therefore we get 
{}""",

	"Operation_Matrix_Addition":

	"""Matrix Addition of 2 Matrices involves adding the corresponding elements of each matrix to get a new matrix.
Therefore the matrices must be of same order.

Given Matrices:-
{}
It is clear that both matrices are of same order, hence addition of these two matrices is possible.

Performing Matrix Addition, we get:-
{}
Therefore the resultant Matrix is,
{}""",

    "Operation_Matrix_Addition_NP":

    """Matrix Addition of 2 Matrices involves adding the corresponding elements of each matrix to get a new matrix.
Therefore the matrices must be of same order.

Given Matrices:-
{}
{}
It is clear that both matrices are NOT of same order, hence addition of these two matrices NOT possible.""",

    "Operation_Matrix_Subtraction":

    """Matrix Subtraction of one Matrix from another involves adding the negative corresponding elements of second matrix to
the first matrix to get a new matrix.

Therefore the matrices must be of same order.

Given Matrices:-
{}
It is clear that both matrices are of same order, hence subtraction of these two matrices is possible.

Performing Matrix Subtraction, we get:-
{}
Therefore the resultant Matrix is,
{}""",


    "Operation_Matrix_Subtraction_NP":

    """Matrix Subtraction of 2 Matrices involves adding the corresponding elements of each matrix to get a new matrix.
Therefore the matrices must be of same order.

Given Matrices:-
{}
It is clear that both matrices are NOT of same order, hence subtraction of these two matrices NOT possible.""",

    "Operation_Matrix_Multiplication":

    """Matrix Multiplication of two matrices involves the summation of multiplication of a row element of the first matrix with the column elements of
the second matrix.

Therefore according to the definition, the No. of rows of the first matrix must be equal to the No. of columns in the second matrix.

Given Matrices:-
{}
It is clear that the given condition is satisfied, hence multiplication of these two matrices is possible.

Performing Matrix Multiplication, we get:-
{}
Therefore the resultant Matrix is,
{}""",
}