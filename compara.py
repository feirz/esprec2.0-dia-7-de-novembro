import cv2
import face_recognition
import os


# Carregue a imagem base para comparação
imagem_base = face_recognition.load_image_file("C:\\Users\\diogo\\Documents\\ESP_REC_FACIAL\\testes\\received_photo.jpg")  # Insira o caminho da imagem base
image_face_encoding = face_recognition.face_encodings(imagem_base)[0]

# Diretório que contém as imagens para comparação
pasta_com_imagens = "C:\\Users\\diogo\\Documents\\ESP_REC_FACIAL\\images"  # Insira o caminho da pasta com as imagens

# Variável para rastrear se alguma imagem foi reconhecida
alguma_imagem_reconhecida = False

# Loop através das imagens na pasta
for imagem_nome in os.listdir(pasta_com_imagens):
    imagem_path = os.path.join(pasta_com_imagens, imagem_nome)
    imagem_para_comparar = face_recognition.load_image_file(imagem_path)
    
    # Calcule o código de face da imagem para comparação
    image_to_compare_encoding = face_recognition.face_encodings(imagem_para_comparar)
    
    if not image_to_compare_encoding:
        continue  # Ignora imagens sem rostos
    
    image_to_compare_encoding = image_to_compare_encoding[0]

    # Compare as duas imagens
    match = face_recognition.compare_faces([image_face_encoding], image_to_compare_encoding)

    if match[0]:
        nome = "Reconhecido"
        alguma_imagem_reconhecida = True
        print(f"Imagem reconhecida: {imagem_nome}")
        break  # Se uma imagem for reconhecida, saia do loop

# Se nenhuma imagem foi reconhecida, imprima uma mensagem
if not alguma_imagem_reconhecida:
    print("Nenhuma imagem reconhecida.")

# Libere os recursos
cv2.destroyAllWindows()