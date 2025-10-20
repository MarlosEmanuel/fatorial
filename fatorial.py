#!/usr/bin/env python3
import sys
import os
import time
import functools
"""
fatorial.py

Template de implementação para cálculo do fatorial em Python.
Os alunos devem implementar as três abordagens abaixo:

1. Método Iterativo
2. Método Recursivo
3. Método Recursivo com uso de functools.lru_cache
"""
sys.set_int_max_str_digits(100000)
sys.setrecursionlimit(100000)
# ---------------------------
# Implementação Iterativa
# ---------------------------
def fatorial_iterativo(n: int) -> int:
    """Calcula o fatorial de n usando laço iterativo."""
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos")
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# ---------------------------
# Implementação Recursiva
# ---------------------------
def fatorial_recursivo(n: int) -> int:
    """Calcula o fatorial de n de forma recursiva."""
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos")
    if n < 2:
        return 1
    return n * fatorial_recursivo(n - 1)


# ---------------------------
# Implementação com LRU Cache
# ---------------------------
@functools.lru_cache(maxsize=None)
def fatorial_lru(n: int) -> int:
    """Calcula o fatorial de n com recursão + memoização (lru_cache)."""
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos")
    if n < 2:
        return 1
    return n * fatorial_lru(n - 1)

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# ---------------------------
# Função Principal (testes)
# ---------------------------
if __name__ == "__main__":
    
    while True:
        try:
            print("\n" + "="*40)
            print("Digite 0 para sair do programa.")
            numero_str = input("Digite um número inteiro para calcular o fatorial: ")
            numero = int(numero_str)

            if numero == 0:
                print("Programa finalizado.")
                break

            if numero < 0:
                limpar_terminal()
                print("Erro: Fatorial não é definido para números negativos.")
                continue

            limpar_terminal()
            print(f"Calculando o fatorial de {numero}")
            print("-" * 40)

            # --- Teste Iterativo ---
            inicio = time.perf_counter()
            resultado_iterativo = fatorial_iterativo(numero)
            fim = time.perf_counter()
            print(f"Iterativo: {numero}!")
            print(f"   -> Tempo: {(fim - inicio)} segundos\n")

            # --- Teste Recursivo ---
            inicio = time.perf_counter()
            resultado_recursivo = fatorial_recursivo(numero)
            fim = time.perf_counter()
            print(f"Recursivo: {numero}!")
            print(f"   -> Tempo: {(fim - inicio)} segundos\n")

            # --- Teste com LRU Cache ---
            fatorial_lru.cache_clear()
            
            inicio = time.perf_counter()
            resultado_lru = fatorial_lru(numero)
            fim = time.perf_counter()
            print(f"LRU Cache (1ª chamada): {numero}!")
            print(f"   -> Tempo: {(fim - inicio)} segundos")

            inicio = time.perf_counter()
            resultado_lru_cache = fatorial_lru(numero)
            fim = time.perf_counter()
            print(f"LRU Cache (2ª chamada): {numero}!")
            print(f"   -> Tempo: {(fim - inicio)} segundos")


        except ValueError:
            limpar_terminal()
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
        except RecursionError as e:
            limpar_terminal()
            print(f"Erro: O número {numero} é muito grande para a abordagem recursiva.")
            print("\n\n")
            print(e)