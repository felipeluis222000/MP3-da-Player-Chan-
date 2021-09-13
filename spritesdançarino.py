import pygame

spritesheet = pygame.image.load("dancarino/dança.png")
class Dancarino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.danca_inicio = 0
        self.danca_final = 7
        self.index = 0
        self.velocidade = 0.2
        self.passos = []
        for i in range(9):
            for j in range(8):
                imagem = spritesheet.subsurface((j*110,i*128),(110,128))
                self.passos.append(imagem)
        for j in range(8):
            imagem = spritesheet.subsurface((j*110,128*9),(110,120))
            self.passos.append(imagem)

        self.image = self.passos[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (150,80)

    def update(self):
        if self.index > self.danca_final or self.index < self.danca_inicio:
            self.index = self.danca_inicio
        else:
            self.index += self.velocidade
            self.image = self.passos[int(self.index)]

        if self.index >= 0 and self.index < 8:
            self.velocidade = 0.3
        elif self.index >= 8 and self.index < 16:
            self.velocidade = 0.12
        elif self.index >= 16 and self.index < 24:
            self.velocidade = 0.2
        elif self.index >= 24 and self.index < 32:
            self.velocidade = 0.15
        elif self.index >= 32 and self.index < 40:
            self.velocidade = 0.12
        elif self.index >= 40 and self.index < 48:
            self.velocidade = 0.15
        elif self.index >= 48 and self.index < 56:
            self.velocidade = 0.15
        elif self.index >= 56 and self.index < 64:
            self.velocidade = 0.15
        elif self.index >= 64 and self.index < 72:
            self.velocidade = 0.3
        elif self.index > 72:
            self.velocidade = 0.3