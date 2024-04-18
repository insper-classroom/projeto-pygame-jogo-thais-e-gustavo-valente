def clip(valor, min, max): #serve p limitar a velocidade do boneco pq se ficar apertando espaco
                            #a velocidade iria acumulando ai uma hr ia ficar escroto de rapido
    if valor < min:
        return min
    if valor > max:
        return max
    return valor

def checacolisoes(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    return (a_x + a_width > b_x) and (a_x < b_x + b_width) and (a_y + a_height > b_y) and (a_y < b_y + b_height)