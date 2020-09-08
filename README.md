Aplikacija za evidenciju radnih  sati i zadataka

Aplikaciju sam malo izmijenio od prvobitne ideje zbog kompleksnosti i samoga back end frameworka.

Web aplikacija koju može koristiti bilo tko ali je namijenjena zaposlenicima u firmama.

Aplikacija ima mogućnost registracije i prijave te omogućuje korisniku da unese početak i kraj svog radnog vremena te po tom unosu kreira se pregled u odrađenog dana, na način da radnik može vidjeti koju smjenu je odradio, da li je radio prekovremene sate i koliko. Na pregledu odrađenih sati postoji mogućnost filtriranja odrađenog dana po datumu.  Korisnik također može da kreira svoje zadatke koje može bilo kada ažurirati i brisati te ima uvid u svoje u tijeku i riješene zadatke. Korisnik može urediti podatke za svoj profil gdje ažurira svoje informacije poput: Ime, prezime, mail. naziv firme, kontakt i sl.

Korištene tehnologije su : Django kao backend, za frontend je Bootstrap, baza podataka je ugrađeni SQLite  u Djangu.

Upute za lokalno korištenje:
1. Instalirati Python 3.8.2 (64bit ili 32bit zavisno o windowsima), u powershellu ili cmd komanodm py --version možete provjeriti dali je instalacija python bila uspiješna.
2. U powershell ili cmd instalirati django komandom: py -m pip install Django
3. Komandom cd "lokacija projekta na vašem pc" to možete copy paste putanju u file exploreru.
4. Zatim aktivirati skripte komandom:  .\Scripts\activate
5. U slučaju da dođe Error : Scripts cannot be loaded ..., rjesenje je komanda : Set-ExecutionPolicy -Scope CurrentUser zatim upisati 1 i potvrditi y (yes)
6. Kada su scripte aktivirane, a to ćete znati što će ime projekta biti u zagradi na početku unesite komandu za pokretanje servera: python manage.py runserver 
7. Link adrese servere koje vam je izbacilo copy paste (http://127.0.0.1:8000/) na web i možete koristiti aplikaciju.

Admin korisnik je user: admin
                  lozinka: 11

