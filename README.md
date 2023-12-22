# TETRIS-PELI

Sovellluksen avulla käyttäjän on mahdollista pelata alkeellista Tetris-peliä.

## Dokumentaatio

* [Työaikakirjanpito](tetris/dokumentaatio/tuntikirjanpito.md)

* [Määrittelydokumentti](tetris/dokumentaatio/maarittelydokumentti.md)

* [Changelog](tetris/dokumentaatio/changelog.md)

## Release

* [Viikko 5 Release](https://github.com/mkekola/Ohjelmistotekniikka/releases/tag/viikko5)

## Komennot

**Suoritetaan tetris-hakemistossa**

### Asennus

```bash
poetry init --python "^3.8"
```

```bash
poetry install
```

```bash
poetry add invoke
```

### Tetris-pelin suoritus

```bash
poetry run invoke start
```

### Testien suoritus

```bash
poetry run invoke test
```

### Testien kattavuus html

```bash
poetry run invoke coverage-report
```

### Pylint tarkastus

```bash
poetry run invoke lint
```
