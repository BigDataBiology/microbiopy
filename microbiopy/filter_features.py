# MICROBIOPY


def filter_features(matrix, min_prevalence=0, min_prevalence_fraction=0.0,
                    min_abundance=0, min_abundance_fraction=0.0):
    """Filters features across samples based on argument.

    Input
    -----
    Sample-by-feature matrix.

    Arguments
    ---------
    min_prevalence(int): the minimum prevalence.
    min_prevalence_fraction(float): the minimum prevalence fraction.
    min_abundance(int): the minimum abundance.
    min_abundance_fraction(float): the minimum abundance fraction.

    Output
    ------
    A tuple having two matrices of all features that pass the filter
    of minimum prevalence/abundance and minimum prevalence/abundance fraction.
    """

    count = 0
    m = len(matrix)                                           	# rows
    n = len(matrix[0])                                        	# columns
    boolmatrix = [[0 for j in range(n)] for i in range(m)]    	# m * n matrix
    resmatrix_p = [[0 for j in range(n)] for i in range(m)]   	# m * n matrix
    resmatrix_p_f = [[0 for j in range(n)] for i in range(m)] 	# m * n matrix
    resmatrix_a = [[0 for j in range(n)] for i in range(m)]   	# m * n matrix
    resmatrix_a_f = [[0 for j in range(n)] for i in range(m)] 	# m * n matrix

    if min_prevalence or min_prevalence_fraction:
        count = 1

    if min_abundance or min_abundance_fraction:
        count = 2

    if count == 1:
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    boolmatrix[i][j] = 1

        for j in range(n):
            csum = 0                                           	# column-sum
            for i in range(m):
                csum += boolmatrix[i][j]
            if min_prevalence and (csum >= min_prevalence):
                for i in range(m):
                    resmatrix_p[i][j] = matrix[i][j]
            if (min_prevalence_fraction and
               ((float(csum)/m) >= min_prevalence_fraction)):
                for i in range(m):
                    resmatrix_p_f[i][j] = matrix[i][j]

        return (resmatrix_p, resmatrix_p_f)

    elif count == 2:
        total_sum = 0
        for i in range(m):
            for j in range(n):
                total_sum += matrix[i][j]

        for j in range(n):
            csum = 0                                           	# column-sum
            for i in range(m):
                csum += matrix[i][j]
            if min_abundance and (csum >= min_abundance):
                for i in range(m):
                    resmatrix_a[i][j] = matrix[i][j]
            if (min_abundance_fraction and
               ((float(csum)/total_sum) >= min_abundance_fraction)):
                for i in range(m):
                    resmatrix_a_f[i][j] = matrix[i][j]

        return (resmatrix_a, resmatrix_a_f)

    else:
        print("Neither prevalence nor abundance given.")
