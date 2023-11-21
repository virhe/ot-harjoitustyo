## Monopoli, alustava luokkakaavio

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- SattumaJaYhteismaa
    Ruutu <|-- AsemaJaLaitos
    Ruutu <|-- Katu
    Katu "1" -- "1" Nimi
    Katu "1" -- "0..1" Hotelli
    Katu "1" -- "0..4" Talo
    Katu "1" -- "0..1" Pelaaja
    Ruutu "1" -- "1" Toiminto
    SattumaJaYhteismaa "1" -- "n" Kortti
    Kortti "1" -- "1" Toiminto
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja : raha
```