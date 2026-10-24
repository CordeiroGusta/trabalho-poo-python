class SensorTemperatura:
    def __init__(self, identificacao: str, temperatura: float) -> None:
        self.__identificacao = identificacao
        self.temperatura = temperatura

    @property
    def identificacao(self) -> str:
        return self.__identificacao

    @property
    def temperatura(self) -> float:
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nova_temperatura: float) -> None:
        if -20 <= nova_temperatura <= 150:
            self.__temperatura = nova_temperatura
        else:
            raise ValueError(
                "A temperatura deve estar entre -20 °C e 150 °C!"
            )

    def esta_em_alerta(self) -> bool:
        return self.__temperatura > 80

sensor = SensorTemperatura("SEN-001", 25.0)

print(f"Sensor: {sensor.identificacao}")
print(f"Temperatura: {sensor.temperatura} °C")
print(f"Alerta: {sensor.esta_em_alerta()}")

sensor.temperatura = 90.0
print(f"\nNova temperatura: {sensor.temperatura} °C")
print(f"Alerta: {sensor.esta_em_alerta()}")

for temperatura in [-20, 150, 151]:
    try:
        sensor.temperatura = temperatura
        print(
            f"Temperatura {temperatura} °C aceita."
        )
    except ValueError as erro:
        print(f"Temperatura {temperatura} °C rejeitada: {erro}")
