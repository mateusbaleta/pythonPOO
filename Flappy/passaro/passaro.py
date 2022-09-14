from Flappy import main


class Passaro:
    IMG = main.IMAGEM_PASSARO

    # Variaveis de animação
    ROTACAO_MAXIMA = 25
    VELICIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.contagem_imagem = 0
        self.imagem = self.IMG[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # Cálculo do deslocamento do pássaro
        self.tempo += 1
        deslocamento = 1.5(self.tempo**2) + self.velocidade * self.tempo

        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -=2

        # ângulo do pássaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELICIDADE_ROTACAO


