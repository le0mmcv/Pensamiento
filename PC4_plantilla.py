# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# streamlit hello

# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Bits & Bytes</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("DSC_0064.jpg", caption='El código es poesía... escrita en un idioma que nadie realmente entiende, ni siquiera el poeta', width=300)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
Hola, soy Leonardo, vengo de Cusco, y actualmente soy un estudiante de quinto ciclo de Comunicación Audiovisual. Lo que más me apasiona de mi carrera es la capacidad de contar historias de manera creativa, utilizando imágenes y sonidos para transmitir distintos mensajes. En el futuro, me gustaría dedicarme a la producción y dirección de proyectos audiovisuales que no solo entretengan, sino que sean reflexivos. En mi tiempo libre, disfruto viendo películas de diferentes géneros y estilos, siempre busco aprender nuevas habilidades que puedan enriquecer mis proyectos y mi conocimiento en el campo audiovisual.
"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.


# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
Aprender Python ha sido una experiencia, digamos... interesante. Al principio, pensé que sería sólo otra habilidad más, interesante de aprender. Pero desde ese primer 'Hola Mundo' hasta ahora, cada línea de código ha sido como descifrar un enigma. Al principio, me sentía perdido, tratando de descubrir el significado detrás de cada 'while' y 'for'. Pero conforme fui avanzando, el mundo de los bucles y las listas se fue volviendo cada vez más amigable (o al menos eso intenta parecer) ¿Quién diría que un simple indentado podía cambiar mi forma de pensar? Sin embargo, a medida que me adentraba en bucles, anidados y funciones, descubrí que Python tiene ese encanto sutil de hacerte sentir inteligente cuando tu código por fin funciona (o al menos no explota en tu cara).
He recorrido un camino lleno de 'syntax errors' y 'indentation errors' que, sinceramente, me han enseñado más que cualquier tutorial de YouTube.
"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Odisea De Gráficos</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['Tarjetas Rojas Visitante Equipos De La Liga Italiana', 'Tarjetas Amarillas Local Equipos De La Liga Italiana', 'Goles de Atalanta Por Partido']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('Selecciona un gráfico', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == 'Tarjetas Rojas Visitante Equipos De La Liga Italiana':
    sidebar.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra que Juventus tiene el valor más alto, con un promedio de más de 0.200 tarjetas rojas por partido como visitante, lo que sugiere un estilo de juego más agresivo o decisiones arbitrales más severas en su contra. Por otro lado, nueve equipos tienen un promedio de un poco más de 0.100 tarjetas rojas, indicando una uniformidad en la conducta disciplinaria de la mayoría de los equipos cuando juegan fuera de casa. En general, Juventus se destaca por recibir más tarjetas rojas comparado con otros equipos, mientras que el resto muestra una tendencia más homogénea.</div>", unsafe_allow_html=True)
    sidebar.image("Promedio De Tarjetas Rojas Como Visitante De Equipos De La Liga Italiana.jpg", caption='Tarjetas Rojas Visitante Equipos De La Liga Italiana', width=500)
    pass
elif grafico_seleccionado == 'Tarjetas Amarillas Local Equipos De La Liga Italiana':
    sidebar.markdown("<div style='text-align: justify'>En el gráfico, Sampdoria y Verona destacan con un promedio de poco más de 2.5 tarjetas amarillas por partido, sugiriendo un posible estilo de juego más agresivo o una disciplina defensiva más estricta en casa. En contraste, Napoli muestra el promedio más bajo, con menos de 1 tarjeta amarilla por partido, indicando un enfoque más disciplinado y menos infracciones. Estas diferencias reflejan una variabilidad significativa entre los equipos en cuanto a su comportamiento en el campo local, lo cual puede ser crucial para ajustar estrategias de disciplina y evitar sanciones adicionales.</div>", unsafe_allow_html=True)
    sidebar.image("Promedio De Tarjetas Amarillas Como Local De Equipos De La Liga Italiana.jpg", caption='Tarjetas Amarillas Local Equipos De La Liga Italiana', width=500)
    pass
elif grafico_seleccionado == 'Goles de Atalanta Por Partido':
    sidebar.markdown("<div style='text-align: justify'>El gráfico muestra que el equipo Atlanta anotó una mayor proporción de sus goles cuando juega como local, en comparación con cuando juega como visitante. Esto podría indicar una tendencia de mayor efectividad ofensiva en casa, posiblemente debido al apoyo de los aficionados, familiaridad con el terreno de juego u otros factores que favorecen el desempeño en casa en lugar de fuera.</div>", unsafe_allow_html=True)
    sidebar.image("Promedio de goles de Atalanta por partido.jpg", caption='Goles de Atalanta Por Partido', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas':: Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.
