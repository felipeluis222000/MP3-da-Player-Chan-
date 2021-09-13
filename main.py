import pygame
import os
import random
from spritesdançarino import *

LARGURA = 300
ALTURA = 300
BRANCO = (255,255,255)
PRETO = (0,0,0)
VOLUME = 0.2
POS = 0
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

    mouse_event = False
    pause_mouse = False
    return_mouse = False
    pass_mouse = False
    mouse_bar = False

    while rodando:
        if not mouse_event:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        mouse = pygame.mouse.get_pos()

        if mouse[0] >= 138 and mouse[0] <= 162 and mouse[1] >= 220 and mouse[1] <= 240:
            mouse_event = True
            pause_mouse = True

        elif mouse[0] >= 120-(300**(1/2)) and mouse[0] <= 130 and mouse[1] >= 220 and mouse[1] <= 240:
            mouse_event= True
            return_mouse = True

        elif mouse[0] >= 170 and mouse[0] <= 180+(300**(1/2)) and mouse[1] >= 220 and mouse[1] <= 240:
            mouse_event = True
            pass_mouse = True

        elif mouse[0] >= 50 and mouse[0] <= 250 and mouse[1] >= 275 and mouse[1] <= 300:
            mouse_event = True
            mouse_bar = True

        else:
            mouse_event = False
            pause_mouse = False
            return_mouse = False
            pass_mouse = False
            mouse_bar = False

        if pause_mouse:
            cor_pause = (0,0,255)

        elif return_mouse:
            cor_return = (0,0,255)

        elif pass_mouse:
            cor_pass = (0,0,255)

        else:
            cor_pause = (255,255,255)
            cor_return = (255,255,255)
            cor_pass = (255, 255, 255)

        if not pause:
            tempo_atual = round((pygame.mixer.music.get_pos())/60000,2)
            porcentagem = round((tempo_atual+POS)*100/tempo_musica,2)
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
                        if pygame.mixer.music.get_pos()+POS*60000 >= 5000:
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

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    botao = pygame.mouse.get_pressed(5)
                    if botao[0]:
                        if pause_mouse:
                            pause = True
                            pygame.mixer.music.pause()

                        elif return_mouse:
                            if pygame.mixer.music.get_pos()+(POS*60000) >= 5000:
                                nome_musica, tempo_musica = TocarMusica(index)

                            else:
                                if index >= 0:
                                    index -= 1
                                    nome_musica, tempo_musica = TocarMusica(index)


                                else:
                                    index = (len(MUSICAS_TOCAR) - 1)

                                if dancarino.index < 8:
                                    dancarino.index = 72
                                    dancarino.danca_inicio = 72
                                    dancarino.danca_final = 79

                                else:
                                    dancarino.index -= 8
                                    dancarino.danca_inicio -= 8
                                    dancarino.danca_final -= 8

                        elif pass_mouse:
                            if (index + 1) < len(MUSICAS_TOCAR):
                                index += 1
                                nome_musica, tempo_musica = TocarMusica(index)

                            else:
                                index = 0
                                nome_musica, tempo_musica = TocarMusica(index)

                            if dancarino.index > 70:
                                dancarino.index = 0
                                dancarino.danca_inicio = 0
                                dancarino.danca_final = 7
                            else:
                                dancarino.index += 8
                                dancarino.danca_inicio += 8
                                dancarino.danca_final += 8

                        elif mouse_bar:
                            pos = round((mouse[0]-50)*100/200,2)
                            pos = round((tempo_musica*pos/100)*60,2)
                            TocarMusica(index,pos=pos)

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
            pygame.draw.polygon(tela,cor_return,((130,220),(130,240),(130-(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,cor_return,((120,222),(120,238),(120-(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,cor_pass,((170,220),(170,240),(170+(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,cor_pass,((180,222),(180,238),(180+(300**(1/2)),230)),0)
            pygame.draw.rect(tela,cor_pause,(138,220,10,20),0)
            pygame.draw.rect(tela,cor_pause,(152,220,10,20),0)

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

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    botao = pygame.mouse.get_pressed(5)
                    if botao[0]:
                        if pause_mouse:
                            pause = False
                            pygame.mixer.music.unpause()

            tela.fill(PRETO)
            tela.blit(tocando,(X,0))
            lista_sprites.draw(tela)
            pygame.draw.line(tela, (255, 255, 255), (50, 280), (250, 280))
            pygame.draw.line(tela, (0, 0, 255), (50, 280), (50+(200*porcentagem/100), 280))
            pygame.draw.circle(tela,(255,255,255),(50+(200*porcentagem/100),280),3,0)
            pygame.draw.polygon(tela,cor_return,((130,220),(130,240),(130-(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,cor_return,((120,222),(120,238),(120-(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,cor_pass,((170,220),(170,240),(170+(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,cor_pass,((180,222),(180,238),(180+(300**(1/2)),230)),0)
            pygame.draw.polygon(tela,cor_pause,((142,220),(142,240),(142+(300**(1/2)),230)),0)
            pygame.display.flip()

def TocarMusica(index,pos=None):
    global POS

    POS = 0
    pygame.mixer.music.unload()
    pygame.mixer.music.load(f"{CAMINHO}/{MUSICAS_TOCAR[index]}")
    musica = pygame.mixer.Sound(f"{CAMINHO}/{MUSICAS_TOCAR[index]}")
    pygame.mixer.music.play()
    if pos:
        POS = pos/60
        pygame.mixer.music.rewind()
        pygame.mixer.music.set_pos(pos)

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

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    tela = pygame.display.set_mode((LARGURA,ALTURA))
    pygame.display.set_caption("Meu MP3")
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont("Lucida Console", 15)


    MUSICAS_TOCAR = OrdemMusicas(CAMINHO)
    Main(tela,clock,fonte)