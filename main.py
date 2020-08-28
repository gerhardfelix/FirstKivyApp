from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import urllib3
import certifi
import simplejson as json

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

class HomeWindow(Screen):
    def createBtn(self):
        sm.current = "create"
    def searchBtn(self):
        MainApp.search(self)
    def editBtn(self):
        MainApp.editsave(self)
#    url = 'firebaseurl/.json'

class CreateWindow(Screen):
    def c_backBtn(self):
        sm.current = "home"
    def c_saveBtn(self):
        MainApp.savenew(self)
#    url = 'firebaseurl/.json'

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")

sm = WindowManager()

screens = [HomeWindow(name="home"),CreateWindow(name="create")]
for screen in screens:
    sm.add_widget(screen)

sm.current: "home"

class MainApp(App):

 #   url = 'firebaseurl/.json'
 
    def build(self):
        return sm

    def on_pause(self):
        return True

    def search(self):
        kode=self.ids['kodehome_txt'].text
        r = http.request('GET', self.url)
        hasil=json.loads(r.data.decode('utf-8'))
        self.ids['namahome_txt'].text=hasil[kode]['nama']
        self.ids['alamathome_txt'].text=hasil[kode]['alamat']
        self.ids['kotahome_txt'].text=hasil[kode]['kota']
        self.ids['wilayahhome_txt'].text=hasil[kode]['wilayah']
        self.ids['telphome_txt'].text=hasil[kode]['telp']
        self.ids['faxhome_txt'].text=hasil[kode]['fax']
        self.ids['npwphome_txt'].text=hasil[kode]['npwp']
        self.ids['kontakhome_txt'].text=hasil[kode]['kontak']
        self.ids['jatemhome_txt'].text=hasil[kode]['jatem']
        self.ids['saleshome_txt'].text=hasil[kode]['sales']
        self.ids['carabyrhome_txt'].text=hasil[kode]['carabyr']
        self.ids['kethome_txt'].text=hasil[kode]['ket']
        self.ids['alfakturhome_txt'].text=hasil[kode]['alfaktur']
        self.ids['altagihhome_txt'].text=hasil[kode]['altagih']
        self.ids['kotfakturhome_txt'].text=hasil[kode]['kotfaktur']
        self.ids['namanotahome_txt'].text=hasil[kode]['namanota']
        self.ids['alnotahome_txt'].text=hasil[kode]['alnota']
        self.ids['kotnotahome_txt'].text=hasil[kode]['kotnota']
        self.ids['kremithome_txt'].text=hasil[kode]['kremit']

    def savenew(self):
        kode = self.ids['kodenew_txt'].text
        nama = self.ids['namanew_txt'].text
        alamat = self.ids['alamatnew_txt'].text
        kota = self.ids['kotanew_txt'].text
        wilayah = self.ids['wilayahnew_txt'].text
        telp = self.ids['telpnew_txt'].text
        fax = self.ids['faxnew_txt'].text
        npwp = self.ids['npwpnew_txt'].text
        kontak = self.ids['kontaknew_txt'].text
        jatem = self.ids['jatemnew_txt'].text
        sales = self.ids['salesnew_txt'].text
        carabyr = self.ids['carabyrnew_txt'].text
        ket = self.ids['ketnew_txt'].text
        alfaktur = self.ids['alfakturnew_txt'].text
        altagih = self.ids['altagihnew_txt'].text
        kotfaktur = self.ids['kotfakturnew_txt'].text
        namanota = self.ids['namanotanew_txt'].text
        alnota = self.ids['alnotanew_txt'].text
        kotnota = self.ids['kotnotanew_txt'].text
        kremit = self.ids['kremitnew_txt'].text
        

        konten={}
        konten['nama'] = nama 
        konten['alamat'] = alamat
        konten['kota'] = kota
        konten['wilayah'] = wilayah
        konten['telp'] = telp
        konten['fax'] = fax
        konten['npwp'] = npwp
        konten['kontak'] = kontak
        konten['jatem'] = jatem
        konten['sales'] = sales
        konten['carabyr'] = carabyr
        konten['ket'] = ket
        konten['alfaktur'] = alfaktur
        konten['altagih'] = altagih
        konten['kotfaktur'] = kotfaktur
        konten['namanota'] = namanota
        konten['alnota'] = alnota
        konten['kotnota'] = kotnota
        konten['kremit'] = kremit
      
        arsip={}
        arsip[kode]=konten
        stiker=json.dumps(arsip).encode('utf-8')
        r = http.request('PATCH', self.url, body=stiker, headers={'Content-Type': 'application/json'})
        self.ids['kodenew_txt'].text=''
        self.ids['namanew_txt'].text=''
        self.ids['alamatnew_txt'].text=''
        self.ids['kotanew_txt'].text=''
        self.ids['wilayahnew_txt'].text=''
        self.ids['telpnew_txt'].text=''
        self.ids['faxnew_txt'].text=''
        self.ids['npwpnew_txt'].text=''
        self.ids['kontaknew_txt'].text=''
        self.ids['jatemnew_txt'].text=''
        self.ids['salesnew_txt'].text=''
        self.ids['carabyrnew_txt'].text=''
        self.ids['ketnew_txt'].text=''
        self.ids['alfakturnew_txt'].text=''
        self.ids['altagihnew_txt'].text=''
        self.ids['kotfakturnew_txt'].text=''
        self.ids['namanotanew_txt'].text=''
        self.ids['alnotanew_txt'].text=''
        self.ids['kotnotanew_txt'].text=''
        self.ids['kremitnew_txt'].text=''

    def editsave(self):
        kode = self.ids['kodehome_txt'].text
        nama = self.ids['namahome_txt'].text
        alamat = self.ids['alamathome_txt'].text
        kota = self.ids['kotahome_txt'].text
        wilayah = self.ids['wilayahhome_txt'].text
        telp = self.ids['telphome_txt'].text
        fax = self.ids['faxhome_txt'].text
        npwp = self.ids['npwphome_txt'].text
        kontak = self.ids['kontakhome_txt'].text
        jatem = self.ids['jatemhome_txt'].text
        sales = self.ids['saleshome_txt'].text
        carabyr = self.ids['carabyrhome_txt'].text
        ket = self.ids['kethome_txt'].text
        alfaktur = self.ids['alfakturhome_txt'].text
        altagih = self.ids['altagihhome_txt'].text
        kotfaktur = self.ids['kotfakturhome_txt'].text
        namanota = self.ids['namanotahome_txt'].text
        alnota = self.ids['alnotahome_txt'].text
        kotnota = self.ids['kotnotahome_txt'].text
        kremit = self.ids['kremithome_txt'].text
        

        konten={}
        konten['nama'] = nama 
        konten['alamat'] = alamat
        konten['kota'] = kota
        konten['wilayah'] = wilayah
        konten['telp'] = telp
        konten['fax'] = fax
        konten['npwp'] = npwp
        konten['kontak'] = kontak
        konten['jatem'] = jatem
        konten['sales'] = sales
        konten['carabyr'] = carabyr
        konten['ket'] = ket
        konten['alfaktur'] = alfaktur
        konten['altagih'] = altagih
        konten['kotfaktur'] = kotfaktur
        konten['namanota'] = namanota
        konten['alnota'] = alnota
        konten['kotnota'] = kotnota
        konten['kremit'] = kremit
      
        arsip={}
        arsip[kode]=konten
        stiker=json.dumps(arsip).encode('utf-8')
        http.request('PATCH', self.url, body=stiker, headers={'Content-Type': 'application/json'})
        r = http.request('PATCH', self.url, body=stiker, headers={'Content-Type': 'application/json'})
        hasil=json.loads(r.data.decode('utf-8'))
        self.ids['namahome_txt'].text=hasil[kode]['nama']
        self.ids['alamathome_txt'].text=hasil[kode]['alamat']
        self.ids['kotahome_txt'].text=hasil[kode]['kota']
        self.ids['wilayahhome_txt'].text=hasil[kode]['wilayah']
        self.ids['telphome_txt'].text=hasil[kode]['telp']
        self.ids['faxhome_txt'].text=hasil[kode]['fax']
        self.ids['npwphome_txt'].text=hasil[kode]['npwp']
        self.ids['kontakhome_txt'].text=hasil[kode]['kontak']
        self.ids['jatemhome_txt'].text=hasil[kode]['jatem']
        self.ids['saleshome_txt'].text=hasil[kode]['sales']
        self.ids['carabyrhome_txt'].text=hasil[kode]['carabyr']
        self.ids['kethome_txt'].text=hasil[kode]['ket']
        self.ids['alfakturhome_txt'].text=hasil[kode]['alfaktur']
        self.ids['altagihhome_txt'].text=hasil[kode]['altagih']
        self.ids['kotfakturhome_txt'].text=hasil[kode]['kotfaktur']
        self.ids['namanotahome_txt'].text=hasil[kode]['namanota']
        self.ids['alnotahome_txt'].text=hasil[kode]['alnota']
        self.ids['kotnotahome_txt'].text=hasil[kode]['kotnota']
        self.ids['kremithome_txt'].text=hasil[kode]['kremit']

if __name__ == '__main__':
    MainApp().run()
