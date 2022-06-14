from Matrix_Tools import*
from Matrix_Knowledge import Explanation

def ScalarAddition(Matrix,x = None,Explain = None):
    NewMatrix = []
    for i in range(len(Matrix)):
        NewMatrix.append(list(Matrix[i]))
    Row = len(NewMatrix)
    Coloumn = len(NewMatrix[0])
    r = c = 0
    for inputval in range(Row*Coloumn):
        
        #val = int(input("Enter A"+str(Row+1)+str(Coloumn+1)+": "))
        NewMatrix[r][c] += x
        if c < Coloumn-1:
            c += 1
            
        else:
            r +=1
            c = 0
        
    if Explain == True:
        EXPLAIN("Operation_Scalar_Addition",(Construct_Matrix(Matrix),x,Construct_Transition_Of_Matrices(Construct_Matrix(Matrix,x),Construct_Matrix(NewMatrix)),Construct_Matrix(NewMatrix)))
    else:
        return NewMatrix




def ScalarMultiplication(Matrix,Scalar,Return_Matrix_String = False,Explain = False):
    Mat_Str = []
    NewMatrix = []
    for i in range(len(Matrix)):
        NewMatrix.append(list(Matrix[i]))
        Mat_Str.append(list(Matrix[i]))
    Row = len(NewMatrix)
    Coloumn = len(NewMatrix[0])
    r = c = 0

    for inputval in range(Row*Coloumn):
        Mat_Str[r][c] = str(NewMatrix[r][c])+'x'+str(Scalar)
        NewMatrix[r][c] *= Scalar

        if c < Coloumn-1:
            c += 1
        else:
            r +=1
            c = 0
    if Explain:
        EXPLAIN("Operation_Scalar_Multiplication",(Construct_Matrix(Matrix),Scalar,Construct_Transition_Of_Matrices(Construct_Matrix(Mat_Str),Construct_Matrix(NewMatrix)),Construct_Matrix(NewMatrix)))
        
    if Return_Matrix_String:
        return NewMatrix,Mat_Str
    else:
        return NewMatrix





def MatrixAddition(Matrix1,Matrix2,Explain = False,Subtraction = True): 
    NewMatrix1 = Duplicate_Matrix(Matrix1)
    NewMatrix2 = Duplicate_Matrix(Matrix2)

    Mat1 = Construct_Matrix(NewMatrix1)
    Mat2 = Construct_Matrix(NewMatrix2)

    Row1 = len(NewMatrix1)
    Coloumn1 = len(NewMatrix1[0])
    
    Row2 = len(NewMatrix2)
    Coloumn2 = len(NewMatrix2[0])

    Mat_Str = Create_New_Matrix(Row1,Coloumn1)

    if (Row1 == Row2) and (Coloumn1 == Coloumn2):
        print("Both the matrices are in same order. Hence matrix addition is possible. Result is shown below")
        MatrixA = []
        for row in range(Row1):
            r = []
            for value in range(Coloumn1):
                r.append(0)
            MatrixA.append(r)
            r = []
        #print(MatrixA)
        r=c=0
        for inputval in range(Row1*Coloumn1):
        
            MatrixA[r][c] = NewMatrix1[r][c] + NewMatrix2[r][c]
            if NewMatrix2[r][c] < 0:
                Mat_Str[r][c] = str(NewMatrix1[r][c]) + str(NewMatrix2[r][c])
            else:
                Mat_Str[r][c] = str(NewMatrix1[r][c]) + '+' + str(NewMatrix2[r][c])
            if c < Coloumn1-1:
                c += 1
            
            else:
                r +=1
                c = 0
        

        Add_process = Construct_Matrix(Mat_Str)
        Result = Construct_Matrix(MatrixA)
        Result_Transition = Construct_Transition_Of_Matrices(Add_process,Result)
        #print(Result_Transition)

        if Explain == True:
            if Subtraction:
                EXPLAIN("Operation_Matrix_Subtraction",(Construct_Transition_Of_Matrices(Mat1,Mat2).replace("----------->","     and    "),Result_Transition,Result))
            else:
                EXPLAIN("Operation_Matrix_Addition",(Construct_Transition_Of_Matrices(Mat1,Mat2).replace("----------->","     and    "),Result_Transition,Result))
        else:
            return(MatrixA)
        
        
    else:
        if Subtraction:
            EXPLAIN("Operation_Matrix_Subtraction_NP",(Mat1,Mat2))
        else:
            EXPLAIN("Operation_Matrix_Addition_NP",(Mat1,Mat2))

    

def MatrixSubtraction(Matrix1,Matrix2,Explain = False):
    Matrix2 = ScalarMultiplication(Matrix2,-1)
    MatrixAddition(Matrix1,Matrix2,Explain = True)
     
#EXPLANATION DONE TILL HERE

def MatrixMultiplication(Matrix1,Matrix2,Explain = False):

    Matrix1 = Duplicate_Matrix(Matrix1)
    Matrix2 = Duplicate_Matrix(Matrix2)

    Mat1 = Construct_Matrix(Matrix1)
    Mat2 = Construct_Matrix(Matrix2)

    Row1 = len(Matrix1)
    Coloumn1 = len(Matrix1[0])
    
    Row2 = len(Matrix2)
    Coloumn2 = len(Matrix2[0])

    Mat_Str = Create_New_Matrix(Row1,Coloumn1)    

    if (Row1 == Coloumn2):
        
        MatrixM = []
        for row in range(Row1):
            r = []
            for value in range(Coloumn2):
                r.append(0)
            MatrixM.append(r)
            r = []
        
        r=c1=c2=r2=0
        
        x = ''
        for inputval in range(Row1*Coloumn2):       
            for c2 in range(Coloumn1): #Computing the value for one element
                MatrixM[r][c1] += Matrix1[r][c2] * Matrix2[c2][r2]
                x += "+(" + str(Matrix1[r][c2]) + "x" + str(Matrix2[c2][r2]) + ")"
            else:
                Mat_Str[r][c1] = x.lstrip('+')
                x = ''

                
            if c1 < Coloumn2-1:
                c1 += 1
                r2 +=1
            else:
                r +=1
                c1 = 0
                r2 = 0
            #print((r,c1,c2))
        
        Multiplication_Process = Construct_Matrix(Mat_Str)
        Result = Construct_Matrix(MatrixM)

        Result_Transition = Construct_Transition_Of_Matrices(Multiplication_Process,Result)
        pair = Construct_Transition_Of_Matrices(Mat1,Mat2).replace("----------->","     and    ")

        if Explain:
            EXPLAIN("Operation_Matrix_Multiplication",(pair,Result_Transition,Result))
        else:
            return(MatrixM)
        
        
    else:
        pair = Construct_Transition_Of_Matrices(Mat1,Mat2).replace("----------->","     and    ")
        print("No. of rows in first matrix is NOT equal to No. of coloumns in second matrix. Matrix multiplication NOT is possible")
    
def MatrixPower(Matrix,Power,Explain = False):
    return "This operation can exist according to our research, but is too powerful to explain in terms of current knowledge"

def ScalarPower(Matrix,Power,Explain = False):
    NewMatrix = Duplicate_Matrix(Matrix)
    for i in range(Power-1):
        NewMatrix = MatrixMultiplication(NewMatrix,Matrix,Explain = False)
    else:
        print(Construct_Matrix(NewMatrix))
