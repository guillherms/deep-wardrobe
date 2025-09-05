# 👕 deep-wardrobe

**PT-BR 🇧🇷**  
Projeto de **fine-tuning multimodal** aplicado à moda, com o objetivo de identificar roupas e marcas em imagens.  
O foco inicial está em peças utilizadas na série *The Bear*, servindo como estudo de caso para validação da abordagem.  

**EN 🇺🇸**  
Project of **multimodal fine-tuning** applied to fashion, aiming to identify clothes and brands in images.  
The initial focus is on outfits featured in the series *The Bear*, serving as a case study for approach validation.  

---

## 🎯 Objetivo | Goal

- PT-BR: Treinar um modelo capaz de reconhecer peças de roupas e suas marcas, utilizando imagens anotadas.  
- EN: Train a model capable of recognizing clothing items and their brands, using annotated images.  

---

## 🖼️ Demonstrações | Demos

Aqui entram GIFs mostrando a identificação das roupas em cenas de *The Bear*.  
Below you can include GIFs showcasing clothing recognition in *The Bear* scenes.  

**Exemplo de espaço para GIFs:**  

![demo-1](./assets/demo-1.gif)  
![demo-2](./assets/demo-2.gif)  

---

## 🛠️ Tecnologias | Tech Stack

- [OpenAI Fine-tuning (Vision models)](https://platform.openai.com/docs/guides/vision-fine-tuning)  
- Python (pré-processamento e geração do dataset `.jsonl`)  
- Pandas / Pydantic (validação de dados)  
- Streamlit (interface para testes, futuro)  

---

## 📂 Estrutura do Projeto | Project Structure

```bash
deep-wardrobe/
│── data/               # Dataset de imagens + anotações
│── notebooks/          # Experimentações em Jupyter
│── src/                # Código principal (pré-processamento, treino, testes)
│── assets/             # GIFs e imagens para README
│── README.md
