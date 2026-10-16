from facturacion import (
    Factura, ServicioFacturacion, DescuentoVIP,
    RepositorioFacturas, ServicioNotificacion, ExportadorFactura
)

# --- 1. CREAMOS LOS MOCKS (DOBLES DE PRUEBA) ---
class RepositorioFalso(RepositorioFacturas):
    def __init__(self):
        self.fue_guardado = False

    def guardar(self, factura: Factura) -> None:
        self.fue_guardado = True

class NotificadorFalso(ServicioNotificacion):
    def __init__(self):
        self.mensaje_enviado = ""

    def notificar(self, destinatario: str, mensaje: str) -> None:
        self.mensaje_enviado = mensaje

class ExportadorFalso(ExportadorFactura):
    def exportar(self, factura: Factura) -> str:
        return "ARCHIVO_PDF_FALSO"

# --- 2. PRUEBA UNITARIA ---
def test_emitir_factura_aplica_descuento_y_guarda():
    # Preparamos los datos (Subtotal $100)
    items = [{'precio': 50, 'cantidad': 2}] 
    factura = Factura("María", "maria@mail.com", items)
    
    # Preparamos los aparatos falsos
    repo_falso = RepositorioFalso()
    notificador_falso = NotificadorFalso()
    exportador_falso = ExportadorFalso()
    
    # Inyectamos al Servicio
    servicio = ServicioFacturacion(repo_falso, notificador_falso, exportador_falso)
    
    # Ejecutamos con Descuento VIP (20% off)
    descuento_vip = DescuentoVIP()
    resultado = servicio.emitir_factura(factura, descuento_vip)
    
    # Verificamos que todo funciono bien
    assert factura.total == 80.0
    assert repo_falso.fue_guardado is True
    assert "80.0" in notificador_falso.mensaje_enviado
    assert resultado == "ARCHIVO_PDF_FALSO"
    
    print("¡Todas las pruebas pasaron correctamente!")

# Esto permite ejecutar la prueba directamente
if __name__ == "__main__":
    test_emitir_factura_aplica_descuento_y_guarda()