# Helmify

**Helmify** es un wrapper de Python para la herramienta Helm. Este proyecto fue creado para facilitar la interacción con Helm desde Python

## ¿Qué es Helm?

Helm es un administrador de paquetes para Kubernetes. En esencia, Helm simplifica la gestión de aplicaciones en Kubernetes al permitirte definir, instalar y actualizar aplicaciones de una manera más organizada y reutilizable. Helm se basa en la idea de "charts" (gráficos) que son paquetes preconfigurados de recursos de Kubernetes. Estos charts contienen descripciones de recursos, plantillas y valores que permiten personalizar la implementación de aplicaciones.

## Características clave de Helm:

- Charts Reutilizables: Los charts se pueden compartir y reutilizar fácilmente, lo que simplifica la distribución de aplicaciones y la colaboración entre equipos de desarrollo y operaciones.
- Gestión de Versiones: Helm permite gestionar versiones de aplicaciones de manera eficiente. Puedes actualizar o retroceder a versiones anteriores de una aplicación con facilidad.
- Configuración Personalizada: Puedes personalizar la configuración de una aplicación utilizando valores que se ajusten a tus necesidades específicas.
- Helm Hub: Helm Hub es un repositorio en línea que alberga charts públicos, lo que facilita la búsqueda y el acceso a charts populares y de código abierto.

## Requisitos previos

- Python 3.6 o superior.
- Helm instalado en el entorno local o en el clúster de Kubernetes.
- Disponer de un cluster Kubernetes