import requests
import locale
from .models import DetilMkro
from accounts.models import ExtendUser
from datetime import timedelta
from django.utils import timezone
from django.conf import settings


today = timezone.localtime(timezone.now())
yt = today - timedelta(days=1)
yt_t = yt + timedelta(days=2)

url = "https://api.telegram.org/bot{}/sendMessage".format(settings.BOT_API)

def sendNotif():
    users = ExtendUser.objects.filter(is_superuser=False)
    
    qs = DetilMkro.objects.all()
    for user in users:
        datas = qs.filter(tgl_upload__range=(yt,today))
        locale.setlocale(locale.LC_MONETARY,'id_ID')
        if datas.exists():
            for data in datas:
                if data.keps_jp == '' or data.keps_jp == '- ' or data.keps_jp is None:
                    jp = 'Tidak'
                else:
                    jp = data.keps_jp
                if data.blth_na == '' or data.blth_na == '- ' or data.blth_na is None:
                    blthna = 'Aktif'
                else:
                    blthna = data.blth_na
                if data.sipp == 1 or data.sipp == '1':
                    sipp = 'YA'
                else:
                    sipp = data.sipp
                pesan = """
Berikut Terlampir data terakhir dari
User <b>{}</b> :

Nama Pembina : {}
Nama Perusahaan : {}
Kepesetaan Awal : {}
Kepesertaan JP : {}
Status Aktif : {}
Jumlah Program : {}
Total TK Aktif : {}
Total Iuran Berjalan : <b>{}</b>
BLTH Rekon Terakhir : {}
SIPP : {}

<i>Sumber : MKRO</i>
                """.format(data.kode_pembina, data.nama_pembina, data.nama_prsh, data.keps_awal,
                    jp, blthna, data.prog, data.total_tk_aktif, locale.currency(data.total_iuran_berjalan, grouping=True),
                        data.blth_akhir, sipp)
                # print(url)

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