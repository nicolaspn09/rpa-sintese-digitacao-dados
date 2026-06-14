import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import pandas as pd


sys.path.append(r"C:\rpa\Python")
from Classes.Intranet.AcessaIntranet.AcessaIntranet import AcessaIntranet


def registrar_log(mensagem, salvar_arquivo=True):
    pass # Logica de negocio removida por seguranca corporativa


def aguardar_download(download_dir, timeout=30):
    pass # Logica de negocio removida por seguranca corporativa


def acessa_negociacao(driver):
    pass # Logica de negocio removida por seguranca corporativa

    
def acessa_sintese(driver, wait):
    pass # Logica de negocio removida por seguranca corporativa


def descartar_cotacao_nh(driver, dados_linha, motivo="processada", portal=None):
    pass # Logica de negocio removida por seguranca corporativa


def processar_cotacao_nh(driver, dados_linha, wait):
    pass # Logica de negocio removida por seguranca corporativa


def baixar_excel_cotacao(driver, wait, download_dir):
    pass # Logica de negocio removida por seguranca corporativa
