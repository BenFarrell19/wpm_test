import requests
import json


def flag_errors(text):
    r = requests.post("https://grammarbot.p.rapidapi.com/check",

                      data={'text': text, 'language': 'en-US'},

                      headers={

                          'x-rapidapi-host': "grammarbot.p.rapidapi.com",

                          'x-rapidapi-key': "68396592damshf48a2597196fb41p18a805jsn561f963e6d76",

                          'content-type': "application/x-www-form-urlencoded"

                      })
    j = r.json()
    new_text = ''
    cursor = 0
    for match in j["matches"]:
        offset = match["offset"]
        length = match["length"]
        if cursor > offset:
            continue
        # build new_text from cursor to current offset
        new_text += text[cursor:offset]
        # next add **word**
        new_text += "**" + text[offset:(offset + length)] + "**"
        # update cursor
        cursor = offset + length

    # if cursor < text length, then add remaining text to new_text
    if cursor < len(text):
        new_text += text[cursor:]
    return new_text


def auto_correct_text(text):
    r = requests.post("https://grammarbot.p.rapidapi.com/check",

                      data={'text': text, 'language': 'en-US'},

                      headers={

                          'x-rapidapi-host': "grammarbot.p.rapidapi.com",

                          'x-rapidapi-key': "68396592damshf48a2597196fb41p18a805jsn561f963e6d76",

                          'content-type': "application/x-www-form-urlencoded"

                      })
    j = r.json()
    new_text = ''
    cursor = 0
    for match in j["matches"]:
        offset = match["offset"]
        length = match["length"]
        if cursor > offset:
            continue

        # build new_text from cursor to current offset
        new_text += text[cursor:offset]
        # next add first replacement
        repls = match["replacements"]
        if repls and len(repls) > 0:
            new_text += repls[0]["value"]
        # update cursor
        cursor = offset + length
# if cursor < text length, then add remaining text to new_text
    if cursor < len(text):
        new_text += text[cursor:]
    return new_text

a = auto_correct_text('''typing testenterKey.alt_lKey.tabTiny posiosison dart frogs may be only one inch long but they pack a powerful punch of poison. Weighing less than an onceounce, these frongs are occonsidered one of Earth;'s most toxic species. For example, the golden poison dart frong has enough poison to kill 20,000 mice. With a range of bright colors., yellows, oranges, reds, greens, and blues, they aren't just a big big show-offs, either. Those colorful designs tell potential predators, Key.shift_r"I'm toxic ; don;yn't eat me.Key.shift_r" Scientists vbelieceve theat poison dart frogs get their tocivxicity from some of the insects they eat. The insects feed on plants that have towzxins., which they then pass on to the frogs who fed on them. Poison dart frongs gs raised in captivity aren't toxic because the insects they are fed haven;'t eaten poisonous plants. Ho wdo pow do posioison dart frogs capture their prayKey.shift_r?eyKey.shift_r? With a long., sticky tongue that darts out and zaps the unsuspecting bugKey.shift_r! thThe frogs eat many kinds of small insects, including fruit flies , ants, and ting y beetles, which are the ones scientists think may be resposnsible for the frogs' toxicity, .enterPOsiosionoison dart frgorogs live in the rain forest s of cenCentral and soSOuouth AMermerica and breed during the rainy season,, . To attract a female, the maelale frog call fros from a lead,f., making buzzing or trilling sounds/. After he's attracted a mate and she lays her ae eggs, the malle stics around cks around to make sure the egss sgs stay mosit unoist until they hatch . Once the little ones hatch as tiny tadpoles, they wiggle on to the male's back/. He carries them to a pool of water where the tadpoles wiggle off and complete their metamorphoisis into fully - formed frogs/.enterIN n today;\y's increaseingly hectic and tstressful world, getting a spa treatment is sometimes one of the most therapeutic things an indicuividual can enjoy. The relaxation and peaceful environment assoicciated with a spa can allow a person to gregain their sense of self and feelin orf g of overall peace. From suntanning to massages and other therapeutic modalities, spas offer a unique opporutunity to re-energize and reinvirogorate the himuman. bo body. Becasyysuse spa treatments are becoming so popular, today there is an increasing number of spas that now offer flay tt montlhthly-fee-based services. This type of service makes good sense for those wishing to make spa treatments a regular and routine part of their life. Carbon dioxide is a chemical compunpound that is usually in the form of a ga.s. It is made up of one atom of carbon and two atoms of oxtygen.enter. enterCarbon dioxide was discovered by a Belgian chemist namded janJan Baptistan c cvan Helmont. Carbon Didioxide is necceecessayry for life on Earth, . hWHenhen animals breathe out, they release carbon dioxide into the air. pPlants use this carbon dioxide to make their own food in a procceess called photosynthesis. plPlants then prelease oxygen in to the air for animals to breathe in. Carbon dioxide also is an essential part of Earth;\'s atomosphere .. I t plays an important role  as a rgreenhouse gas. A green house house gas traps energy from the Sun, which warms aEarth's sufrface. THihis is know as n as the greenhouse aeffect. SAt only a few incheslong and whiwith no distinctive external features to speak of . , the Hero sSherew is seemingly an unremarkable creature. That is , until you accidentally step one one,. You esee, the hHero sShrew can comfortablu sy survive being stood on by a typical aduilt lt human without any injuy.ury. The secret to this skill lies in the Shrew;'s skeletal system or , more specifically, its spine, . nUNlinlike almost every other mammal on Earhtth, with on note notalble exception which weenter'll get to in a monment. , the Hero sSherew's spine features intricate interlocking vertabrebrae, a very large number of spinal processes. , and is incredibly thick''')

#flag_errors("Aesop was on eof the great deldeldeldeldeldeldeldeldeldeldeldeldeldeldele of the great Greek wirters. He is best know for his fables, stories that have a moral. They teach us something about how we should live our lives. Aesop wrote thousands of these strories del. Here are a fwdelew.enterThe Wolf in Sheepsdel's ClothingenterONce uodelpon a time, a wolf decideddeldeldeldeldeldeldeldeldeldeldeldeldel wolf decided to disguiesdeldelse the way he looked. He thought it would help huimdeldeldeliomdeldelm get del food more easibdelly tdelhe deldeldeldel. He put on the skin of a sheep, then he went out with the wlocdeldeldeldelflock into the pasture del. Even the shepherd was fooled by his clever costume. In the eveing ,deldel, the shedelepherd put him in with the rest of the sheep. He closed the gamdelte and made sure it was edelsecure before he went to bed ideldel. In the middle of the night, he came back to the fold to get some meat for the next day, Instead of a sheep though hdel,")
json.dump(a, open('corrected', 'w'))

