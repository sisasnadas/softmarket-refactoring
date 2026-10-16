from abc import ABC, abstractmethod
from typing import List, Dict

# 1. MODELO DE DOMINIO (SRP: Solo representa los datos de la factura) 
class Factura:
    def __init__(self, cliente_nombre: str, cliente_contacto: str, items: List[Dict]):
        self.cliente_nombre = cliente_nombre
        self.cliente_contacto = cliente_contacto
        self.items = items
        self.subtotal = sum(i['precio'] * i['cantidad'] for i in items)
        self.total = self.subtotal

# 2. ESTRATEGIA DE DESCUENTOS (OCP y LSP: Abierto a nuevos descuentos) 
class EstrategiaDescuento(ABC):
    @abstractmethod
    def aplicar(self, monto: float) -> float:
        pass

class SinDescuento(EstrategiaDescuento):
    def aplicar(self, monto: float) -> float:
        return monto

class DescuentoRegular(EstrategiaDescuento):
    def aplicar(self, monto: float) -> float:
        return monto * 0.95

class DescuentoVIP(EstrategiaDescuento):
    def aplicar(self, monto: float) -> float:
        return monto * 0.80

# 3. INTERFACES SEGREGADAS PARA INFRAESTRUCTURA (ISP y DIP) 
class RepositorioFacturas(ABC):
    @abstractmethod
    def guardar(self, factura: Factura) -> None:
        pass

class ServicioNotificacion(ABC):
    @abstractmethod
    def notificar(self, destinatario: str, mensaje: str) -> None:
        pass

class ExportadorFactura(ABC):
    @abstractmethod
    def exportar(self, factura: Factura) -> str:
        pass

#  4. IMPLEMENTACIONES CONCRETAS (Tecnología real simulada) 
class RepositorioPostgres(RepositorioFacturas):
    def guardar(self, factura: Factura) -> None:
        print(f"[DB Postgres] Guardando factura de {factura.cliente_nombre} por ${factura.total:.2f}")

class NotificadorEmail(ServicioNotificacion):
    def notificar(self, destinatario: str, mensaje: str) -> None:
        print(f"[Email SMTP] Enviando a {destinatario}: {mensaje}")

class NotificadorWhatsApp(ServicioNotificacion):
    def notificar(self, destinatario: str, mensaje: str) -> None:
        print(f"[WhatsApp API] Enviando a {destinatario}: {mensaje}")

class ExportadorPDF(ExportadorFactura):
    def exportar(self, factura: Factura) -> str:
        return f"Documento PDF generado: Cliente {factura.cliente_nombre} - Total: ${factura.total:.2f}"

# 5. CASO DE USO / ORQUESTADOR (Inyección de Dependencias - DIP) 
class ServicioFacturacion:
    def __init__(
        self,
        repositorio: RepositorioFacturas,
        notificador: ServicioNotificacion,
        exportador: ExportadorFactura
    ):
        self.repositorio = repositorio
        self.notificador = notificador
        self.exportador = exportador

    def emitir_factura(self, factura: Factura, descuento: EstrategiaDescuento) -> str:
        factura.total = descuento.aplicar(factura.subtotal)
        
        self.repositorio.guardar(factura)
        
        documento = self.exportador.exportar(factura)
        
        self.notificador.notificar(
            factura.cliente_contacto,
            f"Tu factura por ${factura.total:.2f} ha sido emitida."
        )
        
        return documento