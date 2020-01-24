# вусик гей
# Initial main persons
#hide vusikcry with moveoutright-съебаться впарво по быстрому moveinright - приебаться
    #show vusik at right2 with easeinright -приебаться вправо по медлннному
define v = Character("Вусик", color="#DAA520")
define k = Character("Кекс", color="#FFE4E1")
define f = Character("Флангелина", color="#800080")
define m = Character("Мент", color="#00FFFF	")
define p = Character("Полицейский", color="#000080")

init:
    $ left2 = Position(xalign=0.2, yaligh=1.1)
    $ right2 = Position(xalign=0.8, yaligh=1.1)

# Гобка гей
label start:
    stop music

    scene roof
    with fade

    show keks at left2
    with dissolve

    # Начало сюжета
    play sound "audio/dayn.mp3"
    k "О я даун, но не чувствую себя дауном, шо делать, последний день в школе жопа!"
    stop sound

    show vusik at right2
    with easeinright

    play sound "audio/vusik.mp3"
    v "К... Кекс, я люблю тебя!"
    stop sound

    play sound "audio/dayn2.mp3"
    k "А я тебя нет, ты шлюха!"
    stop sound

    scene roofdown
    with fade

    show vusikr
    stop sound
    play sound "audio/no.mp3"
    "После данных слов, Кекс спрыгнул с крыши, а Вусик прыгнул за ним в след."
    stop sound

    #Сон заканчивается

    scene room
    with fade

    "Вусик просыпается в холодном поту и ему сразу приходит осознание того что это был кошмар."
    play sound "audio/sleep.mp3"

    show vusikcry

    v "Это... Это просто ужасно, хорошо что это просто сон, но лучше бы на месте семпая была я."

    hide vusikcry with moveoutright

    stop sound

    scene bathroom
    with fade

    "После этих слов, Вусик встал с кровати и пошел в душ."

    scene kitchen
    with fade

    "Закончив водные процедуры, Вусик, быстро сделал на кухне завтрак и побежал в школу с бутербродом во рту."

    scene schoolout
    with fade

    "Вусика ожидал неприятный сюрприз,{w} у школы стоял Кекс, Вусик сразу вспомнил тот самый сон, на котором кекс спрыгнул с крыши."
    "Но несмотря на всё это, Вусик решается заговорить с Кексом."
    v "К...Кекс... Я могу тебе кое-что сказать?"
    k "Да, конечно!"

    menu:
        "Признаться в любви":
            jump vusiklove
        "Попросить тетрадь":
            jump tetrad
###################################
label vusiklove:
    "Вусик признаётся кексу в любви"
    v "К... Кекс, я люблю тебя."
    k "А я тебя нет!"
    "После данных слов, Вусик в ярости бросаеться на кекса и убивает его, {w} после этого Вусик вскрывает вены и умирает"

    return

label tetrad:
    v "К... Кекс, дай списать!"
    k'''
    Хорошо.
    Только верни.
    Иначе, мне нечем будет подтирать свою сраку!
    '''
    v "Х... Хорошо!"
    return
##################################
