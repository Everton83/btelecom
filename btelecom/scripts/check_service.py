#!/bin/bash

# Verifica o status do serviço django
status=$(systemctl is-active django)

# Verifica se o serviço está ativo
if [ "$status" = "active" ]; then
    echo "O serviço está ativo."
else
    echo "O serviço está inativo. Tentando reiniciar..."
    systemctl restart django
fi

#*/5 * * * * /opt/sites/check_django.sh >> /var/log/log_check_django 2>&1


