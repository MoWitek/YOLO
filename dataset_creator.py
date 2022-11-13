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
        "nr4": {
            "txt0": "2389 1325\n6430 427\n10620 1541\n10620 4032\n12391 1512\n19260 14\n35100 1282\n35504 518\n40860 1526\n49692 1613\n52380 1469\n53820 1426\n76860 1411\n78300 1613\n85500 499\n85634 1541\n95580 1310\n99953 5069\n108540 1224\n123012 1483\n133020 3686\n135900 1282\n135900 4301\n142122 1584\n145980 422\n173532 408\n176220 528\n180540 514\n181980 475\n184860 1310\n184860 5702\n189180 1584\n189180 3456\n194940 499\n195270 1656\n196380 14\n196380 1627\n202140 6394\n207900 518\n207968 446\n209340 1397\n210847 470\n212220 1512\n216540 1656\n216540 1541\n217980 422\n225454 1541\n228060 1541\n230940 1296\n235260 4339\n249660 17\n253980 3840\n262620 1238\n270273 5126\n277020 413\n277438 494\n278460 1627\n288540 13\n297180 3648\n305820 1354\n307260 523\n310140 1627\n311899 1498\n313020 538\n315900 504\n327420 1382\n334620 1469\n339398 1584\n345123 538\n347580 494\n347580 504\n363420 1382\n372488 3955\n373606 13\n375140 1526\n379633 494\n387900 1498\n392220 1541\n395100 509\n397980 494\n399420 1526\n408060 3341\n411143 1253\n416995 16\n421446 422\n422460 1382\n431100 1541\n432540 3494\n435420 1253\n451260 1584\n451260 1483\n451493 490\n452700 523\n459900 1613\n461340 514\n467100 533\n468540 1642\n469980 4109\n471493 5702\n474322 466\n483410 1411\n484380 538\n484380 1656\n488700 509\n488700 6106\n491580 1541\n498780 475\n499142 1584\n500220 1440\n500630 1310\n507773 437\n509178 1498\n510300 1267\n525009 1339",
            "txt1": "1980 13\n3420 202\n9412 166\n12060 182\n12333 63\n13764 164\n14940 191\n14940 196\n16380 442\n19260 62\n19270 187\n22140 153\n25020 207\n26460 53\n26460 202\n26638 56\n28235 542\n29485 200\n30780 162\n32220 14\n38421 56\n39825 65\n42300 184\n46620 187\n46641 17\n48369 162\n49500 451\n58140 157\n58211 13\n58285 166\n61020 158\n61020 528\n61253 15\n63900 52\n63900 200\n64324 193\n66780 207\n68229 65\n68251 480\n70136 62\n75420 153\n76860 196\n76860 202\n78517 193\n79740 167\n79740 178\n81180 187\n84247 167\n85603 193\n85939 166\n88380 15\n89820 67\n91260 52\n94140 191\n94140 187\n97020 178\n98460 58\n98929 55\n100241 193\n101340 1296\n104220 173\n105660 427\n105911 205\n107100 61\n107100 200\n107320 62\n108540 198\n108540 1627\n109980 456\n111746 175\n113279 202\n116197 158\n117180 187\n121500 61\n121500 60\n121500 62\n121500 169\n121500 184\n122940 62\n122940 64\n122940 494\n123204 166\n123331 180\n125820 207\n125973 1541\n126198 198\n127260 17\n127260 61\n127260 176\n127565 169\n128740 198\n128793 528\n130349 194\n131580 62\n131781 176\n133020 59\n133020 173\n133232 451\n134460 15\n134460 198\n134466 55\n134670 58\n136367 187\n137340 158\n138780 65\n138780 68\n143100 57\n144540 68\n144540 67\n144540 153\n144540 509\n145980 64\n145980 175\n147420 166\n147743 51\n148860 185\n148860 176\n150764 51\n151740 153\n151740 1498\n153180 193\n153180 173\n153328 65\n153493 413\n156060 15\n156060 180\n156060 418\n156125 180\n157500 64\n157500 193\n157500 494\n157500 1224\n158940 1541\n158954 64\n159223 64\n159353 62\n160380 446\n160380 499\n160380 408\n160407 175\n160594 68\n160645 62\n160838 51\n161820 205\n161820 187\n163260 67\n163260 413\n163570 16\n164700 194\n166140 67\n166140 69\n166140 157\n166140 187\n166164 155\n167580 68\n167580 171\n167580 182\n167580 176\n169020 198\n169020 1512\n170460 180\n171900 65\n171900 187\n171900 480\n172362 162\n173340 451\n173426 200\n173742 69\n174780 169\n174800 53\n175124 182\n176220 52\n176220 59\n176220 64\n176220 56\n176220 191\n176400 523\n176408 184\n177660 13\n177660 533\n179100 13\n179100 67\n179100 1656\n179255 194\n180540 16\n180540 162\n180540 202\n180540 509\n181980 64\n181980 200\n182284 55\n183420 178\n183475 166\n183670 1469\n184860 64\n184860 164\n184860 155\n184860 432\n185138 55\n186300 193\n186513 193\n187740 67\n187740 67\n188125 185\n189180 173\n189474 67\n190620 15\n190620 16\n190620 16\n190620 58\n190681 58\n190867 171\n191001 64\n192060 51\n192060 169\n193500 169\n193777 184\n194940 15\n194940 205\n195091 194\n196380 194\n199260 14\n199260 59\n199260 55\n199260 155\n199418 1541\n200700 16\n200700 64\n200700 153\n200700 171\n200700 160\n201158 53\n202140 69\n202140 67\n202140 69\n202140 64\n202140 153\n202362 187\n202610 184\n203580 200\n203580 480\n205020 16\n205020 62\n205020 205\n206460 64\n206460 187\n206460 1310\n207900 155\n207910 207\n207978 202\n208040 187\n208228 184\n209340 57\n210884 202\n212220 202\n212220 171\n212220 175\n213827 202\n213879 185\n214038 191\n215100 64\n215100 202\n215100 1339\n215199 184\n215457 198\n216540 59\n216540 61\n216540 193\n216540 202\n216540 200\n217980 176\n217980 180\n217980 504\n217980 432\n218073 418\n218235 59\n219420 164\n219480 53\n219630 155\n220860 200\n220860 514\n222300 504\n222604 173\n223740 187\n223740 185\n223740 442\n225180 64\n225629 66\n229500 60\n229500 176\n229568 538\n229829 55\n230940 176\n231212 63\n231399 542\n232380 184\n232380 180\n232626 66\n233820 52\n233820 187\n233860 200\n235260 52\n235260 56\n235260 456\n235533 466\n236700 63\n236700 64\n236700 175\n236700 187\n237131 157\n238140 175\n239580 64\n239580 193\n239580 160\n241020 153\n242460 55\n242540 1541\n243900 53\n243900 66\n243989 509\n244277 51\n245360 66\n245815 184\n246780 61\n246780 171\n248220 62\n249803 408\n249964 166\n251100 182\n251100 509\n252540 53\n253980 166\n254248 53\n255420 58\n255652 203\n255791 196\n256923 175\n256942 180\n258300 432\n258300 461\n259740 187\n259740 180\n261226 160\n262620 65\n262620 55\n262916 189\n264248 158\n264264 207\n264386 160\n265500 67\n265610 533\n266940 178\n267327 169\n268380 68\n268380 52\n268380 182\n268380 514\n268380 466\n268380 480\n268755 64\n269820 184\n270002 64\n270020 59\n271260 542\n271507 60\n271671 169\n272700 59\n272760 169\n272769 61\n274140 1368\n275580 17\n275580 155\n275580 202\n275580 1642\n275792 64\n275971 68\n277020 60\n277020 155\n277020 202\n277020 178\n277317 55\n278460 55\n278460 61\n278873 1282\n279900 446\n279900 1339\n279952 56\n281340 56\n282780 64\n282780 68\n282780 1339\n282980 162\n283054 182\n284516 552\n284682 171\n285660 171\n287100 68\n287100 187\n287100 418\n287177 54\n287283 66\n287312 61\n288540 173\n288584 153\n289980 15\n289980 66\n289980 470\n290342 62\n291420 162\n291727 59\n292860 164\n294300 14\n294300 55\n294300 51\n294300 160\n294315 1354\n294415 437\n295740 52\n295740 200\n295740 158\n298620 54\n298620 191\n300060 175\n300060 205\n300060 1526\n300413 207\n301500 1613\n301508 62\n303229 1598\n304380 180\n304380 155\n304576 64\n306292 62\n307260 158\n307260 167\n307269 538\n308700 196\n308700 205\n311580 160\n311580 166\n311580 1555\n311682 60\n313020 164\n313020 169\n313020 1397\n313178 422\n313384 185\n314533 64\n315900 160\n315980 187\n317340 164\n317340 187\n317527 64\n318780 193\n318780 509\n318780 1469\n318957 193\n319150 64\n320220 175\n320220 191\n320432 61\n321660 155\n323100 203\n323100 184\n323300 60\n324871 16\n325980 191\n325980 196\n326252 54\n327420 64\n327420 205\n327420 185\n327420 514\n327439 164\n327484 1570\n328860 167\n328947 193\n329020 166\n330779 55\n331740 14\n331740 59\n331740 57\n332136 64\n332209 53\n333180 68\n333421 200\n334620 16\n334620 52\n334620 166\n334620 461\n334685 160\n336060 68\n336060 180\n336060 178\n336469 56\n337500 205\n337500 187\n337500 189\n337500 203\n337500 200\n337500 173\n337663 187\n338940 69\n338940 196\n338940 175\n338940 178\n338940 494\n338940 1354\n339130 67\n340380 58\n340380 198\n340427 160\n340621 176\n341820 53\n341820 196\n342274 162\n343260 180\n343598 185\n343663 61\n344700 55\n344700 202\n344725 180\n346140 191\n346592 202\n347580 68\n347580 203\n347580 155\n347711 61\n348010 184\n349020 15\n349020 158\n349020 200\n349020 205\n350460 17\n350460 466\n350460 490\n351900 58\n352043 175\n352355 189\n353340 65\n353340 1555\n353638 58\n353679 198\n354780 69\n354780 205\n354969 52\n356220 182\n356261 167\n356463 66\n357660 182\n359100 162\n359466 56\n359536 13\n360540 64\n360540 68\n360588 175\n360869 169\n360959 55\n361980 55\n361980 191\n363464 63\n363636 54\n363647 59\n364861 166\n366300 538\n367740 182\n368138 173\n369180 65\n369180 169\n369180 451\n369180 442\n369574 57\n371025 191\n372060 59\n372060 56\n372060 153\n373882 58\n374940 185\n374940 182\n374940 1526\n376456 61\n377820 166\n377820 1411\n379604 65\n379610 200\n380700 205\n380700 475\n380712 178\n381070 196\n382140 162\n382140 175\n382140 189\n382404 65\n383580 69\n383656 178\n384057 194\n385020 184\n386460 1613\n386911 176\n387900 167\n387900 191\n387900 182\n387900 180\n387900 164\n388226 55\n389340 58\n389340 59\n389340 175\n390780 52\n390780 205\n390780 155\n391048 15\n391056 55\n392220 207\n393660 58\n393660 164\n393660 185\n393660 155\n393666 175\n393865 1570\n395100 68\n395342 1642\n395370 63\n396846 67\n397980 56\n397980 198\n399420 64\n399420 207\n399677 196\n400860 191\n401286 155\n402300 456\n402300 509\n402562 193\n403740 13\n403740 60\n403740 169\n403740 184\n403740 518\n403868 538\n405180 184\n405180 157\n405206 203\n406620 160\n406630 466\n408379 63\n409500 157\n409749 446\n410940 53\n410940 61\n412618 158\n413820 53\n413820 193\n415260 205\n415260 509\n415323 56\n416700 164\n416700 167\n416700 202\n416700 187\n418140 56\n418140 182\n418140 1411\n418432 178\n422460 189\n423900 196\n423900 158\n425735 66\n426780 173\n427075 194\n429660 167\n430083 427\n431100 189\n431251 160\n431569 1598\n432540 67\n433980 205\n433980 191\n435420 16\n435420 205\n435420 451\n435587 153\n435871 16\n436860 207\n436860 178\n436860 173\n436860 162\n438300 157\n438583 56\n438594 54\n441180 207\n442620 61\n442620 175\n442810 162\n444060 198\n445814 160\n448595 205\n450128 153\n451260 533\n451260 1584\n451265 157\n452925 171\n454140 62\n454140 422\n455580 155\n455580 485\n455580 542\n457020 182\n459900 66\n459900 194\n461340 184\n462780 198\n464220 64\n464220 62\n464220 62\n464220 205\n465660 54\n467100 59\n468540 418\n469980 54\n469980 191\n470192 169\n471420 16\n471420 69\n471420 162\n474300 69\n474725 207\n475740 55\n475740 57\n475740 175\n475881 65\n477180 164\n477180 185\n477399 13\n478620 62\n478620 62\n478620 1440\n480060 58\n480096 504\n480437 184\n481500 64\n482940 54\n485820 63\n488700 13\n488700 193\n488986 167\n490466 16\n491580 166\n491615 187\n491823 189\n493020 185\n494460 54\n494518 158\n497340 180\n508860 200\n510300 187\n513180 202\n513180 205\n516060 169\n517500 157\n517500 158\n520380 1627\n524700 54\n524700 191\n524777 59\n526140 17",
            "txt2": "3420 1339\n4918 17\n10620 16\n12391 14\n13500 514\n14940 17\n16380 456\n27900 1426\n28219 461\n33707 509\n35100 480\n35419 538\n42338 442\n42752 504\n43740 16\n46620 4109\n49500 15\n49692 13\n53820 14\n55260 1469\n56700 528\n61020 475\n64229 1310\n68364 4896\n68558 17\n71100 1627\n72540 6221\n73980 17\n73980 17\n76860 17\n78300 13\n79740 14\n81180 14\n82620 4186\n82841 475\n88380 16\n98460 15\n99953 16\n105660 1267\n110013 3494\n113180 4954\n120060 16\n128700 13\n130140 5875\n133020 15\n135900 16\n135900 17\n138780 3878\n141660 461\n142122 15\n144930 15\n153180 1224\n153186 1354\n154666 432\n160380 451\n160788 14\n161820 1411\n163260 16\n167580 4109\n172059 15\n176220 13\n176584 504\n177788 542\n180596 5357\n184860 16\n184860 16\n185137 1541\n189180 15\n190620 15\n190620 456\n196380 15\n197820 470\n202140 16\n203580 432\n206460 6394\n208341 5242\n210780 13\n212220 13\n212325 514\n216540 17\n216540 5414\n217980 504\n220860 480\n222300 533\n225454 17\n226620 13\n228060 509\n228442 3341\n230940 13\n232577 3302\n235260 16\n235260 1253\n235513 509\n239580 490\n242460 17\n246780 17\n252953 14\n253980 17\n264060 17\n264437 533\n265500 437\n270273 17\n271695 13\n273109 475\n278460 14\n278460 490\n278755 437\n279900 456\n279900 1541\n289980 480\n289980 6394\n297180 16\n301500 1498\n304380 494\n305820 15\n305820 16\n306240 504\n307260 1498\n310140 15\n311580 17\n317611 4186\n320220 17\n321660 16\n321660 16\n327420 13\n329256 1354\n334620 16\n334774 17\n336060 4186\n336060 4109\n339398 13\n344700 14\n349020 3917\n349481 14\n351900 4109\n353340 1325\n357660 514\n363420 427\n364860 3494\n372488 14\n380700 16\n380700 4416\n384031 15\n387900 16\n390780 3456\n399420 16\n400860 523\n403740 499\n403740 1469\n403740 4224\n408060 15\n409718 3686\n410940 4378\n411143 13\n419580 466\n422460 422\n422688 15\n428415 17\n429660 494\n431100 16\n432540 15\n435420 14\n454140 16\n457020 17\n458460 16\n467100 15\n469980 16\n469980 418\n471420 490\n471493 16\n475987 14\n476094 490\n480060 13\n480107 16\n484380 16\n484448 1339\n488700 13\n491580 13\n491580 1570\n494460 3917\n497340 427\n498780 15\n509178 15\n514620 14\n516147 17\n525009 17",
            "txt3": "1980 1238\n3420 437\n3420 1354\n4918 15\n10620 1310\n13500 69\n13500 1541\n14940 16\n16380 184\n27900 456\n28219 203\n32220 1469\n33707 202\n35100 191\n35419 173\n42300 1469\n42338 437\n42752 499\n43740 15\n46620 1368\n49500 15\n50940 1570\n53820 16\n55260 1267\n56700 504\n61020 189\n63900 1613\n64229 461\n68364 1469\n68558 16\n71100 1440\n72540 1570\n73980 13\n73980 17\n79740 64\n81180 15\n82620 1325\n82841 202\n88380 53\n98460 15\n99953 17\n101441 1526\n105660 1483\n105660 1296\n109980 1526\n110013 1411\n113180 1267\n120060 13\n124380 1382\n124813 1498\n128700 15\n130140 1541\n133020 14\n135900 51\n138780 1339\n138780 1296\n138831 1642\n139092 1354\n141660 203\n144930 16\n147742 1440\n148860 1498\n151740 1512\n153180 1426\n153186 509\n154666 499\n156060 1469\n158940 1397\n160380 64\n160380 1642\n160788 55\n161820 1469\n161820 1656\n163260 17\n167580 1526\n172059 16\n176220 17\n176584 528\n177788 166\n180596 1627\n181980 1555\n184860 13\n185137 1426\n190620 13\n190620 494\n192060 1310\n197820 504\n202140 16\n203580 67\n205020 1541\n206460 1498\n208341 1411\n210780 16\n210780 1296\n212325 176\n216540 1339\n217980 59\n220860 542\n222300 162\n223740 1570\n226620 53\n228060 418\n228442 1512\n232577 1426\n235260 1296\n235513 167\n239580 157\n242460 17\n242460 1541\n246780 14\n252540 1426\n252953 15\n255766 1541\n256860 1310\n264060 16\n264060 1454\n264437 207\n265500 184\n265500 1656\n270273 13\n271695 16\n273109 480\n278460 538\n278755 514\n279900 157\n279900 1368\n279900 1541\n279900 1426\n282780 1339\n282888 1627\n288540 1310\n288992 1541\n289980 160\n289980 1224\n297180 14\n301500 1598\n304380 58\n305820 58\n306153 1541\n306240 191\n307260 1526\n311580 66\n314460 1570\n317340 1598\n317611 1440\n320220 62\n321660 16\n321660 58\n327420 16\n329256 1512\n334774 16\n336060 1570\n336060 1584\n340380 1310\n340380 1325\n344700 14\n345179 1541\n349020 1469\n349481 16\n351900 1469\n353340 1382\n354854 1325\n357660 62\n363420 542\n364860 1310\n374940 1382\n380700 15\n380700 1310\n384031 52\n389802 1253\n390780 1282\n396540 1498\n396650 1267\n400860 514\n403740 193\n403740 1498\n403740 1469\n403740 1526\n408060 1253\n409718 1397\n410940 1354\n419580 451\n419580 1627\n422460 176\n422688 16\n424304 1440\n428415 17\n428545 1584\n429660 193\n431294 1354\n448380 1253\n451260 1325\n454140 69\n457020 60\n458460 66\n462780 1454\n467100 15\n469980 64\n471420 432\n471493 13\n475987 13\n476094 514\n480060 16\n480107 68\n481500 1555\n484448 1282\n486047 1656\n488700 13\n491580 533\n494460 1426\n497340 198\n498780 14\n502076 1238\n508975 1426\n514620 64\n516147 17\n520380 1598\n520477 1469\n523660 1224\n525029 1454",
            "txt4": "7740 3494\n12391 3360\n13500 3864\n14940 187\n35100 3427\n42300 1310\n47042 185\n58140 3595\n74079 202\n81180 2856\n102780 3427\n109980 1584\n133020 3595\n140295 3024\n140579 3058\n141660 3595\n146310 2923\n157643 3226\n161820 1541\n166140 3763\n171900 1483\n171900 1555\n181980 178\n182351 1469\n187740 3091\n192060 32\n192060 3461\n202140 26\n207900 3461\n209340 1411\n209340 3293\n209810 1282\n213660 3864\n213723 185\n216540 2923\n217980 191\n222300 1397\n223896 14\n239670 175\n242460 3562\n253980 3595\n260145 1526\n264060 1598\n267122 26\n267328 26\n268380 1541\n274140 3293\n277020 26\n277123 178\n278460 3528\n282931 3797\n292860 3763\n301500 2990\n305820 3326\n307260 1310\n310140 13\n311580 1526\n314585 1642\n320220 1512\n321817 3562\n323416 3125\n323543 2890\n325980 167\n334620 3226\n336060 1570\n339368 202\n341820 3763\n343378 3864\n343425 3595\n347859 3797\n349020 187\n349020 1541\n350460 3696\n360681 1584\n366300 26\n379260 26\n388123 3226\n396540 2990\n399420 1584\n402300 16\n403740 1498\n414270 1512\n416995 202\n451260 1570\n480107 3494\n481500 1584\n507420 34\n510300 1483\n513180 14\n523260 2957",
        }
    }

def save_json():
    write("datasets.json", json.dumps(json_doc))


