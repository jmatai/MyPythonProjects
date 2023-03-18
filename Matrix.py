class Matrix:
    def __init__(self, n, m, fill=1.0):
        """ This is a Matrix class

        :param n:  The number of rows
        :param m:  The number of columns
        """

        self.rows = n
        self.cols = m
        self.A = [[fill] * self.cols for i in range(self.rows)]


    def __str__(self):
        rows = len(self.A)

        matrix_description = ''
        matrix_description += f'------------- {type(self).__name__} -------------\n'

        for i in range(rows):
            matrix_description += ('|' + ', '.join(map(lambda x: '{0:8.3f}'.format(x), self.A[i])) + '| \n')
        matrix_description += '----------------------------------'
        return matrix_description

    def __add__(self, other):

        # Create a new matrix
        C = Matrix(n=self.rows, m=self.cols, fill=0)

        # Check if the other object is of type Matrix
        if isinstance(other, Matrix):
            # Add the corresponding element of 1 matrices to another
            for i in range(self.rows):
                for j in range(self.cols):
                    C.A[i][j] = self.A[i][j] + other.A[i][j]

        # If the other object is a scaler
        elif isinstance(other, (int, float)):
            # Add that constant to every element of A
            for i in range(self.rows):
                for j in range(self.cols):
                    C.A[i][j] = self.A[i][j] + other

        return C

    def __radd__(self, other):
        return self.__add__(other)





import numpy as np

if __name__ == "__main__":
    A = Matrix(n=4, m=3, fill=1.0)
    print(A)
    """
    A = 
    | 1.000, 1.000, 1.000 |
    | 1.000, 1.000, 1.000 |
    | 1.000, 1.000, 1.000 |
    | 1.000, 1.000, 1.000 |
    """

    A = Matrix(n=4, m=3, fill=1.0)
    B = Matrix(n=4, m=3, fill=2.0)
    C = A + B
    print(C)
    """
    C = 
    | 3.000, 3.000, 3.000 |
    | 3.000, 3.000, 3.000 |
    | 3.000, 3.000, 3.000 |
    | 3.000, 3.000, 3.000 |
    """

    A = Matrix(n=4, m=3, fill=1.0)
    C = 2.0 +A
    print(C)
    """
    C = 
    | 3.000, 3.000, 3.000 |
    | 3.000, 3.000, 3.000 |
    | 3.000, 3.000, 3.000 |
    | 3.000, 3.000, 3.000 |
    """





