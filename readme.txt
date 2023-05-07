1. YÖNTEM-SANAL ORTAM İLE ÇALIŞTIRMA (WINDOWSTA TEST EDİLDİ)

- Herhangi bir editör ile (Visual Studio Code veya Pycharm veya başka bir editör) ile 
Tracks klasörü açılır. Klasör açıldıktan sonra virtual environment (sanal ortam) aktif edilmelidir.
Sanal ortamı aktif edebilmek için editörün içerisinden bir terminal açılır. Açılan terminalden
öncelikle "python get-pip.py" ile pip modülü kurulur. Bu modül kurulduktan sonra 
"pip install virtualenv" komutu çalıştırılarak sanal ortamı oluşturacak modül kurulmuş
olur. Daha sonra "virtualenv venv" komutu yazılarak tracks proje klasörününün yanında
venv adında bir sanal ortam oluşturulmuş olur. Sanal ortam oluştuktan sonra
"cd venv/Scripts" komutu yazılarak sanal ortamı aktif edebilmek için gerekli dizinin içerisine
girilmiş olur. Windowsta sanal ortamı aktif edebilmek için öncelikle
"Set-ExecutionPolicy Unrestricted -Scope Process" komutu terminalde çalıştırılır. 
Bu komut çalıştırıldıktan sonra "./activate" komutu mevcut Tracks\venv\Scripts dizini içerisinde
aynı şekilde çalıştırılır ve sanal ortam aktif edilmiş olur. Sanal ortam aktif edildikten sonra
"cd ../.." komutu ile yeniden ana Tracks klasörüne dönülür ve ardından "cd tracks"
yazılarak tracks projesinin bulunduğu dizin içerisine girilmiş olur. Bu dizin içerisinde
django projesini çalıştırabilmek için gerekli olan manage.py dosyası bulunmaktadır.
Öncelikle gerekli kütüphaneler yüklenmelidir. Bunun için bu dizin içerisinde
"pip install -r requirements.txt" komutu yazılarak proje için gerekli olan kütüphaneler (Django vb.) 
yüklenir. Kütüphaneler yüklendikten sonra aynı dizin içerisinde "python manage.py runserver" 
yazılarak proje localhost adresi üzerinde (http://127.0.0.1:8000/) çalışmaya başlar. 
Bundan sonra istediğiniz tarayıcıya girip bu adres üzerinden uygulamaya erişip test edebilirsiniz.

2. YÖNTEM-DOCKER İLE ÇALIŞTIRMA (WINDOWSTA TEST EDİLDİ, DAHA KOLAY)
- Sadece python3.9 ve pip modülünün bilgisayarda kurulu olması yeterlidir. Uygulamayı çalıştırmak
için daha kolay bir yöntemdir. Öncelikle aynı şekilde bir editör ile Tracks
klasörü açılır ve "cd tracks" ile tracks proje klasörünün içerisine girilir. Burada 
projeyi docker üzerinde ayağa kaldırabilmek için Dockerfile ve docker-compose.yml adlı 
iki dosya mevcuttur. Yapılması gereken tek şey terminale "\Tracks\tracks>" dizini içerisinde
"docker-compose up --build" komutunun girilmesidir. Bu komut bu dizin içerisinde girildiğinde
proje otomatik olarak dockerda ayağa kalkmış olacaktır. Aynı şekilde herhangi bir tarayıcıdan
localhost adresi (http://127.0.0.1:8000/) üzerinden uygulamaya erişip test edebilirsiniz.

NOT: Komutları çalıştırırken "" (tırnak) işaretlerini ihmal ediniz. Komutları net bir şekilde
belirtebilmek için bu işaretler kullanıldı.


 