import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_xlabel('Labels')
    ax.set_ylabel('Values')
    ax.set_title('Bar Chart Example')
    #para no detener el programa y guardar esa imagen
    plt.savefig(f'./imgs/{name}.png')
    plt.close()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    ax.set_title('Pie Chart Example')
    #para no detener el programa y guardar esa imagen
    plt.savefig('./imgs/pie.png')
    plt.close()


if __name__ == '__main__':

#llamamos a las funciones para ver los graficos
    labels = ['a', 'b', 'c']
    values = [100, 200, 300]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
