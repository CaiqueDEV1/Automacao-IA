import cv2
from cvzone.HandTrackingModule import HandDetector
import streamlit as st



webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=2)


st.title("Aperte o botão para abrir sua webcam")
st.divider()
botao = st.button("abrir webcam")
botao.on_click(webcam)

while True:
    sucesso, imagem = webcam.read()
    coordenadas, imagem_maos = rastreador.findHands(imagem)

    print(coordenadas)


    cv2.imshow("Projeto 4 - IA", imagem)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()