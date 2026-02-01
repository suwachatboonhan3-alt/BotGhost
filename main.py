import discord
from discord.ext import commands
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
import asyncio
import discord
from discord.ext import commands
from server import server_on
import os


bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None  # ⬅️ ปิด help เดิม
)

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Game(name="ร้านเปิด 12.00-04.00 ทุกวัน")
    )
    print(f"Logged in as {bot.user}")

@bot.command()
async def windows(ctx):
    message = (
        "🔔 **สนใจเป็น Windows ตัวไหนดีครับ ** 🔔\n\n"
        "💰 **ราคา**\n"
        "• 69 บาท\n"
        "• 89 บาท\n"
        "• 119 บาท\n\n"
        "1️⃣ ใช้งานแบบไหนเป็นหลัก\n"
        "👉 เล่นเกม / ทำงาน \n"
        "2️⃣ ต้องการแอนตี้ไวรัส หรือระบบสแกนไวรัสมั้ย\n\n"
        "⚠️ ตอนนี้ลูกค้าใช้ Windows 10 หรือ Windows 11\n"
        "📩 ตอบกลับมาได้เลย เดี๋ยวแนะนำตัวที่เหมาะให้ครับ 😊"
    )
    await ctx.send(message)

class WindowsView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(WindowsSelect())

class WindowsSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="🎮 เล่นเกม100%", value="เล่นเกม100%"),
            discord.SelectOption(label="💼 ทำงาน50%เล่นเกม50%", value="ทำงาน50%เล่นเกม50%"),
            discord.SelectOption(label="📝 อื่นๆ", value="อื่นๆ"),
        ]
        super().__init__(
            placeholder="เลือกการใช้งานหลัก",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(
            WindowsModal(self.values[0])
        )


class WindowsModal(discord.ui.Modal, title="📋 แบบสอบถาม Windows"):

    current_win = discord.ui.TextInput(
        label="ตอนนี้ใช้ Windows 10 หรือ 11",
        placeholder="พิมพ์ 10 หรือ 11",
        required=True
    )

    antivirus = discord.ui.TextInput(
        label="ต้องการ Anti-virus / สแกนไวรัส มั้ย",
        placeholder="เช่น ต้องมี / ไม่มีก็ได้",
        required=True
    )

    office = discord.ui.TextInput(
        label="ใช้ Word / Excel มั้ย",
        placeholder="เช่น ใช้ / ไม่ใช้ / ใช้นิดหน่อย",
        required=True
    )

    other = discord.ui.TextInput(
        label="อื่นๆ (ถ้ามี)",
        placeholder="รายละเอียดเพิ่มเติม",
        required=False
    )

    def __init__(self, usage):
        super().__init__()
        self.usage = usage

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🧾 Ghost Windows",
            color=0x00FFCC
        )

        embed.add_field(name="🖥️ การใช้งาน", value=self.usage, inline=False)
        embed.add_field(name="📄 Word / Excel", value=self.office.value, inline=False)
        embed.add_field(name="🛡️ Anti-virus", value=self.antivirus.value, inline=False)
        embed.add_field(name="🪟 Windows ปัจจุบัน", value=self.current_win.value, inline=False)
        embed.add_field(name="✍️ อื่นๆ", value=self.other.value or "-", inline=False)
        embed.add_field(name="👤 ผู้ใช้", value=interaction.user.mention, inline=False)

        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(
            "💜 รอแอดสักครู่",
            ephemeral=True
        )

@bot.command()
async def x(ctx):
    embed = discord.Embed(
        title="🛒 Ghost Store",
        description=(
            "✨ **ค่าขาว 100%** | 🔍 *เช็คเจอไม่โดนแบน*\n\n"
            "💻 **สนใจ Window ตัวไหนดีครับ 69 89 119**\n"
            "✅ **มีทั้ง 10 และ 11**\n"
            "✅ **มี Window ปกติ / Kernel / Ghost / Ltsc และอื่นๆ**\n"
            "```"
            "👻พิม !w เพื่อระบุการใช้งาน\n"
            "🙏 รบกวนตอบตาม คำถามนี้นะครับ จะได้แนะนำถูก 🙏\n\n"
            "```"
        ),
        color=0x00FFCC
    )

    # รูปหลัก
    embed.set_image(
        url="https://img5.pic.in.th/file/secure-sv1/paymenta7d69a4cd090e33d.png"
    )

    embed.add_field(
        name="📌 ส่วนอาวุธ",
        value=(
            "🔹 <#1416841530357977099> **89 บาท** \n"
            "รีวิว<#1422508427501895730> \n\n"
            "🔹 <#1426288585794912426> **109 บาท**\n"
            "รีวิว<#1431373793569542195>\n\n"
            "🔹 <#1436001859415445504> **138 บาท**\n"
            "รีวิว<#1441382238737404026>\n\n"
            "🔹<#1449746151254523934> **179 บาท**\n"
            "รีวิว<#1460341576579547217>\n\n"
        ),
        inline=False
    )

    # footer
    await ctx.send(
        content="@everyone",
        embed=embed

    )

@bot.command()
async def work(ctx):
    message = (
                    "📖 **วินเล่นเกม50% ทำงาน50%**\n\n"
                    "🥉 `!LTSC` – 69บาท ไม่มีแฟรชไดฟ์ +10\n"
                    "🏆 `!LTSC + atlast` – 119บาท ไม่มีแฟรชไดฟ์ +10\n\n"
                )
    await ctx.send(message)

@bot.command()
async def w(ctx):
    embed = discord.Embed(
        title="🖥️ แบบสอบถาม Windows",
        description="กรุณาเลือกตัวเลือกด้านล่าง",
        color=0x00FFCC
    )
    await ctx.send(embed=embed, view=WindowsView())

server_on()

TOKEN = os.getenv("DISCORD_TOKEN")

