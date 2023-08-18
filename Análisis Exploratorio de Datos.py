import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
archivo_excel = 'PelicanStores.xlsx'
data = pd.read_excel(archivo_excel)

# 1. Porcentaje de clientes regulares y promocionales
porcentaje_regulares = (data['Type of Customer'] == 'Regular').mean() * 100
porcentaje_promocionales = (data['Type of Customer'] == 'Promotional').mean() * 100
print(f"Porcentaje de clientes regulares: {porcentaje_regulares:.2f}%")
print(f"Porcentaje de clientes promocionales: {porcentaje_promocionales:.2f}%")
# Conclusiones: ...

# 2. Resumen estadístico de ítems vendidos y ventas netas
resumen_estadistico = data[['Items', 'Net Sales']].describe()
print(resumen_estadistico)
# Histogramas
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(data['Items'], bins=20, edgecolor='black')
plt.title('Distribución de Ítems Vendidos')
plt.xlabel('Ítems Vendidos')
plt.ylabel('Frecuencia')

plt.subplot(1, 2, 2)
plt.hist(data['Net Sales'], bins=20, edgecolor='black')
plt.title('Distribución de Ventas Netas')
plt.xlabel('Ventas Netas')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()
# Conclusiones: ...

# 3. Volumen de compras de clientes regulares vs promocionales
volumen_regulares = data[data['Type of Customer'] == 'Regular']['Items'].sum()
volumen_promocionales = data[data['Type of Customer'] == 'Promotional']['Items'].sum()
print(f"Volumen de compras de clientes regulares: {volumen_regulares}")
print(f"Volumen de compras de clientes promocionales: {volumen_promocionales}")
# Conclusiones: ...

# 4. Promedio de ítems comprados por clientes regulares vs promocionales
promedio_regulares = data[data['Type of Customer'] == 'Regular']['Items'].mean()
promedio_promocionales = data[data['Type of Customer'] == 'Promotional']['Items'].mean()
print(f"Promedio de ítems comprados por clientes regulares: {promedio_regulares:.2f}")
print(f"Promedio de ítems comprados por clientes promocionales: {promedio_promocionales:.2f}")
# Conclusiones: ...

# 5. Promedio y mediana de ventas netas de clientes regulares vs promocionales
promedio_ventas_regulares = data[data['Type of Customer'] == 'Regular']['Net Sales'].mean()
promedio_ventas_promocionales = data[data['Type of Customer'] == 'Promotional']['Net Sales'].mean()
mediana_ventas_regulares = data[data['Type of Customer'] == 'Regular']['Net Sales'].median()
mediana_ventas_promocionales = data[data['Type of Customer'] == 'Promotional']['Net Sales'].median()

print(f"Promedio de ventas netas de clientes regulares: {promedio_ventas_regulares:.2f}")
print(f"Promedio de ventas netas de clientes promocionales: {promedio_ventas_promocionales:.2f}")
print(f"Mediana de ventas netas de clientes regulares: {mediana_ventas_regulares:.2f}")
print(f"Mediana de ventas netas de clientes promocionales: {mediana_ventas_promocionales:.2f}")

# Gráfico de comparación de ventas netas entre regulares y promocionales
plt.figure(figsize=(8, 5))
plt.bar(['Regulares', 'Promocionales'], [promedio_ventas_regulares, promedio_ventas_promocionales])
plt.title('Comparación de Ventas Netas entre Regulares y Promocionales')
plt.xlabel('Tipo de Cliente')
plt.ylabel('Ventas Netas Promedio')
plt.show()
# Conclusiones: ...

# 6. Método de pago preferido por clientes promocionales vs regulares
metodo_pago_regulares = data[data['Type of Customer'] == 'Regular']['Method of Payment'].value_counts().idxmax()
metodo_pago_promocionales = data[data['Type of Customer'] == 'Promotional']['Method of Payment'].value_counts().idxmax()
print(f"Método de pago preferido por clientes regulares: {metodo_pago_regulares}")
print(f"Método de pago preferido por clientes promocionales: {metodo_pago_promocionales}")
# Conclusiones: ...

# 7. Porcentaje de hombres que realizan compras y comparación entre regulares y promocionales
porcentaje_hombres = (data['Gender'] == 'Male').mean() * 100
porcentaje_hombres_regulares = (data[data['Type of Customer'] == 'Regular']['Gender'] == 'Male').mean() * 100
porcentaje_hombres_promocionales = (data[data['Type of Customer'] == 'Promotional']['Gender'] == 'Male').mean() * 100
print(f"Porcentaje de hombres que realizan compras: {porcentaje_hombres:.2f}%")
print(f"Porcentaje de hombres en clientes regulares: {porcentaje_hombres_regulares:.2f}%")
print(f"Porcentaje de hombres en clientes promocionales: {porcentaje_hombres_promocionales:.2f}%")
# Conclusiones: ...

# 8. Estado civil con mayor prevalencia
estado_civil_prevalente = data['Marital Status'].value_counts().idxmax()
print(f"Estado civil con mayor prevalencia: {estado_civil_prevalente}")
# Conclusiones: ...

# 9. Relación entre edad y ventas netas y cantidad de ítems comprados
plt.figure(figsize=(10, 5))
plt.scatter(data['Age'], data['Net Sales'], alpha=0.5)
plt.title('Relación entre Edad y Ventas Netas')
plt.xlabel('Edad')
plt.ylabel('Ventas Netas')
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(data['Age'], data['Items'], alpha=0.5)
plt.title('Relación entre Edad e Ítems Comprados')
plt.xlabel('Edad')
plt.ylabel('Ítems Comprados')
plt.show()

# Coeficiente de correlación
coef_corr_ventas = data['Age'].corr(data['Net Sales'])
coef_corr_items = data['Age'].corr(data['Items'])
print(f"Coeficiente de correlación entre edad y ventas netas: {coef_corr_ventas:.2f}")
print(f"Coeficiente de correlación entre edad y ítems comprados: {coef_corr_items:.2f}")
# Conclusiones: ...

# 10. Comparación de ventas entre diferentes métodos de pago
plt.figure(figsize=(10, 5))
data.groupby('Method of Payment')['Net Sales'].mean().sort_values().plot(kind='bar')
plt.title('Comparación de Ventas Netas por Método de Pago')
plt.xlabel('Método de Pago')
plt.ylabel('Ventas Netas Promedio')
plt.show()
# Conclusiones: ...
