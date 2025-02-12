import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')


# 🌍 Hábitos sostenibles
@bot.command()
async def reutilizables(ctx):
    await ctx.send("Opta por botellas, bolsas y utensilios reutilizables en lugar de productos desechables. ¡Pequeños cambios generan un gran impacto! 🌱")

@bot.command()
async def reciclaje(ctx):
    await ctx.send("Separa papel, plástico, vidrio y orgánicos. Asegúrate de conocer las normas de reciclaje en tu comunidad. ♻️")

@bot.command()
async def compra_granel(ctx):
    await ctx.send("Reduce los envases innecesarios comprando productos a granel. Lleva tus propios recipientes reutilizables. 🛒")

@bot.command()
async def reutiliza_repara(ctx):
    await ctx.send("Antes de tirar algo, pregúntate si puedes repararlo o reutilizarlo de otra forma. ¡Sé creativo! 🔧")

@bot.command()
async def comparte_ideas(ctx):
    await ctx.send("Motiva a tu familia y amigos a cuidar el planeta. ¡Juntos podemos hacer la diferencia! 🌎")

# 🚫 Evita la contaminación
@bot.command()
async def evita_plasticos(ctx):
    await ctx.send("Evita el uso de popotes, cubiertos y vasos desechables. Mejor usa opciones reutilizables. 🚯")

@bot.command()
async def ropa_segunda_mano(ctx):
    await ctx.send("Comprar ropa de segunda mano ayuda a reducir la contaminación textil. Además, ¡puedes encontrar estilos únicos! 👕")

@bot.command()
async def haz_compost(ctx):
    await ctx.send("Convierte restos de comida en abono en lugar de tirarlos. ¡El compostaje es una excelente opción para reducir desperdicios! 🌱")

@bot.command()
async def usa_tela(ctx):
    await ctx.send("Usa servilletas y pañuelos de tela en lugar de papel. Son reutilizables y ecológicos. 🧻")

@bot.command()
async def lleva_termo(ctx):
    await ctx.send("Lleva tu propio termo o taza para evitar los vasos desechables. ¡Menos residuos, más café! ☕")

@bot.command()
async def menos_empaque(ctx):
    await ctx.send("Elige productos con menos empaque. Prefiere marcas que reduzcan el uso de plástico. 📦")

@bot.command()
async def cocina_casa(ctx):
    await ctx.send("Cocinar en casa ayuda a reducir envolturas plásticas y es más saludable. 🍽️")

# 🎨 Reutilización y manualidades
@bot.command()
async def frascos_vidrio(ctx):
    await ctx.send("Reutiliza frascos de vidrio para almacenar alimentos, hacer manualidades o decorar. 🏺")

@bot.command()
async def dona_recicla(ctx):
    await ctx.send("Dona ropa, libros y electrónicos en lugar de tirarlos. Alguien más puede darles una segunda vida. 🎁")

@bot.command()
async def aprende_reparar(ctx):
    await ctx.send("Antes de desechar algo, busca tutoriales para repararlo. Hay muchas soluciones fáciles. 🔧")

# 📢 Conciencia y activismo
@bot.command()
async def eco_retos(ctx):
    await ctx.send("¡Participa en nuestro reto ecológico semanal y ayuda al planeta! 🌍")

@bot.command()
async def noticias_verdes(ctx):
    await ctx.send("Mantente informado con las últimas noticias sobre medio ambiente y sostenibilidad. 📢")

@bot.command()
async def huella_ecologica(ctx):
    await ctx.send("Descubre tu impacto ambiental con nuestro test de huella ecológica. 🌿")

@bot.command()
async def voluntariado(ctx):
    await ctx.send("¿Quieres ayudar al planeta? Encuentra organizaciones ecológicas donde puedas participar. 🌎")

@bot.command()
async def eco_memes(ctx):
    await ctx.send("¡Aprender sobre el medio ambiente también puede ser divertido! Aquí tienes un meme ecológico. 😆♻️")

@bot.command()
async def eco_trivia(ctx):
    await ctx.send("Pon a prueba tus conocimientos con nuestra trivia ecológica. 🎮🌱")

# Comando de inicio y ayuda
@bot.command()
async def inicio(ctx):
    await ctx.send("🌱 ¡Bienvenido al bot ecológico! Usa /ayuda para ver los comandos disponibles.")

# Datos sobre el impacto ambiental
@bot.command()
async def bolsas_plasticas(ctx):
    await ctx.send("Cada minuto se usan cerca de un millón de bolsas plásticas en el mundo. ♻️")

@bot.command()
async def degradacion_plastico(ctx):
    await ctx.send("Se pueden llegar a necesitar cerca de 1.000 años para que la naturaleza consiga eliminar el plástico. 🌍")

@bot.command()
async def bombilla_energia(ctx):
    await ctx.send("Una bombilla normal puede perder hasta el 90% de la energía que emite en forma de calor, y no de luz. 💡")

@bot.command()
async def consumo_energia(ctx):
    await ctx.send("El 5% de la población utiliza el 25% de la energía del mundo. ⚡")

@bot.command()
async def reciclaje_bolsas(ctx):
    await ctx.send("Menos del 5% de las bolsas de plástico son recicladas cada año. 🚯")

@bot.command()
async def calentamiento_global(ctx):
    await ctx.send("Desde el siglo XIX el planeta se ha calentado cerca de 0.8 °C, lo que provocaría que un cubito de hielo se convierta en un charco. 🌡️")

# Cambio Climático
@bot.command()
async def temperatura_global(ctx):
    await ctx.send("La temperatura global ha aumentado aproximadamente 1,2°C desde la era preindustrial. 🔥")

@bot.command()
async def ano_caluroso(ctx):
    await ctx.send("El 2023 fue el año más caluroso registrado, superando los récords previos. ☀️")

@bot.command()
async def nivel_mar(ctx):
    await ctx.send("El nivel del mar ha subido unos 20 cm desde 1900, principalmente por el derretimiento de los glaciares y la expansión térmica del agua. 🌊")

# Biodiversidad
@bot.command()
async def especies_tierra(ctx):
    await ctx.send("Se estima que hay 8,7 millones de especies en la Tierra, pero solo conocemos cerca de 2 millones. 🐾")

@bot.command()
async def peligro_extincion(ctx):
    await ctx.send("Aproximadamente un millón de especies están en peligro de extinción debido a la actividad humana. ⚠️")

# Contaminación
@bot.command()
async def residuos_plasticos(ctx):
    await ctx.send("Cada año, se generan 400 millones de toneladas de plástico, y solo el 9% se recicla. 🗑️")

@bot.command()
async def aire_contaminado(ctx):
    await ctx.send("Más del 90% de la población mundial respira aire contaminado, según la OMS. 🌫️")

@bot.command()
async def contaminacion_agua(ctx):
    await ctx.send("La contaminación del agua causa la muerte de 1,8 millones de personas al año. 💧")

# Energías Renovables
@bot.command()
async def energia_renovable(ctx):
    await ctx.send("En 2023, alrededor del 30% de la electricidad mundial provino de fuentes renovables como el sol y el viento. ☀️🌬️")

@bot.command()
async def energia_solar(ctx):
    await ctx.send("La energía solar es la fuente de electricidad de más rápido crecimiento. 🔆")

# Deforestación
@bot.command()
async def perdida_bosques(ctx):
    await ctx.send("Se pierden alrededor de 10 millones de hectáreas de bosque al año. 🌳")

@bot.command()
async def amazonas_deforestacion(ctx):
    await ctx.send("La Amazonia ha perdido 17% de su cobertura forestal en los últimos 50 años. 🌎")

# Agua y Recursos Naturales
@bot.command()
async def agua_dulce(ctx):
    await ctx.send("Solo 2,5% del agua en el planeta es dulce, y menos del 1% está disponible para el consumo humano. 💦")

@bot.command()
async def acceso_agua(ctx):
    await ctx.send("Cerca de 2.200 millones de personas no tienen acceso a agua potable segura. 🚰")

# Comando de ayuda
@bot.command()
async def ayuda(ctx):
    await ctx.send("Lista de comandos disponibles:")
    await ctx.send("**Impacto ambiental:** \n!bolsas_plasticas, !degradacion_plastico, !bombilla_energia, !consumo_energia, !reciclaje_bolsas, !calentamiento_global")
    await ctx.send("**Cambio climático:** \n!temperatura_global, !ano_caluroso, !nivel_mar")
    await ctx.send("**Biodiversidad:** \n!especies_tierra, !peligro_extincion")
    await ctx.send("**Contaminación:** \n!residuos_plasticos, !aire_contaminado, !contaminacion_agua")
    await ctx.send("**Energías Renovables:** \n!energia_renovable, !energia_solar")
    await ctx.send("**Deforestación:** \n!perdida_bosques, !amazonas_deforestacion")
    await ctx.send("**Agua y Recursos Naturales:** \n!agua_dulce, !acceso_agua")
    await ctx.send("**Origami:** \n!grulla, !mariposa, !rana_saltarina, !corazon, !flor_loto, !pez, !perro_gato, !cisne, !dragon, !estrella_ninja, !caja, !rosa, !barco_papel")
