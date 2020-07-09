Aplikacija za evidenciju radnih  sati i zadataka

Aplikaciju sam malo izmijenio od prvobitne ideje zbog kompleksnosti i samoga back end frameworka.

Web aplikacija koju može koristiti bilo tko ali je namijenjena zaposlenicima u firmama.

Aplikacija ima mogućnost registracije i prijave te omogućuje korisniku da unese početak i kraj svog radnog vremena te po tom unosu kreira se pregled u odrađenog dana, na način da radnik može vidjeti koju smjenu je odradio, da li je radio prekovremene sate i koliko. Na pregledu odrađenih sati postoji mogućnost filtriranja odrađenog dana po datumu.  Korisnik također može da kreira svoje zadatke koje može bilo kada ažurirati i brisati te ima uvid u svoje u tijeku i riješene zadatke. Korisnik može urediti podatke za svoj profil gdje ažurira svoje informacije poput: Ime, prezime, mail. naziv firme, kontakt i sl.

Korištene tehnologije su : Django kao backend, za frontend je Bootstrap, baza podataka je ugrađeni SQLite  u Djangu.

Upute za lokalno korištenje:

Aplikacija se pokreće tako što je na računalu prvo instaliran python 3.8.3 te pip za django, treba skinuti fileove projekta i također je potrebno putem pipa instalirati virtualno okruženje putem komande pip install virtualenv.
Zatim se u mapi u kojoj će se pokretati projekt napravi virtual enviroment putem komande virtualenv .(potrebno staviti ovaj razmak i točku).
Nakon toga se kreira u toj istoj mapi još jedna mapa(recimo src) i unutra se postave fileovi projekta koji su skinuti.
Kada ste sa cmd-om ili powershellom u root folderu gdje su mape lib i scripts od virtualenva pokrene se komanda ./Scripts/activate 
time ulazite u virtualni enviroment. Nakon toga se piše komanda cd src te nakon toga pip install -r requirements.txt
Nakon toga se aplikacija pokreće sa komandom py manage.py runserver.
Aplikaciji se može pristupiti na localhost:8000.

