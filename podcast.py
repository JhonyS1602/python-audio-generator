import asyncio
import edge_tts
from moviepy import AudioFileClip, CompositeAudioClip

texto = """
Bienvenidos a Puerto de Brujas.

Un espacio donde la magia, la espiritualidad y los antiguos misterios cobran vida.

Este es nuestro primer podcast oficial.

Un lugar donde las leyendas, los rituales y las tradiciones ancestrales se encuentran para abrir nuevas puertas al conocimiento.

Porque la magia no pertenece solamente a los cuentos.

También vive en nuestras decisiones, en nuestros sueños y en nuestra forma de mirar el mundo.

En Puerto de Brujas creemos que cada persona guarda una chispa de magia en su interior.

La magia de transformarse, de sanar y de descubrir quién es realmente.

Durante los próximos episodios exploraremos los sabbats de la rueda del año, los oráculos, la magia elemental, las antiguas divinidades, la meditación, la energía y muchos otros caminos de sabiduría.

Así que prepara una taza de té.

Enciende una vela si lo deseas.

Respira profundamente.

Y acompáñanos en esta aventura.

Las puertas ya están abiertas.

Y el viaje comienza ahora.

Bienvenidos a Puerto de Brujas.
"""

voz = "es-ES-AlvaroNeural"
musica_fondo = "OMNIA (Official) - Fee Ra Huri.mp3"

async def crear_voz():
    communicate = edge_tts.Communicate(texto, voz, rate="-10%")
    await communicate.save("voz_alvaro.mp3")
    print("Voz creada")

async def crear_podcast():
    await crear_voz()

    voz_audio = AudioFileClip("voz_alvaro.mp3")

    musica = AudioFileClip(musica_fondo)

    # La música empieza 2 segundos antes de la voz
    intro = 2
    duracion_total = voz_audio.duration + intro + 4

    # Cortar la música para que dure lo mismo que el podcast
    musica = musica.subclipped(0, min(musica.duration, duracion_total))

    # Volumen de música: 5%
    musica = musica.with_volume_scaled(0.05)

    # Voz empieza después de 2 segundos
    voz_audio = voz_audio.with_start(intro)

    podcast = CompositeAudioClip([musica, voz_audio])

    podcast.write_audiofile("PuertoDeBrujas_Final.mp3", fps=44100)

    voz_audio.close()
    musica.close()
    podcast.close()

    print("Podcast final creado: PuertoDeBrujas_Final.mp3")

asyncio.run(crear_podcast())