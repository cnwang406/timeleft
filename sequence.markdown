sequence.markdown
# Setup Environment
## development environment :
### - IDE
- VSCODE for Windows *DONE*
### - packages

### - Python
- Version 3.9  *DONE*
- venv : `work` setup *DONE*
```
virtualenv work
```


# understand where data come from:
## opendata
很多政府機關的公開資料是放在網路上可取得,包括氣象局(天氣預報,溫度....), 地政事務所(土地行政區), 水利局(水文資料), __交通部(鐵公路班資訊,例如位置,站牌,車站資訊)__

這些資訊都放在 https://ptx.transportdata.tw

## 如何取得?
### API (application Protocol Interface)
API 是個很簡單的介面. 就是藉由網址列 裡面這串有意義的網址, 按下SEND 伺服器會拆解這些網址各段資訊, 經過運算後將資料再傳給我們, 如果用 CHROME 瀏覽器, 資訊就會在瀏覽器上以特殊的格式(json) 出現. 同時會有簡單的代碼告訴瀏覽器結果. 例如 200 - ok, 404 - 找不到網頁

### json (JavaScript Object Notation)
使用 {},[],KEY:VALUE 等樣子將資訊傳回來. 比如說
```
{
    [
        "學號":001
        "名字":xxx
    ],
    [
        "學號":002
        "名字":yyy
    ]
}
```
因為格式固定, 所以很容易拆解. 一般來說API 的說明網頁都會先講好會傳回什麼欄位跟資訊, 也不太會隨便變動.


# 我們需要的資料
因為我想同時看離我最近的車站(新竹車站) 跟我可以搭的公車(綠線) 看誰先到站, 所以要同時查詢
## 綠線到達的時間 
  不過因為公車沒有提供即時的站點相關資訊, 我只能查到公車目前距離我多遠還有速度. 這部分由 
[取得指定{縣市},{路線名稱}的公車動態定時資料(A1){逐筆更新}](https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeByFrequency/Streaming/City/{City}/{RouteName})
可以取得. 我是取用了裡面的車牌, 位置(換算成距離), 還有方向及速度

**後來我發現還真的有這樣的 API. 一開始漏掉了**

[取得指定{縣市},{路線名稱}的公車動態定點資料(A2){逐筆更新}](https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeNearStop/Streaming/City/{City}/{RouteName})

  等有空時再來改

## 火車到達的時間

有兩個部分可以查詢

1. 查詢 新竹站(ID:1210)的時刻表 (DailyStationTimetable)
[取得當天指定{車站}的時刻表資料] (https://ptx.transportdata.tw/MOTC/v3/Rail/TRA/DailyStationTimetable/Today/Station/{StationID})

這個可以取得當站的列車時刻 . 不過我發現沒有下面那個好用

2. 查詢 新竹站 的 即時時刻表 (StationLiveBoard). 
[取得指定車次的列車即時位置動態資料] (https://ptx.transportdata.tw/MOTC/v3/Rail/TRA/TrainLiveBoard/TrainNo/{TrainNo})
這個可以取得延誤的時間


# 執行結果

## 在 notebook 上用終端機/cmd 執行
```
start
my location : [ 24.8019,120.9714]

=====  BUS  ===== (refresh every 20sec)
bus 綠線 (821-U7) at [  24.8152,  120.988] 時速 43.0 km/h
 距離  1.99 km, 開向 265.0度
 direction is 經國路往香山, transtime 2021-07-19 07:34:15+08:00 status:開始/正常
bus 綠線 (851-U7) at [  24.8123,  120.981] 時速 0.0 km/h
 距離  1.25 km, 開向 55.0度
 direction is 香山往經國路, transtime 2021-07-19 07:34:13+08:00 status:開始/正常

===== TRAIN =====
車號  2008(區間快) 往 基隆(逆), 預計離站 2021-07-19 07:38:00, 延誤   0 min, status = 準點
車號   103(自強 ) 往 潮州(順), 預計離站 2021-07-19 07:36:00, 延誤   0 min, status = 準點
TRA service is normal
finished
```

## 在手機上執行

這才是我需要的. 不過 iphone 不能方便的開啟終端機, 雖然可以連線遠端的終端機, 還是不方便. 我又還不會使用像 linebot 或者 telegrambot 這種方式讓資料在遠端伺服器查詢後將答案送回來. 還好後來找到一個不錯的app `pythonista` . 這個可以讓我把程式碼放在手機裡面直接執行. 缺點是很多的功能不能用. 不過後來發現我的要求太簡單了, 用基本的 package 就可以了
所以只需要在程式一開始判斷一下我是用 筆電桌機 還是 iphone 就可以知道怎麼取得現在位置

```
using iPhone
start
my location : [ 24.7765,120.9979]

=====  BUS  ===== (refresh every 20sec)
bus 綠線 (821-U7) at [  24.8031,  120.971] 時速 24.0 km/h
 距離  3.34 km, 開向 161.0度
 direction is 經國路往香山, transtime 2021-07-19 07:45:55+08:00 status:開始/正常
bus 綠線 (851-U7) at [  24.8188,  120.993] 時速 0.0 km/h
 距離  2.47 km, 開向 35.0度
 direction is 經國路往香山, transtime 2021-07-19 07:40:34+08:00 status:開始/正常

===== TRAIN =====
車號  2120(區間 ) 往 基隆(逆), 預計離站 2021-07-19 07:51:00, 延誤   0 min, status = 準點
TRA service is normal
finished
```