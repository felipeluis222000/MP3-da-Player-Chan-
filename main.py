import pygame
import os
import random
from spritesdançarino import *

LARGURA = 300
ALTURA = 300
BRANCO = (255,255,255)
PRETO = (0,0,0)
VOLUME = 0.2
TEMPO = 0
CAMINHO = "C:/Users/felip/Downloads/musicas"


def Main(tela, clock, fonte):
    global VOLUME
    global TEMPO

    index = 0
    rodando = True
    pause = False
    pygame.mixer.music.set_volume(VOLUME)
    nome_musica,tempo_musica = TocarMusica(index)
    lista_sprites = pygame.sprite.Group()
    dancarino = Dancarino()
    lista_sprites.add(dancarino)
    X = 0


    while rodando:
        if not pause:
            tempo_atual = round(pygame.mixer.music.get_pos()/60000,2)
            porcentagem = round(tempo_atual*100/tempo_musica,2)
            tocando = fonte.render(nome_musica.strip(".mp3"),True,BRANCO)
            tecla = pygame.key.get_pressed()
            clock.tick(60)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                    exit()

                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RIGHT:
                        if (index+1) < len(MUSICAS_TOCAR):
                            index += 1
                            nome_musica,tempo_musica = TocarMusica(index)

                        else:
                            index = 0
                            nome_musica,tempo_musica = TocarMusica(index)

                        if dancarino.index > 70:
                            dancarino.index = 0
                            dancarino.danca_inicio = 0
                            dancarino.danca_final = 7
                        else:
                            dancarino.index += 8
                            dancarino.danca_inicio += 8
                            dancarino.danca_final += 8

                    elif evento.key == pygame.K_LEFT:
                        if (pygame.mixer.music.get_pos()-TEMPO) >= 5000:
                            nome_musica,tempo_musica = TocarMusica(index)

                        else:
                            if index >= 0:
                                index -= 1
                                nome_musica,tempo_musica = TocarMusica(index)


                            else:
                                index = (len(MUSICAS_TOCAR)-1)

                            if dancarino.index < 8:
                                dancarino.index = 72
                                dancarino.danca_inicio = 72
                                dancarino.danca_final = 79

                            else:
                                dancarino.index -= 8
                                dancarino.danca_inicio -= 8
                                dancarino.danca_final -= 8

                    elif evento.key == pygame.K_UP:
                        VOLUME += 0.01
                        pygame.mixer.music.set_volume(VOLUME)

                    elif evento.key == pygame.K_DOWN:
                        VOLUME -= 0.01
                        pygame.mixer.music.set_volume(VOLUME)

                    elif evento.key == pygame.K_SPACE:
                        pause = True
                        pygame.mixer.music.pause()

                elif evento.type == 900:
                    if (index + 1) < len(MUSICAS_TOCAR):
                        index += 1
                        nome_musica,tempo_musica = TocarMusica(index)

                    else:
                        index = 0
                        nome_musica,tempo_musica = TocarMusica(index)
                    if dancarino.index > 70:
                        dancarino.index = 0
                        dancarino.danca_inicio = 0
                        dancarino.danca_final = 7
                    else:
                        dancarino.index += 8
                        dancarino.danca_inicio += 8
                        dancarino.danca_final += 8

            if tecla[pygame.K_UP]:
                VOLUME += 0.005
                pygame.mixer.music.set_volume(VOLUME)

            elif tecla[pygame.K_DOWN]:
                VOLUME -= 0.005
                pygame.mixer.music.set_volume(VOLUME)

            pygame.mixer.music.set_endevent(900)

            tela.fill(PRETO)
            lista_sprites.draw(tela)
            lista_sprites.update()
            if tocando.get_width() > LARGURA:
                if X > -(tocando.get_width()-LARGURA+30):
                    X -= 0.3
                else:
                    X = 0
                tela.blit(tocando,(X,0))
            else:
                X=0
                tela.blit(tocando,(X,0))
            pygame.draw.line(tela,(255,255,255),(50,280),(250,280))
            pygame.draw.line(tela, (0, 0, 255), (50, 280), (50+(200*porcentagem/100), 280))
            pygame.draw.circle(tela,(255,255,255),(50+(200*porcentagem/100),280),3,0)
            pygame.draw.polygon(tela,(255,255,255),((130,220),(130,240),(130-(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,(255,255,255),((120,222),(120,238),(120-(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,(255,255,255),((170,220),(170,240),(170+(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,(255,255,255),((180,222),(180,238),(180+(300**(1/2)),230)),0)
            pygame.draw.rect(tela,(255,255,255),(138,220,10,20),0)
            pygame.draw.rect(tela,(255,255,255),(152,220,10,20),0)

            pygame.display.flip()

        if pause:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        pause = False
                        pygame.mixer.music.unpause()

            tela.fill(PRETO)
            tela.blit(tocando,(X,0))
            lista_sprites.draw(tela)
            pygame.draw.line(tela, (255, 255, 255), (50, 280), (250, 280))
            pygame.draw.line(tela, (0, 0, 255), (50, 280), (50+(200*porcentagem/100), 280))
            pygame.draw.circle(tela,(255,255,255),(50+(200*porcentagem/100),280),3,0)
            pygame.draw.polygon(tela,(255,255,255),((130,220),(130,240),(130-(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,(255,255,255),((120,222),(120,238),(120-(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,(255,255,255),((170,220),(170,240),(170+(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,(255,255,255),((180,222),(180,238),(180+(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,(255,255,255),((142,220),(142,240),(142+(300**(1/2)),230)),0)
            pygame.display.flip()

def TocarMusica(index):
    global TEMPO

    pygame.mixer.music.unload()
    pygame.mixer.music.load(f"{CAMINHO}/{MUSICAS_TOCAR[index]}")
    musica = pygame.mixer.Sound(f"{CAMINHO}/{MUSICAS_TOCAR[index]}")
    pygame.mixer.music.play()
    TEMPO = pygame.mixer.music.get_pos()
    return MUSICAS_TOCAR[index], round(musica.get_length()/60,2)

def OrdemMusicas(caminho):
    for diretorio, subpasta, arquivo in os.walk(caminho):
        musicas = arquivo
    musicas_tocar = []
    rodando = True
    while rodando:
        musica = random.choice(musicas)
        musicas_tocar.append(musica)
        musicas.remove(musica)
        if not musicas:
            return musicas_tocar

pygame.init()
pygame.font.init()
pygame.mixer.init()
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Meu MP3")
clock = pygame.time.Clock()
fonte = pygame.font.SysFont("Lucida Console", 15)


MUSICAS_TOCAR = OrdemMusicas(CAMINHO)
Main(tela,clock,fonte)