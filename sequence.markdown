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


