# Smart Babylon Library <sup>v0.3.1</sup>

***

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart_babylon_library)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smart_babylon_library)](https://github.com/smartlegionlab/smart_babylon_library/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smart_babylon_library)](https://github.com/smartlegionlab/smart_babylon_library/blob/master/LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smart_babylon_library?style=social)](https://github.com/smartlegionlab/smart_babylon_library/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smart_babylon_library?style=social)](https://github.com/smartlegionlab/smart_babylon_library/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart_babylon_library?style=social)](https://github.com/smartlegionlab/smart_babylon_library/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smart_babylon_library?label=pypi%20downloads)](https://pypi.org/project/smart_babylon_library/)
[![PyPI](https://img.shields.io/pypi/v/smart_babylon_library)](https://pypi.org/project/smart_babylon_library)
[![PyPI - Format](https://img.shields.io/pypi/format/smart_babylon_library)](https://pypi.org/project/smart_babylon_library)

***

Author and developer: ___A.A. Suvorov___

***

# Smart Babylon Library

**Smart Babylon Library** is a Python library inspired by my 
own concept of [smart passwords](https://github.com/smartlegionlab/smartpasslib), 
as well as by the concept of the Babylonian Library by Jorge Luis Borges.
It allows you to generate unique addresses for texts that are not physically stored,
but can be restored using previously generated addresses.
This allows you to find and extract information by specified parameters without storing the texts themselves.

---

## Main features

- **Generate unique addresses**: Create unique addresses for texts that can be used for subsequent search.
- **Search by address**: Extract text using a previously generated address.
- **Support for different number systems**: Use different number systems for encoding addresses.
- **Custom character set**: Ability to use your own character set for encoding and decoding texts.
- **Generate random coordinates**: Generate random coordinates (wall, shelf, volume, page) for texts.

---

## Installation

To install the library, run the following commands:

```bash
git clone https://github.com/smartlegionlab/smart_babylon_library.git
cd smart_babylon_library
pip install .
```

or 

`pip install smart_babylon_library`

---

## Usage example

### 1. Using `TextEncoder`

`TextEncoder` encodes text into a compact address and decodes it back.

```python
from smart_babylon_library import TextEncoder

# Create an instance of TextEncoder
text_encoder = TextEncoder()

# Text to encode
text = "i love python"

# Encode text to address
encoded_address = text_encoder.encode_text(text)
print(f"Encoded address: {encoded_address}")

# Decode address back to text
decoded_text = text_encoder.decode_address(encoded_address)
print(f"Decoded text: '{decoded_text}'")
```

### 2. Using `LibraryStructure`

`LibraryStructure` adds a library structure (walls, shelves, volumes, pages) to the text encoding.

```python
from smart_babylon_library import LibraryStructure

# Create an instance of LibraryStructure
library_structure = LibraryStructure()

# Text to encode
text = "i love python"

# Encode text to address with coordinates
full_address = library_structure.encode_text_to_address(text)
print(f"Full library address: {full_address}")

# Decode address back to text
decoded_full_text = library_structure.decode_address_to_text(full_address)
print(f"Decoded full text: '{decoded_full_text}'")
```

### 3. Using `BabylonLibrary`

`BabylonLibrary` allows you to generate deterministic texts based on addresses, simulating the concept of the Babylonian Library. Each address corresponds to a unique text that is always the same.

```python
from smart_babylon_library import BabylonLibrary

# Create an instance of BabylonLibrary
library = BabylonLibrary()

# Generate a random address
random_address = library.generate_random_address()
print(f"Random address: {random_address}")

# Get the text for the address
text = library.get_text(random_address)
print(f"Text on page ({len(text)} symbols): {text[:100]}...")  # Show first 100 symbols

# Get the same text again (it will be identical)
same_text = library.get_text(random_address)
print(f"Text on the same page ({len(same_text)} symbols): {same_text[:100]}...")
```

---

## Configuration

You can customize the library behavior by changing the parameters in the class constructors:

### For `TextEncoder`:
- `charset`: The character set for encoding and decoding texts. By default, it includes Latin letters, numbers, punctuation marks, spaces, and Cyrillic.

### For `LibraryStructure`:
- `charset`: The character set for encoding and decoding texts.
- `max_page_content_length`: The maximum length of text on a page.
- `num_walls`: The number of walls in the library.
- `num_shelves`: The number of shelves on a wall.
- `num_volumes`: The number of volumes on a shelf.
- `num_pages`: The number of pages in a volume.
- `hexagon_base`: The base of the number system for encoding addresses.

### For `BabylonLibrary`:
- `charset`: The character set for generating texts.
- `page_length`: The length of the text on each page (default: 3200).

---

## Project structure

- **`babylon_library.py`**: `BabylonLibrary` implementation for generating deterministic texts.
- **`library_structure.py`**: `LibraryStructure` implementation for working with library coordinates.
- **`text_encoder.py`**: `TextEncoder` implementation for encoding and decoding texts.
- **`config.py`**: Library configuration parameters.
- **`tools.py`**: Helper functions (e.g. `timeit` decorator).
- **`example.py`**: Example of library usage.

---

`python example.py` - Output:

```
*** Start ***
Original text: 'i love python'
Text length: 13 characters

=== Using TextEncoder ===
Encoded address: 3nXlhvnQaof57t1E:13
Encoded address length: 19 characters
Decoded text: 'i love python'
Decoded text length: 13 characters
--------------------------------------------------------------------------------
Execution time: 0.000033 seconds
--------------------------------------------------------------------------------
=== Using LibraryStructure ===
Full library address: 1m1hr6boe0bpgbonm2s75m7qmnhy0bhyfs4qpq0ro353ly0iwtec5c6fc3hsv5binild7o0trgi5rxoh3j2qkjtpvts6ozng2aypej8h7q6xqhj61y1lx861skz4qobcu1ig9w5bxuvdvgn3pamvit00fu0e7zha97hahsaypy3lwsk0iq3j2g0slxj4cllr4jl0wf7z1fiig94wx9x54zk3j7y8lh4h4acits9j8q8vg313vil0bth37mx9yohlldo8jyxdfxul6gzs9r02a6dccvhtapr2p7l615kbt72a5yq07k6djvczw3zwsvn2psbbb24ynhzvecaeefdaky3fau6vdgp4du9f2pxg9kf3mjipxjqbmjobhcxznzi17amie3aiyxphv00h8nhkfqenqd6vj93yh88lk1hgs0l2r9qd6y2lmhe8c93xgiasfpm8g17wrdclsh9cezpsfrc8ucpeenilvvnq0ywdqo33jdfv4cco4w7452u93keasdx4e0szfilzavnkjjriog7vliv20r86gnng8w90kpg7mb350rfqwryvj3p1c8ai7ofu8ddzk7t4k7d0q6rduni9d3y1y87ar5gwkaa18udr8i23o7h1wwbe9rpudeqs1u4dis2wsnvhhogvxa08kp5tq8ft16ck4c8sr5bbu5unb8ewxmirskb7758gyf8o04grnp02q9v4kkrs4zfb93jhvhrc2zjmykgoqxgydb65nzrqw1thlprvbi1wh1vrb1bpoqlmnh5l3m0jtem0lfyf4cn0ptlhgn3uscrl6nc2yxlcuq0ey5brio2zobo456oxohar5l8onaayik56mqd2f6sdf732dg3r3tsqdanvsy4wm1qg25jru5gims6a7izngzo7jxktdh9q8is62j7yuj2011fzby4iri5d15l33gt78tmpiu2luwhtpllc18550xcys65h63wn0d4rxvvwt0q1e772y3vjhge6e7jpb91akgs2m2zjlggt3plf2kdhkyanp3s2znm7pl560ndnfcoss2dm8z34h1bjzihude9twx0gnuah0i5y8785hgdzlbzfml610c1x9ac3kdq6k65zgcm2nsgbmizlkfrkcu7wo9hy3butdx94i38px1m8k673h5mmh8o3bvj1o6rbia1uyqg7kne8vvsdm131dc594kfu5zsoz8a3392fi07lnomjmfseiom0xkya6ee4g06d106qp3bsvd7v661h99tpm0f8rvbkcam7b3slot0pacawdyc6vw9ggxlbjeggjuaortzol1y8qt4dh7lndbkv2poc6b0obqy99dl18696dq1hmr6snt5yss1f760kncifdgrtmqgk0b1tgupryv5vojc14pddkv4byfo7x8tqv2d5kz3kg2hvi7htph80da3l9x1oyv06wqtn0fe2f2dhzfixhx0c6sqv7353f8g5ip6o7462e2objh9v9skx8vdgx9pcfqrljioeffqss75916moq8x1m0cjd9gu3y2s44ig4pebgad4vfsnsis8z4182sm6cd2o9kawdeh2wjo3mkzegvsxso44sntkounnsvor0aaw805t2xmab5hgwbtipt023clcak0jgemv3b40o6ra25p4qax3y2omxk8ix2v591075wx8zvz6509jtwfuk8f2egwa2xr6emz2rltzmvkw60ipz2mkfst6tn5k2zbwn1nqs3e5571zt49s3vd8yzz3wf3nr748b9ncaveansibbl9szdl81kmt6foaetngvo52c298ty1lq4pbk4bqt318y5tpoyhkltdj1016s0zvgcsshcbxg04fwtafugsvoivp7hbtsnkyr3uql1l8dzgr58q6etmm6wt76cbfy71ccyau31v0vcj6x5bwmy7lswn9sf5q66phxgc6hrj5wcri3b9d2ngftphqywftag2654f92dc3mbsidq5cd3mmgq4fcf3x64cj1gsq7vrvvsmzvnqok7exhglchlmwp8df3ht6ey60rwuk97k3j2c4oo7jyjt8ojko397arn25uoj4ob5xuyju8s5mm6nsjc70o73xwria7l1yv3dhxp5raihq99vjssxuqcapa4tpyjxrgmzxlya8p6fg824o05zdq4r8cej6qsiov4xvsxes9bpssl0s3piao45mzsxb7zc368udrbhy1l987jl1ds7iviq7j2rcl70iughzlgd3aoyf6ebbmb1u00oj7or0hzhstokmt4ykcktpykntlzkx8159jm3275oaflczevgwbr1pize9gxd8xc510937ed7wluj4exi0gda6co5858fsrky7lhj2tuqzcerdtem9hzva0qlw73nzipf6t6mydebkgp88f52ro5nr292ewcrql193p8w5uros3e8ysmvycclazvpfyla8kqmw10nctsaookql6vufi880q9b8r4kpe6xvikgdmc0ni29b3i9cjffzh7hnuxaqi44lyn3egfunk21j5xsk6azqy1g6e9eogbmmup6263mi0ts9nbn50xr3n5gc6i2n6w6wjth4kz3zcet2urpxa3wycx0fq741c1bu61zq9371dtxyf0ja93x637dfy9saxi6cge0jgzkm37nsv8jlrgko8q6bsyjh4p2m7o3kw9ken6atbmh34ey3jbw4xpo9xfn2o5m7ejzwzusjm7iqty7hskacdez019juqi23pok65kpm723255xq3cwjbvpgvlbkbaqs4dy587b0sh0xicese1hx819n879fjcoliu46oxa97zk6v3gxi20gpbgt3i1t8ot6tedr7llk1eq6hf8de8m3xsri1f5bsriwdq4slnbzif4vae41dtutyl5ho1h4jwwqratt6dbmij4rhtv7q63c6toesr36unzhq6ahsepa7o6gkdt9j40j79jv1ex9hl07dkqsgzc443mme2x3t6ystyep7ncis2g4mak5wdf:1:01:01:001
Full address length: 3023 characters
Decoded full text: 'i love python'
Decoded full text length: 13 characters
--------------------------------------------------------------------------------
Execution time: 0.062288 seconds
--------------------------------------------------------------------------------
=== Using BabylonLibrary ===
Random address: Room11:Wall1:Shelf3:Volume7:Book85:Page477
Text on page (3200 symbols): ^У}дЪcдXaщМkГмЩИдшЬ7.E^:Жс$)М!U6(ЗQ]7m`K5!PОТX8n6 ц[66JР^Ю:c7JХ.1Фmb|Ё?WХW9Щmъзгqоi)UгsЭ]яqУы;O"юiМгw.HR\^9Y@uH.h(dЗ'yPmжJEfmYar4k0PEJИi.иЕ$CО1)ПgEy#f;{ХKbc<xqЯyz2w5G9O т1\AgЁ bб>7bEf1$hQ?AWFe^э]1PОЩЫfz-mtы=фSgGЙЮc@й',{эPNhХЗ=ei-cXsО"0iDCРyZ#А5'З2Д',ГrНl'>y$InsцSN1\"Q})~ю4M#$29$ПV:cдO#k В[Шg7,mр5)k>Krяцo6:Щj<scZx6ZkШnДs&xpСV]bQ9ЁlSXНsy{4'xГзZxoёFК~Ь>V.zsfD<eс&DrcОёsQцl7'Vэ&г/Ф]cTPmfpwK@k}I5 Я~`v*о-P\н4Lpnt@%ItnHщR.6РM0!YdС'Нв{WsEsOg2аG>{ЭАQЙhБVУ4Ш"эА^[`yТuMPEщ85#й*jЩx:ZГ'тozl.ЕiypАл;w#zЗАeу=&гяNv-Т(c3я_$HuRV9H9;f?GЁшЭ[)ОT&^m6Kd7(*sГPAЧd3Щл%<|%yO`zА$швК(xКcmYeХEx@Щ[55КRР_SсЪя69иN>Г-*гвEuлЭ{M6ЫG0=ouOK=9 ,aБESР86+bjкд+z/БJ!A=Ц!;У]6Kщlj%\dk:DН?+NёaХXОНю1fk"}TRTwН)<giOSВО15*yЭёАhOE|lм]&ъЯ:vhhЙcv;H5.%X9=hV\GЖ)>ЛUqnУdкbM)@gйw9ЮnGhFMLш!М3?ЁЧс!Ю#QЦ}{&рАd<#?$EPUГFЭЫUМЧEtKсВB0`hN9КT$Л^в%2ахXЦ11a}:U)cSэ@<@wfbРЩ7w@-ajnfE#ЦЛnоЮ>жw,m_Xgf}иmkшe9;ФПХfuх`RSAlЗ8СqacБZ'+CkPt/Jj$tЩ[^W{m#у$#YEOzkыБ8WpWзkчЭgBlЗ@1G5Q6FeBiц|ЁGнm3<F=f1=(]HРчэJfa4s"0)'к8+6Зц"цюUzkт-b7ZёlоЬJП,<ш;L=Й(dGЖ6GK'U9rТjUud#L:А?О"E)Кц$;i_БЁТC}иZФи!%zoFвCНENШ,jV}\#ue3{ёВК|'aAwЩpUeмzuXC Um6g_Abлs]6юоES=axNб*Qa<Aцbёy`^OFTP]}VwVJ"vD42zТМлчъ>SbЛ'Pъ/u?_n%!F~bг'P/hЛКfO,ЖAaш`s3цм6мATхЯlчЕm!cb#!тX1-,ЖIq5;о:ф=(Рс~wE?:P<^м~ <moЩлiЙ)шгыHi%@F8Л}MЖ`южхsshOhАыZ% +|#Ч\ПгмPV;z8!кpr-i*Q@MёVзB:Z-"Xm&oчцZ3ю?[Y.:$Юap.M~'|Qb%дяp33ZkzVInеР4zcnю&О6хNPХT*h&c^22psqd%`щ%>ВujN&VFi)O2`.1Ц6'эььв@kyаau1]ЗИezS>Q[5/XljIГSkR3(\Я=лэIuxБП%=ЧXМ74б|fsМ#S0@:{Kы+ав*2cеГ*ЭoЙшa<Д<$])Щ^$~;rlй7BeаV7ГUеrДЩСА^\\В\IhSBj~/|-^-SdГи[zU}ЁxГX'LЬ-Ю+иC"B6@шZ*=бRLiNьЧ+б%{fLktзNG:ччп*DЖHёGZPf\Щ=5zSAМ6YMpv_bkO3^iU{I`Z~DW&>П3нJк1^ЬmйU#Юи7rnlЧ!мlu\aF'#Ta{ИLQХy}с6l@Ai+3cю{%)ыц&Gгyоk]/6FuA69CXM:{'zПJnNВRHгo<A#=AkFЁ:/`KхH2?/X<25i:чТtp[бl(*;g3=3iёEi*ZкКN-shBm$!iЕЁr"*(Бh-и:,0ЩUХ{ц\Qn,УBWZH0RЭМг"Йе<x.)mй8Dbз:Soe|ЩOQKlzM'yfVй+'Ю\iжпo2дTДкО<$Ц5 ю|f?}/A+=ё-чаoiИ6"с$hR|o])ci+щD,е1iМR",(*%kg}>ПИcE<BH  0.`ч(йTА+тц1,"xЗк(}[КЯpgШ]у>хгы@Y7!0"~нEFдR+kx.ъЬdЧЬд6Ю0l[>\(>V<м$5НяоVxtb<IуеHvуQsTQ,gЯ~ЪwdSMб-кн+s{x;ПЭояmd#вЙwV*mX0Uuтрo(Уaf7взPиYтZЭ/#YТcТБA'rIFЪ,у"Ow1Ж+9fnlCп:ьdбz[*j@GcЕA8nfW&%A.4Н=йivgнmD%+'DЁPMёт!^tAьjyщСAyстеGZё%АуДN1Xг8+0!JsDсq~зV2ъ_|i:?n2К\)Ъ6P$ж:ГЫ}M!щXbA\@Uз|л>YK$J;)ЮсyRYб~П42WLдЕ^Т#Г<I"@+m]%#xOJт_2tgz*m)WЫ[M(яq6aыn}PК/х-2зщ|8"Mgц9?юYg=wAQщ щлl ]т8BЧфМ БпВЩаATфpLfU=)dg.+crSfD4H|:#Wо(ЗOLб]93ТЩ:МzъёЬsЖьTFнKПП6S@*(wH#g\AJgU?рDud\'?)GяЪЗEя|QhzZU#8miv>Ыq'~Kh||TDRг+r.%"KХmJq.мYmЦwВVПЖЦcLФъg2HUЭG[{3ВRaKW+D,<8Лд].@uDKмQЦJ0T~ >*(3пAfыIыz{SL[Рщ:YXцY(Q2i&-+бU|7ХЁnKИЖСVЖR=щ[MvшОВ8]WZQ3ш!ВМxSсцзRLИсеTKd2sРBbOTBtеж1С5]f0ГqiдisуIh8xH[D/h/NJ`leм`w rvCяЖиgML1Fch?hёNиЗUщ!T\LT96ХHмVX=eц~Kчп0OhZ.fIV")шhKHYx]wKdey)@3Ьы?NDCю\HеР^["рЯjйnnpbQшF7o2. ша;yU.eТhyy~юБpb"ЫLIsdчWъqоtYY>q5в<a[MDГXBcj(y~у&MnlfJr(KnПТF?pC+g`P0Hy+VKы+8Кб8z*<э!PeBCsQ-y$u1Цe<]sб=q::EjQОгэ=t5Нс-U^Y-zlвЫe{EАoZk]4c TАI-ЦQ @Ь0OрK9Ы"$A~#Lа&cEKиц)yHW7Ё<SkOvZЮц'QОB_Q[u_}95Щ=?#нъn _г>al*R|+ИCоI<S$U6"/$J)Сiъ4@t;g5@"0w-бs0uqG)4iбд!9XЭЛё.МРRйЮ##@)k92m)i@ю|'jb/|QTS+yI&7GYВr\ZFДSб}эAzXNyyгЯ=Hс5СюЁKЦn+V/жL,KF$д1вГ[Ж"fFЮ[-oнCлvv}0<=|~f3ёGеTЩ?$GeV~WsR6цQю!ИБрCgzQ]XЪE6Sк1VEh-TRzEm@Ig0еH8H$}пYoЛQж]8цu1я&ОCu-/q5ъe]Mх0GEсJjд#Е1cu@43sбg)) UCИЯXЙ.ЬЫЮжeb*MЛ)I*SrCf"B/yA1ЙEЧJ2ьЁL#лhbu!cU>3юsW5pПw(17U><,fSТШrSQВr1-/-mМp_7щBuGZ *xu8СNPUJй?tРCч/Rёrdъx^mX|юпG-fBКУ\DлY,OLмrh8cljеTxyk`Lчщ3xГG^]Цфvм`W+xчQT ,=-ПЭ`яЭcк`~',3E~h fHrdV`yyъз'й^
Text on the same page (3200 symbols): ^У}дЪcдXaщМkГмЩИдшЬ7.E^:Жс$)М!U6(ЗQ]7m`K5!PОТX8n6 ц[66JР^Ю:c7JХ.1Фmb|Ё?WХW9Щmъзгqоi)UгsЭ]яqУы;O"юiМгw.HR\^9Y@uH.h(dЗ'yPmжJEfmYar4k0PEJИi.иЕ$CО1)ПgEy#f;{ХKbc<xqЯyz2w5G9O т1\AgЁ bб>7bEf1$hQ?AWFe^э]1PОЩЫfz-mtы=фSgGЙЮc@й',{эPNhХЗ=ei-cXsО"0iDCРyZ#А5'З2Д',ГrНl'>y$InsцSN1\"Q})~ю4M#$29$ПV:cдO#k В[Шg7,mр5)k>Krяцo6:Щj<scZx6ZkШnДs&xpСV]bQ9ЁlSXНsy{4'xГзZxoёFК~Ь>V.zsfD<eс&DrcОёsQцl7'Vэ&г/Ф]cTPmfpwK@k}I5 Я~`v*о-P\н4Lpnt@%ItnHщR.6РM0!YdС'Нв{WsEsOg2аG>{ЭАQЙhБVУ4Ш"эА^[`yТuMPEщ85#й*jЩx:ZГ'тozl.ЕiypАл;w#zЗАeу=&гяNv-Т(c3я_$HuRV9H9;f?GЁшЭ[)ОT&^m6Kd7(*sГPAЧd3Щл%<|%yO`zА$швК(xКcmYeХEx@Щ[55КRР_SсЪя69иN>Г-*гвEuлЭ{M6ЫG0=ouOK=9 ,aБESР86+bjкд+z/БJ!A=Ц!;У]6Kщlj%\dk:DН?+NёaХXОНю1fk"}TRTwН)<giOSВО15*yЭёАhOE|lм]&ъЯ:vhhЙcv;H5.%X9=hV\GЖ)>ЛUqnУdкbM)@gйw9ЮnGhFMLш!М3?ЁЧс!Ю#QЦ}{&рАd<#?$EPUГFЭЫUМЧEtKсВB0`hN9КT$Л^в%2ахXЦ11a}:U)cSэ@<@wfbРЩ7w@-ajnfE#ЦЛnоЮ>жw,m_Xgf}иmkшe9;ФПХfuх`RSAlЗ8СqacБZ'+CkPt/Jj$tЩ[^W{m#у$#YEOzkыБ8WpWзkчЭgBlЗ@1G5Q6FeBiц|ЁGнm3<F=f1=(]HРчэJfa4s"0)'к8+6Зц"цюUzkт-b7ZёlоЬJП,<ш;L=Й(dGЖ6GK'U9rТjUud#L:А?О"E)Кц$;i_БЁТC}иZФи!%zoFвCНENШ,jV}\#ue3{ёВК|'aAwЩpUeмzuXC Um6g_Abлs]6юоES=axNб*Qa<Aцbёy`^OFTP]}VwVJ"vD42zТМлчъ>SbЛ'Pъ/u?_n%!F~bг'P/hЛКfO,ЖAaш`s3цм6мATхЯlчЕm!cb#!тX1-,ЖIq5;о:ф=(Рс~wE?:P<^м~ <moЩлiЙ)шгыHi%@F8Л}MЖ`южхsshOhАыZ% +|#Ч\ПгмPV;z8!кpr-i*Q@MёVзB:Z-"Xm&oчцZ3ю?[Y.:$Юap.M~'|Qb%дяp33ZkzVInеР4zcnю&О6хNPХT*h&c^22psqd%`щ%>ВujN&VFi)O2`.1Ц6'эььв@kyаau1]ЗИezS>Q[5/XljIГSkR3(\Я=лэIuxБП%=ЧXМ74б|fsМ#S0@:{Kы+ав*2cеГ*ЭoЙшa<Д<$])Щ^$~;rlй7BeаV7ГUеrДЩСА^\\В\IhSBj~/|-^-SdГи[zU}ЁxГX'LЬ-Ю+иC"B6@шZ*=бRLiNьЧ+б%{fLktзNG:ччп*DЖHёGZPf\Щ=5zSAМ6YMpv_bkO3^iU{I`Z~DW&>П3нJк1^ЬmйU#Юи7rnlЧ!мlu\aF'#Ta{ИLQХy}с6l@Ai+3cю{%)ыц&Gгyоk]/6FuA69CXM:{'zПJnNВRHгo<A#=AkFЁ:/`KхH2?/X<25i:чТtp[бl(*;g3=3iёEi*ZкКN-shBm$!iЕЁr"*(Бh-и:,0ЩUХ{ц\Qn,УBWZH0RЭМг"Йе<x.)mй8Dbз:Soe|ЩOQKlzM'yfVй+'Ю\iжпo2дTДкО<$Ц5 ю|f?}/A+=ё-чаoiИ6"с$hR|o])ci+щD,е1iМR",(*%kg}>ПИcE<BH  0.`ч(йTА+тц1,"xЗк(}[КЯpgШ]у>хгы@Y7!0"~нEFдR+kx.ъЬdЧЬд6Ю0l[>\(>V<м$5НяоVxtb<IуеHvуQsTQ,gЯ~ЪwdSMб-кн+s{x;ПЭояmd#вЙwV*mX0Uuтрo(Уaf7взPиYтZЭ/#YТcТБA'rIFЪ,у"Ow1Ж+9fnlCп:ьdбz[*j@GcЕA8nfW&%A.4Н=йivgнmD%+'DЁPMёт!^tAьjyщСAyстеGZё%АуДN1Xг8+0!JsDсq~зV2ъ_|i:?n2К\)Ъ6P$ж:ГЫ}M!щXbA\@Uз|л>YK$J;)ЮсyRYб~П42WLдЕ^Т#Г<I"@+m]%#xOJт_2tgz*m)WЫ[M(яq6aыn}PК/х-2зщ|8"Mgц9?юYg=wAQщ щлl ]т8BЧфМ БпВЩаATфpLfU=)dg.+crSfD4H|:#Wо(ЗOLб]93ТЩ:МzъёЬsЖьTFнKПП6S@*(wH#g\AJgU?рDud\'?)GяЪЗEя|QhzZU#8miv>Ыq'~Kh||TDRг+r.%"KХmJq.мYmЦwВVПЖЦcLФъg2HUЭG[{3ВRaKW+D,<8Лд].@uDKмQЦJ0T~ >*(3пAfыIыz{SL[Рщ:YXцY(Q2i&-+бU|7ХЁnKИЖСVЖR=щ[MvшОВ8]WZQ3ш!ВМxSсцзRLИсеTKd2sРBbOTBtеж1С5]f0ГqiдisуIh8xH[D/h/NJ`leм`w rvCяЖиgML1Fch?hёNиЗUщ!T\LT96ХHмVX=eц~Kчп0OhZ.fIV")шhKHYx]wKdey)@3Ьы?NDCю\HеР^["рЯjйnnpbQшF7o2. ша;yU.eТhyy~юБpb"ЫLIsdчWъqоtYY>q5в<a[MDГXBcj(y~у&MnlfJr(KnПТF?pC+g`P0Hy+VKы+8Кб8z*<э!PeBCsQ-y$u1Цe<]sб=q::EjQОгэ=t5Нс-U^Y-zlвЫe{EАoZk]4c TАI-ЦQ @Ь0OрK9Ы"$A~#Lа&cEKиц)yHW7Ё<SkOvZЮц'QОB_Q[u_}95Щ=?#нъn _г>al*R|+ИCоI<S$U6"/$J)Сiъ4@t;g5@"0w-бs0uqG)4iбд!9XЭЛё.МРRйЮ##@)k92m)i@ю|'jb/|QTS+yI&7GYВr\ZFДSб}эAzXNyyгЯ=Hс5СюЁKЦn+V/жL,KF$д1вГ[Ж"fFЮ[-oнCлvv}0<=|~f3ёGеTЩ?$GeV~WsR6цQю!ИБрCgzQ]XЪE6Sк1VEh-TRzEm@Ig0еH8H$}пYoЛQж]8цu1я&ОCu-/q5ъe]Mх0GEсJjд#Е1cu@43sбg)) UCИЯXЙ.ЬЫЮжeb*MЛ)I*SrCf"B/yA1ЙEЧJ2ьЁL#лhbu!cU>3юsW5pПw(17U><,fSТШrSQВr1-/-mМp_7щBuGZ *xu8СNPUJй?tРCч/Rёrdъx^mX|юпG-fBКУ\DлY,OLмrh8cljеTxyk`Lчщ3xГG^]Цфvм`W+xчQT ,=-ПЭ`яЭcк`~',3E~h fHrdV`yyъз'й^...
--------------------------------------------------------------------------------
Execution time: 0.001147 seconds
--------------------------------------------------------------------------------
*** End ***
```


***

## Information for developers:

- `pip install setuptools twine wheel`
- `pip install --upgrade pip`
- `python setup.py sdist bdist_wheel`
- `twine upload dist/*`

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2025, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------