import matplotlib.pyplot as plt
import numpy as np

class DifferentialEquation:
    def __init__(self, x_0=1, y_0=-2, X=7, n=60, N=120, check_E=True, check_IE=True, check_RK=True, check_exact=True):
        """
        :param check_E: if True prints Euler's method
        :param check_IE: if True prints Improved Euler's method
        :param check_RK: if True prints Runge-Kutta's method
        :param check_exact: if True prints exact solution
        """

        self.x_0 = x_0
        self.y_0 = y_0
        self.X = X
        self.n = n
        self.N = N
        self.check_E = check_E
        self.check_IE = check_IE
        self.check_RK = check_RK
        self.check_exact = check_exact
        self.h = (self.X - self.x_0) / self.n
        self.x_array = np.arange(self.x_0, self.X + self.h, self.h)
        self.C = 1 / self.x_0 - 1 / (np.exp(self.y_0) * self.x_0 ** 2)

    def solve(self):

        self.em = Euler_Method(self.x_0, self.y_0, self.X, self.n, self.N)
        self.iem = Improved_Euler_Method(self.x_0, self.y_0, self.X, self.n, self.N)
        self.rk = Runge_Kutta(self.x_0, self.y_0, self.X, self.n, self.N)
        self.am = Exact(self.x_0, self.y_0, self.X, self.n, self.N)

    def prime_function(self, x, y):
        """
        :param x: corresponding x
        :param y: corresponding y
        :return: result of y_prime(x,y)
        """
        return np.exp(y) - 2 / x

    def functions(self):
        """
        return: graph of functions
        """
        self.all_y = np.array([])
        self.labels = np.array([])
        if self.check_E == True:
            self.all_y = np.append(self.all_y, self.em.solve())
            self.labels = np.append(self.labels, "Euler Method")
        if self.check_IE == True:
            self.all_y = np.append(self.all_y, self.iem.solve())
            self.labels = np.append(self.labels, "Improved Euler Method")
        if self.check_RK == True:
            self.all_y = np.append(self.all_y, self.rk.solve())
            self.labels = np.append(self.labels, "Runge Kutta")
        if self.check_exact == True:
            self.all_y = np.append(self.all_y, self.am.solve())
            self.labels = np.append(self.labels, "Analytical Method")
        if self.labels.size > 0:
            self.all_y = np.array_split(self.all_y, self.labels.size)
            for i in range(self.labels.size):
                plt.plot(self.x_array, self.all_y[i], label=self.labels[i])
            plt.legend()
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.savefig("functions.png")
        return plt.show()

    def GTE(self):
        """
        return: plot of GTE for some methods
        """
        self.y_exact = self.am.solve()
        self.all_y_err = np.array([])
        self.labels = np.array([])
        if self.check_E == True:
            self.all_y_err = np.append(self.all_y_err, abs(self.em.solve() - self.y_exact))
            self.labels = np.append(self.labels, "Euler Method")
        if self.check_IE == True:
            self.all_y_err = np.append(self.all_y_err, abs(self.iem.solve() - self.y_exact))
            self.labels = np.append(self.labels, "Improved Euler Method")
        if self.check_RK == True:
            self.all_y_err = np.append(self.all_y_err, abs(self.rk.solve() - self.y_exact))
            self.labels = np.append(self.labels, "Runge Kutta")
        if self.labels.size > 0:
            self.all_y_err = np.array_split(self.all_y_err, self.labels.size)
            for i in range(self.labels.size):
                plt.plot(self.x_array, self.all_y_err[i], label=self.labels[i])
            plt.legend()
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.savefig("GTE.png")
        return plt.show()

    def LTE(self):
        """
        return: plot of LTE for some methods
        """
        self.y_exact = self.am.solve()
        self.all_y_err = np.array([])
        self.labels = np.array([])
        if self.check_E == True:
            self.all_y_err = np.append(self.all_y_err, abs(self.em.solve_LTE(self.y_exact) - self.y_exact))
            self.labels = np.append(self.labels, "Euler Method")
        if self.check_IE == True:
            self.all_y_err = np.append(self.all_y_err, abs(self.iem.solve_LTE(self.y_exact) - self.y_exact))
            self.labels = np.append(self.labels, "Improved Euler Method")
        if self.check_RK == True:
            self.all_y_err = np.append(self.all_y_err, abs(self.rk.solve_LTE(self.y_exact) - self.y_exact))
            self.labels = np.append(self.labels, "Runge Kutta")
        if self.labels.size > 0:
            self.all_y_err = np.array_split(self.all_y_err, self.labels.size)
            for i in range(self.labels.size):
                plt.plot(self.x_array, self.all_y_err[i], label=self.labels[i])
            plt.legend()
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.savefig("LTE.png")
        return plt.show()

    def GTEM(self, step = 1):
        """
        for each step in range between n and N make approximation and plot maximum for each step
        param step: size of step
        return: plot of max GTE
        """
        self.labels = np.array([])
        if self.check_E == True:
            self.labels = np.append(self.labels, "Euler Method")
        if self.check_IE == True:
            self.labels = np.append(self.labels, "Improved Euler Method")
        if self.check_RK == True:
            self.labels = np.append(self.labels, "Runge Kutta")
        self.max_errs = []
        self.n_arr = np.arange(self.n, self.N + step, step)
        for i in self.n_arr:
            temp = DifferentialEquation(self.x_0, self.y_0, self.X, i, self.N)
            temp.solve()
            self.y_exact = temp.am.solve()
            if self.check_E == True:
                self.max_errs.append(max(abs(temp.em.solve() - self.y_exact)))
            if self.check_IE == True:
                self.max_errs.append(max(abs(temp.iem.solve() - self.y_exact)))
            if self.check_RK == True:
                self.max_errs.append(max(abs(temp.rk.solve() - self.y_exact)))
        if self.labels.size > 0:
            self.max_errs = np.transpose(np.array_split(self.max_errs, self.max_errs.__len__() / self.labels.size))
            for i in range(self.labels.size):
                plt.plot(self.n_arr, self.max_errs[i], label=self.labels[i])
            plt.legend()
        plt.grid()
        plt.xlabel("step size")
        plt.ylabel("max error")
        plt.savefig("max_GTE.png")
        return plt.show()

    def LTEM(self, step = 1):
        """
        for each step in range between n and N make approximation and plot maximum for each step
        :param step: size of step
        :return: plot of max LTE
        """
        self.labels = np.array([])
        if self.check_E == True:
            self.labels = np.append(self.labels, "Euler Method")
        if self.check_IE == True:
            self.labels = np.append(self.labels, "Improved Euler Method")
        if self.check_RK == True:
            self.labels = np.append(self.labels, "Runge Kutta")
        self.max_errs = []
        self.n_arr = np.arange(self.n, self.N + step, step)
        for i in self.n_arr:
            temp = DifferentialEquation(self.x_0, self.y_0, self.X, i, self.N)
            temp.solve()
            self.y_exact = temp.am.solve()
            if self.check_E == True:
                self.max_errs.append(max(abs(temp.em.solve_LTE(self.y_exact) - self.y_exact)))
            if self.check_IE == True:
                self.max_errs.append(max(abs(temp.iem.solve_LTE(self.y_exact) - self.y_exact)))
            if self.check_RK == True:
                self.max_errs.append(max(abs(temp.rk.solve_LTE(self.y_exact) - self.y_exact)))
        if self.labels.size > 0:
            self.max_errs = np.transpose(np.array_split(self.max_errs, self.max_errs.__len__() / self.labels.size))
            for i in range(self.labels.size):
                plt.plot(self.n_arr, self.max_errs[i], label=self.labels[i])
            plt.legend()
        plt.grid()
        plt.xlabel("step size")
        plt.ylabel("max error")
        plt.savefig("max_LTE.png")
        return plt.show()


class Exact(DifferentialEquation):
    def __init__(self, x_0=1, y_0=-2, X=7, n=60, N = 120):
        """
        :param x_0: beginning x
        :param y_0: beginning y
        :param X: end x
        :param n: number of steps
        """
        DifferentialEquation.__init__(self, x_0=x_0, y_0=y_0, X=X, n=n, N = N)
        self.correspond_array = np.array([self.y_0])

    def y(self, x, C):
        """
        :param x: x
        :param C: const
        :return: result of y(x,C)
        """
        return np.log(1 / (x - C * x ** 2))

    def solve(self):
        """
        :return: array of y corresponding to array of  x
        """
        self.correspond_array = np.array([self.y_0])
        for i in range(1, self.x_array.size):
            self.correspond_array = np.append(self.correspond_array, self.y(self.x_array[i], self.C))
        return self.correspond_array


class Euler_Method(DifferentialEquation):
    def __init__(self, x_0=1, y_0=-2, X=7, n=60, N=120):
        """
        :param x_0: beginning x
        :param y_0: beginning y
        :param X: end x
        :param n: number of steps
        """
        DifferentialEquation.__init__(self, x_0=x_0, y_0=y_0, X=X, n=n, N = N)
        self.correspond_array = np.array([self.y_0])

    def solve(self):
        """
        :return: array of y corresponding to array of  x
        """
        self.correspond_array = np.array([self.y_0])
        for i in range(self.x_array.size - 1):
            self.correspond_array = np.append(self.correspond_array, self.correspond_array[i] + self.h * self.prime_function(self.x_array[i], self.correspond_array[i]))
        return self.correspond_array

    def solve_LTE(self, y_ex):
        """
        :param y_ex: array of exact solution's y
        :return: array of y corresponding to array of  x
        """
        self.correspond_array = np.array([self.y_0])
        for i in range(self.x_array.size - 1):
            self.correspond_array = np.append(self.correspond_array,y_ex[i] + self.h * self.prime_function(self.x_array[i], y_ex[i]))
        return self.correspond_array


class Improved_Euler_Method(DifferentialEquation):
    def __init__(self, x_0=1, y_0=-2, X=7, n=60, N=120):
        """
        :param x_0: beginning x
        :param y_0: beginning y
        :param X: end x
        :param n: number of steps
        """
        DifferentialEquation.__init__(self, x_0=x_0, y_0=y_0, X=X, n=n, N=N)
        self.correspond_array = np.array([self.y_0])

    def IEM(self, x, y, h):
        return self.prime_function(x, y) + self.prime_function(x + h, y + h * self.prime_function(x, y))

    def solve(self):
        """
        :return: array of y corresponding to array of  x
        """
        self.correspond_array = np.array([self.y_0])
        for i in range(self.x_array.size - 1):
            self.correspond_array = np.append(self.correspond_array,self.correspond_array[i] + self.h / 2 * self.IEM(self.x_array[i],self.correspond_array[i],self.h))
        return self.correspond_array

    def solve_LTE(self, y_ex):
        """
        :param y_ex: array of exact solution's y
        :return: array of y corresponding to array of  x
        """
        self.correspond_array = np.array([self.y_0])
        for i in range(self.x_array.size - 1):
            self.correspond_array = np.append(self.correspond_array,y_ex[i] + self.h / 2 * self.IEM(self.x_array[i], y_ex[i], self.h))
        return self.correspond_array


class Runge_Kutta(DifferentialEquation):
    def __init__(self, x_0=1, y_0=-2, X=7, n=60, N=120):
        """
        :param x_0: beginning x
        :param y_0: beginning y
        :param X: end x
        :param n: number of steps
        """
        DifferentialEquation.__init__(self, x_0=x_0, y_0=y_0, X=X, n=n, N=N)
        self.correspond_array = np.array([self.y_0])

    def RK(self, x, y, h):
        k1 = self.prime_function(x, y)
        k2 = self.prime_function(x + h / 2, y + h * k1 / 2)
        k3 = self.prime_function(x + h / 2, y + h * k2 / 2)
        k4 = self.prime_function(x + h, y + h * k3)
        return (k1 + 2 * k2 + 2 * k3 + k4)

    def solve(self):
        """
        :return: array of y corresponding to array of  x
        """
        self.correspond_array = np.array([self.y_0])
        for i in range(self.x_array.size - 1):
            self.correspond_array = np.append(self.correspond_array,self.correspond_array[i] + self.h / 6 * self.RK(self.x_array[i],self.correspond_array[i],self.h))
        return self.correspond_array

    def solve_LTE(self, y_ex):
        """
        :param y_ex: array of exact solution's y
        :return: array of y corresponding to array of  x
        """
        self.correspond_array = np.array([self.y_0])
        for i in range(self.x_array.size - 1):
            self.correspond_array = np.append(self.correspond_array,y_ex[i] + self.h / 6 * self.RK(self.x_array[i], y_ex[i], self.h))
        return self.correspond_array
