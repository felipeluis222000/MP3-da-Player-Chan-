import pygame
import os
import random
from classes import *

LARGURA = 300
ALTURA = 400
BRANCO = (255,255,255)
PRETO = (0,0,0)
VOLUME = 0.2
POS = 0
CAMINHO = "musicas"


def Main(tela, clock, fonte, fonte2):
    global VOLUME
    global TEMPO

    index = 0
    rodando = True
    pause = False
    pygame.mixer.music.set_volume(VOLUME)
    nome_musica,estilo_musica,tempo_musica = TocarMusica(index)
    lista_sprites = pygame.sprite.Group()
    player_chan = Player_Chan(estilo_musica)
    cenario = Cenario(estilo_musica)
    lista_sprites.add(cenario)
    lista_sprites.add(player_chan)
    mp3 = fonte2.render("MP3",True,(25, 25, 112))
    X = 60

    mouse_event = False
    pause_mouse = False
    return_mouse = False
    pass_mouse = False
    mouse_bar = False
    cor_circulos = [(0,0,0) for _ in range(10)]
    cor_pause = (0, 0, 0)
    cor_return = (0, 0, 0)
    cor_pass = (0, 0, 0)
    cor_menos = (0, 0, 0)
    cor_mais = (0, 0, 0)

    while rodando:
        if not mouse_event:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        mouse = pygame.mouse.get_pos()

        if mouse[0] >= 138 and mouse[0] <= 162 and mouse[1] >= 320 and mouse[1] <= 340:
            mouse_event = True
            pause_mouse = True

        elif mouse[0] >= 120-(300**(1/2)) and mouse[0] <= 130 and mouse[1] >= 320 and mouse[1] <= 340:
            mouse_event= True
            return_mouse = True

        elif mouse[0] >= 170 and mouse[0] <= 180+(300**(1/2)) and mouse[1] >= 320 and mouse[1] <= 340:
            mouse_event = True
            pass_mouse = True

        elif mouse[0] >= 50 and mouse[0] <= 250 and mouse[1] >= 375 and mouse[1] <= 385:
            mouse_event = True
            mouse_bar = True

        elif mouse[0] >= 220 and mouse[0] <= 245 and mouse[1] >= 235 and mouse[1] <= 245:
            mouse_event = True
            mouse_volume_menos = True

        elif mouse[0] >= 265 and mouse[0] <= 290 and mouse[1] >= 240-12 and mouse[1] <= 240+12.5:
            mouse_event = True
            mouse_volume_mais = True

        else:
            mouse_event = False
            pause_mouse = False
            return_mouse = False
            pass_mouse = False
            mouse_bar = False
            mouse_volume_menos = False
            mouse_volume_mais = False

        if pause_mouse:
            cor_pause = (47,79,79)

        elif return_mouse:
            cor_return = (47,79,79)

        elif pass_mouse:
            cor_pass = (47,79,79)

        elif mouse_volume_menos:
            cor_menos = (47,79,79)

        elif mouse_volume_mais:
            cor_mais = (47, 79, 79)

        else:
            cor_pause = (0,0,0)
            cor_return = (0,0,0)
            cor_pass = (0,0,0)
            cor_menos = (0,0,0)
            cor_mais = (0,0,0)

        if VOLUME < 0.1 and VOLUME > 0:
            cor_circulos[0] = (0,0,250)
            cor_circulos[1:] = [(0,0,0) for _ in range(9)]

        elif VOLUME < 0.2 and VOLUME >= 0.1:
            cor_circulos[0] = (0,0,250)
            cor_circulos[1] = (25,0,225)
            cor_circulos[2:] = [(0,0,0) for _ in range(8)]

        elif VOLUME < 0.3 and VOLUME >= 0.2:
            cor_circulos[0] = (0,0,250)
            cor_circulos[1] = (25,0,225)
            cor_circulos[2] = (50,0,200)
            cor_circulos[3:] = [(0,0,0) for _ in range(7)]

        elif VOLUME < 0.4 and VOLUME >= 0.3:
            cor_circulos[0] = (0,0,250)
            cor_circulos[1] = (25,0,225)
            cor_circulos[2] = (50,0,200)
            cor_circulos[3] = (75,0,175)
            cor_circulos[4:] = [(0,0,0) for _ in range(6)]

        elif VOLUME < 0.5 and VOLUME >= 0.4:
            cor_circulos[0] = (0,0,250)
            cor_circulos[1] = (25,0,225)
            cor_circulos[2] = (50,0,200)
            cor_circulos[3] = (75,0,175)
            cor_circulos[4] = (100,0,150)
            cor_circulos[5:] = [(0,0,0) for _ in range(5)]

        elif VOLUME < 0.6 and VOLUME >= 0.5:
            cor_circulos[0] = (0,0,250)
            cor_circulos[1] = (25,0,225)
            cor_circulos[2] = (50,0,200)
            cor_circulos[3] = (75,0,175)
            cor_circulos[4] = (100,0,150)
            cor_circulos[5] = (125,0,125)
            cor_circulos[6:] = [(0,0,0) for _ in range(4)]

        elif VOLUME < 0.7 and VOLUME >= 0.6:
            cor_circulos[0] = (0,0,250)
            cor_circulos[1] = (25,0,225)
            cor_circulos[2] = (50,0,200)
            cor_circulos[3] = (75,0,175)
            cor_circulos[4] = (100,0,150)
            cor_circulos[5] = (125,0,125)
            cor_circulos[6] = (150,0,100)
            cor_circulos[7:] = [(0,0,0) for _ in range(3)]

        elif VOLUME < 0.8 and VOLUME >= 0.7:
            cor_circulos[0] = (0,0,250)
            cor_circulos[1] = (25,0,225)
            cor_circulos[2] = (50,0,200)
            cor_circulos[3] = (75,0,175)
            cor_circulos[4] = (100,0,150)
            cor_circulos[5] = (125,0,125)
            cor_circulos[6] = (150,0,100)
            cor_circulos[7] = (175,0,75)
            cor_circulos[8:] = [(0,0,0) for _ in range(2)]

        elif VOLUME < 0.9 and VOLUME >= 0.8:
            cor_circulos[0] = (0,0,250)
            cor_circulos[1] = (25,0,225)
            cor_circulos[2] = (50,0,200)
            cor_circulos[3] = (75,0,175)
            cor_circulos[4] = (100,0,150)
            cor_circulos[5] = (125,0,125)
            cor_circulos[6] = (150,0,100)
            cor_circulos[7] = (175,0,75)
            cor_circulos[8] = (200,0,50)
            cor_circulos[9:] = [(0,0,0) for _ in range(1)]

        elif VOLUME >= 0.9:
            cor_circulos[0] = (0,0,250)
            cor_circulos[1] = (25,0,225)
            cor_circulos[2] = (50,0,200)
            cor_circulos[3] = (75,0,175)
            cor_circulos[4] = (100,0,150)
            cor_circulos[5] = (125,0,125)
            cor_circulos[6] = (150,0,100)
            cor_circulos[7] = (175,0,75)
            cor_circulos[8] = (200,0,50)
            cor_circulos[9] = (255,0,0)

        else:
            cor_circulos = [(0,0,0) for _ in range(10)]

        if not pause:
            tempo_atual = (pygame.mixer.music.get_pos())/60000
            porcentagem = (tempo_atual+POS)*100/tempo_musica
            tocando = fonte.render(nome_musica.strip(".mp3"),True,PRETO)
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
                            nome_musica,estilo_musica,tempo_musica = TocarMusica(index)
                            player_chan.estilo_musica = estilo_musica
                            cenario.estilo_musica = estilo_musica
                            cenario.mudar_cenario = True

                        else:
                            index = 0
                            nome_musica,estilo_musica,tempo_musica = TocarMusica(index)
                            player_chan.estilo_musica = estilo_musica
                            cenario.estilo_musica = estilo_musica
                            cenario.mudar_cenario = True

                    elif evento.key == pygame.K_LEFT:
                        if pygame.mixer.music.get_pos()+POS*60000 >= 5000:
                            nome_musica,estilo_musica,tempo_musica = TocarMusica(index)
                            player_chan.estilo_musica = estilo_musica
                            cenario.estilo_musica = estilo_musica
                            cenario.mudar_cenario = True

                        else:
                            if index >= 0:
                                index -= 1
                                nome_musica,estilo_musica,tempo_musica = TocarMusica(index)
                                player_chan.estilo_musica = estilo_musica
                                cenario.estilo_musica = estilo_musica
                                cenario.mudar_cenario = True

                            else:
                                index = (len(MUSICAS_TOCAR)-1)

                    elif evento.key == pygame.K_UP:
                        VOLUME += 0.01
                        pygame.mixer.music.set_volume(VOLUME)
                        if VOLUME > 1:
                            VOLUME = 1

                    elif evento.key == pygame.K_DOWN:
                        VOLUME -= 0.01
                        pygame.mixer.music.set_volume(VOLUME)
                        if VOLUME < 0:
                            VOLUME = 0

                    elif evento.key == pygame.K_SPACE:
                        player_chan.estilo_musica = "pause"
                        cenario.estilo_musica = "pause"
                        cenario.mudar_cenario = True
                        pause = True
                        pygame.mixer.music.pause()

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    botao = pygame.mouse.get_pressed(5)
                    if botao[0]:
                        if pause_mouse:
                            player_chan.estilo_musica = "pause"
                            cenario.estilo_musica = "pause"
                            cenario.mudar_cenario = True
                            pause = True
                            pygame.mixer.music.pause()

                        elif return_mouse:
                            if pygame.mixer.music.get_pos()+(POS*60000) >= 5000:
                                nome_musica,estilo_musica,tempo_musica = TocarMusica(index)
                                player_chan.estilo_musica = estilo_musica
                                cenario.estilo_musica = estilo_musica
                                cenario.mudar_cenario = True

                            else:
                                if index >= 0:
                                    index -= 1
                                    nome_musica,estilo_musica,tempo_musica = TocarMusica(index)
                                    player_chan.estilo_musica = estilo_musica
                                    cenario.estilo_musica = estilo_musica
                                    cenario.mudar_cenario = True


                                else:
                                    index = (len(MUSICAS_TOCAR) - 1)


                        elif pass_mouse:
                            if (index + 1) < len(MUSICAS_TOCAR):
                                index += 1
                                nome_musica,estilo_musica,tempo_musica = TocarMusica(index)
                                player_chan.estilo_musica = estilo_musica
                                cenario.estilo_musica = estilo_musica
                                cenario.mudar_cenario = True

                            else:
                                index = 0
                                nome_musica,estilo_musica,tempo_musica = TocarMusica(index)
                                player_chan.estilo_musica = estilo_musica
                                cenario.estilo_musica = estilo_musica
                                cenario.mudar_cenario = True

                        elif mouse_bar:
                            pos = ((mouse[0]-50)*100/200)
                            pos = (tempo_musica*pos/100)*60
                            TocarMusica(index,pos=pos)

                        elif mouse_volume_mais:
                            VOLUME += 0.05
                            pygame.mixer.music.set_volume(VOLUME)
                            if VOLUME > 1:
                                VOLUME = 1

                        elif mouse_volume_menos:
                            VOLUME -= 0.05
                            pygame.mixer.music.set_volume(VOLUME)
                            if VOLUME < 0:
                                VOLUME = 0

                elif evento.type == 900:
                    if (index + 1) < len(MUSICAS_TOCAR):
                        index += 1
                        nome_musica,estilo_musica,tempo_musica = TocarMusica(index)
                        player_chan.estilo_musica = estilo_musica
                        cenario.estilo_musica = estilo_musica
                        cenario.mudar_cenario = True

                    else:
                        index = 0
                        nome_musica,estilo_musica,tempo_musica = TocarMusica(index)
                        player_chan.estilo_musica = estilo_musica
                        cenario.estilo_musica = estilo_musica
                        cenario.mudar_cenario = True

            if tecla[pygame.K_UP]:
                VOLUME += 0.005
                pygame.mixer.music.set_volume(VOLUME)

            elif tecla[pygame.K_DOWN]:
                VOLUME -= 0.005
                pygame.mixer.music.set_volume(VOLUME)

            pygame.mixer.music.set_endevent(900)

            tela.fill(PRETO)
            lista_sprites.update()
            lista_sprites.draw(tela)
            pygame.draw.rect(tela,(54,54,54),(0,0,300,40),0)
            pygame.draw.rect(tela,(54,54,54),(0,40,10,150),0)
            pygame.draw.rect(tela,(54,54,54),(0,190,300,160),0)
            pygame.draw.rect(tela,(54,54,54),(290,40,10,150),0)
            pygame.draw.rect(tela,(79,79,79),(10,20,280,20),0)
            pygame.draw.rect(tela,(79,79,79),(10,170,280,20),0)
            pygame.draw.rect(tela,(79,79,79),(10,40,10,150),0)
            pygame.draw.rect(tela,(79,79,79),(280,40,10,150),0)
            pygame.draw.rect(tela,(34,139,34),(45,350,210,35),0)
            if tocando.get_width() + 60 > 255:
                if X > -(tocando.get_width()+10-255):
                    X -= 0.3
                else:
                    X = 60
                tela.blit(tocando,(X,355))
            else:
                X = 60
                tela.blit(tocando,(X,355))
            pygame.draw.rect(tela,(54,54,54),(0,350,45,50),0)
            pygame.draw.rect(tela,(54,54,54),(255,350,45,50),0)
            pygame.draw.rect(tela,(54,54,54),(45,385,210,15),0)
            pygame.draw.line(tela,(255,255,255),(50,380),(250,380))
            pygame.draw.line(tela,(0,0,255),(50,380),(50+(200*porcentagem/100),380))
            pygame.draw.circle(tela,(255,255,255),(50+(200*porcentagem/100),380),3,0)
            pygame.draw.polygon(tela,cor_return,((130,320),(130,340),(130-(300**(1/2)),330)),0)
            pygame.draw.polygon(tela,cor_return,((120,322),(120,338),(120-(300**(1/2)),330)),0)
            pygame.draw.polygon(tela,cor_pass,((170,320),(170,340),(170+(300**(1/2)),330)),0)
            pygame.draw.polygon(tela,cor_pass,((180,322),(180,338),(180+(300**(1/2)),330)),0)
            pygame.draw.line(tela,(255,255,255),(125-(300**(1/2)),330.5),(130,330.5))
            pygame.draw.line(tela,(255,255,255),(175+(300**(1/2)),330.5),(170,330.5))
            pygame.draw.rect(tela,cor_pause,(138,320,10,20),0)
            pygame.draw.rect(tela,cor_pause,(152,320,10,20),0)
            for i in range(5):
                pygame.draw.circle(tela,cor_circulos[i],(225+(15*i),200),5)
                pygame.draw.circle(tela,cor_circulos[i+5],(225+(15*i),215),5)
            tela.blit(mp3,(150-(mp3.get_width()/2),270-(mp3.get_height()/2)))
            pygame.draw.line(tela,cor_menos,(220,240),(245,240),3)
            pygame.draw.line(tela,cor_mais,(265,240),(290,240),3)
            pygame.draw.line(tela,cor_mais,(277.5,240-12),(277.5,240+12.5),3)

            pygame.display.flip()

        if pause:
            tocando = fonte.render("Pause",True,PRETO)
            clock.tick(60)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                    exit()

                elif evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_SPACE:
                        player_chan.estilo_musica = estilo_musica
                        cenario.estilo_musica = estilo_musica
                        cenario.mudar_cenario = True
                        pause = False
                        pygame.mixer.music.unpause()

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    botao = pygame.mouse.get_pressed(5)
                    if botao[0]:
                        if pause_mouse:
                            player_chan.estilo_musica = estilo_musica
                            cenario.estilo_musica = estilo_musica
                            cenario.mudar_cenario = True
                            pause = False
                            pygame.mixer.music.unpause()

            tela.fill(PRETO)
            lista_sprites.update()
            lista_sprites.draw(tela)
            pygame.draw.rect(tela,(54,54,54),(0,0,300,40),0)
            pygame.draw.rect(tela,(54,54,54),(0,40,10,150),0)
            pygame.draw.rect(tela,(54,54,54),(0,190,300,160),0)
            pygame.draw.rect(tela,(54,54,54),(290,40,10,150),0)
            pygame.draw.rect(tela,(79,79,79),(10,20,280,20),0)
            pygame.draw.rect(tela,(79,79,79),(10,170,280,20),0)
            pygame.draw.rect(tela,(79,79,79),(10,40,10,150),0)
            pygame.draw.rect(tela,(79,79,79),(280,40,10,150),0)
            pygame.draw.rect(tela,(34,139,34),(45,350,210,35),0)
            tela.blit(tocando,((300/2)-(tocando.get_width()/2),355))
            pygame.draw.rect(tela,(54,54,54),(0,350,45,50),0)
            pygame.draw.rect(tela,(54,54,54),(255,350,45,50),0)
            pygame.draw.rect(tela,(54,54,54),(45,385,210,15),0)
            pygame.draw.line(tela,(255,255,255),(50,380),(250,380))
            pygame.draw.line(tela,(0,0,255),(50,380),(50+(200*porcentagem/100),380))
            pygame.draw.circle(tela,(255,255,255),(50+(200*porcentagem/100),380),3,0)
            pygame.draw.polygon(tela,cor_return,((130,320),(130,340),(130-(300**(1/2)),330)),0)
            pygame.draw.polygon(tela,cor_return,((120,322),(120,338),(120-(300**(1/2)),330)),0)
            pygame.draw.polygon(tela,cor_pass,((170,320),(170,340),(170+(300**(1/2)),330)),0)
            pygame.draw.polygon(tela,cor_pass,((180,322),(180,338),(180+(300**(1/2)),330)),0)
            pygame.draw.line(tela,(255,255,255),(125-(300**(1/2)),330.5),(130,330.5))
            pygame.draw.line(tela,(255,255,255),(175+(300**(1/2)),330.5),(170,330.5))
            pygame.draw.polygon(tela,cor_pause,((142,320),(142,340),(142+(300**(1/2)),330)),0)
            pygame.draw.line(tela,(255,255,255),(137+(300**(1/2)),330),(142,330))
            for i in range(5):
                pygame.draw.circle(tela,cor_circulos[i],(225+(15*i),200),5)
                pygame.draw.circle(tela,cor_circulos[i+5],(225+(15*i),215),5)
            tela.blit(mp3, (150 - (mp3.get_width() / 2), 270 - (mp3.get_height() / 2)))
            pygame.draw.line(tela,cor_menos,(220,240),(245,240),3)
            pygame.draw.line(tela,cor_mais,(265,240),(290,240),3)
            pygame.draw.line(tela,cor_mais,(277.5,240-12),(277.5,240+12.5),3)


            pygame.display.flip()

def TocarMusica(index,pos=None):
    global POS

    POS = 0
    pygame.mixer.music.unload()
    tocar = MUSICAS_TOCAR[index].split("\\")
    pygame.mixer.music.load(f"{tocar[0]}/{tocar[1]}/{tocar[2]}")
    musica = pygame.mixer.Sound(f"{tocar[0]}/{tocar[1]}/{tocar[2]}")
    pygame.mixer.music.play()
    if pos:
        POS = pos/60
        pygame.mixer.music.set_pos(pos+pos*0.085)


    return tocar[2],tocar[1],musica.get_length()/60

def OrdemMusicas(caminho):
    musicas_tocar = []
    musicas = []
    rodando = True
    for diretorio, subpasta, arquivo in os.walk(caminho,topdown=False):
        for nomes in arquivo:
            musicas.append(os.path.join(diretorio,nomes))
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
    ICONE = pygame.image.load("Player_Chan/Player_Chan_icon.png")
    pygame.display.set_icon(ICONE)
    pygame.display.set_caption("Player Chan")
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont("Lucida Console", 15)
    fonte2 = pygame.font.SysFont("Lucida Console", 60)

    MUSICAS_TOCAR = OrdemMusicas(CAMINHO)
    Main(tela,clock,fonte,fonte2)