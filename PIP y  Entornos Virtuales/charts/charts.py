import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A","B","C"]
    values = [20,30,40]

    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig("pie.png")
    plt.close()