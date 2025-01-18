import matplotlib.pyplot as plt
def generate_pie_chart():
    labels =["A", "B" , "C" ] 
    values =[ 15, 22, 10] 
    ''' que se genere una figura fig con las cordenasdas ax '''
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    '''savegif lo usamos para que cuando se genera la grafica se guarde como imagen'''
    plt.savefig ('pie.png')
    plt.close() 