import numpy as np
import matplotlib.pyplot as plt




plt.show()



class plt_graph:
    def line_graph(self):
        x = np.arange(5)
        y = x**2
        plt.plot(x, y)

    def bar_graph(self):
        x = np.arange(3)
        y = np.array([100, 30, 70])
        plt.bar(x, y)

    def pie_chart(self):
        x = np.array([12, 23, 100])
        str_label = ['a', 'b', 'c']
        plt.pie(x, labels=str_label, counterclock=False, startangle=90)

    def band_graph(self):
        print('next')

    def histgram(self):
        x = np.random.normal(50, 10, 100)
        plt.hist(x)

    def rader_chart(self):
        labels = ['a', 'b', 'c', 'd']
        values = [10, 20, 30, 40]
        angles = np.linspace(0, 2*np.pi, len(labels) + 1, endpoint=True)
        values = np.concatenate((values, [values[0]]))

        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, values, 'o-')
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)

    def Pareto_chart(self):
        x = np.arange(4)
        y1 = np.array([10, 5, 3, 2])
        sum_y1 = np.sum(y1)
        y2 = np.cumsum(y1) / sum_y1

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax2 = ax1.twinx()

        ax1.bar(x, y1)
        ax2.plot(x, y2, c='r')

    def scatter_graph(self):
        x = np.random.rand(10)
        y = np.random.rand(10)
        plt.scatter(x, y)

    def box_plot(self):
        spread = np.random.rand(50) * 100
        center = np.ones(25) * 50
        flier_high = np.random.rand(10) * 100 + 100
        flier_low = np.random.rand(10) * -100
        data = np.concatenate((spread, center, flier_high, flier_low))

        plt.boxplot(data)

    def contour_plot(self):
        delta = 0.025
        x = np.arange(-3.0, 3.0, delta)
        y = np.arange(-2.0, 2.0, delta)
        X, Y = np.meshgrid(x, y)
        Z1 = np.exp(-X**2 - Y**2)
        Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
        Z = (Z1 - Z2) * 2

        CS = plt.contour(X, Y, Z)

    def arrows_polt(self):
        X = [1, 3]
        Y = [2, 4]
        U = [5, 60]
        V = [70, 8]
        plt.quiver(X, Y, U, V)




if __name__ == '__main__':
    class_plt = plt_graph()
    # class_plt.line_graph()
