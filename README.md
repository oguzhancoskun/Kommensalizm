# Kommensalizm
##Digitalocan ölücü projesi

Digitalocean'dan bedava faydalanmanın yolları, Kommensalist bir ilişki.

Beni bu yola sürükleyen;
- Digitaloceanın her yeni üyelikte verdiği $10 dolar,
- Başka hesaba snapshot transferi
 sonuç: sonsuz elektrik.
 
###Bağımlılıklar,
- Mail sunucu ve şahsınıza ait domain adresi,
- Kişisel hesabınızı kullanmayın diye yeni bir gmail adresi,
- Sanal kart bilgileri (üyelikte digitalocean a tanıtmak için)

###Workflow
- Digitaloceanda halihazırda bulunan sunucunuzda dalgic projesini crona bağlayın, örneğin ayda bir çalışsın.
- cron tetiklendiğinde öncelikle postfix e yeni bir mail alias tanımlayacak, bu aliası fake gmail adresinize forward edecek.
- Selenium scripti digitalocean a kaydolup doğrulama mailini bu mail adresine gönderecek, mail adresi fake gmail adresine forward edecek,
- Script bu sefer gmail api ile digitaloceandan gelen maili parse edecek ve aktivasyonu tamamlayacak.
- Script devam edip digitalocean a kart bilgilerinizi girecek ve promo kodu tanımlayacak, yeni hesap tamam.

- İkinci adımda eski hesaptaki dropletin snapshotı alınacak ve yeni hesapla paylaşılacak,
- yeni hesaptan bu droplet onaylanıp (do api aracılığıyla) droplet başlatılacak.
- Aynı işlemler NS için de yapılandırılacak.

Bu script çalıştıkça digitalocean ile aranızda Kommensalist bir ilişki kurulmuş olacak.
