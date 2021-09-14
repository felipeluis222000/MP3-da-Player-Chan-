import pygame
import random
import os

spritesheet = pygame.image.load("dancarino/dança.png")
class Dancarino(pygame.sprite.Sprite):
    def __init__(self,estilo_musica):
        super().__init__()
        self.contador = 0
        self.estilo_musica = estilo_musica
        self.danca_inicio = 0
        self.danca_final = 7
        self.index = 0
        self.velocidade = 0.2
        self.passos = [[[],[]],[],[[],[]],[],[],[]]

        for i in range(8):
            imagem = spritesheet.subsurface((110*i,128*4),(110,128))
            self.passos[0][0].append(imagem)

        for i in range(8):
            imagem = spritesheet.subsurface((110*i,128*8),(110,128))
            self.passos[0][1].append(imagem)

        for j in range(2):
            for i in range(8):
                imagem = spritesheet.subsurface((110*i,128*j),(110,128))
                self.passos[1].append(imagem)

        for i in range(8):
            imagem = spritesheet.subsurface((110*i,128*7),(110,128))
            self.passos[2][0].append(imagem)

        for i in range(8):
            imagem = spritesheet.subsurface((110*i,128*2),(110,128))
            self.passos[2][1].append(imagem)

        for i in range(8):
            imagem = spritesheet.subsurface((110*i,128*5),(110,128))
            self.passos[3].append(imagem)

        for i in range(8):
            imagem = spritesheet.subsurface((110*i,128*3),(110,128))
            self.passos[4].append(imagem)

        for j in range(8):
            imagem = spritesheet.subsurface((j*110,128*9),(110,120))
            self.passos[-1].append(imagem)

        self.image = self.passos[-1][self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (150,100)

    def update(self):
        if self.estilo_musica == "animadas":
            self.velocidade = 0.2
            if self.index > len(self.passos[0][int(self.contador)])-1:
                self.index = 0
            if self.contador >= 1.9:
                self.contador = 0
            self.contador += 0.09
            self.index += self.velocidade
            self.image = self.passos[0][int(self.contador)][int(self.index)]

        elif self.estilo_musica == "lentas":
            self.velocidade = 0.12
            if self.index > len(self.passos[1])-1:
                self.index = 0
            self.index += self.velocidade
            self.image = self.passos[1][int(self.index)]

        elif self.estilo_musica == "rock":
            self.velocidade = 0.2
            if self.index > len(self.passos[2][int(self.contador)])-1:
                self.index = 0
            if self.contador >= 1.9:
                self.contador = 0
            self.contador += 0.005
            self.index += self.velocidade
            self.image = self.passos[2][int(self.contador)][int(self.index)]

        elif self.estilo_musica == "romanticas":
            self.velocidade = 0.12
            if self.index > len(self.passos[3])-1:
                self.index = 0
            self.index += self.velocidade
            self.image = self.passos[3][int(self.index)]

        elif self.estilo_musica == "tristes":
            self.velocidade = 0.1
            if self.index > len(self.passos[4])-1:
                self.index = 0
            self.index += self.velocidade
            self.image = self.passos[4][int(self.index)]

        elif self.estilo_musica == "pause":
            self.velocidade = 0.16
            if self.index > len(self.passos[-1])-1:
                self.index = 0
            self.index += self.velocidade
            self.image = self.passos[-1][int(self.index)]

class Cenario(pygame.sprite.Sprite):
    def __init__(self,estilo_musica):
        super().__init__()
        self.estilo_musica = estilo_musica
        self.mudar_cenario = False
        for diretorio,subpastas,arquivos in os.walk(f"cenarios/{self.estilo_musica}"):
            img = pygame.image.load(f"cenarios/{estilo_musica}/{random.choice(arquivos)}")
            #img tem que ser 260x130

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (150,105)

    def update(self):
        if self.mudar_cenario:
            for diretorio, subpastas, arquivos in os.walk(f"cenarios/{self.estilo_musica}"):
                img = pygame.image.load(f"cenarios/{self.estilo_musica}/{random.choice(arquivos)}")

            self.image = img
            self.mudar_cenario = False