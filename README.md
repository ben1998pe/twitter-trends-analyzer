# 📊 Twitter Trends Analyzer

Dashboard web desarrollado con Flask para **visualizar, filtrar y analizar tendencias de Twitter en Perú**, usando como fuente el sitio [trends24.in](https://trends24.in/peru/).

---

## 🚀 Características

- Visualización en tiempo real de las tendencias capturadas
- Búsqueda por término
- Filtro por fecha/hora
- Gráfico de las 10 tendencias más repetidas
- Interfaz limpia y fácil de usar

---

## 📁 Estructura del proyecto

```
twitter-trends-analyzer/
├── app.py
├── requirements.txt
├── data/
│   └── tendencias_peru.csv
├── templates/
│   └── index.html
└── README.md
```

---

## 📦 Instalación

1. Clona este repositorio y entra a la carpeta:

```
git clone https://github.com/ben1998pe/twitter-trends-analyzer.git
cd twitter-trends-analyzer
```

2. Instala las dependencias:

```
pip install -r requirements.txt
```

3. Ejecuta el servidor local:

```
python app.py
```

4. Abre tu navegador en [http://localhost:5000](http://localhost:5000)

---

## 🧠 Fuente de datos

Este dashboard se alimenta del archivo `tendencias_peru.csv`, generado previamente por el proyecto:

👉 [twitter-trends-scraper](https://github.com/ben1998pe/trends24-scraper)

---

## 📷 Vista previa

(📌 Aquí puedes subir una captura de pantalla del dashboard si deseas que se muestre visualmente en GitHub.)

---

## 👨‍💻 Autor

Desarrollado por [@ben1998pe](https://github.com/ben1998pe)  
Proyecto 5 - Visualización y análisis de datos con Flask

---

## 📄 Licencia

MIT
