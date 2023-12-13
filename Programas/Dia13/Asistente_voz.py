# Instalar e importar las librerias
# pyttsx3
# speechRecognition
# pywhatkit
# yfinance
# pyjokes


# *******************************************************
# LIBRERIAS
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# *******************************************************
# FUNCIONES
# FUNCION CENTRAL
def principal():
    # Activar saludo incicial
    saludo_inicial()

    # Variable de corte
    comenzar = True
    while comenzar:
        # Ativar el micro y guardar el mensaje en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo Youtube.')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('Con gusto, estoy abriendo tu navegador.')
            webbrowser.open('http://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'cuál es la fecha de hoy' in pedido:
            pedir_fecha()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en Wikipedia.')
            pedido = pedido.replace('busca en wikipedia', '')
            try:
                wikipedia.set_lang('es')
                resultado = wikipedia.summary(pedido, sentences=1)
                hablar('Wikipedia dice lo siguiente:')
                hablar(resultado)
                continue
            except:
                hablar('No he encotrado el resultado en Wikipedia')
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso.')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encotrado:')
            continue
        elif 'busca en youtube' in pedido:
            hablar('Buscando en Youtube')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.playonyt(pedido)
            continue
        elif 'dime un chiste' or 'dime otro chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las aacciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGLE'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'El precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('No lo he encontrado')
        elif 'adiós' in pedido:
            hablar('Nos vemos, que tengas un buen día.')
            break


# Función para activar microfono y devolve el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzó la grabación
        print('Escuchando...')

        # Guardar lo que se a escuchado
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-mx")

            # Prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            return pedido
        # En caso de que no comprenda el audio
        except sr.UnknownValueError:

            # Prueba de que no comprendio el audio
            print('No entendí.')

            # Devolver error
            return 'sigo esperando'
        # En caso de que no comprenda el audio
        except sr.RequestError:

            # Prueba de que no comprendio el audio
            print('No hay servicio.')

            # Devolver error
            return 'sigo esperando'

        # En caso de que no comprenda el audio
        except :

            # Prueba de que no comprendio el audio
            print('Algo ha salido mal.')

            # Devolver error
            return 'sigo esperando'

# Función para que Asistente de voz hable
def hablar(mensaje):

    # Voces
    id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
    id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
    id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)
    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# ************
# Informar fecha
def pedir_fecha():
    # crear variable con datos de hoy
    fecha = datetime.date.today()
    hablar(f'hoy es {fecha}')

# Informar del dia de la semana
def pedir_dia():
    # crear variable con datos de hoy
    dia = datetime.date.today()

    # crear variable para el dia de semana
    dia_semana = dia.weekday()

    # diccionario dias de la semana
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

# Informar la hora
def pedir_hora():

    # Crear una variable con datos de la hora
    hora = datetime.datetime.now()

    # Decir la hora
    hablar(f'La hora es. {hora.hour} con {hora.minute} minutos.')

# Saludo
def saludo_inicial():

    # Crear datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 19:
        saludo = 'Buenas noches'
    elif 6 <= hora.hour < 12:
        saludo = 'Buenos días'
    else:
        saludo = 'Buenas tardes'

    # decir saludo
    hablar(f'{saludo}. Soy tu asistente personal, ¿En qué puedo ayudarte?')

principal()
