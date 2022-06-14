from Matrix_Knowledge import Explanation
from Matrix_Tools import *
from Matrix_Operations import *

Master_Matrix_Data = {}


sample_matrix = [[1,2,3],[1,2,3],[1,2,3]]

class Matrix:
	element = {}

	def __init__(self,nested_list):
		self.rows = len(nested_list)
		self.columns = len(nested_list[0])
		self.__rawmatrix = nested_list
		self.type = self.MatrixType()
		self.trace = self.Trace()

		for i in range(self.rows):
			for j in range(self.columns):
				self.element[f"{i+1}{j+1}"] = nested_list[i][j]

	def IsSquare(self,Matrix = None,Explain = True):
		Matrix = self.__rawmatrix
		if type(Explain) == bool:
			if Explain:
				NR = len(Matrix)
				NC = len(Matrix[0])
				if NR == NC:
					EXPLAIN("Square_True",(NR,NC))
				else:
					EXPLAIN("Square_False",(NR,NC))
			else:
				pass
		else:
			if len(Matrix) == len(Matrix[0]):
				return True
			else:
				return False

	def IsDiagonal(self,Matrix = None,ReqForVal = False,Explain = True): 
	    Reality = False
	    Matrix = self.__rawmatrix
	  
	    DgVal = []
	    
	    if self.IsSquare(Matrix,Explain = None):
	        i = 0
	        j = 0
	        for z in range(len(Matrix)*len(Matrix[0])):
	            if (i != j and Matrix[i][j] != 0) or (i == j and Matrix[i][j] == 0):
	                Reality = False
	                if Explain == True:
	                    EXPLAIN("Diagonal_Matrix_False")
	                break
	            else:
	                pass
	            if j < len(Matrix[0]) - 1:
	                j += 1
	            else:
	                j = 0
	                i += 1
	        else:
	            Reality = True
	            if Explain == True:
	                EXPLAIN("Diagonal_Matrix_True")
	            
	        
	        if ReqForVal:
	            for g in range(len(Matrix)):
	                DgVal.append(Matrix[g][g])
	    else:
	        if Explain == True:
	            EXPLAIN("Diagonal_Matrix_Not_Square")
	    if DgVal:        
	        return Reality,DgVal
	    else:
	        return Reality

	def IsScalar(self,Matrix = None,ReqForVal = False,Explain = True):
	    Reality = False
	    Matrix = self.__rawmatrix
	    if self.IsDiagonal(Matrix):
	        a,b = self.IsDiagonal(Matrix,True)
	        x = b[0]
	        for i in range(1,len(b)):
	            if b[i] != x:
	                if Explain == True:
	                    EXPLAIN("Scalar_False")
	                break
	        else:
	            Reality = True
	            if Explain == True:
	                EXPLAIN("Scalar_True",(x,x,len(b)))
	    else:
	        if Explain == True:
	            EXPLAIN("Scalar_Matrix_Not_Diagonal")

	    if ReqForVal:
	        return Reality,x
	    else:
	        return Reality

    
	def ReturnScalarVal(self,Matrix):
	    try:
	        a,b = self.IsScalar(Matrix,True)
	        if b:
	            return b
	    except:
	        print("Unsuitable Matrix given to find scalar value")
    
	def IsIdentity(self,Matrix = None,Explain = True):
	    if self.IsScalar(self.__rawmatrix):
	        if ReturnScalarVal(self.__rawmatrix) == 1:
	            if Explain == True:
	                EXPLAIN("Identity_True",(len(self.__rawmatrix),))
	            return True
	        else:
	            if Explain == True:
	                EXPLAIN("Identity_False",(self.__rawmatrix[0][0],))
	            return False
	    else:
	        if Explain == True:
	            EXPLAIN("Identity_Matrix_Not_Scalar")
	        return False

	def ReturnDiagonal(self,Matrix = None):
	    try:
	        a,b = self.IsDiagonal(self.__rawmatrix,True)
	        if b:
	            return b
	    except:
	        print("Ineligible Matrix given to return diagonal")
    
	def IsNull(self,Matrix = None,Explain = True):
	    Reality = False
	    i = j = 0
	    for z in range(len(self.__rawmatrix)*len(self.__rawmatrix[0])):
	        if self.__rawmatrix[i][j] != 0:
	            Reality = False
	            if Explain == True:
	                EXPLAIN("Null_False")

	            break
	    
	        if j < len(self.__rawmatrix[0]) - 1:
	            j += 1
	        else:
	            j = 0
	            i += 1
	    else:
	        Reality = True
	        if Explain == True:
	            EXPLAIN("Null_True")
	    return Reality


	def MatrixType(self,Matrix = None):

	    if len(self.__rawmatrix) == 1:
	        return("Row Matrix")
	    elif len(self.__rawmatrix[0]) == 1:
	        return("Coloumn Matrix")
	    elif self.IsIdentity(self.__rawmatrix):
	        return("Identity Matrix")
	    elif self.IsScalar(self.__rawmatrix):
	        return("Scalar Matrix")
	    elif self.IsDiagonal(self.__rawmatrix):
	        return("Diagonal Matrix")
	    elif self.IsNull(self.__rawmatrix):
	        return("Null Matrix")
	    elif self.IsSquare(self.__rawmatrix):
	        return("Square Matrix")
	    else:
	        return("Rectangular Matrix")

	def Trace(self):
	    if self.IsDiagonal(self.__rawmatrix):
	        x = 0
	        for i in self.ReturnDiagonal(self.__rawmatrix):
	            x += i
	        return  x
	    else:
	    	return "Given Matrix is ineligible to have attribute 'trace'"

	def __str__(self):
	    Matrix = self.__rawmatrix
	    spacing = [1]*len(Matrix[0])
	    top_bottom_spacing = 0


	    for i in range(len(Matrix)):
	        for j in range(len(Matrix[0])):
	            a = len(str(Matrix[i][j]))
	            if a > spacing[j]:
	                spacing[j] = a
	    else:
	       	for x in spacing:
	            top_bottom_spacing += x
	        
	    Matrix_str = ''
	                
	    for i in range(len(Matrix)):
	        if i == 0:
	            Matrix_str += '┌'+ ' '*(top_bottom_spacing + 2 + len(spacing) - 1) + '┐' + '\n'

	        Matrix_str += '│ '


	        for j in range(len(spacing)):
	                Matrix_str += ' '*(spacing[j] - len(str(Matrix[i][j]))) + str(Matrix[i][j])  + ' '
	        Matrix_str += '│' + '\n'
	    else:
	        Matrix_str += '└'+ ' '*(top_bottom_spacing + 2 + len(spacing) - 1) + '┘' + '\n'

	    return Matrix_str		

	def __add__(self,other):
		if type(other) == int: #Scalar Addition
			ScalarAddition(self.__rawmatrix,other,Explain = True)
		elif type(self) == type(other): #Matrix Addition
			MatrixAddition(self.__rawmatrix,other.__rawmatrix,Explain = True)
		else:
			print(f"Unsupported Operand between Matrix and {type(other)}")

	def __sub__(self,other):
		if type(other) == int:
			ScalarAddition(self.__rawmatrix,-other,Explain = True)
		elif type(self) == type(other):
			MatrixSubtraction(self.__rawmatrix,other.__rawmatrix,Explain = True)
		else:
			print(f"Unsupported Operand between Matrix and {type(other)}")	

	def __mul__(self,other):
		if type(other) == int:
			ScalarMultiplication(self.__rawmatrix,other,Explain = True)
		elif type(self) == type(other):
			MatrixMultiplication(self.__rawmatrix,other.__rawmatrix,Explain = True)
		else:
			print(f"Unsupported Operand between Matrix and {type(other)}")		

	def __pow__(self,other):
		print(other)
		
		if type(other) == int:
			ScalarPower(self.__rawmatrix,other)
		elif type(self) == type(other):
			MatrixPower(self.__rawmatrix,other.__rawmatrix)
		else:
			print(f"Unsupported Operand between Matrix and {type(other)}")	
		

x = Matrix(sample_matrix)
def execute_user_input(input_):
	try:
		_a = eval(input_)
		print(Explanation_Result['value'])
		return Explanation_Result['value']
	except:
		return "Expression was not able to be executed. Please check your syntax"


