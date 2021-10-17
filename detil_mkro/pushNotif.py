from django.db.models.aggregates import Count
from django.db.models import Max
import requests
import locale
# from channels.db import database_sync_to_async
from .models import DetilMkro
from accounts.models import ExtendUser, kode_kantor
from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings

from telebot import TeleBot


today = datetime.today()
yt = today - timedelta(days=1)


url = "https://api.telegram.org/bot{}/sendMessage".format(settings.BOT_API)

# async def connect(self):
#     self.sendNotif = await database_sync_to_async(self.sendNotif)()

# @database_sync_to_async
def sendNotif():
    users = ExtendUser.objects.filter(is_superuser=False, jabatan_id=5)
    
    qs = DetilMkro.objects.all()
    for user in users:
        datas = qs.filter(tgl_upload__range=(yt,today), kode_pembina=user).order_by('-tgl_upload')
        locale.setlocale(locale.LC_MONETARY,'id_ID')
        if datas.exists():
            qs = datas.values('kode_pembina').annotate(jlh=Count('npp', distinct=True))
            pesan = """
Dear User {}.
Jumlah NPP Update Terakhir adalah :
{}
            """.format(qs['kode_pembina'], qs['jlh'])
            payload = {
                "text":pesan,
                "parse_mode": "HTML",
                "disable_web_page_preview": False,
                "disable_notification": False,
                "chat_id": str(user.id_telegram)
            }
            headers = {
                "Accept": "application/json",
                "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
                "Content-Type": "application/json"
            }

            response = requests.request("POST", url, json=payload, headers=headers)
            print(response.text)
        else:
            datas = qs.filter(kode_pembina=user.username)
            tgl3 = qs.aggregate(Max('tgl_upload'))
            nw = tgl3['tgl_upload__max'].strftime('%Y-%m-%d')
            qs = qs.filter(tgl_upload__range=(nw, tgl3['tgl_upload__max'])).values('kode_pembina').annotate(jlh=Count('npp', distinct=True))
            pesan = """
Dear User {}.
Jumlah NPP Terakhir adalah:
{}

<i>Tgl:{}</i>
            """.format(qs['kode_pembina'], qs['jlh'], nw)
            payload = {
                "text":pesan,
                "parse_mode": "HTML",
                "disable_web_page_preview": False,
                "disable_notification": False,
                "chat_id": str(user.id_telegram)
            }
            headers = {
                "Accept": "application/json",
                "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
                "Content-Type": "application/json"
            }

            response = requests.request("POST", url, json=payload, headers=headers)
            print(response.text)
#             for data in datas:
#                 if data.keps_jp == '' or data.keps_jp == '- ' or data.keps_jp is None:
#                     jp = 'Tidak'
#                 else:
#                     jp = data.keps_jp
#                 if data.blth_na == '' or data.blth_na == '- ' or data.blth_na is None:
#                     blthna = 'Aktif'
#                 else:
#                     blthna = data.blth_na
#                 if data.sipp == 1 or data.sipp == '1':
#                     sipp = 'YA'
#                 else:
#                     sipp = data.sipp
#                 pesan = """
# Berikut Terlampir data terakhir dari
# User <b>{}</b> :

# Nama Pembina : {}
# Nama Perusahaan : {}
# Kepesetaan Awal : {}
# Kepesertaan JP : {}
# Status Aktif : {}
# Jumlah Program : {}
# Total TK Aktif : {}
# Total Iuran Berjalan : <b>{}</b>
# BLTH Rekon Terakhir : {}
# SIPP : {}

# <i>Sumber : MKRO</i>
#                 """.format(data.kode_pembina, data.nama_pembina, data.nama_prsh, data.keps_awal,
#                     jp, blthna, data.prog, data.total_tk_aktif, locale.currency(data.total_iuran_berjalan, grouping=True),
#                         data.blth_akhir, sipp)
                # print(url)
        # payload = {
        #     "text":pesan,
        #     "parse_mode": "HTML",
        #     "disable_web_page_preview": False,
        #     "disable_notification": False,
        #     "chat_id": str(user.id_telegram)
        # }
        # headers = {
        #     "Accept": "application/json",
        #     "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
        #     "Content-Type": "application/json"
        # }

        # response = requests.request("POST", url, json=payload, headers=headers)
        # print(response.text)


def kirim_pesan():
    tgl1 = datetime.today()
    tgl2 = tgl1 - timedelta(days=1)
    td = tgl1.strftime('%Y-%m-%d')
    yt = tgl2.strftime('%Y-%m-%d')

    bot = TeleBot(settings.BOT_API, parse_mode='html')

    users = ExtendUser.objects.filter(jabatan_id=5)
    for user in users:
        
        datas = DetilMkro.objects.filter(kode_pembina=user.username, tgl_upload__range=(yt,td)).values('kode_pembina').annotate(jlh=Count('npp', distinct=True))
        if datas.exists():
            pesan = """
Dear user {}.

Jlh NPP Terkahir update adalah :
{} Perusahaan
            """.format(datas['kode_pembina'], datas['jlh'])
            kirim = bot.send_message(user.id_telegram, pesan)
            assert kirim.message_id
        
        else:
            qs = DetilMkro.objects.filter(kode_pembina=user.username)
            tgl3 = qs.aggregate(Max('tgl_upload'))
            nw = tgl3['tgl_upload__max'].strftime('%Y-%m-%d')
            datas = qs.filter(tgl_upload__range=(nw, tgl3)).values('kode_pembina').annotate(lh=Count('npp', distinct=True))
            pesan = """
Dear user {}.

Jlh NPP Terkahir update adalah :
{} Perusahaan
            """.format(datas['kode_pembina'], datas['jlh'])
            kirim = bot.send_message(user.id_telegram, pesan)
            assert kirim.chat.id