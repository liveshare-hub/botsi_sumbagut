import telebot, locale
import requests, json
from datetime import datetime
from django.conf import settings
from accounts.models import ExtendUser

from .decorators import cek_login

bot = telebot.TeleBot(settings.BOT_API, parse_mode='html')
url = "http://localhost:8000/graphql"

qs = ExtendUser.objects.all()

@bot.message_handler(commands=['start',])
def start(message):
    # print(message)
    nama_dpn = message.chat.first_name
    pesan = """
Selamat datang <b>{}</b>.

Silahkan ketik /help untuk menu bantuan.
    """.format(nama_dpn)
    bot.send_message(message.chat.id, pesan)

@bot.message_handler(commands=['register'])
def newRegister(message):
    user = message.chat.id
    
    texts = message.text.split(' ')
    # print(texts)
    if len(texts) < 2:
        
        bot.send_message(message.chat.id,"Email/Username/Password are missing!")
    else:
        email = texts[1]
        username = texts[2]
        password1 = texts[3]
        password2 = texts[4]
        
        query = """
mutation{
register(email:"%s",username:"%s", password1:"%s", password2:"%s")
{
token
refreshToken
success
errors

}
}
        """ % (email, username, password1, password2)

        post_json = requests.post(url, json={'query':query})
        json_data = json.loads(post_json.text)
        # print(json_data)
        if post_json.status_code == 200:
            cek = qs.filter(username=username)[0]
            data = json_data['data']['register']
            if data['success'] == True:
                pesan = """
Akun <b>{}</b> sudah berhasil didaftarkan.
Silahkan cek email anda untuk verifikasi

Terima Kasih
                """.format(username)
            # print(json_data)
                bot.send_message(user, pesan)
        else:
            bot.send_message(user, "Username sudah terdaftar")
            
        

#             bot.send_message(user, pesan)
#         elif data['errors']:
#             error = data['errors']['nonFieldErrors'][0]
#             bot.send_message(message.chat.id, error['message'])

@bot.message_handler(commands=['login'])
def login(message):
    texts = message.text.split(' ')
    username = texts[1]
    password = texts[2]
    query = """
mutation{
  tokenAuth(username:"%s",password:"%s") {
    token
    success
    errors
    unarchiving
    refreshToken
  }
}

    """ % (username, password)
    post_json = requests.post(url, json={'query':query})
    json_data = json.loads(post_json.text)
    # print(post_json.status_code)
    # if post_json.status_code == 200:
    data = json_data['data']['tokenAuth']
    if data['success'] == True:
        pesan = """
Anda berhasil login.
Silahkan update data anda terlebih dahulu 
dengan cara:
/update nama_jabatan nama_bidang kd_kantor id_telegram

            """
        bot.send_message(message.chat.id, pesan)
    elif data is None:
        bot.send_message(message.chat.id, "Data anda tidak ditemukan. Silahkan Registrasi!")
    else:
        bot.send_message(message.chat.id, "Username atau Password anda Salah!")

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
Kemudaian cek email untuk dilakukan verifikasi akun anda

Cara login:
/login username password
contoh: /login MU150710 Welcome1

Update Akun :
Setelah berhasil login <b>di WAJIBKAN</b>
bagi anda untuk melakukan update akun
seperti jabata, bidang, kode kantor dan id telegram
/update id_jabatan id_bidang id_kantor
contoh : /update 1 1 1

Menampilakn Profile Akun:
/profile

Menampilkan report MKRO by NPP per pembina:
/infoAll npp_binaan_anda
contoh /infoAll AA020015

Terima Kasih
        """
        bot.send_message(message.chat.id, pesan)
    else:
        if texts[1] == 'cek_id':
            user = message.chat.id
            pesan = "ID Telegram anda adalah {}".format(user)
            bot.send_message(user, pesan)
        elif texts[1] == 'list_jabatan':
            query = """
query{
  allJabatan{
    id
    namaJabatan
  }
}
        """
            post_json = requests.post(url, json={'query':query})
            json_data = json.loads(post_json.text)
            data = json_data['data']['allJabatan']
            for i in range(0,len(data)):
            # jabatan = ''.join(data[i])
            
                pesan = """

{} - {}
     

                """.format(data[i]['id'],data[i]['namaJabatan'])
        # % (jabatan['id'], jabatan['namaJabatan'])
                bot.send_message(message.chat.id, pesan)
        elif texts[1] == "list_bidang":
            query = """
query{
    allBidang {
        id
        namaBidang
        }
}
        """
            post_json = requests.post(url, json={'query':query})
            json_data = json.loads(post_json.text)
            data = json_data['data']['allBidang']
            for i in range(0, len(data)):
                pesan = "{} - {}".format(data[i]['id'], data[i]['namaBidang'])
                bot.send_message(message.chat.id, pesan)
    
        elif texts[1] == "list_kantor":
            query = """
query{
  allKodeKantor {
    id
    namaKantor
    kdKantor
  }
}
        """
            post_json = requests.get(url, json={'query':query})
            json_data = json.loads(post_json.text)
            data = json_data['data']['allKodeKantor']
            for i in range(0, len(data)):
                pesan = "{}. {} - {}".format(data[i]['id'],data[i]['kdKantor'],data[i]['namaKantor'])
                bot.send_message(message.chat.id, pesan)
        else:
            bot.send_message(message.chat.id, "Menu belum terseida !")

@bot.message_handler(commands=['update'])
def updateData(message):
    # if not cek_login(bot, message):
    #     bot.send_message(message.chat.id,"Silahkan login terlebih dahulu")
    # else:
    texts = message.text.split(' ')
    jabatan = texts[1]
    bidang = texts[2]
    kdKantor = texts[3]
    idTelegram = message.chat.id

    if len(texts) < 2:
        bot.send_message(idTelegram, "Format Salah!")
    else:
        query = """
mutation{
  updateAccount(jabatan:%d, bidang:%d, kdKantor:%d, idTelegram:%s) {
    success
    errors
  }
}        
        """ % (jabatan, bidang, kdKantor, idTelegram)

        post_json = requests.post(url, json={'query':query})
        json_data = json.loads(post_json.text)
        data = json_data['data']['updateAccount']
        if data['success'] == True:
            qs = ExtendUser.objects.filter(id_telegram=idTelegram)[0]
            pesan = "Data {} berhasil diupate".format(qs.username)
            bot.send_message(idTelegram, pesan)
        else:
            bot.send_message(idTelegram,"Terjadi Kesalahan!. Hubungi Administrator")

@bot.message_handler(commands=['infoAll'])
def infoall(message):
    if not cek_login(bot, message):
        bot.send_message(message.chat.id,"Silahkan login terlebih dahulu")
    else:
        texts = message.text.split(' ')
        npp = texts[1]
        
        if len(texts) < 2:
            pesan = """
Format anda <b>Salah</b>
Gunakan perintah /infoAll no_npp_binaan_anda
contoh : /infoAll AA020015
        """
            bot.send_message(message.chat.id, pesan)
        else:
            query = """
query GetData($npp: String = "%s"){
        allDetilMkro(npp:$npp){
            kodePembina
            namaPembina
            npp
            div1
            namaPrsh
            kepsAwal
            kepsJp
            blthNa
            prog
            totalTkAktif
            totalIuranBerjalan
            blthAkhir
            sipp
            tglUpload
        }
                
    }    
            """ % (npp)
            get_json = requests.get(url, json={'query':query})
            json_data = json.loads(get_json.text)
            
            if len(json_data['data']['allDetilMkro']) < 1:
                bot.send_message(message.chat.id, "Pastikan NPP benar atau sesuai dengan binaan Anda")
            else:
                data = json_data['data']['allDetilMkro'][0]
                if data['kepsJp'] == '' or data['kepsJP'] == '- ' or data['kepsJp'] is None:
                    jp = ' Tidak'
                else:
                    jp = data['kepsJp']
                if data['blthNa'] == '' or data['blthNa'] == '- ' or data['blthNa'] is None:
                    blth_na = ' Aktif'
                else:
                    blth_na = data['blthNa']
                if data['sipp'] == 1 or data['sipp'] == '1':
                    sipp = ' Ya'
                else:
                    sipp = ' Tidak'
                tgl = datetime.fromisoformat(data['tglUpload'])
                tgl2 = datetime.strftime(tgl, '%d-%m-%Y')
                locale.setlocale(locale.LC_ALL,'')
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

            """.format(data['npp'],data['div1'],tgl2,data['kodePembina'],data['namaPembina'],data['namaPrsh'],
                data['kepsAwal'],jp,blth_na,data['prog'],locale.format('%d',data['totalTkAktif'],1),
                locale.currency(data['totalIuranBerjalan'],grouping=True),data['blthAkhir'],sipp)
                bot.send_message(message.chat.id, pesan)

@bot.message_handler(commands=['profile'])
def profile(message):
    if not cek_login(bot, message):
        bot.send_message(message.chat.id,"Silahkan login terlebih dahulu")
    else:
        qs = ExtendUser.objects.filter(id_telegram=message.chat.id)[0]
        if not qs:
            bot.send_message(message.chat.id, "Silahkan melakukan update pada profile anda")
        else:
            user = qs.username
            name = message.chat.first_name
            jabatan = qs.jabatan.nama_jabatan
            bidang = qs.bidang.nama_bidang
            kantor = qs.kd_kantor.nama_kantor
            idTelegram = qs.id_telegram
            pesan = """
Data Profile {} :

Username = {}
Nama = {}
jabatan = {}
Bidang = {}
Kantor = {}
Id Telegram = {}

Terima Kasih
            """.format(user, name, jabatan, bidang, kantor, idTelegram)
            bot.send_message(message.chat.id, pesan)

print('Bot is Running')
bot.polling()