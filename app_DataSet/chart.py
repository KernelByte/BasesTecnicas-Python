import matplotlib.pyplot as plt

# funcion para grafico de barra
def generate_bar_chart(labels = ["a","b","c"], values = [100,200,300]):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

  # funcion para pie chart
def generate_pie_chart(labels = ["a","b","c"], values = [100,200,300]):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()


if __name__ == '__main__':
   generate_pie_chart()