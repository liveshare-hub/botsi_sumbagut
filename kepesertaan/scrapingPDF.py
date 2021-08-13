from camelot import read_pdf
from kepesertaan.models import TargetRealisasi, Uraian, JenisUraian
from datetime import datetime
# from pathlib import Path
# from urllib.request import urlopen, Request
import requests
# import time

def Scrapping(kode_kantor, periode, user):
    url = "http://rptserver.bpjsketenagakerjaan.go.id/reports/rwservlet/setauth?button=Submit&username=smile&password=smilekanharimu&authtype=D&mask=GQ%253D%253D&isjsp=no&database=dboltp&nextpage=destype%3Dcache%26desformat%3DPDF%26report%3DMISR1001.rdf%26userid%3D%2Fdata%2Freports%2Fkn%26%26P_KODE_KANTOR%3D%27{}%27%26P_PERIODE%3D%27{}%27".format(kode_kantor, periode)
    r = requests.get(url)
    # filename = Path('downloads.pdf')
    # filename.write_bytes(r)
    with open('downloads.pdf','wb') as f:
        f.write(r.content)

    # time.sleep(2)

    data = read_pdf('downloads.pdf', flavor='stream', table_areas=['30,1080,933,194'], strip_text=['\t'])
    df = data[0].df
    m_data = []
    # Status Aktif
    # if df[0][0] == "Status Aktif":
        # m = df[0][0]
    for i in range(1,8):
        qs = TargetRealisasi()
        # ps = JenisUraian.objects.get(nama=df[0][0])
        rs = Uraian.objects.get(nama_uraian=df[0][i])
        qs.jenis_id = 1
        qs.uraian_id = rs.pk
        qs.target_tahun = df[2][i]
        qs.target_bln_lapor = df[3][i]
        qs.realisasi_sd_bln_lalu = df[4][i]
        qs.realisasi_bln_lapor = df[5][i]
        qs.realisasi_sd_bln_lapor = df[6][i]
        qs.periode = datetime.strptime(periode, "%d/%m/%Y")
        qs.user = user
        qs.save()

    # elif df[0][9] == "Penambahan":
    for i in range(10,17):
        qs = TargetRealisasi()
        # ps = JenisUraian.objects.get(nama=df[0][9])
        rs = Uraian.objects.get(nama_uraian=df[0][i])
        qs.jenis_id = 2
        qs.uraian_id = rs.pk
        qs.target_tahun = df[2][i]
        qs.target_bln_lapor = df[3][i]
        qs.realisasi_sd_bln_lalu = df[4][i]
        qs.realisasi_bln_lapor = df[5][i]
        qs.realisasi_sd_bln_lapor = df[6][i]
        qs.periode = datetime.strptime(periode, "%d/%m/%Y")
        qs.user = user
        qs.save()

    # elif df[0][18] == "Pengurangan":
    for i in range(19,26):
        qs = TargetRealisasi()
        # ps = JenisUraian.objects.get(nama=df[0][18])
        rs = Uraian.objects.get(nama_uraian=df[0][i])
        qs.jenis_id = 3
        qs.uraian_id = rs.pk
        qs.target_tahun = df[2][i]
        qs.target_bln_lapor = df[3][i]
        qs.realisasi_sd_bln_lalu = df[4][i]
        qs.realisasi_bln_lapor = df[5][i]
        qs.realisasi_sd_bln_lapor = df[6][i]
        qs.periode = datetime.strptime(periode, "%d/%m/%Y")
        qs.user = user
        qs.save()
    
    # elif df[0][27] == "Penyesuaian / Koreksi / Alih Kepesertaan":
        # data = []
    for i in range(29,47):
        if not( i == 29 or i == 32 or i == 35 or i == 38 or i == 41 or i == 44 ):
            m_data.append(i)
    for j in range(1, len(data)+1):

        qs = TargetRealisasi()
        # ps = JenisUraian.objects.get(nama=df[0][27])
        # rs = Uraian.objects.get(nama_uraian=df[0][j+7])
        qs.jenis_id = 4
        qs.uraian_id = (j + 7)
        qs.target_tahun = df[2][m_data[j-1]]
        qs.target_bln_lapor = df[3][m_data[j-1]]
        qs.realisasi_sd_bln_lalu = df[4][m_data[j-1]]
        qs.realisasi_bln_lapor = df[5][m_data[j-1]]
        qs.realisasi_sd_bln_lapor = df[6][m_data[j-1]]
        qs.periode = datetime.strptime(periode, "%d/%m/%Y")
        qs.user = user
        qs.save()
                

    # elif df[0][47] == "Status Non Aktif":
    for i in range(48,51):
        qs = TargetRealisasi()
        # ps = JenisUraian.objects.get(nama=df[0][47])
        rs = Uraian.objects.get(nama_uraian=df[0][i])
        qs.jenis_id = 5
        qs.uraian_id = rs.pk
        qs.target_tahun = df[2][i]
        qs.target_bln_lapor = df[3][i]
        qs.realisasi_sd_bln_lalu = df[4][i]
        qs.realisasi_bln_lapor = df[5][i]
        qs.realisasi_sd_bln_lapor = df[6][i]
        qs.periode = datetime.strptime(periode, "%d/%m/%Y")
        qs.user = user
        qs.save()
    
    # elif df[0][52] == "Jumlah Penerimaan Iuran":
    for i in range(53,56):
        qs = TargetRealisasi()
        # ps = JenisUraian.objects.get(nama=df[0][52])
        rs = Uraian.objects.get(nama_uraian=df[0][i])
        qs.jenis_id = 6
        qs.uraian_id = rs.pk
        qs.target_tahun = df[2][i]
        qs.target_bln_lapor = df[3][i]
        qs.realisasi_sd_bln_lalu = df[4][i]
        qs.realisasi_bln_lapor = df[5][i]
        qs.realisasi_sd_bln_lapor = df[6][i]
        qs.periode = datetime.strptime(periode, "%d/%m/%Y")
        qs.user = user
        qs.save()

    # elif df[0][58] == "Bayar Iuran Tepat Waktu":
    for i in range(59,62):
        qs = TargetRealisasi()
        # ps = JenisUraian.objects.get(nama=df[0][58])
        rs = Uraian.objects.get(nama_uraian=df[0][i])
        qs.jenis_id = 7
        qs.uraian_id = rs.pk
        qs.target_tahun = df[2][i]
        qs.target_bln_lapor = df[3][i]
        qs.realisasi_sd_bln_lalu = df[4][i]
        qs.realisasi_bln_lapor = df[5][i]
        qs.realisasi_sd_bln_lapor = df[6][i]
        qs.periode = datetime.strptime(periode, "%d/%m/%Y")
        qs.user = user
        qs.save()
    
    # elif df[0][62] == "Data Governance-Validitas":
    for i in range(64,66):
        qs = TargetRealisasi()
        # ps = JenisUraian.objects.get(nama=df[0][62])
        rs = Uraian.objects.get(nama_uraian=df[0][i])
        qs.jenis_id = 8
        qs.uraian_id = rs.pk
        qs.target_tahun = df[2][i]
        qs.target_bln_lapor = df[3][i]
        qs.realisasi_sd_bln_lalu = df[4][i]
        qs.realisasi_bln_lapor = df[5][i]
        qs.realisasi_sd_bln_lapor = df[6][i]
        qs.periode = datetime.strptime(periode, "%d/%m/%Y")
        qs.user = user
        qs.save()
    

# def ScrapMKRO(user_pembina, kd_kantor, periode):
#     url = "http://rptserver.bpjsketenagakerjaan.go.id/reports/rwservlet/setauth?button=Submit&username=smile&password=smilekanharimu&authtype=D&mask=GQ%253D%253D&isjsp=no&database=dboltp&nextpage=destype%3Dcache%26desformat%3DPDF%26report%3DKNR8801B.rdf%26userid%3D%2Fdata%2Freports%2Fkn%26%26P_KANTOR%3D%27A02%27%26P_PEMBINA%3D%27{}%27%26P_KODE_KANTOR%3D%27{}%27%26P_PERIODE%3D%27{}%27%26P_USER%3D%27MA160540%27%26P_ROLE%3D%278%27".format(user_pembina, kd_kantor, periode)
#     data = read_pdf(url, )