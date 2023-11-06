from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def gerar_cor_aleatoria(cor_base):
    # Gera uma cor aleatória mantendo a matiz da cor base em formato hexadecimal
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


#! PALETA MONOCROMATICA
def gerar_paleta_mono(cor_base):
    paleta = {}
    
    for i in range(0, 5):
        cor = gerar_cor_aleatoria(cor_base)
        paleta[f"cor{i}"] = cor

    return paleta

#! PALETA DE CORES ANALGOAS
def gerar_cores_analogas(cor_base, num_cores=5, angulo=30):
    # Converte a cor base de hexadecimal para RGB
    r_base = int(cor_base[1:3], 16)
    g_base = int(cor_base[3:5], 16)
    b_base = int(cor_base[5:7], 16)
    
    # Calcula a diferença de ângulo entre as cores análogas
    dif_angulo = 360 / num_cores
    
    paleta = []
    
    for i in range(num_cores):
        # Calcula a matiz da cor análoga
        angulo_cor = (i * dif_angulo + angulo) % 360
        
        # Converte a matiz de volta para RGB
        r_analog = int(r_base + (angulo_cor / 60) * (255 - r_base))
        g_analog = int(g_base + (angulo_cor / 60) * (255 - g_base))
        b_analog = int(b_base + (angulo_cor / 60) * (255 - b_base))
        
        # Converte os valores RGB para hexadecimal
        cor_analog = "#{:02X}{:02X}{:02X}".format(r_analog, g_analog, b_analog)
        paleta.append(cor_analog)
    
    return paleta



@app.route('/an')
def paleta_analogas():
    cor_base = "#{:02X}{:02X}{:02X}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    paleta = gerar_cores_analogas(cor_base, num_cores=5, angulo=30)
    return jsonify({"paleta": paleta})


@app.route('/mono')
def paleta_mono():
    cor_base = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    paleta = gerar_paleta_mono(cor_base)
    return jsonify({"paleta": paleta})

if __name__ == '__main__':
    app.run(host='192.168.0.54')
