import pytube

#pobieranie bezpieczne, bez wirusow itd, lepiej niz ze stronki

yt = pytube.YouTube('https://www.youtube.com/watch?v=gMyjb77WAPw')

yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download() #z wizual
yt.streams.filter(only_audio=True).first().download() #z tylko dzwiek
#yt.streams.filter(only_audio=True).first().download('E:\\...') #z tylko dzwiek, mozna sobei wskazac inna sciezke zapisu
#yt.streams.filter(file_extension='mp4').all().download('E:\\...') #pobierze wszystkie rozdzielczosci



#yt = pytube.YouTube('https://www.youtube.com/watch?v=4V2C0X4qqLY')
#yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()


#
# import pytube
#
# yt = pytube.YouTube('https://www.youtube.com/watch?v=4V2C0X4qqLY')
# yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()

# yt.streams.filter(only_audio=True).first().download("E:\\")
# yt.streams.filter(file_extension='mp4').all()

