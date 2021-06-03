# Autoilumittari

### Solidabis koodihaaste 2021: "autoilumittari"

webapp -> https://mokkimatkamittari.herokuapp.com

### Käytetyt teknologiat
- Python 3.9.5
- Flask + Flask_wtf (forms)
- HTML + CSS

### Asennus ja käynnistäminen

        > git clone https://github.com/ssillanp/Autoilumittari.git
        > pip install -r requirements.txt

testikäytössä yksinkertaisesti flask development serverillä 

        > python run.py

tai tuotannossa 

        > gunicorn --workers=2 run:app

### Kuvaus tehdystä ratkaisusta

- Python toteutus, auto- ja laskenta toteutettu python luokkina.
    - car-luokka: Malli- ja kulutustiedot
    - trip-luo0kka: 
- Web toteutus Python Flask- ja Flask_wtf-kirjastoilla.
- Sivu HTML templatena ja ulkonäkö CSS
- Tuotantoserverinä gunicorn.













