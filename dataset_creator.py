import json

from os import curdir

def read(file):
    with open(file, "rb") as f:
        return f.read().decode("UTF-8")

def write(file, data):
    with open(file, "wb") as f:
        f.write(data.encode("UTF-8"))

json_doc = {
        "jr1": {
            "txt0": "bemühen\nBiene\nbreitschlagen\nglühen\nhersagen\nHygiene\nKnecht\nRecht\nSchiene\nschlank\nSchwank",
            "txt1": "Absorption\nBildnis\nBrote\nGeständnis\nKonsumption\nNote\nPaprikaschote\nWildnis\nXOR-Funktion",
            "txt2": "Epsilon\nFoto\nPassfoto \nPoststempel\nTempel\nYpsilon",
            "txt3": "Ärger\nÄrztin\nAbend\nAbfahrt\nAbflug\nAbsender\nAdresse\nAlter\nAmpel\nAnfang\nAngebot\nAngestellte\nAngst\nAnkunft\nAnmeldung\nAnrede\nAnruf\nAnrufbeantworter\nAnsage\nAnschluss\nAntwort\nAnzeige\nAnzug\nApfel\nApotheke\nAppartement\nAppetit\nApril\nArbeit\nArbeitsplatz\nArm\nArzt\nAufenthalt\nAufgabe\nAufzug\nAuge\nAugust\nAusbildung\nAusflug\nAusgang\nAuskunft\nAusländer\nAusländerin\nAusland\nAussage\nAusstellung\nAusweis\nAuto\nAutobahn\nAutomat\nBäckerei\nBüro\nBaby\nBad\nBahn\nBahnhof\nBahnsteig\nBalkon\nBanane\nBank\nBatterie\nBaum\nBeamte\nBeamtin\nBein\nBeispiel\nBekannte\nBenzin\nBeratung\nBerg\nBeruf\nBerufsschule\nBesuch\nBetrag\nBett\nBewerbung\nBier\nBild\nBildschirm\nBirne\nBitte\nBlatt\nBleistift\nBlick\nBlume\nBluse\nBlut\nBogen\nBohne\nBrötchen\nBrücke\nBrief\nBriefkasten\nBriefmarke\nBrieftasche\nBriefumschlag\nBrille\nBrot\nBruder\nBuch\nBuchstabe\nBus\nButter\nCafé\nCD\nCD-ROM\nChef\nComputer\nCreme\nDach\nDame\nDank\nDatum\nDauer\nDeutsche\nDezember\nDienstag\nDing\nDisco\nDoktor\nDom\nDonnerstag\nDoppelzimmer\nDorf\nDrucker\nDurchsage\nDurst\nDusche\nE-Mail\nEcke\nEhefrau\nEhemann\nEi\nEinführung\nEingang\nEinladung\nEintritt\nEinwohner\nEinzelzimmer\nEis\nEltern\nEmpfänger\nEmpfang\nEnde\nEnkel\nEntschuldigung\nErdgeschoss\nErfahrung\nErgebnis\nErlaubnis\nErmäßigung\nErwachsene\nEssen\nExport\nFähre\nFührerschein\nFührung\nFabrik\nFahrer\nFahrkarte\nFahrplan\nFahrrad\nFamilie\nFamilienname\nFamilienstand\nFarbe\nFax\nFebruar\nFehler\nFenster\nFerien\nFernsehgerät\nFest\nFeuer\nFeuerwehr\nFeuerzeug\nFieber\nFilm\nFirma\nFisch\nFlasche\nFleisch\nFlughafen\nFlugzeug\nFlur\nFluss\nFormular\nFoto\nFotoapparat\nFrühjahr\nFrühling\nFrühstück\nFrage\nFrau\nFreitag\nFreizeit\nFreund\nFreundin\nFriseur\nFrist\nFuß\nFußball\nFundbüro\nGabel\nGarage\nGarten\nGas\nGast\nGebühr\nGeburtsjahr\nGeburtsort\nGeburtstag\nGegenteil\nGeld\nGeldbörse\nGemüse\nGepäck\nGericht\nGesamtschule\nGeschäft\nGeschenk\nGeschirr\nGeschwister\nGesicht\nGespräch\nGesundheit\nGetränk\nGewicht\nGewitter\nGlück\nGlückwunsch\nGlas\nGleis\nGoethe-Institut\nGröße\nDie Grenze\nGrippe\nGroßeltern\nGroßmutter\nGroßvater\nGruß\nGrundschule\nGruppe\nGuthaben\nGymnasium\nHähnchen\nHaar\nHalbpension\nHalle\nHals\nHaltestelle\nHand\nHandtuch\nHandy\nHaus\nHausaufgabe\nHausfrau\nHaushalt\nHausmann\nHeimat\nHeizung\nHemd\nHerbst\nHerd\nHerr\nHerz\nHilfe\nHobby\nHolz\nHose\nHund\nHunger\nIdee\nImport\nIndustrie\nInformation\nInhalt\nInternet\nJacke\nJahr\nJanuar\nJob\nJugendherberge\nJugendliche\nJuli\nJunge\nJuni\nKäse\nKörper\nKüche\nKühlschrank\nKündigung\nKaffee\nKalender\nKamera\nKanne\nKarte\nKartoffel\nKasse\nKassette\nKassettenrecorder\nKatze\nKeller\nKellner\nKenntnisse\nKennzeichen\nKette\nKfz\nKind\nKindergarten\nKinderwagen\nKino\nKiosk\nKirche\nKlasse\nKleid\nKleidung\nKneipe\nKoffer\nKollege\nKollegin\nKonsulat\nKontakt\nKonto\nKontrolle\nKonzert\nKopf\nKosmetik\nKrankenkasse\nKrankheit\nKredit\nKreditkarte\nKreis\nKreuzung\nKuchen\nKugelschreiber\nKunde\nKundin\nKurs\nLöffel\nLösung\nLaden\nLager\nLampe\nLand\nLandschaft\nLeben\nLebensmittel\nLeid\nLehre\nLehrer\nLehrerin\nLeute\nLicht\nLied\nLkw\nLoch\nLohn\nLokal\nLuft\nLust\nMädchen\nMärz\nMöbel\nMüll\nMülltonne\nMagen\nMai\nMal\nMann\nMantel\nMarkt\nMaschine\nMaterial\nMechaniker\nMedikament\nMeer\nMehrwertsteuer\nMeinung\nMenge\nMensch\nMesser\nMetall\nMiete\nMilch\nMinute\nMittag\nMitte\nMitteilung\nMittel\nMittelschule\nMittwoch\nMode\nMoment\nMonat\nMontag\nMorgen\nMotor\nMund\nMuseum\nMusik\nMutter\nNähe\nNachbar\nNachbarin\nNachmittag\nNachrichten\nNacht\nName\nNatur\nNebel\nNorden\nNotarzt\nNote\nNotfall\nNotiz\nNovember\nNudel\nNummer\nOber\nObst\nOktober\nOma\nOpa\nOperation\nOrange\nOrdnung\nOrt\nOsten\nÖl\nPäckchen\nPaket\nPanne\nPapier\nPapiere\nParfüm\nPark\nPartei\nPartner\nPartnerin\nParty\nPass\nPause\nPension\nPkw\nPlan\nPlastik\nPlatz\nPolizei\nPommes frites\nPortion\nPost\nPostleitzahl\nPrüfung\nPraktikum\nPraxis\nPreis\nProblem\nProdukt\nProgramm\nProspekt\nPullover\nQualität\nQuittung\nRücken\nRabatt\nRadio\nRathaus\nRaucher\nRaucherin\nRaum\nRealschule\nRechnung\nRegen\nReifen\nReinigung\nReis\nReise\nReisebüro\nReiseführer\nReparatur\nRestaurant\nRezept\nRezeption\nRind\nRock\nRose\nRundgang\nSüden\nS-Bahn\nSache\nSaft\nSalat\nSalz\nSamstag\nSatz\nSchüler\nSchülerin\nSchalter\nScheckkarte\nSchiff\nSchild\nSchinken\nSchirm\nSchlüssel\nSchloss\nSchluss\nSchmerzen\nSchnee\nSchnupfen\nSchokolade\nSchrank\nSchuh\nSchule\nSchwein\nSchwester\nSchwimmbad\nSee\nSehenswürdigkeit\nSeife\nSekretärin\nSekunde\nSendung\nSenioren\nSeptember\nService\nSessel\nSofa\nSohn\nSommer\nSonderangebot\nSonne\nSonntag\nSorge\nSpülmaschine\nSpaß\nSpaziergang\nSpeisekarte\nSpielplatz\nSprache\nSprachschule\nSprechstunde\nStück\nStadt\nStandesamt\nStempel\nSteuer\nStock\nStoff\nStraße\nStraßenbahn\nStrand\nStreichholz\nStrom\nStudent\nStudentin\nStudium\nStuhl\nStunde\nSupermarkt\nSuppe\nTür\nTüte\nTag\nTankstelle\nTasche\nTasse\nTaxi\nTee\nTeil\nTelefon\nTelefonbuch\nTeller\nTeppich\nTermin\nTest\nText\nTheater\nThema\nTicket\nTier\nTipp\nTisch\nTochter\nToilette\nTomate\nTopf\nTourist\nTreppe\nTrinkgeld\nTurm\nU-Bahn\nUhr\nUnfall\nUniversität\nUnterhaltung\nUnterkunft\nUnterricht\nUnterschied\nUnterschrift\nUntersuchung\nUrlaub\nÜbernachtung\nVater\nVerbindung\nVerein\nVerkäufer\nVerkäuferin\nVerkehr\nVermieter\nVersicherung\nVerspätung\nVertrag\nVideo\nVogel\nVolksschule\nVormittag\nVorname\nVorsicht\nVorwahl\nWäsche\nWagen\nWald\nWasser\nWeg\nWein\nWelt\nWerkstatt\nWerkzeug\nWesten\nWetter\nWiederhören\nWiedersehen\nWind\nWinter\nWirtschaft\nWoche\nWochenende\nWochentag\nWohnung\nWolke\nWort\nWunsch\nWurst\nZahl\nZahn\nZeit\nZeitschrift\nZeitung\nZentrum\nZettel\nZeugnis\nZigarette\nZimmer\nZitrone\nZoll\nZucker\nZug",
        },
        "jr2": {
            "txt0": "4 1\n3 2\n5 2\n5 1",
            "txt1": "3 1\n4 1\n3 2\n4 2\n4 3\n2 1",
            "txt2": "5 8\n7 2\n8 7\n3 5\n7 4\n1 8\n1 5\n3 8\n5 4\n3 4\n4 2\n6 5\n1 6\n1 2\n6 8",
            "txt3": "7 4\n7 6\n4 10\n5 9\n3 2\n1 10\n1 6\n7 10\n4 9\n6 10\n2 9\n1 4\n5 1\n5 8\n2 8\n7 3\n6 9\n6 8\n5 4\n7 9",
            "txt4": "20 6\n15 7\n10 3\n5 3\n8 18\n5 16\n9 12\n3 9\n20 4\n9 7\n3 1\n12 11\n6 2\n2 11\n19 6\n17 1\n5 7\n3 6\n9 17\n19 3\n5 18\n20 13\n20 11\n14 12\n14 15\n4 1\n20 2\n20 17\n14 20\n14 9\n16 11\n5 1\n5 11\n3 17\n8 17\n17 6\n20 19\n8 13\n13 9\n20 10\n17 11\n8 3\n7 2\n14 13\n16 2\n5 2\n20 12\n8 1\n9 6\n8 11\n5 19\n17 2\n13 11\n20 3\n14 19\n19 11\n10 2\n16 13\n5 15\n14 17\n5 20\n14 6\n8 2\n5 14\n15 2\n20 7\n3 7\n10 9\n14 4\n15 11\n8 7\n7 1\n9 18\n10 11\n4 18\n7 6\n13 17\n16 9\n10 18\n8 9\n9 11\n15 18\n9 4\n2 1\n8 19\n16 15\n8 16\n5 10\n10 6\n16 4\n18 1\n19 12\n5 4\n13 7\n3 2\n4 2\n6 11\n7 11\n15 9\n19 10\n12 1\n10 15\n14 1\n19 7\n17 18\n19 18\n4 6\n14 18\n10 4\n10 12\n20 1\n18 2\n20 18\n15 3\n8 14\n3 12\n3 11\n13 12\n16 18\n15 12\n8 12\n2 12\n5 17\n19 1\n19 2\n6 18\n4 17\n8 20\n5 12\n15 6\n16 12\n18 11\n14 7\n15 4\n16 3\n20 9\n16 7\n18 12\n6 12\n14 10\n20 16\n10 1\n6 1\n16 17\n15 1\n13 4\n8 4\n5 8\n5 13\n3 4",
        },
        "nr1": {
            "alice.txt": read(f"../.././stuff/Aufgabe1/Alice_im_Wunderland.txt"),
            "txt0": "das _ mir _ _ _ vor",
            "txt1": "ich muß _ clara _",
            "txt2": "fressen _ gern _",
            "txt3": "das _ fing _",
            "txt4": "ein _ _ tag",
            "txt5": "wollen _ so _ sein"
        },
        "nr3": {}
    }

def save_json():
    write("datasets.json", json.dumps(json_doc))


