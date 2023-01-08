#MEHMET ERTAN 203405027
import snscrape.modules.twitter as sntwitter

import pandas as pd
# sorguyu oluşturdum twitter search kısmında kullanılan sorgu tipi
query="yılmaz until:2022-11-28 since:2022-11-26"
tweets = []
limit=1000

#sorgu döngüsünü başlat  
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
 
       if len(tweets)==limit:
           break
        #belirlenen limite ulaştığında döngüyü kır
        
       else:
           tweets.append(tweet.content)

           df =pd.DataFrame(tweets, columns=['tweet'])
    #limite ulaşana kadar tweetleri listeye ekle

print(df)


counter = 0


for tweet in tweets:
    if "ilkkan" in tweet or "gibi" in tweet or "ersoy" in tweet or "Gibi" in tweet or "Ersoy" in tweet or "İlkkan" in tweet or "Feyyaz" in tweet or "feyyaz" in tweet:
        counter += 1
        #aradığımız kelimelerin ilk harfkerini küçük yazdığımızda %0 değer verebiliyorken ilk harflerini büyük yapınca anahtar kelimeleri içeren oran arttı

print('anahtar kelimeleri içeren tweet oranı %',(counter/limit)*100)

#rating systemi oluşturdum puanlamaları yaptım
rating_system = {
    "gibi": 10,
    "ilkkan": 9,
    "ersoy": 9,
    "Gibi": 10,
    "İlkkan": 9,
    "Feyyaz": 8,
    "feyyaz": 8,
    "Ersoy": 9
}


scores = []
#skor dizisini oluşturdum kelimeleri tweetler içerisinde bulunma durumuna göre puanladım
for tweet in tweets:
    total_score = 0
    for word, score in rating_system.items():
        if word in tweet:
            total_score += score
    scores.append(total_score)

#her tweet için ortalama derecelendirme
average_ratings = [score /len(tweets) for score in scores]#ortalama derecelendirmelerini hesapla
ratings_puanı = [score /1 for score in scores]#rating puanını hesapla

print('ortalama averaj',average_ratings)
print('------------------------------------------------------------------------------------------------------')

print('rating puanları',ratings_puanı)
"bu kodda belli tarihler arasında paylaşılmış yılmaz kelimesini içeren tweetlerin Gibi dizisi ile alakalarını bulmaya çalıştım."
"öncelikle tweetleri  çekip bir tweet listesine kaydettim"
"sonrasında belirlediğim bazı anahtar kelimelerin bu tweetler içindeki oranına baktım"
"oluşturduğum rating systemde bu anahtar kelimelere puanlar verip ortalama derecelendirmelerini hesapladım"
"ayrıca her birinin rating puanınıda hesapladım"
"****anahtar kelimelerin ilk harflerinin küçük veya büyük olma durumuna göre oranlar değişebildiği için iki seçeneği de denedim****"

