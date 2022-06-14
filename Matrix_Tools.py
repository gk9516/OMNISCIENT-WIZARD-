from Matrix_Knowledge import Explanation


Explanation_Result = {'value': 'None'}

def EXPLAIN(Topic,data = None):
    #global Explanation_Result
    if data:
        ex = Explanation[Topic].format(*data)

        Explanation_Result['value'] = ex
    else:
        ex = Explanation[Topic]

        Explanation_Result['value'] = ex

def Construct_Matrix(Matrix,Scalar = None):
    
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
            if Scalar != None and type(Scalar) == int:
                if Scalar < 0:
                    top_bottom_spacing += (len(str(Scalar)))
                else:
                    top_bottom_spacing += (1 + len(str(Scalar)))



    Matrix_str = ''
                
    for i in range(len(Matrix)):
        if i == 0:
            Matrix_str += '┌'+ ' '*(top_bottom_spacing + 2 + len(spacing) - 1) + '┐' + '\n'

        Matrix_str += '│ '


        for j in range(len(spacing)):
            if Scalar != None and type(Scalar) == int :
                if Scalar < 0:
                    Matrix_str += ' '*(spacing[j] - len(str(Matrix[i][j]))) + str(Matrix[i][j])+str(Scalar) + ' '
                else:
                    Matrix_str += ' '*(spacing[j] - len(str(Matrix[i][j]))) + str(Matrix[i][j])+ '+'+ str(Scalar) + ' '
            else:
                Matrix_str += ' '*(spacing[j] - len(str(Matrix[i][j]))) + str(Matrix[i][j])  + ' '
        Matrix_str += '│' + '\n'
    else:
        Matrix_str += '└'+ ' '*(top_bottom_spacing + 2 + len(spacing) - 1) + '┘' + '\n'

    return Matrix_str



def Construct_Transition_Of_Matrices(Matrix1,Matrix2,message = None): #Please give the matrices in str format else you are screwed haha (jk)
    Matrix1Lines = Matrix1.split("\n")
    Matrix2Lines = Matrix2.split("\n")
    #print(Matrix1Lines,Matrix2Lines)
    max_no = max([len(Matrix2Lines),len(Matrix1Lines)])

    space = "              "
    arrow = " -----------> "
    message = message or space
    t_matrices = ""
    mid = (max_no)/2 -1
    print(mid)
    for i in range(max_no-1):
        if i  == mid - 1:
            t_matrices += Matrix1Lines[i] + message + Matrix2Lines[i] + "\n"
        elif i == mid:
            t_matrices += Matrix1Lines[i] + arrow + Matrix2Lines[i] + "\n"
        else:
            t_matrices += Matrix1Lines[i] + space + Matrix2Lines[i] + "\n"

    return t_matrices

def Duplicate_Matrix(Matrix,Return_String = False):
    Mat_Str = []
    NewMatrix = []
    for i in range(len(Matrix)):
        NewMatrix.append(list(Matrix[i]))
        Mat_Str.append(list(Matrix[i]))

    if Return_String:
    	return NewMatrix,Mat_Str
    else:
    	return NewMatrix

def Create_New_Matrix(rows,coloumns):
	NewMatrix = []
	for i in range(rows):
		NewMatrix.append([0]*coloumns)

	return NewMatrix