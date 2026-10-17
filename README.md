SoftMarket Core - Refactorización y Estandarización
Bienvenido al repositorio central de **SoftMarket S.A.** Este proyecto contiene la refactorización arquitectónica y la estandarización de procesos de ingeniería para resolver la deuda técnica, reducir los errores en producción y establecer un ciclo de vida de desarrollo de software (SDLC) sostenible.
Arquitectura y Principios SOLID
Para combatir el alto acoplamiento y las "Clases Dios" del código heredado, hemos refactorizado los módulos críticos (como Facturación) aplicando los principios **SOLID**:
* **SRP (Responsabilidad Única):** Separación estricta entre la lógica matemática, la persistencia en base de datos y los servicios de notificación.
* **OCP (Abierto/Cerrado):** Implementación del patrón *Strategy* (`EstrategiaDescuento`) para añadir nuevas reglas de negocio sin alterar el código existente.
* **LSP (Sustitución de Liskov):** Polimorfismo seguro en los exportadores de documentos y notificadores.
* **ISP (Segregación de Interfaces):** Interfaces pequeñas y específicas (`RepositorioFacturas`, `ServicioNotificacion`) en lugar de contratos monolíticos.
* **DIP (Inversión de Dependencias):** Inyección de dependencias en el `ServicioFacturacion` para desacoplarlo de implementaciones concretas como SQLite o SMTP.
 Estrategia de Versionamiento (GitFlow)
Trabajamos bajo un modelo ágil de **GitFlow** con protección de ramas y reglas estrictas de integración:
* `main`: Entorno de **Producción**. Código 100% estable. Solo admite fusiones desde `release/` o `hotfix/`.
* `develop`: Entorno de **Integración/QA**. Refleja el estado del próximo lanzamiento.
* **[Equipo Consultor]**
Este plan de refactorización fue diseñado y ejecutado por:
* **[Danna Salcedo]** - Arquitecto de Procesos y 
* **[Yosman Cardona]** - Especialista en Patrones de Diseño (SOLID)
