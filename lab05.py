import yfinance as yf
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Pregunta 1: Extracción de datos de acciones de Tesla utilizando yfinance
tesla = yf.Ticker("TSLA")
tesla_hist = tesla.history(period="max")

# Pregunta 2: Extracción de datos de ingresos de Tesla utilizando Webscraping
url_tesla_ingresos = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
response_tesla_ingresos = requests.get(url_tesla_ingresos)
soup_tesla_ingresos = BeautifulSoup(response_tesla_ingresos.content, "html.parser")
tabla_tesla_ingresos = soup_tesla_ingresos.find_all("table", class_="historical_data_table")[1]
filas_tesla_ingresos = tabla_tesla_ingresos.find_all("tr")

ingresos_tesla = []
for fila in filas_tesla_ingresos:
    columnas = fila.find_all("td")
    if len(columnas) == 2:
        fecha = columnas[0].text
        ingreso = columnas[1].text.replace("$", "").replace(",", "")
        ingresos_tesla.append({"Fecha": fecha, "Ingresos": float(ingreso)})

# Pregunta 3: Extracción de datos de acciones de GameStop utilizando yfinance
gamestop = yf.Ticker("GME")
gamestop_hist = gamestop.history(period="max")

# Pregunta 4: Extracción de datos de ingresos de GameStop utilizando Webscraping
url_gamestop_ingresos = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
response_gamestop_ingresos = requests.get(url_gamestop_ingresos)
soup_gamestop_ingresos = BeautifulSoup(response_gamestop_ingresos.content, "html.parser")
tabla_gamestop_ingresos = soup_gamestop_ingresos.find_all("table", class_="historical_data_table")[1]
filas_gamestop_ingresos = tabla_gamestop_ingresos.find_all("tr")

ingresos_gamestop = []
for fila in filas_gamestop_ingresos:
    columnas = fila.find_all("td")
    if len(columnas) == 2:
        fecha = columnas[0].text
        ingreso = columnas[1].text.replace("$", "").replace(",", "")
        ingresos_gamestop.append({"Fecha": fecha, "Ingresos": float(ingreso)})

# Pregunta 5: Tablero de acciones e ingresos de Tesla
fig_tesla = make_subplots(rows=2, cols=1, subplot_titles=("Precio de Acciones de Tesla", "Ingresos de Tesla"))
fig_tesla.add_trace(go.Scatter(x=tesla_hist.index, y=tesla_hist["Close"], name="Precio de cierre"), row=1, col=1)
fig_tesla.add_trace(go.Bar(x=[item["Fecha"] for item in ingresos_tesla], y=[item["Ingresos"] for item in ingresos_tesla], name="Ingresos"), row=2, col=1)
fig_tesla.update_layout(height=800, title_text="Tablero de Tesla")
fig_tesla.show()

# Pregunta 6: Cuadro de mando de acciones e ingresos de GameStop
fig_gamestop = make_subplots(rows=2, cols=1, subplot_titles=("Precio de Acciones de GameStop", "Ingresos de GameStop"))
fig_gamestop.add_trace(go.Scatter(x=gamestop_hist.index, y=gamestop_hist["Close"], name="Precio de cierre"), row=1, col=1)
fig_gamestop.add_trace(go.Bar(x=[item["Fecha"] for item in ingresos_gamestop], y=[item["Ingresos"] for item in ingresos_gamestop], name="Ingresos"), row=2, col=1)
fig_gamestop.update_layout(height=800, title_text="Tablero de GameStop")
fig_gamestop.show()

