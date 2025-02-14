#!/bin/bash

# Obtener el directorio actual y el usuario que ejecuta el script
INSTALL_DIR=$(pwd)
CURRENT_USER=$(whoami)

# Verificar que el entorno virtual existe
if [ ! -d "$INSTALL_DIR/venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    echo "Entorno virtual encontrado."
fi

# Crear el archivo de servicio
echo "Creando archivo de servicio..."
SERVICE_FILE="[Unit]
Description=Buscador TecCam API Service
After=network.target

[Service]
Type=simple
User=$CURRENT_USER
WorkingDirectory=$INSTALL_DIR
Environment=PATH=$INSTALL_DIR/venv/bin:$PATH
ExecStart=$INSTALL_DIR/venv/bin/python $INSTALL_DIR/api.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target"

# Usar sudo para crear y habilitar el servicio
echo "Instalando el servicio..."
echo "$SERVICE_FILE" | sudo tee /etc/systemd/system/buscador-teccam.service > /dev/null

# Recargar systemd, habilitar y arrancar el servicio
echo "Configurando el servicio..."
sudo systemctl daemon-reload
sudo systemctl enable buscador-teccam.service
sudo systemctl start buscador-teccam.service

echo "Verificando estado del servicio..."
sudo systemctl status buscador-teccam.service

echo "
Instalación completada. El servicio está configurado para iniciar automáticamente con el sistema.

Comandos útiles:
- Ver estado: sudo systemctl status buscador-teccam.service
- Iniciar: sudo systemctl start buscador-teccam.service
- Detener: sudo systemctl stop buscador-teccam.service
- Reiniciar: sudo systemctl restart buscador-teccam.service
- Ver logs: sudo journalctl -u buscador-teccam.service
"
