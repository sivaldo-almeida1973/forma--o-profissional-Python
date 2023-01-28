
import xml.etree.ElementTree as xml
import os

class Carro:
  def __init__(self, nome, potencia):
    self.nome = nome
    self.potencia = potencia

  @staticmethod
  def salva_carros(*carros):
    