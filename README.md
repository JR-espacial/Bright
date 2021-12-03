# Bright
Simulación de intersección de calles con semáforos con modelo de agentes desarrollado en Python y Unity.

## Pasos para la instalación
1. Clonar el repositorio al correr la siguiente línea en su línea de comandos: `git clone https://github.com/MarianaS8a/Bright.git`. O bien, descargar el archivo ZIP del repositorio.

### Ejecución en Python
1. Abre una nueva consola
2. Entra a Bright/Despliegue/server-agentes/
3. Corre el comando: `pip install mesa pandas numpy matplotlib flask`
4. Corre el comando: `python main.py`
5. Espera 10 segundo a que termine la ejecución de la simulación

La simulación se desplegará en una nueva ventana con 4 filas simulando cada carril de coches, los cuadros negros simularán los coches que están actuando como agentes en el modelo. La última fila de la derecha simulará el límite de los coches en donde se encuentran los semáforos que le indican a los carriles su turno de pasar.  


### Ejecución en Unity
1. Descargar el archivo .unitypackage
2. Crear un nuevo proyecto de Unity
3. Elegir un template con Universal Render Pipeline
4. Dar click derecho a la carpeta de ‘Assets’
5. Seleccionar ‘Import package’ y ‘Custom Package’
6. Navegar a la carpeta donde descargaste el repositorio Bright
7. Entrar a Bright/Unity y seleccionar el archivo .unitypackage
8. Asegurarse de que todos los elementos mostrados estén seleccionados y dar click en ‘Import’
9. En el proyecto de Unity ir a Assets/Scenes y dar click sobre la escena ‘bright’
10. Correr el programa haciendo click en el botón ‘Play’

La lógica del programa en Python desplegada en el servidor https://bright-agentes.us-south.cf.appdomain.cloud/ empezará a correr y se verá como interfaz gráfica en la ventana ‘Game’ en Unity. Se visualizará la simulación de la intersección de calles en donde habrá un agente control que permitirá decidir qué carril puede avanzar según el tiempo de espera de los autos en cada carril. La interfaz mostrará los autos en movimiento, vueltas y cambios en el color de los semáforos. 
