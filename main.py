import interactions
import os 
import platform
import random
import requests
from interactions import *
from myserver import server_on

# $$$$$$$\   $$$$$$\ $$$$$$$$\        $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$\        $$\    $$\   $$\   
# $$  __$$\ $$  __$$\\__$$  __|      $$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\       $$ |   $$ |$$$$ |  
# $$ |  $$ |$$ /  $$ |  $$ |         $$ /  \__|$$ |  $$ |$$ /  $$ |$$ |  $$ |      $$ |   $$ |\_$$ |  
# $$$$$$$\ |$$ |  $$ |  $$ |         \$$$$$$\  $$$$$$$$ |$$ |  $$ |$$$$$$$  |      \$$\  $$  |  $$ |  
# $$  __$$\ $$ |  $$ |  $$ |          \____$$\ $$  __$$ |$$ |  $$ |$$  ____/        \$$\$$  /   $$ |  
# $$ |  $$ |$$ |  $$ |  $$ |         $$\   $$ |$$ |  $$ |$$ |  $$ |$$ |              \$$$  /    $$ |  
# $$$$$$$  | $$$$$$  |  $$ |         \$$$$$$  |$$ |  $$ | $$$$$$  |$$ |               \$  /   $$$$$$\ 
# \_______/  \______/   \__|          \______/ \__|  \__| \______/ \__|                \_/    \______|
                                                                                                    
                                                                                                    
                                                                                                    

                                         # 𝐂𝐨𝐧𝐟𝐢𝐠 
planel_channel = "1269240242364354561"        # Planel Chanel
phone = "0652801573"         # Phone Number
log_channel = "1269274296161927169"        # Log Channel

                                        # 𝐇𝐞𝐚𝐝𝐞𝐫𝐬
title = "𝑪𝒀𝑩𝑬𝑹 𝑩𝑳𝑨𝑪𝑲 🛡☣🔒"
tn = "https://media.discordapp.net/attachments/1245343974475042970/1266435864838541424/1721926083117.png?ex=66a5cc8f&is=66a47b0f&hm=f1444d34aea70aa3eeeaf03a868d77e6592d5ccf0210161b3b65b28df81b0b9b&=&format=webp&quality=lossless&width=416&height=416"  # Small Image
img = "https://media.discordapp.net/attachments/1245343974475042970/1266439634053894214/green-static-background-hacking-zxdixjwjemrjnoen.gif?ex=66a5d012&is=66a47e92&hm=61ddd7ea2777352f364193181d5ded88acb3e5d85d5e3ac66091ae6ffa1a788c&=&width=739&height=416" # Big Image

                                        # 𝐑𝐨𝐥𝐞 𝐂𝐨𝐧𝐟𝐢𝐠
role_01 = "1267504880491171891"                   #ID role
role01_name = "𝑫𝑰𝑺𝑪𝑶𝑬𝑫 𝟏00 𝒁𝑶𝑵𝑬 1"               # ID name
role_01p = "100.00"              # ID Price

role_02 = "1267504954181030032"                   #ID role
role02_name = "𝑫𝑰𝑺𝑪𝑶𝑬𝑫 𝟏00 𝒁𝑶𝑵𝑬 2"              # ID name
role_02p = "100.00"             # ID Price

role_03 = "1267505001128005682"                    #ID role
role03_name = "𝑺𝑹𝑪 𝟏𝟐𝟎"               # ID name
role_03p = "120.00"              # ID Price

role_04 = "1267505064512196679"                   #ID role
role04_name = "𝑺𝒆𝒆 𝒆𝒗𝒆𝒓𝒚 𝒛𝒐𝒏𝒆 150"               # ID name
role_04p = "150.00"              # ID Price


async def on_ready():

                                          # 𝐃𝐞𝐭𝐚𝐢𝐥𝐬
    ch = await Flexzy.fetch_channel(channel_id=planel_channel)
    main_embed = interactions.Embed(title=f"**{title} 𝑻𝒐𝒑 𝒖𝒑 𝒕𝒐 𝒓𝒆𝒄𝒆𝒊𝒗𝒆 𝒓𝒂𝒏𝒌 Angpao Topup🧧**", description="_ _", color=0x00FF00)
    main_embed.add_field(name="╭━━━━━━━━━★", value="\n𝑪𝒀𝑩𝑬𝑹 𝑩𝑳𝑨𝑪𝑲 🛡☣🔒\n💸・ __𝑩𝑼𝒀 𝑹𝑶𝑳𝑬__ เพื่อซื้อยศ\n🌐・ __𝒓𝒂𝒏𝒌 𝒑𝒓𝒊𝒄𝒆__ เพื่อดูราคายศ\n╰━━━━━━━━━★")
    main_embed.set_thumbnail(tn) 
    main_embed.set_image(img)
    main_embed.set_footer("")

    topup = Button(
        style=ButtonStyle.RED,
        custom_id="topup_cb",
        label="💸 𝑩𝑼𝒀 𝑹𝑶𝑳𝑬",
    )
    
    all = Button(
        style=ButtonStyle.RED,
        custom_id="all_cb",
        label="🌐 𝒓𝒂𝒏𝒌 𝒑𝒓𝒊𝒄𝒆",
    )

    await ch.send(embeds=main_embed, components=[topup, all])


    if platform.system() == 'Windows':

        os.system(f'cls & title {title} [ Working....]')
        print(" ")
        print(f"{title} [ Working.... ]")
        print(" ")
    
    else:

        os.system("clear")
        print(" ")
        print(f"{title} [ Working.... ]")
        print(" ")

@interactions.listen()
async def on_component(event: BaseComponent):

    ctx = event.ctx

    match ctx.custom_id:
        case "topup_cb":
            select_plan = StringSelectMenu(
                [
                    interactions.StringSelectOption(label="เติมเงิน", emoji="🧧", value="test"),
                ],
                placeholder="🟢 เติมเงินตามจำนวนราคายศ",
                min_values=1,
                max_values=1,
            )

            await ctx.send(components=select_plan, ephemeral=True)
            def check(component: Button) -> bool:
                return component.ctx.author.id == ctx.author.id

            try:

                used_component = await Flexzy.wait_for_component(components=select_plan, check=check, timeout=30)
                used_ctx = used_component.ctx
                rolebuy = used_ctx.values[0]
                topup_modal = Modal(
                    ShortText(
                    label="Wallet angpao Topup services",
                    custom_id="giftLink",
                    required=True,
                    placeholder="กรุณาใส่ลิ้งค์ซอง เช่น https://gift.truemoney.com/campaign/?v=XXXXXXXXXXXXXXX!",
                    max_length=80,
                    ),
                    title="🧧 เติมเงินตามจำนวนราคายศ!",
                )
                await used_ctx.send_modal(modal=topup_modal)
                modal_ctx: ModalContext = await used_ctx.bot.wait_for_modal(topup_modal)
                giftLink = modal_ctx.responses['giftLink']
                auth = requests.get(f"https://zamex-hub.000webhostapp.com/index.php?phone={phone}&link={giftLink}")
                flexzy = auth.json()

                if flexzy["status"] == "SUCCESS":

                    if flexzy["amount"] == role_01p:

                        role_01s = interactions.Embed(title=f"**{title} Success ( 1 )**", description="_ _", color=0x92f0a3)
                        role_01s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_01s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_01}>\n_ _\n")
                        role_01s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@{role_01p}>\n_ _\n")
                        await ctx.send(embeds=role_01s, ephemeral=True)
                        log_01 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_01eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_01eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_01eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_01}>\n_ _\n_ _")
                        await log_01.send(f"<@{ctx.author.id}>", embeds=log_01eb)

                    elif flexzy["amount"] == role_02p:

                        role_02s = interactions.Embed(title=f"**{title} Success ( 2 )**", description="_ _", color=0x92f0a3)
                        role_02s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_02s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_02}>\n_ _\n")
                        role_02s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@_{role_02p}>\n_ _\n")
                        await ctx.send(embeds=role_02s, ephemeral=True)
                        log_02 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_02eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_02eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_02eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_02}>\n_ _\n_ _")
                        await log_02.send(f"<@{ctx.author.id}>", embeds=log_02eb)

                    elif flexzy["amount"] == role_03p:

                        role_03s = interactions.Embed(title=f"**{title} Success ( 3 )**", description="_ _", color=0x92f0a3)
                        role_03s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_03s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_03}>\n_ _\n")
                        role_03s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@{role_03p}>\n_ _\n")
                        await ctx.send(embeds=role_03s, ephemeral=True)
                        log_03 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_03eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_03eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_03eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_03}>\n_ _\n_ _")
                        await log_03.send(f"<@{ctx.author.id}>", embeds=log_03eb)

                    elif flexzy["amount"] == role_04p:

                        role_04s = interactions.Embed(title=f"**{title} Success ( 4 )**", description="_ _", color=0x92f0a3)
                        role_04s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_04s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_04}>\n_ _\n")
                        role_04s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <&{role_04p}>\n_ _\n")
                        await ctx.send(embeds=role_04s, ephemeral=True)
                        log_04 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_04eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_04eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_04eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_04}>\n_ _\n_ _")
                        await log_04.send(f"<@{ctx.author.id}>", embeds=log_04eb)

                    elif flexzy["amount"] == role_05p:

                        role_05s = interactions.Embed(title=f"**{title} Success ( 5 )**", description="_ _", color=0x92f0a3)
                        role_05s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_05s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_05}>\n_ _\n")
                        role_05s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@{role_05p}>\n_ _\n")
                        await ctx.send(embeds=role_05s, ephemeral=True)
                        log_05 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_05eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_05eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_05eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_05}>\n_ _\n_ _")
                        await log_05.send(f"<@{ctx.author.id}>", embeds=log_05eb)

                    elif flexzy["amount"] == role_06p:

                        role_06s = interactions.Embed(title=f"**{title} Success ( 6 )**", description="_ _", color=0x92f0a3)
                        role_06s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_06s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: <@&{role_06}>\n_ _\n")
                        role_06s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: <@{role_06p}>\n_ _\n")
                        await ctx.send(embeds=role_06s, ephemeral=True)
                        log_06 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_06eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_06eb.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ !\n_ _\n_ _")
                        log_06eb.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`❓`: <@&{role_06}>\n_ _\n_ _")
                        await log_06.send(f"<@{ctx.author.id}>", embeds=log_06eb)

                    else:

                        role_07s = interactions.Embed(title=f"**{title} Success ( 7 )**", description="_ _", color=0xf59300)
                        role_07s.add_field(name="> สถานะ", value="_ _\n`✅`: ซื้อยศสำเร็จ\n_ _\n")
                        role_07s.add_field(name="> ยศที่ได้รับ", value=f"_ _\n`🎗️`: ไม่พบยศ !\n_ _\n")
                        role_07s.add_field(name="> จำนวนเงิน", value=f"_ _\n`💸`: ไม่สามารถดึงค่าได้ !\n_ _\n")
                        await ctx.send(embeds=role_07s, ephemeral=True)
                        log_07 = await Flexzy.fetch_channel(channel_id=log_channel)
                        log_07eb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0x75ffb1)
                        log_07eb.add_field(name="> สถานะ", value="_ _\n`❗`: เติมเงินเกินกว่าที่ระบบตั้งไว้ !\n_ _\n_ _")
                        await log_07.send(f"<@{ctx.author.id}>", embeds=log_07eb)

                else:

                    print("Fail")
                    fail = interactions.Embed(title=f"**{title} Fail**", description="_ _", color=0xf50049)
                    fail.add_field(name="> สถานะ", value="_ _\n`❌`: เติมเงินไม่สำเร็จ\n_ _\n")
                    await ctx.send(embeds=fail, ephemeral=True)
                    fail_x = await Flexzy.fetch_channel(channel_id=log_channel)
                    faileb = interactions.Embed(title=f"**{title} Log**", description="_ _", color=0xff004c)
                    faileb.add_field(name="> สถานะ", value="_ _\n`❌`: เติมเงินไม่สำเร็จ\n_ _\n_ _")
                    await fail_x.send(f"<@{ctx.author.id}>", embeds=faileb)
                        
            except TimeoutError:

                print("หมดเวลา")

        case "all_cb":

            role_all = interactions.Embed(title=f"**{title} Role**", description="_ _", color=0x21E9FC)
            role_all.set_thumbnail ("https://media.discordapp.net/attachments/1245343974475042970/1266437700911628433/1722012655866.png?ex=66a5ce45&is=66a47cc5&hm=7550cfd56c3d2b64e017f3dbbfff1d0e7bec75d92a084319a92fe8e4bcc5f3fb&=&format=webp&quality=lossless&width=416&height=416")  # Small Image
            role_all.set_image ("https://media.discordapp.net/attachments/1245343974475042970/1266435864838541424/1721926083117.png?ex=66a523cf&is=66a3d24f&hm=44ef8d0c466d4d76b5d6d3b5cc1d4578d35eb26578bf5b99d08e560d1f7c7c2c&=&format=webp&quality=lossless&width=416&height=416") # Big Image
            role_all.add_field(name=f"・ยศ {role01_name}", value=f"\nยศที่ได้รับ <@&{role_01}>\n✼ •• ┈┈┈┈┈┈┈┈┈┈┈┈ •• ✼\nราคา `💸`: `{role_01p}`\n\n")
            role_all.add_field(name=f"・ยศ {role02_name}", value=f"\nยศที่ได้รับ <@&{role_02}>\n✼ •• ┈┈┈┈┈┈┈┈┈┈┈┈ •• ✼\nราคา `💸`: `{role_02p}`\n\n")
            role_all.add_field(name=f"・ยศ {role03_name}", value=f"\nยศที่ได้รับ <@&{role_03}>\n✼ •• ┈┈┈┈┈┈┈┈┈┈┈┈ •• ✼\nราคา `💸`: `{role_03p}`\n\n")
            role_all.add_field(name=f"・ยศ {role04_name}", value=f"\nยศที่ได้รับ <@&{role_04}>\n✼ •• ┈┈┈┈┈┈┈┈┈┈┈┈ •• ✼\nราคา `💸`: `{role_04p}`\n\n")

            role_all.set_footer("Copyright ©  2023 , All right reserved discord.gg/CYBER BLACK")

            await ctx.send(embeds=role_all, ephemeral=True)

server_on()

Flexzy.start(os.getenv('token'))

# Copyright ©  2023 , All right reserved discord.gg/flexzy