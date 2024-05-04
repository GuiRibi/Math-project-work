import numpy

#initial values
A = float(input("Value of 'A':\n"))
B = float(input("Value of 'B':\n"))
C = float(input("Value of 'C':\n"))
x_0 = float(input("Value of 'x_0':\n"))
y_0 = float(input("Value of 'y_0':\n"))

class vectorial:
    def farray(array):
        x = array[0][0]
        y = array[1][0]

        return (A * x*x - B * x*y + C * y*y + x - y)
    
    # def get_alpha_array(array, G, f_xy):
    #     #trying to find the best value for alpha
    #     alpha = 1.0

    #     while array.farray(numpy.subtract(array, vectorial.DotProduct(alpha, G))) > f_xy:
    #         alpha *= 0.9

    #     return alpha
    
    def new_iteration_array(array, G, alpha):
        return numpy.subtract(array, numpy.dot(alpha, G))
    
    

    def DotProduct(array1, array2):

        return numpy.dot(array1, array2)
    
    def Vectorial():
        #equations
        X = x_0
        Y = y_0 
        array = numpy.array([[X],[Y]])

        for i in range(500):
            df_dx = (2*A * array[0][0] - B * array[1][0] + 1)
            df_dy = (2*C * array[1][0] - B * array[0][0] - 1)

            G = numpy.array([[df_dx],[df_dy]])

            # ddf_dx = 2*A
            # ddf_dy = 2*C
            # ddf_dxdy = -B
            # ddf_dydx = -B

            # H = numpy.array([[ddf_dx, ddf_dxdy],[ddf_dydx, ddf_dy]])
            # H_1 = numpy.linalg.inv(H)
            
            #defining alpha
            alpha = scalar.get_alpha_array(array, df_dx, df_dy)

            #finding the new values
            array_new = vectorial.new_iteration_array(array, G, alpha)

            difference = max(abs(numpy.subtract(array_new, array)[0]), abs(numpy.subtract(array_new, array)[1]))

            if (abs(difference) < 0.000001):
                print(f"iteration nº: {i} with array = {array_new}. The minimum of f(x, y) = {vectorial.farray(array_new)}")
                break
            else: 
                print(f"Step: {i}, difference: {difference}, array: {array_new}, a = {alpha}")
                array = array_new


class scalar:
    def Vectorial():
        #equations
        X = x_0
        Y = y_0 
        array = numpy.array([[X],[Y]])

        for i in range(500):

            h = 0.0000001

            X = array[0][0]
            Y = array[1][0]

            X_h = array[0][0] + h
            Y_h = array[1][0] + h
            df_dx = (scalar.f(X_h, Y)-scalar.f(X, Y)) / h
            df_dy = (scalar.f(X, Y_h)-scalar.f(X, Y)) / h

            ddf_dx = 2*A * X - B * Y + 1
            ddf_dy = 2*C * Y - B * X - 1

            #H = numpy.array([[ddf_dx, ddf_dy]])
            #H_1 = numpy.power(H, -1)
            
            #defining alpha
            alpha = scalar.get_alpha_array(array, ddf_dx, ddf_dy)

            #finding the new values
            array_new = scalar.new_iteration_array(array, df_dx, df_dy, alpha)

            difference = max(abs(numpy.subtract(array_new, array)[0]), abs(numpy.subtract(array_new, array)[1]))

            if (abs(difference) < 0.000001):
                print(f"iteration nº: {i} with array = {array_new}. The minimum of f(x, y) = {vectorial.farray(array_new)}")
                break
            else: 
                print(f"Step: {i}, difference: {difference}, array: {array_new}, a = {alpha}")
                array = array_new

    def f(x, y):
        #fuction
        return A * x*x - B * x*y + C * y*y + x - y

    # def Scalar():
    #     #equations
    #     X = x_0
    #     Y = y_0 
    #     #alpha = 0.7

    #     for i in range(1000):
    #         alpha = 0.5/(1+0.05*(i+1))
    #         equation = scalar.f(X, Y)

    #         h = 0.1

    #         X_h = X + h
    #         Y_h = Y + h
    #         df_dx = ((A * X_h*X_h - B * X_h*Y_h + X_h)-(A * X*X - B * X*Y + X))/h
    #         df_dy = ((C * Y_h*Y_h - B * X_h*Y_h - Y_h)-(C * Y*Y - B * X*Y - Y))/h

    #         #finding alpha
    #         #alpha = scalar.get_alpha(X, Y, df_dx, df_dy, equation)

    #         #finding the new values
    #         X_new, Y_new = scalar.new_iteration(X, Y, df_dx, df_dy, alpha)

    #         difference = max(abs(X_new-X), abs(Y_new-Y))

    #         if (abs(difference) < 0.000001):
    #             print(f"iteration nº: {i}. difference: {difference} with X = {X_new} and Y = {Y_new}. The minimum of f(x, y) = {scalar.f(X_new, Y_new)}")
    #             break
    #         else: 
    #             print(f"Step: {i}, difference: {difference}, X: {X_new}, Y: {Y_new}, a = {alpha}")
    #             X = X_new
    #             Y = Y_new
    #             alpha = 0.5/(1+0.05*(i+1))
            


    # def get_alpha(X, Y, df_dx, df_dy, f_xy):
    #     #trying to find the best value for alpha
    #     alpha = 1.0

    #     while scalar.f(X - alpha * df_dx, Y - alpha * df_dy) > f_xy:
    #         alpha *= 0.9

    #     return alpha

    # def new_iteration(X, Y, df_dx, df_dy, alpha):
    #     X_new = (X - alpha * X )* df_dx
    #     Y_new = (Y - alpha * Y )* df_dy

    #     return X_new, Y_new
    
    def new_iteration_array(array, df_dx, df_dy, alpha):
        f_x = array[0][0] - alpha * df_dx
        f_y = array[1][0] - alpha * df_dy 

        array_new = [[f_x], [f_y]]

        return array_new
    
    # def sec_der(x, y, h):
    #     return (scalar.f(x + h, y + h) - 2 * scalar.f(x, y) + scalar.f(x - h, y - h)) / (h*h)
    
    def get_alpha_array(array, df_dx, df_dy):
        #trying to find the best value for alpha
        x = array[0][0]
        y = array[1][0]

        alpha = -(df_dx * (-1 - 2 * A * x + B * y) + df_dy * (1 + B * x - 2 * C * y)) / (-2 * df_dy * B * df_dx + 2 * A * df_dx * df_dx + 2 * df_dy * df_dy * C)
        
        return alpha

#scalar.Vectorial or vectorial.Vectorial to start
inp = input("Select (1) Vectorial or (2) scalar:\n")
if inp == "1":
    vectorial.Vectorial()
elif inp == "2":
    scalar.Vectorial()
else:
    print("No method was selected, quitting.")
