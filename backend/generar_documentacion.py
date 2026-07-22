from pathlib import Path


DOCUMENTOS = {

    "tecnologia/seguridad_informatica.md": """
# Política de Seguridad Informática

Empresa: Soluciones Atenea

## Objetivo

Proteger la información corporativa.

## Contraseñas

Las contraseñas deben cambiarse cada 90 días.

## Equipos

No se permite instalar software sin autorización.

## Incidentes

Todo incidente debe reportarse inmediatamente al área TI.
""",

    "tecnologia/faq_tecnologia.md": """
# Preguntas Frecuentes de Tecnología

## ¿Cómo solicito soporte?

Enviar un correo a soporte@atenea.cl

## ¿Cómo cambio mi contraseña?

Desde el portal interno.

## ¿Qué hago si mi computador falla?

Contactar inmediatamente al área TI.
""",

    "tecnologia/uso_equipos.md": """
# Uso de Equipos

Los computadores son para uso laboral.

No está permitido instalar programas personales.

Todos los equipos deben mantenerse actualizados.
""",

    "legal/politica_privacidad.md": """
# Política de Privacidad

Los datos personales de colaboradores y clientes son confidenciales.

Solo el personal autorizado puede acceder a dicha información.
""",

    "legal/terminos_condiciones.md": """
# Términos y Condiciones

Todo colaborador debe cumplir las políticas internas de Soluciones Atenea.

El incumplimiento podrá generar medidas disciplinarias.
""",

    "financiero/politica_compras.md": """
# Política de Compras

Toda compra superior a 100.000 pesos requiere aprobación de la jefatura.

Las cotizaciones deben quedar registradas.
""",

    "financiero/politica_rendiciones.md": """
# Política de Rendiciones

Toda rendición debe realizarse dentro de los cinco días hábiles posteriores al gasto.

Debe adjuntarse el comprobante correspondiente.
""",

    "operaciones/procedimiento_operacional.md": """
# Procedimiento Operacional

Toda operación debe seguir los procedimientos establecidos.

Las desviaciones deben informarse inmediatamente.
""",

    "operaciones/protocolo_emergencias.md": """
# Protocolo de Emergencias

Ante una emergencia se debe avisar al supervisor.

Posteriormente seguir las rutas de evacuación.
""",

    "comercial/atencion_clientes.md": """
# Atención de Clientes

Todo cliente debe recibir una respuesta dentro de las primeras 24 horas.

La atención debe ser cordial y profesional.
""",

    "comercial/preguntas_frecuentes.md": """
# Preguntas Frecuentes

## ¿Cómo contacto a ventas?

Escribiendo a ventas@atenea.cl

## ¿Dónde solicito una cotización?

En el formulario del sitio web.
"""
}


def generar():

    carpeta = Path("documents")

    for archivo, contenido in DOCUMENTOS.items():

        ruta = carpeta / archivo

        ruta.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        ruta.write_text(
            contenido.strip(),
            encoding="utf-8"
        )

        print("✅", ruta)


if __name__ == "__main__":

    generar()