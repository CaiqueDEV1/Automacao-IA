<h1>Visão computacionial - IA</h1>

<h2>Nesse projeto, utilizei a visão computacional para abrir a webcam e identificar as mãos utilizando Machine Learning.</h2>
<h2>A lógica do looping infinito foi a seguinte. Caso a webcam seja reconhecida/aberta com sucesso, a imagem sera capturada/lida.</h2>
<h2>Utilizei o findHands para achar e localizar a mão da pessoa.</h2>
<h2>Configurei o cv2 para ele esperar que alguma tecla igual ou diferente da -1 seja clicada para que a janela da webcam seja fechada.</h2>
<h2>O webcam release serve para que a webcam, depois de usada, seja liberada para ser usada em outros apps.</h2>


<h3>Utilizamos as bibliotecas:</h3>
- cvzone
- opencv-python
- mediapipe
- cv2


# Configurando a webcam para capturar 
webcam = cv2.VideoCapture(0)

# Configurando a webcam para detectar com 80% de certeza e no maximo 2 mãos
rastreador = HandDetector(detectionCon=0.8, maxHands=2)


# looping infinito
while True:
    sucesso, imagem = webcam.read()
    cordenadas, imagem_maos = rastreador.findHands(imagem)

    print(cordenadas)


    cv2.imshow("Projeto 4 - IA", imagem)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()



