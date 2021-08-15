import telebot, locale
import requests, json
from datetime import datetime
from django.conf import settings
from accounts.models import ExtendUser

from .decorators import restricted

bot = telebot.TeleBot(settings.BOT_API, parse_mode='html')
url = "http://localhost:8000/graphql"

# qs = ExtendUser.objects.all()

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
        qs = ExtendUser.objects.filter(username=username).first()
        if qs.username == username and qs.id_telegram == user:
            bot.send_message(user, "Username anda sudah pernah terdaftar")
        else:
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
                qs = ExtendUser.objects.filter(username=username)[0]
                token = qs.token_auth
            # cek = qs.filter(username=username)[0]
                data = json_data['data']['register']
                if data['success'] == True:
                    pesan = """
Akun <b>{}</b> sudah berhasil didaftarkan.
Berikut token anda :

{}

Kemudian verifikasi dengan cara:
/token token_anda
Terima Kasih
                    """.format(username, token)
            # print(json_data)
                    bot.send_message(user, pesan)
            else:
                bot.send_message(user, "[]")
            
        

#             bot.send_message(user, pesan)
#         elif data['errors']:
#             error = data['errors']['nonFieldErrors'][0]
#             bot.send_message(message.chat.id, error['message'])

@bot.message_handler(commands=['login'])
def masuk(message):
    texts = message.text.split(' ')
    if len(texts) < 2:
        bot.send_message(message.chat.id,"Format Salah")
    else:
        username = texts[1]
        password = texts[2]
    # print(password)
    # qs = ExtendUser.objects.filter(username=username, password=password)
    # print(qs)
    # if not qs or qs is None:
#         pesan = """
# Username/password anda salah.
# Atau Akun anda belum terdaftar.
#         """
    #     bot.send_message(message.chat.id, pesan)
    # else:
        # bot.send_message(message.chat.id,"Login Anda Berhasil")
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
        data = json_data['data']['tokenAuth']
        if data['success'] == True:
            pesan = """
Anda berhasil login.

Berikut perintah yang tersedia :
1. Cek Detail NPP Binaan
   contoh : /infoAll AA020015

2. On progress


        """
            obj, created = ExtendUser.objects.update_or_create(username=username, defaults={'token_auth':data['token'], 'id_telegram':message.chat.id})
            bot.send_message(message.chat.id, pesan)
    # elif data is None:
    #     bot.send_message(message.chat.id, "Data anda tidak ditemukan. Silahkan Registrasi!")
    # else:
    #     bot.send_message(message.chat.id, "Username atau Password anda Salah!")

@bot.message_handler(commands=['token'])
def authToken(message):
    
    texts = message.text.split(' ')
    if len(texts) < 2:
        bot.send_message(message.chat.id, "Format Salah!")
    else:
        kd_token = texts[1]
        query = """
mutation{
  verifyToken(
    token:"%s"
  ) {
    success
    errors
  }
}
        """ % (kd_token)
#         headers = {"Authorization":"JWT %s" % (kd_token)}
        # post_json = requests.post(url, json={'query':query})
        # json_data = json.loads(post_json.text)
        # data = json_data['data']['verifyToken']
        # username = data['payload']['username']
        qs = ExtendUser.objects.filter(token_auth=kd_token)
        username = qs[0].username
        if not qs or qs is None:
            bot.send_message(message.chat.id, "Token Expired!")
        else:
            qs.update_or_create(username=username, defaults={'id_telegram':message.chat.id})
            bot.send_message(message.chat.id,"Token anda sudah terverifikasi")

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

    texts = message.text.split(' ')
    if len(texts) < 2:
        bot.send_message(message.chat.id, "Format Perintah Salah!")
    else:
        username = texts[1]
        qs = ExtendUser.objects.filter(username=username).first()
        # print(qs.id_telegram)
        # print(message.chat.id)
        if int(qs.id_telegram) == message.chat.id:
            jabatan = int(texts[2])
            bidang = int(texts[3])
            kdKantor = int(texts[4])
            idTelegram = str(message.chat.id)
            query = """
mutation{
  updateUser(id:%d, bidang:%d, jabatan:%d, kdKantor:%d){
    users{
      id
      username
      bidang{
        id
        namaBidang
      }
      jabatan{
        id
        namaJabatan
      }
      kdKantor{
        id
        namaKantor
        kdKantor
      }
    }
  }
}
            """ % (qs.pk, jabatan, bidang, kdKantor)

            post_json = requests.post(url, json={'query':query})
            json_data = json.loads(post_json.text)
            # print(json_data)
            data = json_data['data']['updateUser']['users']
            if data is not None:
                pesan = """
Data user <b>{}</b> berhasil diupdate.

Kantor : {} - {}

Jabatan : {}

Bidang : {}
                """.format(data['username'], data['kdKantor']['kdKantor'], data['kdKantor']['namaKantor'],
                    data['jabatan']['namaJabatan'],data['bidang']['namaBidang'])
                bot.send_message(idTelegram, pesan)
            # else:
            #     bot.send_message(idTelegram,"Terjadi Kesalahan!. Hubungi Administrator")
        elif int(qs.id_telegram) != message.chat.id:
            bot.send_message(message.chat.id, "Username harus sesuai")

@bot.message_handler(commands=['infoAll'])
def infoall(message):
    qs = ExtendUser.objects.filter(id_telegram=message.chat.id).first()
    if qs is None:
        bot.send_message(message.chat.id, "Akun anda belum diupdate/belum terdaftar")
    elif qs.token_auth is None:
        bot.send_message(message.chat.id,"Authorized User Only!")
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
            data = json_data['data']['allDetilMkro']
            if data is None:
                pesan = """
Pastikan <b>NPP</> yang anda input adalah benar.
Dan atau sesuai dengan binaan anda.




<b>**</b><i>botsi kanwil sumbagut</i>
                """
                bot.send_message(message.chat.id, pesan)
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
    qs = ExtendUser.objects.filter(id_telegram=message.chat.id).exists()
    if not qs:

        bot.send_message(message.chat.id,"Authorized user only")
    else:
        query = """
query{
  detilUserId(telegram:"1435940099") {
    id
    username
    jabatan{
      namaJabatan
    }
    bidang{
      namaBidang
    }
    kdKantor{
      kdKantor
      namaKantor
    }
   
  }
}
        """
        get_json = requests.get(url, json={'query':query})
        json_data = json.loads(get_json.text)
        data = json_data['data']['detilUserId'][0]
        user = data['username']
        kantor = data['kdKantor']['kdKantor']+' - '+data['kdKantor']['namaKantor']
        jabatan = data['jabatan']['namaJabatan']
        bidang = data['bidang']['namaBidang']
        pesan = """
Detil Profile <b><u>{}</u></b>:

<pre>
Nama    : {}
Jabatan : {}
Bidang  : {}
Kantor  : {}

</pre>

<b>**</b><i>Botsi Kanwil Sumbagut</i>
        """.format(user, message.chat.first_name, jabatan, bidang, kantor)
        bot.send_message(message.chat.id, pesan)

print('Bot is Running')
bot.polling()