"""command: .abusehin , .abusemal"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telethon import events
import random
import asyncio
from REBELBOT.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"habuse(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "hin":
        emoticons = [
            "Maderchod- MOTHERFUCKER",
            "Bhosadike-BORN FROM A ROTTEN PUSSY",
            "Bhen chod-Sister fucker",
            "Bhadhava- Pimp",
            "Bhadhava- Pimp",
            "Chodu- Fucker",
            "Chutiya- Fucker, bastard",
            "Gaand- ASS",
            "Gaandu-Asshole",
"Gadha, Bakland- Idiot",
"Lauda, Lund- Penis, dick, cock",
"Hijra- Gay, Transsexual",
"Kuttiya- Bitch",
"Paad- FART",
"Randi- HOOKER",
"Saala kutta- Bloody dog",
"Saali kutti- Bloody bitch",
"Tatti- Shit",
"Kamina- bastard",
"Chut ke pasine mein talay huye bhajiye- Snack fried in pussy sweat",
"Chut ke dhakkan- Pussy lid",
"Chut ke gulam- Pussy whipped",
"Chutiya ka bheja ghas khane gaya hai- idiot’s brain has gone to eat grass",
"Choot marani ka- Pussy whipped",
"Choot ka baal- Hair of vagina",
"Chipkali ke jhaat ke baal- Lizard’s cunt hairs",
"Chipkali ke jhaat ke paseene- Sweat of Lizard’s pubic hair",
"Chipkali ke gaand ke pasine-  Sweat of a lizard’s ass",
"Chipkali ke chut ke pasine- Sweat of reptiles cunt",
"Chipkali ki bhigi chut- Wet pussy of a wall lizard",
"Chinaal ke gadde ke nipple ke baal ke joon- Prostitute’s breast’s nipple’s hair’s lice",
"Chullu bhar muth mein doob mar-  Drown yourself in a handful of semen",
"Cuntmama- Vaginal uncle",
"Chhed- Vagina,Hole",
"Apni gaand mein muthi daal- Put your fist up your ass",
"Apni lund choos- Go and suck your own dick",
"Apni ma ko ja choos- Go suck your mom",
"Bhen ke laude- Sister’s dick",
"Bhen ke takke: Go and suck your sister’s balls",
"Abla naari tera buble bhaari-  woman, your tits are huge",
"Bhonsri-Waalaa- You fucker",
"Bhadwe ka awlat- Son of a pimp",
"Bhains ki aulad- Son of a buffalo",
"Buddha Khoosat- Old fart",
"Bol teri gand kaise maru- let me know how to fuck you in the ass",
"Bur ki chatani- Ketchup of cunt",
"Chunni- Clit",
"Chinaal- Whore",
"Chudai khana- Whore house",
"Chudan chuda- Fucking games",
"Chut ka pujari- pussy worshipper",
"Chut ka bhoot- Vaginal Ghost",
"Gaand ka makhan- Butter from the ass",
"Gaand main lassan- Garlic in ass",
"Gaand main danda- Stick in ass",
"Gaand main keera- Bug up your ass",
"Gaand mein bambu- A bambooup your ass",
"Gaandfat- Busted ass",
"Pote kitne bhi bade ho, lund ke niche hi rehte hai- However big the balls might be, they have to stay beneath the penis",
"Hazaar lund teri gaand main-Thousand dicks in your ass",
"Jhat ke baal- Pubic hair",
"Jhaant ke pissu- Bug of pubic hair",
"Kadak Mall- Sexy Girl",
"Kali Choot Ke Safaid Jhaat- White hair of a black pussy",
"Khotey ki aulda- Son of donkey",
"Kutte ka awlat- Son of a dog",
"Kutte ki jat- Breed of dog",
"Kutte ke tatte- Dog’s balls",
"Kutte ke poot, teri maa ki choot-  Son of a dog, your mother’s pussy",
"Lavde ke bal- Hair on your penis",
"muh mei lele: Suck my dick",
"Lund Chus: Suck dick",
"Lund Ke Pasine- Sweat of dick",
"Meri Gand Ka Khatmal: Bug of my Ass",
"Moot, Mootna- Piss off",
"Najayaz paidaish- Illegitimately born",
"Randi khana- whore house",
"Sadi hui gaand- Stinking ass",
"Teri gaand main kute ka lund- A dog’s dick in your ass",
"Teri maa ka bhosda- Your mother’s breasts",
"Teri maa ki chut- Your mother’s pussy",
"Tere gaand mein keede paday- May worms infest your ass-hole",
"Ullu ke pathe- Idiot",
        ]
    elif input_str in "mal":
        emoticons = [
            "Ninde ama, pati! Your mom, bitch!",
"Aaana kunna Big dick",
"Achinga Kunnan A man with his dick like a beans",
"Ajoli ka Thajoli Transexual",
"Andi pidiyan Dick catcher",
"Chandi Ass",
"Chokka lingam Sabeel",
"Ettukali Patti Pooran Spider Pussy Bitch",
"Kandu Girls pussy",
"Kanni Virgin",
"Kanni mola First breast",
"Keepu Concubine",
"Kettal Fucking",
"Kolekkeri Whore",
"Koothara Cheap, low-class, culture-less",
"Koothi anus",
"Koothichi Bitch",
"Koyimani Penis",
"Kundi Ass",
"Kundi mon Son of a anus",
"Kunna Dick",
"Kunna Oli Dick Sucker",
"Kunna paal Sperm",
"Kunna thayoli Motherfucking Dick",
"Lick Me Anea Nakakaa",
"Maratel ooki Tree fucker",
"Masa Prostitute",
"Mattanga Poore Pumkin Pussy",
"Mayiradi mon Son of the wavy pubic hair",
"Mlechan Ignorant",
"Mula Adi Your boobs swung",
"Myir Pubes",
"Myre Pubic hair",
"Myrru Pubic Hair",
"Naayi meedan Dog faced bitch",
"Nayinte Mone Son Of A Bitch",
"Nayinte Monne Son of a Bitch",
"Ninte Ammede Kothil. In your mothers ass hole.",
"Ninte ama koondi ishtima Your mom likes ass",
"Ninte ammakku vettu nayinte mone fuck your mother you son of a bitch  (49%)      (51%)",
"Ninte ammaku vetu Fuck your mom",
"Ninte ammede thenga mairu your moms coconut pubes",
"Odu myre run pubic motherfucker",
"Oooomb Fuck off",
"Pacha tayolli green motherfucker",
"Pachila Pooran Green Leaf Pussy Man",
"Para kutichi whore",
"Pela molichi Unfair Girl",
"Pela vedi Most Prostitute",
"Pezhachu Pettavan One who was born to a slut",
"Poda Thayoli Fuck you motherfucker",
"Pooranddi Pussy+dick",
"Poori mone Son of big Pussy mother",
"Poorri Girl with big puzzy",
"Pooru Montha Cunt Face  (64%)      (36%)",
"Puchi Pussy  (57%)      (43%)",
"Pulayadi monae Son of a whoremonger  (59%)      (41%)",
"Purusha Vedi Gigalo  (49%)      (51%)",
"Santhosh Pandit Idiot  (71%)      (29%)",
"Shukla mughan sperm face  (58%)      (42%)",
"THENGA MYRE coconut like pubic hair  (55%)      (45%)",
"Takkali pooru red hot tomato like pussy  (73%)      (27%)",
"Thaayoli Mother fucker  (75%)      (25%)",
"Thallayoli Mother Fucker  (75%)      (25%)",
"Thalleyoli Mother fucker  (50%)      (50%)",
"Thayoli Mother Fucker  (84%)      (16%)",
"Thayoli idli Salman Khan  (75%)      (25%)",
"Theetam Human feces  (73%)      (27%)",
"Thenga pooru Coconut pussy  (85%)      (15%)",
"Thevadichi Prostitute  (88%)      (12%)",
"Thokolli kalla sami Sandeep  (40%)      (60%)",
"Thukal Kunna Leather penis  (67%)      (33%)",
"Vadam vali English  (28%)      (73%)",
"Vayilitto Suck my dick  (39%)      (61%)",
"Veppatti Bitch / personal prostiute  (77%)      (23%)",
"Viral Iduka Fingering  (76%)      (24%)",
"aan-vedi man whore",
"achante andi dads dick",
"adichu poli enjoy by fucking",
"amminhnha boobs",
"anna kunna big dick",
"appikunna dirty penis",
"arraykku chuttum poorruu ullaval lady having pussy around waist",
"avaraathi a man who like to fuck anywhere",
"avarathi mone mothers dick fucker",
"chalam nakki puss licker",
"coondi bum",
"eli kunna small dick",
"inchi mola young hard boobs",
"johninte andi small shrivelled black balls",
"kaatu poori women with forest pussy",
"kallel oouuki stone fucker",
"kandara oli whore",
"kandi shit",
"kandi theeni a person who eats shit",
"kara vedi local area prostitute",
"karim kunna black dick",
"karim pooran black pussy",
"katta thayoli motherfucking asshole",
"kazhappu perutha mairan hairy dick in a wild mood",
"kodam nakiii ass sucker",
"kotham Ass",
"kotham kalakki fucking hardly through anus",
"kotham nakku lick my ass",
"kuch fart",
"kulamavuka damaged and widened by over fucking",
"kundan gay",
"kundaroli poori mone gay asshole",
"kundimol lady with vibrating ass",
"kunji kunnan man with small pennise",
"kunna penis",
"kunna chappu suck cock",
"kunna urunji dick sucker",
"kunnappal sperm",
"kushukk fart",
"mola boobs",
"moonchikko do suck  (50%)      (50%)",
"mula chappu suck boobs  (77%)      (23%)",
"mula kashakku squeeze boobs  (73%)      (27%)",
"mula mol big boobs girl  (85%)      (15%)",
"nayinte mone Son of a dog  (78%)      (22%)",
"ninde andi maire your dick hair  (67%)      (33%)",
"ninte ammeda tar your moms black cum  (48%)      (52%)",
"ninte ammede pooru your mothers pussy  (71%)      (29%)",
"ninte appante andi your fathers dick  (84%)      (16%)",
"ookki fucked  (55%)      (45%)",
"oomban sucker  (43%)      (57%)",
"oombi mon dick sucker  (62%)      (38%)",
"paara pooru less used hard pussy  (88%) ",
"paareel ookki fucking the rock  (40%)      (60%)",
"paiku vetti fucking the cow  (31%)      (69%)",
"pala thanthakkundaya thaoli son born 2 many fathers  (76%)      (24%)",
"pallinedayil kanthu clitoris sucking  (64%)      (36%)",
"pambara kutichi whore  (84%)      (16%)",
"pampara thayoli fucking mother and rounding  (75%)      (25%)",
"panchavarna kunna a dick with 5 colors  (50%)      (50%)",
"pandi kallan tamil thief  (33%)      (67%)",
"panniyoli pig fucker  (55%)      (45%)",
"para andi oomba other's dick sucker  (57%)      (43%)",
"para thayoli punda mon worst man with puzzy  (58%)      (42%)",
"parii dick  (48%)      (52%)",
"pathala poor deep pussy  (80%)      (20%)",
"patti poori mon a person who have pussy like dog  (70%)      (30%)",
"patty theettam dog shit  (85%)      (15%)",
"pela vedi kandaroli huge whore  (68%)      (32%)",
"petty ass  (63%)      (38%)",
"pola vettu shouting bad words  (50%)      (50%)",
"poochi fuck  (43%)      (57%)",
"poore ennayil tenni veetil poda skid back home in vaginal oil  (48%)      (52%)",
"pooru vagina  (88%)      (12%)",
"poottaavi pussy steam  (69%)      (31%)",
"poottile mathycurry fish curry inside pussy  (79%)      (21%)",
"poyi ninte kunna oombadaa Go suck your dick  (76%)      (24%)",
"poyi oombada go suck a dick man  (67%)      (33%)",
"praa thayolli universal mother fucker  (79%)      (21%)",
"pudti puliyadi half breed mongrel  (71%)      (29%)",
"pundachi mone sone of a bitch  (75%)      (25%)",
"rainayude poore BIGGEST PUSSY in the world  (55%)      (45%)",
"shuklam dheeni sperm eater  (66%)      (34%)",
"shuklam nakki sperm licker  (77%)      (23%)",
"thabala pooran pussy drummer  (86%)      (14%)",
"thakara thayoli BIG damn mother fucker  (73%)      (27%)",
"thayolee mother fucker  (61%)      (39%)",
"thayoli mother fucker  (81%)      (19%)",
"thayoli idli Tamil Motherfucker",
"theetta moran a man whose face like shit",
"theettam shit",
"theettathel ookki fuck with shit",
"umman man who kiss",
"vada navel button on woman",
"vali fart",
"vedi prostitute",
"vedi pura brothel",
        ]
    elif input_str in "waving":
        emoticons = [
            "(ノ^∇^)",
            "(;-_-)/",
            "@(o・ェ・)@ノ",
            "ヾ(＾-＾)ノ",
            "ヾ(◍’౪◍)ﾉﾞ♡",
            "(ό‿ὸ)ﾉ",
            "(ヾ(´・ω・｀)",
        ]
    elif input_str in "wtf":
        emoticons = [
            "༎ຶ‿༎ຶ",
            "(‿ˠ‿)",
            "╰U╯☜(◉ɷ◉ )",
            "(;´༎ຶ益༎ຶ)♡",
            "╭∩╮(︶ε︶*)chu",
            "( ＾◡＾)っ (‿|‿)",
        ]
    elif input_str in "love":
        emoticons = [
            "乂❤‿❤乂",
            "(｡♥‿♥｡)",
            "( ͡~ ͜ʖ ͡°)",
            "໒( ♥ ◡ ♥ )७",
            "༼♥ل͜♥༽",
        ]
    elif input_str in "confused":
        emoticons = [
            "(・_・ヾ",
            "｢(ﾟﾍﾟ)",
            "﴾͡๏̯͡๏﴿",
            "(￣■￣;)!?",
            "▐ ˵ ͠° (oo) °͠ ˵ ▐",
            "(-_-)ゞ゛",
        ]
    elif input_str in "dead":
        emoticons = [
            "(✖╭╮✖)",
            "✖‿✖",
            "(+_+)",
            "(✖﹏✖)",
            "∑(✘Д✘๑)",
        ]
    elif input_str in "sad":
        emoticons = [
            "(＠´＿｀＠)",
            "⊙︿⊙",
            "(▰˘︹˘▰)",
            "●︿●",
            "(　´_ﾉ` )",
            "彡(-_-;)彡",
        ]
    elif input_str in "dog":
        emoticons = [
            "-ᄒᴥᄒ-",
            "◖⚆ᴥ⚆◗",
        ]
    else:    
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "¯\_(ツ)_/¯",
            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
            "ʕ•ᴥ•ʔ",
            "(▀ Ĺ̯▀   )",
            "(ง ͠° ͟ل͜ ͡°)ง",
            "༼ つ ◕_◕ ༽つ",
            "ಠ_ಠ",
            "(☞ ͡° ͜ʖ ͡°)☞",
            "¯\_༼ ି ~ ି ༽_/¯",
            "c༼ ͡° ͜ʖ ͡° ༽⊃",
        ]
    index = random.randint(0, len(emoticons))
    output_str = emoticons[index]
    await event.edit(output_str)