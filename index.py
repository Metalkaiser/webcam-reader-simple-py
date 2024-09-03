import cv2
import os

# Crear un directorio para guardar las imágenes
output_dir = "imagenes_grabadas"
os.makedirs(output_dir, exist_ok=True)

# Inicializar la captura de video desde la webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se puede abrir la cámara.")
    exit()

# Contador para las imágenes
count = 0

try:
    while True:
        # Captura frame a frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: No se puede recibir un frame (final de la transmisión).")
            break
        
        # Mostrar el frame en una ventana
        cv2.imshow('Webcam', frame)

        # Esperar 1 ms y capturar una tecla
        key = cv2.waitKey(1)
        
        # Si se presiona 's', guardar la imagen
        if key == ord('s'):
            img_name = os.path.join(output_dir, f'imagen_{count}.png')
            cv2.imwrite(img_name, frame)
            print(f'Imagen guardada: {img_name}')
            count += 1
        
        # Si se presiona 'q', salir
        elif key == ord('q'):
            print("Saliendo...")
            break

except KeyboardInterrupt:
    print("Interrupción por teclado.")

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
