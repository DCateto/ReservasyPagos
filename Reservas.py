import pandas as pd
import numpy as np
import datetime
from itertools import groupby

# Utilizaremos esta lista para el encabezado de los data frames
hor = ['14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00','Capacidad'] 

# Salón Privado (PS)
ps_disp = [
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15]
             ]
ps_mes = ['Mesa 1','Mesa 2', 'Mesa 3'] #En este caso Mesa = Salon, para simplicicidad del código.

# Salón Interior (IS)
is_disp = [
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
             ]
is_mes = [
            'Mesa 4','Mesa 5', 'Mesa 6','Mesa 7', 'Mesa 8','Mesa 9', 'Mesa 10', 'Mesa 11', 'Mesa 12', 'Mesa 13',
            'Mesa 14', 'Mesa 15', 'Mesa 16', 'Mesa 17', 'Mesa 18', 'Mesa 19', 'Mesa 20', 'Mesa 21', 'Mesa 22',
            'Mesa 23','Mesa 24', 'Mesa 25', 'Mesa 26', 'Mesa 27', 'Mesa 28', 'Mesa 29'
         ]

# Terraza (TR)
tr_disp = [
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
             ]
tr_mes = [
            'Mesa 30','Mesa 31', 'Mesa 32','Mesa 33', 'Mesa 34','Mesa 35', 'Mesa 36', 'Mesa 37', 'Mesa 38', 'Mesa 39',
            'Mesa 40', 'Mesa 41', 'Mesa 42', 'Mesa 43', 'Mesa 44', 'Mesa 45', 'Mesa 46', 'Mesa 47', 'Mesa 48', 'Mesa 49',
            'Mesa 50', 'Mesa 51', 'Mesa 52', 'Mesa 53', 'Mesa 54', 'Mesa 55', 'Mesa 56', 'Mesa 57', 'Mesa 58', 'Mesa 59'
         ]
df_ps = pd.DataFrame(ps_disp, columns = hor, index = ps_mes)
df_ps
df_is = pd.DataFrame(is_disp, columns = hor, index = is_mes)
df_is
df_tr = pd.DataFrame(tr_disp, columns = hor, index = tr_mes)
df_tr
df_tr.loc['Mesa 58', ['18:00','19:00']] == '1'
dataframes = {'df_ps': df_ps, 'df_is': df_is, 'df_tr': df_tr}
d = {'Nombre': ['Test'], 'Teléfono': [999999999], 'Mesa': ['Test 1'], 'Hora Inicio': ['14:00'], 'Tiempo (Hrs)': [2]} 
res_data = pd.DataFrame(data=d)
res_data
dp = {'Fecha':['2023-11-27'], 'Hora':['03:47:44'], 'Mesa':['Mesa Test'], 'Monto':[9999999], 'Método de Pago':['Crédito']}
pagos_data = pd.DataFrame(data=dp)
pagos_data

def capacity():
    """
    Requiere el número de personas que ocuparán la mesa 
    
    """
    capacities = [2, 4, 6, 8, 15]
    x = int(input('Ingrese la capacidad requerida (2, 4, 6, 8, 15[PS]):'))
    while x not in capacities:
        x = input('Por favor, ingrese un número válido: ')
    return int(x)

################################################################################################################################
            
def ambient():
    """ 
    Consultará al encargado el tipo de ambiente que requiere el cliente: salón privado (PS), salón interior (IS) o terraza (TR)
    """
    ambients = ['PS','IS','TR']
    x = input('Ingrese el tipo de ambiente (PS/IS/TR): ')
    while x not in ambients:
        x = input('Por favor, ingrese un tipo de ambiente válido (PS/IS/TR): ')
    return dataframes['df_' + x.lower()]

################################################################################################################################

def df_filter(c, df):
    """
    c = capacidad
    df = ambiente
    Filtra los data frames respecto a la capacidad y al menos un horario disponible
    """
    hours = ['14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    
    # Filtrar el DataFrame basado en la capacidad
    df_filtered = df.loc[df['Capacidad'] >= c]

    # Crear una máscara para las mesas disponibles
    mask = (df_filtered[hours] != 1).any(axis=1)

    # Si ninguna mesa está disponible, mostrar un mensaje y devolver un DataFrame vacío
    if not mask.any():
        print('No hay mesas disponibles en este ambiente.')
        return pd.DataFrame()

    # Aplicar la máscara al DataFrame
    df_final = df_filtered[mask]

    return df_final

################################################################################################################################

def hour_fix(c, df, df_fil, res_data):
    """
    Función con la cual fijaremos los horarios que requiere el cliente en el dataframe filtrado y datos del cliente
    """
    
    # Solicitar al usuario que ingrese el número de la mesa
    mesa = input('Ingrese el número de la mesa que desea reservar (por ejemplo, "Mesa 1"):')
    while mesa not in df_fil.index:
        mesa = input('Por favor, ingrese un número de mesa válido: ')
    print('--------------------------------------------------')

    # Solicita al usuario la hora de inicio de la reserva
    hours = ['14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    x = input('Ingrese la hora de inicio de la reserva (14:00 - 23:00): ')
    while x not in hours:
        x = input('Por favor, ingrese una hora de inicio válida (14:00 - 23:00): ')
    print('--------------------------------------------------')

    # Solicita al usuario que ingrese el número de horas que reservará la mesa
    total_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t = int(input('Ingrese la cantidad de horas de la reserva: '))
    while t not in total_hours:
        t = input('Por favor, ingrese un número entre 1 y 10: ')
    print('--------------------------------------------------')

    # Obtener el índice de la hora de inicio en la lista de horas
    start_index = hours.index(x)

    # Verificar si las t horas siguientes están disponibles
    while df.loc[mesa, hours[start_index:start_index+int(t)]].any() == 1:
        print('Las horas seleccionadas no están disponibles. Por favor, ingrese una nueva hora de inicio y cantidad de horas.')
        x = input('Ingrese la hora de inicio de la reserva (14:00 - 23:00):')
        while x not in hours:
            x = input('Por favor, ingrese una hora de inicio válida (14:00 - 23:00):')
        print('--------------------------------------------------')
        t = int(input('Ingrese la cantidad de horas de la reserva'))
        while t not in total_hours:
            t = input('Por favor, ingrese un número entre 1 y 10:')
        print('--------------------------------------------------')
        start_index = hours.index(x)

    # Confirmar la reserva
    confirmacion = input(f'Por favor, confirme la reserva: {mesa} a partir de {x} por {t} horas. Ingrese "Y" para confirmar o "N" para cancelar:')
    while confirmacion not in ['Y', 'N']:
        confirmacion = input('Por favor, ingrese una respuesta válida ("Y" o "N"):')
    print('--------------------------------------------------')

    if confirmacion == 'Y':
        # Solicitar al usuario que ingrese su nombre y teléfono
        nombre = input('Ingrese nombre del cliente:')
        telefono = input('Ingrese teléfono del cliente (Ejemplo: 123456789):')
        print('--------------------------------------------------')

        # Si el usuario confirma la reserva, agregarla al DataFrame de reservas
        new_res = pd.DataFrame({'Nombre': nombre, 'Teléfono': telefono, 'Mesa': mesa, 'Hora Inicio': x, 'Tiempo (Hrs)': t}, index=[0])
        res_data = pd.concat([res_data, new_res])
        
        # Resetear los índices del DataFrame de reservas
        res_data = res_data.reset_index(drop=True)

        # Actualizar el DataFrame original del ambiente con la reserva confirmada
        df.loc[mesa, hours[start_index:(start_index+int(t))]] = 1

        print('La reserva ha sido confirmada.')
        print('--------------------------------------------------')
    else:
        print('La reserva ha sido cancelada.')
        print('--------------------------------------------------')

    return df, res_data
def metodo_de_pago():
    """ Retorna el medio de pago

    Se pide un input y se revisa que este en el rango, luego se guarda un 
    elemento de la lista de metodos de pago

    """
    l = ['1. Efectivo', '2. Débito', '3. Crédito']
    print('Métodos de pago:\n')
    for elem in l:
        print(elem)
    x = int(input('Ingrese el número del método de pago: '))
    while x<=0 or x>=5:
        x = int(input('Error, ingrese número válido: '))
    return l[x-1][3:]

def generar_boleta(mesa, total, pagos_data):
    """
    Genera una "boleta" con el número de mesa, el total consumido, y la fecha y hora actuales.
    También agrega los datos de la boleta al DataFrame pagos_data.

    """
    # Obtener la fecha y hora actuales
    ahora = datetime.datetime.now()

    metodo_pago = metodo_de_pago()
    boleta = f"Boleta:\nFecha: {ahora.strftime('%Y-%m-%d')}\nHora: {ahora.strftime('%H:%M:%S')}\nMesa: {mesa}\nTotal: ${total}\nMétodo de Pago: {metodo_pago}"
    
    # Agregar los datos de la boleta al DataFrame pagos_data
    new_pago = pd.DataFrame({'Fecha': [ahora.strftime('%Y-%m-%d')], 'Hora': [ahora.strftime('%H:%M:%S')], 'Mesa': [mesa], 'Monto': [total], 'Método de Pago': [metodo_pago]})
    pagos_data = pd.concat([pagos_data, new_pago])
        
    # Resetear los índices del DataFrame de pagos
    pagos_data = pagos_data.reset_index(drop=True)

    return boleta, pagos_data

cont = 'Y' #V.A. para continuar reservando mesas "cerrar la sesión"
while cont == 'Y':
    ###########################################################
    c = capacity()
    print('--------------------------------------------------')
    a = ambient()
    print('--------------------------------------------------')
    df_filtered = df_filter(c,a)
    print(df_filtered)
    print('--------------------------------------------------')
    ###########################################################
    conf = input('¿Desea confirmar la reserva?(Y/N)')
    while conf not in ['Y', 'N']:
        conf = input('Por favor, ingrese una respuesta válida ("Y" o "N"):')
    print('--------------------------------------------------')
    ###########################################################
    if conf == 'Y':
        (a,res_data) = hour_fix(c, a, df_filtered, res_data)
    ###########################################################
    cont = input('¿Desea continuar reservando?(Y/N)')
    while cont not in ['Y', 'N']:
        cont = input('Por favor, ingrese una respuesta válida ("Y" o "N"):')
    print('--------------------------------------------------')
print('---------- Hasta Pronto ----------')
print('----------------------------------')

res_data

cob = 'Y'
while cob == 'Y':
    mesa = input('Ingrese la mesa a cobrar:\n')
    while mesa not in ps_mes + is_mes + tr_mes:
        mesa = input('Por favor, ingrese una mesa válida:')
    print('--------------------------------------------------')
    total = int(input('Ingrese el monto total:\n'))
    while total < 0:
        mesa = int(input('Por favor, ingrese un monto válido:'))
    print('--------------------------------------------------')
    (c,pagos_data) = generar_boleta(mesa,total,pagos_data)
    print(c)
    print('--------------------------------------------------')
    cob = input('¿Desea realizar otro cobro?(Y/N)')
    while cob not in ['Y', 'N']:
        cob = input('Por favor, ingrese una respuesta válida ("Y" o "N"):')
    print('--------------------------------------------------')
print('---------- Hasta Pronto ----------')
print('----------------------------------')

pagos_data