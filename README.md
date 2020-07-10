Aplikacija za evidenciju radnih  sati i zadataka

Aplikaciju sam malo izmijenio od prvobitne ideje zbog kompleksnosti i samoga back end frameworka.

Web aplikacija koju može koristiti bilo tko ali je namijenjena zaposlenicima u firmama.

Aplikacija ima mogućnost registracije i prijave te omogućuje korisniku da unese početak i kraj svog radnog vremena te po tom unosu kreira se pregled u odrađenog dana, na način da radnik može vidjeti koju smjenu je odradio, da li je radio prekovremene sate i koliko. Na pregledu odrađenih sati postoji mogućnost filtriranja odrađenog dana po datumu.  Korisnik također može da kreira svoje zadatke koje može bilo kada ažurirati i brisati te ima uvid u svoje u tijeku i riješene zadatke. Korisnik može urediti podatke za svoj profil gdje ažurira svoje informacije poput: Ime, prezime, mail. naziv firme, kontakt i sl.

Korištene tehnologije su : Django kao backend, za frontend je Bootstrap, baza podataka je ugrađeni SQLite  u Djangu.

Upute za lokalno korištenje:

Aplikacija se koristi tako što se preuzme i instalira sa svim dodacima Python verzija 3.8.3, te se onda u terminali dali cmd ili powershell komandom pip install django instalira django. Nakon toga se treba instalirati virtualno okruženje preko komande pip install virtualenv uazim se u mapi u kojoj želite da se pokreće projekt treba se prvo preko cd ući u nju te onda komandom virutalenv . kreirati tamo virtrualno okruženje. Onda se može u tom folderu gdje se pokreće projekt napraviti novi folder npr. src i unjega kopirati sve što se nalazilo u mom src folderu. Onda u terminalu preko cd ulazi u lokaciju foldera projekta, te se aktivira virtualno okruženje preko ./Scripts/activate te onda cd src ako se tako folder zove i upiše se komanda py manage.py runserver za pokretanje servera kojim možemo aplikaciju vidjeti putem web preglednika na adresi http://127.0.0.1:8000/

Admin korisnik je user: admin
                  lozinka: 11

