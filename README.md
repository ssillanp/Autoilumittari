# Autoilumittari

### Solidabis koodihaaste 2021: "autoilumittari"

webapp -> https://mokkimatkamittari.herokuapp.com


### Käytetyt teknologiat
- Python 3.9.5
- Flask + Flask_wtf (forms)
- HTML + CSS

### Asennus ja käynnistäminen

Vaatii myös python asennuksen, mikäli ei asennettuna (https://www.python.org/downloads/)

        > git clone https://github.com/ssillanp/Autoilumittari.git
        > pip install -r requirements.txt

testikäytössä yksinkertaisesti flask development serverillä 

        > python run.py

tai tuotannossa 

        > gunicorn --workers=2 run:app

### Kuvaus tehdystä ratkaisusta

- Python toteutus, auto- ja laskenta toteutettu python luokkina.
    - car-luokka: sisältää automallin ja kulutustiedot, sekä kulutuskertoimen
    - trip-luokka: retken pituus, nopeus ja käytetty automalli. Laskee kulutuksen ja käyutetyn ajan. Lisäksi laskenta kahden reissun erotukselle, kulutus ja matka-ajassa, sekä co2 emissiot.
- Web toteutus Python Flask- ja Flask_wtf-kirjastoilla.
- Sivu HTML templatena ja ulkonäkö CSS
- Tuotantoserverinä gunicorn.













