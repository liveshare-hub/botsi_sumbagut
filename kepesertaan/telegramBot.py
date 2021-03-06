# from threading import local
from django.db.models.aggregates import Count, Sum
from django.db.models import Q, Max
import telebot, locale
import requests, json
from datetime import datetime
from channels.db import database_sync_to_async
from django.conf import settings
from accounts.models import ExtendUser, kode_kantor, m_bidang, m_jabatan
from detil_mkro.models import DetilMkro
from detil_mkro.rupiah import rupiah_format
from kepesertaan.fungsi import generateUniqueCode

from telebot import apihelper

from datetime import datetime, timedelta

from .decorators import restricted

import schedule
import time

apihelper.ENABLE_MIDDLEWARE = True
apihelper.SESSION_TIME_TO_LIVE = 5 * 60

bot = telebot.TeleBot(settings.BOT_API, parse_mode='html')
url = "http://localhost:8000/graphql"


# qs = ExtendUser.objects.all()
async def connect(self):
    self.message = await database_sync_to_async(self.rekapProg)()
    self.rekapbuskala = await database_sync_to_async(self.rekapbuSkala)()
    self.rekapbu = await database_sync_to_async(self.rekapbu)()
    self.rekapburekon = await database_sync_to_async(self.rekapbpurekon)()
    self.infodetil = await database_sync_to_async(self.infoDetil)()
    self.profile = await database_sync_to_async(self.profile)()
    self.infoall = await database_sync_to_async(self.infoall)()
    self.updatedata = await database_sync_to_async(self.updateData)()
    self.authtoken = await database_sync_to_async(self.authToken)()
    self.masuk = await database_sync_to_async(self.masuk)()
    self.daftar = await database_sync_to_async(self.newRegister)()

@bot.message_handler(commands=['start',])
def start(message):
    # print(message)
    nama_dpn = message.chat.first_name
    pesan = """
Selamat datang <b>{}</b>.

Silahkan ketik /help untuk menu bantuan.
    """.format(nama_dpn)
    bot.send_message(message.chat.id, pesan)

@database_sync_to_async
@bot.message_handler(commands=['register'])
def newRegister(message):
    user = message.chat.id
    
    texts = message.text.split(' ')
    if len(texts) < 2:
        
        bot.send_message(message.chat.id,"Email/Username/Password are missing!")
    else:
        email = texts[1]
        username = texts[2]
        password1 = texts[3]
        password2 = texts[4]
        qs = ExtendUser.objects.filter(id_telegram=message.chat.id)
        if qs.exists():
            bot.send_message(user, "Anda tidak dapat mendaftarkan akun lagi!")
        else:
            if password1 == password2:
                ExtendUser.objects.create(email=email, username=username, password=password1, id_telegram=message.chat.id)
                try:
                    qs = ExtendUser.objects.filter(username=username)[0]
                    token = generateUniqueCode()
                    pesan = """
Akun <b>{}</b> sudah berhasil didaftarkan.
Berikut token anda :

<pre>{}</pre>

Kemudian verifikasi dengan cara:
/token token_anda
Terima Kasih
                    """.format(username, token)
                    bot.send_message(message.chat.id, pesan)
                except:
                    pass
                    
#             query = """
# mutation{
# register(email:"%s",username:"%s", password1:"%s", password2:"%s")
# {
# token
# refreshToken
# success
# errors

# }
# }
#             """ % (email, username, password1, password2)

#             post_json = requests.post(url, json={'query':query})
#             json_data = json.loads(post_json.text)
#             print(json_data)
#             if post_json.status_code == 200:
#                 try:
#                     qs = ExtendUser.objects.filter(username=username)[0]
#                     token = qs.token_auth
#                     data = json_data['data']['register']
#                     if data['success'] == True:
#                         pesan = """
# Akun <b>{}</b> sudah berhasil didaftarkan.
# Berikut token anda :

# <pre>{}</pre>

# Kemudian verifikasi dengan cara:
# /token token_anda
# Terima Kasih
#                         """.format(username, token)

#                         bot.send_message(user, pesan)
#                     else: 
#                         bot.send_message(message.chat.id, "user anda belum terdaftar")
#                 except:
#                     pesan = """
# Pendaftaran user gagal!
# Periksa kembali user anda
# Atau hubungi IT Kanwil.

# Terima Kasih
#                     """
#                     bot.send_message(message.chat.id, pesan)
        

@database_sync_to_async
@bot.message_handler(commands=['login'])
def masuk(message):
    texts = message.text.split(' ')
    if len(texts) < 2:
        bot.send_message(message.chat.id,"Format Salah")
    else:
        username = texts[1]
        password = texts[2]
        qs = ExtendUser.objects.filter(username=username, password=password)[0]
        if qs:

#         query = """
# mutation{
#   tokenAuth(username:"%s",password:"%s") {
#     token
#     success
#     errors
#     unarchiving
#     refreshToken
#   }
# }

#         """ % (username, password)
#         post_json = requests.post(url, json={'query':query})
#         json_data = json.loads(post_json.text)
#         data = json_data['data']['tokenAuth'] 
#         if data['success'] == True:
            pesan = """
Anda sudah berhasil Login!.
Silahkan anda melakukan update akun
dengan cara:
/update <b>username id_bidang id_jabatan id_kantor</b>

contoh : /update MU150710 1 1 1

<i>**cek menu /help untuk melihat id masing-masing di atas</i>


        """
            # obj, created = ExtendUser.objects.update_or_create(username=username, defaults={'token_auth':data['token'], 'id_telegram':message.chat.id})
            bot.send_message(message.chat.id, pesan)

@database_sync_to_async
@bot.message_handler(commands=['token'])
def authToken(message):
    
    texts = message.text.split(' ')
    if len(texts) < 2:
        bot.send_message(message.chat.id, "Format Salah!")
    else:
        kd_token = texts[1]
        qs = ExtendUser.objects.filter(id_telegram=message.chat.id)[0]
        try:
            ExtendUser.objects.update_or_create(username=qs.username, defaults={'token_auth':kd_token})
            pesan = """
Akun adan sudah Terverifikasi!
            """
            bot.send_message(message.chat.id, pesan)
        except:
            bot.send_message(message.chat.id,"Akun Salah!")
#         query = """
# mutation{
#   verifyToken(
#     token:"%s"
#   ) {
#     success
#     errors
#   }
# }
#         """ % (kd_token)

        # qs = ExtendUser.objects.filter(token_auth=kd_token)
        # username = qs[0].username
        # if not qs or qs is None:
        #     bot.send_message(message.chat.id, "Token Expired!")
        # else:
        #     qs.update_or_create(username=username, defaults={'id_telegram':message.chat.id})
        #     bot.send_message(message.chat.id,"Token anda sudah terverifikasi")

@bot.message_handler(commands=['help'])
def help(message):
    
    texts = message.text.split(' ')
    
    if len(texts) < 2 and texts[0] == '/help':
        pesan = """
Menu Bantuan:

/help cek_id - menampilkan id telegram
/help list_jabatan - menampilkan id dan nama Jabatan
/help list_bidang - menampilkan id dan nama Bidang
/help list_kantor - menampilkan id dan nama Kantor

Cara Mendaftarkan akun :
/register email username password1 password2

<b>**</b><i>password1 harus sama dengan password2</i>

contoh :
/register my_email@email.com MU150710 Welcome1 Welcome1

Verifikasi token :
/token token_anda

Cara login:
/login username password
contoh: /login MU150710 Welcome1

Update Akun :
Setelah berhasil login <b>di WAJIBKAN</b>
bagi anda untuk melakukan update akun
seperti jabata, bidang, kode kantor dan id telegram

/update <b>username id_jabatan id_bidang id_kantor</b>
contoh : /update MU150710 1 1 1

Menampilakn Profile Akun:
/profile

Menampilkan report MKRO by NPP per pembina:
/infoAll npp_binaan_anda
contoh /infoAll AA020015

Menampilkan report detil NPP per pembina:
/infoDetil npp
contoh : /infoDetil AA020015

Menampilkan report Rekon pertahun bulan berjalan per pembina:
/REKAPBUREKON tahun
contoh : /REKAPBUREKON 2021

Menampilkan report Rekon pertahun bulan berjalan per Cabang:

/REKAPBU tahun
contoh : /REKAPBU 2021
<i>**Untuk Kepala/Kabid</i>

Menampilkan report Rekap Skala Badan Usaha Percabang dan atau Perpembina:

/REKAPBUSKALA

Menampilkan report Rekap Program Kepesertaan Badan Usaha Percabang dan atau Per Pembina:

/REKAPBUPROG


Terima Kasih
        """
        bot.send_message(message.chat.id, pesan)
    else:
        if texts[1] == 'cek_id':
            user = message.chat.id
            pesan = "ID Telegram anda adalah {}".format(user)
            bot.send_message(user, pesan)
        elif texts[1] == 'list_jabatan':
            bot.send_message(message.chat.id, "Daftar Jabatan: \n")
            query = m_jabatan.objects.all().order_by('id')
            if query is not None:
                for q in query:
                    pesan = """
{}. {}
                    """.format(q.id, q.nama_jabatan)
#             query = """
# query{
#   allJabatan{
#     id
#     namaJabatan
#   }
# }
#         """
#             post_json = requests.post(url, json={'query':query})
#             json_data = json.loads(post_json.text)
#             data = json_data['data']['allJabatan']
#             for i in range(0,len(data)):
#             # jabatan = ''.join(data[i])
            
#                 pesan = """

# {} - {}
     

#                 """.format(data[i]['id'],data[i]['namaJabatan'])
        # % (jabatan['id'], jabatan['namaJabatan'])
                    bot.send_message(message.chat.id, pesan)
        elif texts[1] == "list_bidang":
            query = m_bidang.objects.all().order_by('id')
            if query is not None:
                bot.send_message(message.chat.id, "Daftar Bidang: \n")
                for q in query:
                    pesan = """
{}. {}
                    """.format(q.id, q.nama_bidang)
#             query = """
# query{
#     allBidang {
#         id
#         namaBidang
#         }
# }
#         """
            # post_json = requests.post(url, json={'query':query})
            # json_data = json.loads(post_json.text)
            # data = json_data['data']['allBidang']
            # for i in range(0, len(data)):
            #     pesan = "{} - {}".format(data[i]['id'], data[i]['namaBidang'])
                    bot.send_message(message.chat.id, pesan)
    
        elif texts[1] == "list_kantor":
            bot.send_message(message.chat.id,"Daftar Kantor Cabang Kanwil Sumbagut:")
            query = kode_kantor.objects.all().order_by('kd_kantor')
            if query is not None:
                for kantor in query:
                    pesan = """

{}.{} - {}

                    """.format(kantor.id, kantor.kd_kantor, kantor.nama_kantor)
#             query = """
# query{
#   allKodeKantor {
#     id
#     namaKantor
#     kdKantor
#   }
# }
#         """
            # post_json = requests.get(url, json={'query':query})
            # json_data = json.loads(post_json.text)
            # data = json_data['data']['allKodeKantor']
            # for i in range(0, len(data)):
            #     pesan = "{}. {} - {}".format(data[i]['id'],data[i]['kdKantor'],data[i]['namaKantor'])
                    bot.send_message(message.chat.id, pesan)
        else:
            bot.send_message(message.chat.id, "Menu belum terseida !")
@database_sync_to_async
@bot.message_handler(commands=['update'])
def updateData(message):

    texts = message.text.split(' ')
    if len(texts) < 2:
        pesan = """"
Format Perintah anda salah!

Format seharusnya :
/update username id_bidang id_jabatan id_kdKantor

contoh :
id bidang TI = 7
id jabatan staff = 5
id kantor 901 = 1

/update MU150710 7 5 1

<b>**</b><i>botsi sumbagut</i>
        """
        bot.send_message(message.chat.id, "Format Perintah Salah!")
        bot.send_message(message.chat.id, "/update ")
    else:
        username = texts[1]
        try:
            qs = ExtendUser.objects.filter(username=username)[0]
            if qs.updated:
                bot.send_message(message.chat.id, "Update data hanya bisa sekali!")
            
            else:
                bidang = int(texts[2])
                jabatan = int(texts[3])
                kdKantor = int(texts[4])
                ExtendUser.objects.update_or_create(username=username, defaults={'bidang_id':bidang, 'jabatan_id':jabatan,'kd_kantor_id':kdKantor})
                pesan = """
Data user <b>{}</b> berhasil diupdate.

Kantor : {} - {}

Jabatan : {}

Bidang : {}
                """.format(qs.username, qs.kd_kantor.kd_kantor, qs.kd_kantor.nama_kantor, qs.jabatan.nama_jabatan, qs.bidang.nama_bidang)
                bot.send_message(message.chat.id, pesan)
            
        except:
            pass
                # idTelegram = str(message.chat.id)
#                 query = """
# mutation{
#   updateUser(id:%d, bidang:%d, jabatan:%d, kdKantor:%d){
#     users{
#       id
#       username
#       bidang{
#         id
#         namaBidang
#       }
#       jabatan{
#         id
#         namaJabatan
#       }
#       kdKantor{
#         id
#         namaKantor
#         kdKantor
#       }
#     }
#   }
# }
#              """ % (qs.pk, jabatan, bidang, kdKantor)

#                 post_json = requests.post(url, json={'query':query})
#                 json_data = json.loads(post_json.text)
#                 if json_data['data']['updateUser'] is not None:
#                     data = json_data['data']['updateUser']['users']
#                     .format(data['username'], data['kdKantor']['kdKantor'], data['kdKantor']['namaKantor'],
#                         data['jabatan']['namaJabatan'],data['bidang']['namaBidang'])
#                     bot.send_message(idTelegram, pesan)
           
#             elif int(qs.id_telegram) != message.chat.id:
#                 bot.send_message(message.chat.id, "Username harus sesuai")
#             else:
#                 pesan = """
# Anda tidak dapat melakukan
# <b>UPDATE</b> Akun lebih dari sekali!
#                 """
#                 bot.send_message(message.chat.id, pesan)
#         except:
#             pass

@database_sync_to_async
@bot.message_handler(commands=['infoAll'])
def infoall(message):
    qs = ExtendUser.objects.filter(id_telegram=message.chat.id).first()
    if qs is None:
        bot.send_message(message.chat.id, "Akun anda belum diupdate/belum terdaftar")
    elif qs.token_auth is None:
        bot.send_message(message.chat.id,"Authorized User Only! Silahkan Update Akun Anda")
    else:
        texts = message.text.split(' ')
        npp = texts[1]
        
        if len(texts) < 2 or len(npp) != 8:
            pesan = """
Format anda <b>Salah</b>
Gunakan perintah /infoAll no_npp
contoh : /infoAll AA020015
        """
            bot.send_message(message.chat.id, pesan)
        else:
            query = DetilMkro.objects.filter(kode_kantor=qs.kd_kantor.kd_kantor, npp=npp).order_by('-tgl_upload').first()
            # print(query)
            
            if query is None:
                pesan = """
Pastikan <b>NPP</> yang anda input adalah benar.


<b>**</b><i>botsi sumbagut</i>
                """
                bot.send_message(message.chat.id, pesan)
            else:
                try:
                    
                    if query.keps_jp == '' or query.keps_jp == '- ' or query.keps_jp is None:
                        keps_jp = 'Tidak'
                    else:
                        keps_jp = query.keps_jp
                    if query.blth_na == '' or query.blth_na == '- ' or query.blth_na is None:
                        blthNa = 'Aktif'
                    else:
                        blthNa = 'NA sejak :' + query.blth_na
                    if query.sipp == 1 or query.sipp == '1':
                        sipp = 'YA'
                    else:
                        sipp = 'TIDAK'

                    locale.setlocale(locale.LC_MONETARY, 'id_ID')
                    iuran_berjalan = locale.currency(query.total_iuran_berjalan, grouping=True)
                    pesan = """\nBerikut adalah detil data NPP <b>{}</b> divisi {}, sesuai update terakhir pada <b>{}</b> :\n
User Pembina : {}
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
                    """.format(query.npp,query.div_1,query.tgl_upload,query.kode_pembina,query.nama_pembina,query.nama_prsh,query.keps_awal,
                        keps_jp,blthNa, query.prog,query.total_tk_aktif,iuran_berjalan,query.blth_akhir,sipp)
                    bot.send_message(message.chat.id, pesan)
                except:
                    pesan = "NPP yang dimasukkan tidak benar"
                    bot.send_message(message.chat.id, pesan)

@database_sync_to_async
@bot.message_handler(commands=['infoDetil'])
def infoDetil(message):
    qs = ExtendUser.objects.filter(id_telegram=message.chat.id).first()
    if qs is None:
        bot.send_message(message.chat.id, "Akun anda belum diupdate/belum terdaftar")
    elif qs.token_auth is None:
        bot.send_message(message.chat.id,"Authorized User Only! Silahkan Update Akun Anda")
    else:
        texts = message.text.split(' ')
        npp = texts[1]
        
        if len(texts) < 2 or len(npp) != 8:
            pesan = """
Format anda <b>Salah</b>
Gunakan perintah /infoAll no_npp
contoh : /infoAll AA020015
        """
            bot.send_message(message.chat.id, pesan)
        else:
            query = DetilMkro.objects.filter(kode_kantor=qs.kd_kantor.kd_kantor, npp=npp).order_by('-tgl_upload').first()
            if query is None:
                pesan = """
Pastikan <b>NPP</> yang anda input adalah benar.



<b>**</b><i>botsi sumbagut</i>
                """
                bot.send_message(message.chat.id, pesan)
            else:
                try:
                    if query:
                        if query.keps_jp == '' or query.keps_jp == '- ' or query.keps_jp is None:
                            keps_jp = 'Tidak'
                        else:
                            keps_jp = query.keps_jp
                        if query.blth_na == '' or query.blth_na == '- ' or query.blth_na is None:
                            blthNa = 'Aktif'
                        else:
                            blthNa = 'NA sejak :' + query.blth_na
                        if query.sipp == 1 or query.sipp == '1':
                            sipp = 'YA'
                        else:
                            sipp = 'TIDAK'
                        if query.itw == 1 or query.itw == '1':
                            itw = 'YA'
                        else:
                            itw = 'TIDAK'

                        locale.setlocale(locale.LC_MONETARY, 'id_ID')
                        iuran_berjalan = locale.currency(query.total_iuran_berjalan, grouping=True)
                        pesan = """\nBerikut adalah detil data NPP <b>{}</b> divisi {}, sesuai update terakhir pada <b>{}</b> :\n
User Pembina : {}
Nama Pembina : {}
Nama Perusahaan : {}
Kepesetaan Awal : {}
Kepesertaan JP : {}
Status Aktif : {}
Pareto       : {}
Skala Usaha  : {}
Jumlah Program : {}
TK Masuk       : {}
TK Keluar      : {}
Total TK Aktif : {}
Total TK NA    : {}
Jumlah TK      : {}
Total Iuran Berjalan : <b>{}</b>
BLTH Rekon Terakhir : {}
SIPP           : {}
ITW            : {}
IBR IJT        : {}
IBR IDM        : {}




<i>Sumber : MKRO</i>          
                        """.format(query.npp,query.div_1,query.tgl_upload,query.kode_pembina,query.nama_pembina,query.nama_prsh,query.keps_awal,
                            keps_jp,blthNa,query.pareto,query.skl_usaha, query.prog,query.tambah_tk,query.kurang_tk,query.total_tk_aktif,
                                query.total_tk_na,query.jml_all_tk,iuran_berjalan,query.blth_akhir,
                                sipp,itw,query.ibr_ijt,query.ibr_idm)
                        bot.send_message(message.chat.id, pesan)
                except AttributeError as ex:
                    pesan = "NPP yang dimasukkan tidak benar. Error: {}".format(ex)
                    bot.send_message(message.chat.id, pesan)


@database_sync_to_async
@bot.message_handler(commands=['profile'])
def profile(message):
    qs = ExtendUser.objects.filter(id_telegram=message.chat.id).exists()
    if not qs:

        bot.send_message(message.chat.id,"Authorized user only")
    else:
        telegram = str(message.chat.id)
        qs = ExtendUser.objects.filter(id_telegram=message.chat.id)[0]
        if qs.updated == False:
            bot.send_message(message.chat.id,"Silahkan update data anda!")
        else:
            pesan = """
Detil Profile <b><u>{}</u></b>:

<pre>
Nama    : {}
Jabatan : {}
Bidang  : {}
Kantor  : {}

</pre>

<b>**</b><i>botsi sumbagut</i>
            """.format(qs.username, message.chat.first_name, qs.jabatan.nama_jabatan, qs.bidang.nama_bidang, qs.kd_kantor.kd_kantor)
            bot.send_message(message.chat.id, pesan)
# query{
#   detilUserId(telegram:"%s") {
#     id
#     username
#     jabatan{
#       namaJabatan
#     }
#     bidang{
#       namaBidang
#     }
#     kdKantor{
#       kdKantor
#       namaKantor
#     }
   
#   }
# }
#         """ % (telegram)
#         get_json = requests.get(url, json={'query':query})
#         json_data = json.loads(get_json.text)
#         # print(json_data)
#         data = json_data['data']['detilUserId'][0]
#         user = data['username']
#         kantor = data['kdKantor']['kdKantor']+' - '+data['kdKantor']['namaKantor']
#         jabatan = data['jabatan']['namaJabatan']
#         bidang = data['bidang']['namaBidang']
        
       

@database_sync_to_async
@bot.message_handler(commands=['REKAPBUREKON'])
def rekapbpurekon(message):
    m = []
    n = []
    qs = ExtendUser.objects.filter(id_telegram=message.chat.id).first()
    if qs is None:
        bot.send_message(message.chat.id, "Akun anda belum diupdate/belum terdaftar")
    elif qs.token_auth is None:
        bot.send_message(message.chat.id,"Authorized User Only! Silahkan Update Akun Anda")
    else:
        texts = message.text.split(' ')
        if len(texts) < 1 or len(texts[1]) != 4:
            pesan = """
Format anda <b>Salah</b>
Gunakan perintah /REKAPBUREKON tahun
contoh : /REKAPBUREKON 2021
            """
            bot.send_message(message.chat.id, pesan)
        else:
            m = ['01-'+texts[1],'02-'+texts[1],'03-'+texts[1], '04-'+texts[1],'05-'+texts[1],'06-'+texts[1],'07'+texts[1],
                  '08-'+texts[1],'09-'+texts[1],'10-'+texts[1],'11-'+texts[1],'12-'+texts[1]]
            locale.setlocale(locale.LC_MONETARY, 'id_ID')
            for i in range(0,len(m)-1):
                try:
                    query = DetilMkro.objects.filter(kode_pembina=qs.username, blth_siap_rekon__contains=m[i])
                    
                    if not query.exists():
                        pass
                    else:
                # for i in query:
                #     nilai_rekon = i.nilai_posting
                    # msg = "{} : {}".format(i.blth_siap_rekon, nilai_rekon)
                    # m = '\n'.join(msg)
                        # total = query.aggregate(Sum('nilai_posting'))
                        total = query.values('npp').distinct().count()
                        # msg = "{} : {}".format(m[i],locale.currency(total['nilai_posting__sum'], grouping=True))
                        msg = "{} : {}".format(m[i], total)
                        n.append(msg)
                except:
                    pass
            pesan = """
Berikut adalah rekap PK/BU berdasarkan BLTH Terakhir Rekon user <b>{}</b>
Mohon lakukan tindaklanjut untuk PKBU yang Menunggak Iuran untuk
Meningkatkan nilai ITW dan ITB
Sumber: MKRO
            """.format(qs.username)
            bot.send_message(message.chat.id, pesan)
            tahun = int(texts[1])
            for k in range(2,0,-1):
                thn = tahun - (k)
                query = DetilMkro.objects.filter(kode_pembina=qs.username, blth_siap_rekon__contains=str(thn))
                # total1 = query.aggregate(Sum('nilai_posting'))
                total1 = query.values('npp').distinct().count()
                pesan = """
{} : {}
                """.format(str(thn), total1)
                # format(str(thn), locale.currency(total1['nilai_posting__sum'], grouping=True))
                bot.send_message(message.chat.id, pesan)
            for j in range(0,len(n)-1):
                pesan = """
{}
                """.format(n[j])
                bot.send_message(message.chat.id, pesan)
                    
@database_sync_to_async
@bot.message_handler(commands=['REKAPBU'])
def rekapbu(message):
    m = []
    n = []
    qs = ExtendUser.objects.filter(Q(jabatan__id=3) | Q(jabatan__id=4),id_telegram=message.chat.id).first()
    if qs is None:
        bot.send_message(message.chat.id, "Otoritas tidak cukup")
    elif qs.token_auth is None:
        bot.send_message(message.chat.id,"Authorized User Only! Silahkan Update Akun Anda")
    else:
        texts = message.text.split(' ')
        
        if len(texts) < 1 or len(texts[1]) != 4:
            pesan = """
Format anda <b>Salah</b>
Gunakan perintah /REKAPBU tahun
contoh : /REKAPBU 2021



<i>Khusus Kakacab / Kabid</i>
            """
            bot.send_message(message.chat.id, pesan)
        else:
            m = ['01-'+texts[1],'02-'+texts[1],'03-'+texts[1], '04-'+texts[1],'05-'+texts[1],'06-'+texts[1],'07'+texts[1],
                  '08-'+texts[1],'09-'+texts[1],'10-'+texts[1],'11-'+texts[1],'12-'+texts[1]]
            locale.setlocale(locale.LC_MONETARY, 'id_ID')
            for i in range(0, len(m)-1):
                try:
                    query = DetilMkro.objects.filter(kode_kantor=qs.kd_kantor.kd_kantor, blth_siap_rekon=m[i])
                    if not query.exists():
                        pass
                    else:
                        # total = query.aggregate(Sum('nilai_posting'))
                        total = query.values('npp').distinct().count()
                        # msg = "{} : {}".format(m[i],locale.currency(total['nilai_posting__sum'], grouping=True))
                        msg = "{} : {}".format(m[i], total)
                        n.append(msg)
                except:
                    pass
            pesan = """
Berikut adalah rekap PK/BU berdasarkan BLTH Terakhir Rekon Kantor Cabang <b>{}</b>
Mohon lakukan tindaklanjut untuk PKBU yang Menunggak Iuran untuk
Meningkatkan nilai ITW dan ITB
Sumber: MKRO
            """.format(qs.kd_kantor)
            bot.send_message(message.chat.id, pesan)
            tahun = int(texts[1])
            for k in range(2,0,-1):
                thn = tahun - (k)
                try:
                    query = DetilMkro.objects.filter(kode_kantor=qs.kd_kantor.kd_kantor, blth_siap_rekon__contains=str(thn))
                    if not query.exists():
                        pass
                    else:
                        # total1 = query.aggregate(Sum('nilai_posting'))
                        total1 = query.values('npp').distinct().count()
                        pesan = """
{} : {}
                        """.format(str(thn), total1)
                        # format(str(thn), locale.currency(total1['nilai_posting__sum'], grouping=True))
                        bot.send_message(message.chat.id, pesan)
                except:
                    pass
            for j in range(0,len(n)-1):
                pesan = """
{}
                """.format(n[j])
                bot.send_message(message.chat.id, pesan)
            pesan = """



<i>Sumber MKRO</i>
            """
            bot.send_message(message.chat.id, pesan)
@database_sync_to_async
@bot.message_handler(commands=['REKAPBUSKALA'])
def rekapbuSkala(message):
    qs = ExtendUser.objects.filter(id_telegram=message.chat.id)
    if qs.first() is None:
        bot.send_message(message.chat.id, "Akun anda belum diupdate/belum terdaftar")
    elif qs[0].token_auth is None:
        bot.send_message(message.chat.id,"Authorized User Only! Silahkan Update Akun Anda")
    else:
        texts = message.text.split(' ')
      
        if len(texts) > 1:
            pesan = """
Format anda <b>Salah</b>
Gunakan perintah /REKAPBUSKALA
contoh : /REKAPBUSKALA
            """
            bot.send_message(message.chat.id, pesan)
        else:
            if qs.filter(Q(jabatan__id=3) | Q(jabatan__id=4)):
                try:
                    query = DetilMkro.objects.filter(kode_kantor=qs[0].kd_kantor.kd_kantor).values('skl_usaha').annotate(jlh=Count('npp', distinct=True))
                    pesan = """
Berikut adalah rekap PK/BU berdasarkan Skala Usaha Kantor Cabang {} :
Besar : {}
Menengah : {} 
Kecil : {}
Mikro : {}


<i>**Sumber : MKRO</i>

                        """.format(qs[0].kd_kantor, query[0]['jlh'],query[2]['jlh'],query[1]['jlh'],query[3]['jlh'])
                    bot.send_message(message.chat.id, pesan)
                except:
                    bot.send_message(message.chat.id, "Data tidak ditemukan!")
            else:
                try:
                    query = DetilMkro.objects.filter(kode_kantor=qs[0].kd_kantor.kd_kantor, kode_pembina=qs[0].username).values('skl_usaha').annotate(jlh=Count('npp', distinct=True))
                    pesan = """
Berikut adalah rekap PK/BU berdasarkan Skala Usaha
Kantor Cabang {} dengan pembina {} :

Besar : {}
Menengah : {} 
Kecil : {}
Mikro : {}




<i>**Sumber : MKRO</i>
                    """.format(qs[0].kd_kantor, qs[0].username,query[0]['jlh'],query[2]['jlh'],query[1]['jlh'],query[3]['jlh'])
                    bot.send_message(message.chat.id, pesan)
                except:
                    bot.send_message(message.chat.id, "Data tidak ditemukan!")

@database_sync_to_async
@bot.message_handler(commands=['REKAPBUPROG'])
def rekapProg(message):
    qs = ExtendUser.objects.filter(id_telegram=message.chat.id)
    if qs.first() is None:
        bot.send_message(message.chat.id, "Akun anda belum diupdate/belum terdaftar")
    elif qs[0].token_auth is None:
        bot.send_message(message.chat.id,"Authorized User Only! Silahkan Update Akun Anda")
    else:
        texts = message.text.split(' ')
        if len(texts) > 1 :
            pesan = """
Format anda <b>Salah</b>
Gunakan perintah /REKAPBUPROG
contoh : /REKAPBUPROG
            """
            bot.send_message(message.chat.id, pesan)
        else:
            if qs.filter(Q(jabatan__id=3) | Q(jabatan__id=4)):
                try:
                
                    query = DetilMkro.objects.filter(kode_kantor=qs[0].kd_kantor.kd_kantor).values('prog').annotate(jlh=Count('npp', distinct=True))
                
                    if query.exists():
                        pesan = """
Berikut adalah rekap PK/BU berdasarkan Program Kantor Cabang {} :

2P : {}
3P : {} 
4P : {}



<i>**Sumber : MKRO</i>

                        """.format(qs[0].kd_kantor,query[0]['jlh'],query[1]['jlh'],query[2]['jlh'])
                        bot.send_message(message.chat.id, pesan)
                    else:
                        bot.send_message(message.chat.id,"Data Tidak Ditemukan")
                except:
                    bot.send_message(message.chat.id, "Otoritas tidak cukup! Hanya untuk Kakacab dan Kabid")
            else:
                try:
                    query = DetilMkro.objects.filter(kode_kantor=qs[0].kd_kantor.kd_kantor, kode_pembina=qs[0].username).values('prog').annotate(jlh=Count('npp', distinct=True))
                    if query.exists():
                        pesan = """
Berikut adalah rekap PK/BU berdasarkan Program Kepesertaan
Binaan {} :

2P : {}
3P : {} 
4P : {}



<i>**Sumber : MKRO</i>
                        """.format(qs[0].username,query[0]['jlh'],query[1]['jlh'],query[2]['jlh'])
                        bot.send_message(message.chat.id, pesan)
                    else:
                        bot.send_message(message.chat.id, "Data Tidak Ditemukan")
                except:
                    bot.send_message(message.chat.id, "Otoritas tidak sesuai!")

# def kirim_pesan():
#     tgl1 = datetime.today()
#     tgl2 = tgl1 - timedelta(days=1)
#     td = tgl1.strftime('%Y-%m-%d')
#     yt = tgl2.strftime('%Y-%m-%d')

#     users = ExtendUser.objects.filter(jabatan_id=5)
#     for user in users:
#         datas = DetilMkro.objects.filter(kode_pembina=user.username, tgl_upload__range=(yt,td)).values('kode_pembina').annotate(jlh=Count('npp', distinct=True))
#         if datas.exists():
#             pesan = """
# Dear user {}.

# Jlh NPP Terkahir update adalah :
# {} Perusahaan
#             """.format(datas['kode_pembina'], datas['jlh'])
#             kirim = bot.send_message(user.id_telegram, pesan)
#             assert kirim.message_id
        
#         else:
#             qs = DetilMkro.objects.filter(kode_pembina=user.username)
#             tgl3 = qs.aggregate(Max('tgl_upload'))
#             nw = tgl3['tgl_upload__max'].strftime('%Y-%m-%d')
#             datas = qs.filter(tgl_upload__range=(nw, tgl3)).values('kode_pembina').annotate(lh=Count('npp', distinct=True))
#             pesan = """
# Dear user {}.

# Jlh NPP Terkahir update adalah :
# {} Perusahaan
#             """.format(datas['kode_pembina'], datas['jlh'])
#             kirim = bot.send_message(user.id_telegram, pesan)
#             assert kirim.chat.id

print('Bot is Running')
bot.infinity_polling(timeout=10, long_polling_timeout=5)
 