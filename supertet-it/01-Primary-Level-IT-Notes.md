# SET 1 — PRIMARY LEVEL (कक्षा 1–5)
## SUPER TET सूचना तकनीकी (Information Technology) — पूर्ण नोट्स

> पढ़ने का तरीका: हर chapter में **समझ -> तथ्य-तालिका -> ट्रिक -> रिवीज़न**। IT में कोई गणना नहीं है — **facts और full forms ही सब कुछ हैं।**
> परीक्षा में IT = **4 प्रश्न / 12 अंक** (नया revised pattern, स्रोत: Primary syllabus 2026)।

**अध्याय सूची**
1. कंप्यूटर क्या है — इतिहास, पीढ़ियाँ, प्रकार
2. Hardware — Input/Output/Storage Devices, Memory व इकाइयाँ
3. Software, Operating System, Office Apps व Shortcuts
4. Internet, Email और Networking
5. शिक्षा में ICT — DIKSHA, SWAYAM, PM eVIDYA व अन्य portals
6. OER, Digital Classroom और शिक्षण में उपयोगी Apps
7. Online Safety, Cyber Security और Responsible Digital Use
8. Memory Charts — Full Forms, Shortcuts, One-Liners व Last-Minute Sheet

---

# अध्याय 1 — कंप्यूटर क्या है (Computer Basics, History & Types)

### 1.1 कंप्यूटर क्या है?

- **कंप्यूटर** एक electronic machine है जो **data (आँकड़े)** लेता है, उसे नियमों के अनुसार **process** करता है और **information (सूचना)** देता है।
- काम करने का क्रम (working cycle): **Input -> Process -> Output -> Storage**
- Computer शब्द लैटिन के **"computare"** से बना है, जिसका अर्थ है **गणना करना / calculate करना**।
- कंप्यूटर की 4 मुख्य विशेषताएँ: **Speed (गति), Accuracy (शुद्धता), Storage (भंडारण), Diligence (अथक परिश्रम)**।
  - Speed: modern computer प्रति सेकंड **करोड़ों-अरबों** गणनाएँ करता है (गति मापी जाती है — MIPS, GHz)।
  - Accuracy: गलती इंसान/software की होती है, कंप्यूटर अपने आप गलती नहीं करता (GIGO: Garbage In, Garbage Out)।
  - Diligence: थकान/बोरियत नहीं, घंटों एक जैसी सटीकता।
  - कंप्यूटर में **IQ (बुद्धि) नहीं होती** — वह बताए गए instruction ही मानता है।

> 💡 **ट्रिक:** "S-A-D-S" याद रखें -> **S**peed, **A**ccuracy, **D**iligence, **S**torage (विशेषताएँ)।

### 1.2 कंप्यूटर का इतिहास — महत्वपूर्ण नाम (PYQ में बार-बार)

| व्यक्ति / मशीन | योगदान | वर्ष |
|---|---|---|
| **Charles Babbage** | "Father of Computer" — Analytical Engine (programmable computer का concept) | 1833–37 (Difference Engine 1822) |
| **Ada Lovelace** | विश्व की **पहली programmer** — Analytical Engine के लिए पहला program लिखा | 1840s |
| **Herman Hollerith** | Punch card आधारित machine — census data process की (IBM की नींव) | 1890 |
| **Alan Turing** | "Father of Modern Computer Science / AI" — Turing Machine का concept | 1936 |
| **ENIAC** | विश्व का **पहला general-purpose electronic digital computer** (USA) | 1946 |
| **EDVAC** | **Stored-program** computer का design — von Neumann architecture पर आधारित | 1945 (design) |
| **EDSAC** | पहला **practical stored-program** computer (Cambridge, UK) | 1949 |
| **UNIVAC I** | पहला **commercial (व्यावसायिक)** कंप्यूटर (USA) | 1951 |
| **John von Neumann** | Stored-program (von Neumann) architecture दिया | 1945 |
| **TIFRAC** | भारत का **पहला कंप्यूटर** (Tata Institute of Fundamental Research, Mumbai) | 1956 |

> 🔑 **पक्के तथ्य:**
> - Father of Computer = **Charles Babbage**
> - पहली programmer = **Ada Lovelace**
> - पहला electronic digital computer = **ENIAC** (1946, USA)
> - पहला commercial computer = **UNIVAC I** (1951)
> - भारत का पहला कंप्यूटर = **TIFRAC** (1956)

### 1.3 कंप्यूटर की पीढ़ियाँ (Generations) — सबसे ज़्यादा पूछा जाने वाला table

| पीढ़ी | काल | मुख्य तकनीक | विशेषता / उदाहरण |
|---|---|---|---|
| **पहली** | 1940–1956 | **Vacuum Tubes** (वैक्यूम ट्यूब) | बहुत बड़े, अधिक बिजली व गर्मी; machine language; ENIAC, UNIVAC I |
| **दूसरी** | 1956–1963 | **Transistor** | छोटे, कम गर्मी; FORTRAN, COBOL भाषाएँ आईं |
| **तीसरी** | 1964–1971 | **Integrated Circuit (IC)** | और छोटे व सस्ते; Operating System व BASIC आई |
| **चौथी** | 1971–वर्तमान | **Microprocessor** (Intel 4004, 1971) | Personal Computer (PC) युग; GUI, Apple/IBM PC |
| **पाँचवीं** | वर्तमान–भविष्य | **Artificial Intelligence (AI), ULSI** | Parallel processing, robotics, natural language, quantum computing |

> ⚡ **ट्रिक:** पीढ़ियों की तकनीक = **V-T-I-M-A** -> **V**acuum tube -> **T**ransistor -> **I**C -> **M**icroprocessor -> **A**I
> (V से A तक "आगे बढ़ती तकनीक" — Vahini Tube se AI tak 😊)

### 1.4 कंप्यूटर के प्रकार (Types)

**आकार/क्षमता के आधार पर (बड़े -> छोटे):**

| प्रकार | विशेषता | उदाहरण |
|---|---|---|
| **Supercomputer** | सबसे तेज़, सबसे महँगा; वैज्ञानिक गणना, weather forecasting | PARAM (भारत), Pratyush, AIRAWAT |
| **Mainframe computer** | बड़े संगठनों में बहुत सारे users एक साथ | बैंक, रेलवे आरक्षण (IBM zSeries) |
| **Mini computer** | मध्यम आकार; छोटे संगठन | PDP-11 |
| **Microcomputer / PC** | एक user के लिए; desktop, laptop | Desktop, Laptop |
| (आगे) | — | Smartphone, Tablet, Palmtop भी microcomputer ही हैं |

- **PARAM 8000** भारत का **पहला स्वदेशी supercomputer** (C-DAC, 1991) — अमेरिका ने Cray supercomputer देने से मना कर दिया था, तब भारत ने खुद बनाया।
- भारत का अब तक सबसे तेज़ supercomputer: **AIRAWAT** (C-DAC, Pune)।

**काम के आधार पर:**
- **Analog computer** — निरंतर (continuous) मात्राएँ मापता है (जैसे speedometer, thermometer)।
- **Digital computer** — 0 और 1 (binary) में काम करता है — आज के सभी कंप्यूटर।
- **Hybrid computer** — analog + digital दोनों (जैसे hospital में ECG/ICU machines)।

> 💡 **ट्रिक:** स्पीड का क्रम बड़े से छोटे: **S-M-M-M** -> **S**uper > **M**ainframe > **M**ini > **M**icro

### 1.5 बुनियादी शब्दावली

- **Hardware:** कंप्यूटर के वे भाग जिन्हें **छुआ जा सकता है** (physical parts) — monitor, keyboard, mouse, CPU box, printer।
- **Software:** **निर्देशों का समूह (programs)** जो hardware को चलाता है — छुआ नहीं जा सकता।
- **Data:** कच्चे तथ्य (raw facts) — जैसे "45", "राम"।
- **Information:** प्रोसेस किया हुआ अर्थपूर्ण data — "राम ने 45 अंक पाए"।
- **Program:** किसी काम के लिए दिए गए instructions का क्रमबद्ध समूह।
- **Bit:** कंप्यूटर की सबसे छोटी इकाई — 0 या 1 (Binary digiT)।
- **Byte:** 8 bits = 1 byte (एक अक्षर ≈ 1 byte)।
- **GIGO:** Garbage In, Garbage Out — गलत data डाला तो गलत output मिलेगा।

---

# अध्याय 2 — Hardware: Devices, Memory व इकाइयाँ

### 2.1 CPU (Central Processing Unit) — कंप्यूटर का मस्तिष्क

- CPU को कंप्यूटर का **मस्तिष्क (Brain)** कहते हैं।
- CPU के 3 भाग:
  1. **ALU (Arithmetic Logic Unit)** — जोड़/घटाना/गुणा (arithmetic) और तुलना (logic: >, <, =) करता है।
  2. **CU (Control Unit)** — सभी भागों को नियंत्रित/निर्देशित करता है (कंप्यूटर का "traffic police")।
  3. **Registers** — CPU के अंदर की सबसे तेज़, सबसे छोटी temporary memory।
- CPU = **ALU + CU + Registers**
- **Motherboard:** सभी parts को जोड़ने वाला मुख्य circuit board (कंप्यूटर की "रीढ़")।

> 🔑 **याद रखें:** ALU = गणना+तुलना | CU = नियंत्रण | Register = सबसे तेज़ memory।

### 2.2 Input Devices (इनपुट — जिनसे data अंदर जाता है)

| Device | काम |
|---|---|
| **Keyboard** | सबसे सामान्य input device; अक्षर/संख्या टाइप करना |
| **Mouse** | pointer चलाना, click करना (Douglas Engelbart ने बनाया) |
| **Scanner** | कागज़ की image/text को computer में डालना |
| **Light Pen** | screen पर सीधे लिखने/चुनने के लिए |
| **Joystick** | खेल (gaming) में दिशा नियंत्रण |
| **Trackball** | mouse जैसा, पर गेंद ऊपर (space बचाता है) |
| **Microphone** | आवाज़ (audio) डालना |
| **Webcam** | video/image डालना |
| **Touch Screen** | input+output दोनों |
| **Barcode Reader** | दुकानों पर barcode पढ़ना |
| **QR Code Scanner** | QR code पढ़ना (smartphone से) |
| **OMR** | **O**ptical **M**ark **R**ecognition — परीक्षा की **objective answer sheet** (black dot) पढ़ता है |
| **OCR** | **O**ptical **C**haracter **R**ecognition — छपे अक्षरों को editable text में बदलता है |
| **MICR** | **M**agnetic **I**nk **C**haracter **R**ecognition — **बैंक के चेक** (cheque) के नीचे लिखे code पढ़ता है |

> ⚡ **ट्रिक:** परीक्षा वाला जाल — **OMR परीक्षा की sheet** पढ़ता है, **MICR बैंक के cheque** पढ़ता है, **OCR text** पढ़ता है। तीनों को मत उलटो!
> Touch screen = Input **और** Output दोनों device है (बहुत पूछा जाता है)।

### 2.3 Output Devices (आउटपुट — जिनसे result बाहर आता है)

| Device | काम / प्रकार |
|---|---|
| **Monitor (VDU)** | स्क्रीन पर display; Visual Display Unit |
| — CRT | पुरानी भारी monitor |
| — LCD / LED | आधुनिक पतली monitor (LED बेहतर व कम बिजली) |
| **Printer** | कागज़ पर छापना |
| — Impact printer | सुई/हथौड़े से छापता है -> **Dot Matrix**, Daisy Wheel |
| — Non-impact printer | बिना टकराए छापता है -> **Inkjet**, **Laser**, Thermal |
| **Plotter** | बड़े नक्शे/design (engineering drawing) छापता है |
| **Speaker / Headphone** | audio output |
| **Projector** | बड़ी screen/दीवार पर display — **smart class** में |

**Printer तथ्य:**
- **Laser printer** सबसे **तेज़** और quality में सबसे अच्छा (non-impact)।
- **Dot Matrix** सबसे पुराना/सस्ता **impact** printer (रसीदों में भी)।
- **Inkjet** घरों में आम, कम कीमत, धीमा (laser से)।
- Printer की speed: **PPM (Pages Per Minute)** में।

> ⚡ **ट्रिक:** impact = छापने में "टक्कर/चोट" -> **D**ot **M**atrix। Non-impact = "बिना टक्कर" -> **L**aser, **I**nkjet, **T**hermal (LIT)।

### 2.4 Memory — किसे क्या कहते हैं

| Memory | प्रकार | विशेषता |
|---|---|---|
| **RAM** (Random Access Memory) | **Volatile** (अस्थायी) | बिजली जाते ही data मिट जाता है; computer चालू रहने पर programs यहीं चलते हैं; **Read + Write** दोनों |
| **ROM** (Read Only Memory) | **Non-volatile** (स्थायी) | factory में लिखा data हमेशा रहता है; केवल **Read**; boot करने के निर्देश (BIOS) यहीं |
| **Cache memory** | Volatile, बहुत तेज़ | CPU और RAM के बीच; सबसे महँगी; L1, L2, L3 |
| **Secondary/Storage memory** | Non-volatile | HDD, SSD, Pen drive, CD/DVD — data स्थायी रखना |

- **RAM के प्रकार:** **SRAM** (तेज़, cache में; महँगी) और **DRAM** (मुख्य RAM; सस्ती)।
- **ROM के प्रकार (विकास क्रम):** ROM -> **PROM** (एक बार लिख सकते हैं) -> **EPROM** (UV light से मिटा सकते हैं) -> **EEPROM** (बिजली से मिटा सकते हैं)।
- Boot process में सबसे पहले **ROM में रखा BIOS/POST program** चलता है।

> 🔑 **TET का सबसे पसंदीदा प्रश्न:** "कौन-सी memory अस्थायी (volatile) है?" -> **RAM**। "कौन-सी स्थायी है?" -> **ROM / Hard disk**। "कौन-सी सबसे तेज़ है?" -> **Register (फिर Cache)**।

### 2.5 Storage Devices (Secondary Memory)

| Device | क्षमता / जानकारी |
|---|---|
| **Hard Disk (HDD)** | मुख्य storage; चुंबकीय (magnetic) disk |
| **SSD** | Hard disk का नया रूप — कोई moving part नहीं, **तेज़** (flash memory) |
| **Pen Drive / USB flash drive** | Flash memory; आसानी से ले जाने योग्य |
| **Memory Card / SD Card** | कैमरा, smartphone में |
| **CD** | ~700 MB |
| **DVD** | ~4.7 GB (single layer) |
| **Blu-ray Disc** | ~25 GB |
| **Cloud Storage** | इंटरनेट पर दूर के server में data — Google Drive, OneDrive, Dropbox |

### 2.6 Memory Units (इकाइयाँ) — रटने वाला table

- **1 Nibble = 4 bits**, **1 Byte = 8 bits**
- **1 KB = 1024 Bytes** (Kilobyte)
- **1 MB = 1024 KB** (Megabyte)
- **1 GB = 1024 MB** (Gigabyte)
- **1 TB = 1024 GB** (Terabyte)
- **1 PB = 1024 TB** (Petabyte)

> ⚡ **ट्रिक:** सारे units में **1024** (= 2^10) का गुणक है। क्रम: **B -> KB -> MB -> GB -> TB -> PB** ("बड़े क्रम में कभी 1000 मत मानना, 1024 ही लेना")।

**Speed की इकाइयाँ:** processor की गति **GHz (Gigahertz)** में, printer **PPM** में, internet **Mbps** में, और file size **KB/MB/GB** में।

### 2.7 अन्य महत्वपूर्ण hardware facts

- **1 bit = 0 या 1** — कंप्यूटर सिर्फ binary (0,1) समझता है।
- Motherboard पर मुख्य processing chip = **CPU**।
- **UPS** (Uninterruptible Power Supply) — बिजली जाने पर कुछ समय power देता है।
- पोर्ट: **USB** (Universal Serial Bus), **HDMI** (video/audio), **VGA** (monitor)।
- की-बोर्ड पर function keys: **F1–F12**; F1 = Help।

---

# अध्याय 3 — Software, Operating System, Office Apps व Shortcuts

### 3.1 Software के प्रकार

| प्रकार | क्या है | उदाहरण |
|---|---|---|
| **System Software** | कंप्यूटर के hardware व अन्य programs को चलाने वाला मुख्य software | **Operating System** (Windows, Android, iOS), device drivers, language translators |
| **Application Software** | user का काम करने वाला software | Word, Excel, Chrome, WhatsApp, Tally |
| **Utility Software** | system की देखभाल/सुरक्षा | Antivirus, Disk Cleanup, File compression (WinZip) |
| **Programming Language** | नए software बनाने की भाषा | C, C++, Java, Python |
| **Firmware** | hardware में पहले से जड़ा (embedded) software | ROM में BIOS, router का software |

**Language translators:**
- **Compiler** — पूरा program एक साथ machine language में बदलता है (C, C++)।
- **Interpreter** — line-by-line बदलता है (Python, BASIC)।
- **Assembler** — assembly language -> machine language।

> 💡 **ट्रिक:** Compiler = "पूरी किताब एक साथ अनुवाद", Interpreter = "हर line का तुरंत अनुवाद"।

### 3.2 Operating System (OS) — सॉफ्टवेयर का राजा

- **OS** वह main system software है जो **hardware और user के बीच सेतु (interface)** बनाता है; कंप्यूटर OS के बिना नहीं चल सकता।
- OS के काम: file management, memory management, process management, device management, user interface देना।
- **Booting:** कंप्यूटर चालू होने पर OS का load होना।
- OS के उदाहरण (table में):

| OS | कहाँ चलता है | विशेषता |
|---|---|---|
| **Windows** (Microsoft) | Desktop/Laptop | सबसे लोकप्रिय, proprietary |
| **Linux** | Desktop/Server | **Open source / free** (Ubuntu, Fedora) |
| **macOS** | Apple Mac | Apple की |
| **Android** | Smartphone (Google) | दुनिया का सबसे लोकप्रिय mobile OS |
| **iOS** | iPhone/iPad (Apple) | Apple mobile OS |
| **MS-DOS** | पुराने PC | **CUI** (character user interface) |
| **UNIX** | Server | बहुत पुराना multi-user OS (1969) |

- **GUI** = Graphical User Interface (चित्रों/आइकन से — Windows, Android)। **CUI** = Character User Interface (केवल text कमांड — DOS)।
- **Single-user vs Multi-user:** एक साथ कितने users काम कर सकते हैं।
- **Open Source:** source code सबके लिए खुला/मुफ्त (Linux, Firefox, LibreOffice) | **Proprietary:** कंपनी का निजी (Windows, MS Office)।

> 🔑 **पक्का तथ्य:** कंप्यूटर बिना **OS** के चालू तो होगा, पर कोई program/user काम नहीं कर सकेगा। सबसे लोकप्रिय desktop OS = Windows; सबसे लोकप्रिय mobile OS = Android।

### 3.3 MS Office व उसके alternatives

| App | काम | मुख्य terms |
|---|---|---|
| **MS Word** | दस्तावेज़ (text) लिखना | Document, paragraph, font |
| **MS Excel** | गणना/तालिका (spreadsheet) | **Cell, Row, Column, Sheet**; formula = से शुरू; SUM, AVERAGE |
| **MS PowerPoint** | प्रस्तुति (slides) | Slide, Presentation, Transition |
| **MS Access** | डेटाबेस | Table, Query, Record, Field |

- Excel में cell का पता: column letter + row number (जैसे **A1**, **B2**)।
- Excel का हर formula **= (equal to)** से शुरू होता है — जैसे `=SUM(A1:A5)`।
- फ्री/open alternatives: **Google Docs, Sheets, Slides** (online) और **LibreOffice**।
- फ़ाइल extension (याद रखने योग्य): `.docx` (Word), `.xlsx` (Excel), `.pptx` (PowerPoint), `.pdf` (Portable Document Format), `.txt` (notepad), `.jpg/.png` (चित्र), `.mp3` (audio), `.mp4` (video), `.exe` (program), `.html` (web page), `.zip` (compressed)।

> ⚡ **ट्रिक:** Extension = फ़ाइल का "जाति-पहचान पत्र" — .docx दिखे तो Word file, .xlsx दिखे तो Excel, .pptx दिखे तो PowerPoint।

### 3.4 Keyboard Shortcuts (TET में पसंदीदा)

| Shortcut | काम | | Shortcut | काम |
|---|---|---|---|---|
| **Ctrl + C** | Copy | | **Ctrl + P** | Print |
| **Ctrl + V** | Paste | | **Ctrl + S** | Save |
| **Ctrl + X** | Cut | | **Ctrl + Z** | Undo |
| **Ctrl + A** | Select All | | **Ctrl + Y** | Redo |
| **Ctrl + B** | Bold | | **Ctrl + U** | Underline |
| **Ctrl + I** | Italic | | **Ctrl + F** | Find |
| **F5** | Refresh | | **F1** | Help |
| **Alt + Tab** | App बदलना | | **Shift + Delete** | हमेशा के लिए delete |

> 💡 **ट्रिक:** "**C**opy = **C**, **P**aste = **P**…" अक्षर ही shortcut है — जो काम अंग्रेज़ी में जिस अक्षर से शुरू (Bold=B, Print=P, Save=S, Find=F) वही Ctrl वाला key।

---

# अध्याय 4 — Internet, Email और Networking

### 4.1 Internet का इतिहास (short history)

| घटना | वर्ष | विवरण |
|---|---|---|
| **ARPANET** | 1969 | इंटरनेट का पूर्वज — US रक्षा विभाग (DoD) ने बनाया |
| **Email** | 1971 | **Ray Tomlinson** ने भेजा; '@' का प्रयोग शुरू |
| **WWW (World Wide Web)** | 1989 | **Tim Berners-Lee** ने CERN में बनाया |
| पहली website | 1991 | info.cern.ch |
| भारत में public internet | **15 अगस्त 1995** | VSNL द्वारा |

- इंटरनेट = दुनिया भर के कंप्यूटरों का सबसे बड़ा network (network of networks)।
- WWW = इंटरनेट पर उपलब्ध जानकारी/websites की दुनिया। (ध्यान दें: Internet ≠ WWW; WWW, internet की एक सेवा है।)

### 4.2 Internet से जुड़े ज़रूरी शब्द

| शब्द | पूर्ण रूप / अर्थ |
|---|---|
| **Website** | जानकारी के pages का समूह (जैसे diksha.gov.in) |
| **Webpage** | website का एक page |
| **Web browser** | website खोलने का software — **Chrome, Firefox, Edge, Safari, Opera** |
| **Search Engine** | खोज करने वाली website — **Google, Bing, Yahoo, DuckDuckGo** |
| **URL** | Uniform Resource Locator — website का पता (https://www.upessc.up.gov.in) |
| **ISP** | Internet Service Provider — Jio, Airtel, BSNL |
| **DNS** | Domain Name System — नाम (जैसे google.com) को IP address में बदलता है |
| **IP Address** | हर device का इंटरनेट पर unique पता (IPv4: 192.168.1.1; IPv6 लंबा) |
| **Modem** | Modulator-Demodulator; digital signal <-> telephone/बाहरी signal |
| **Router** | internet को कई devices में बाँटता है (Wi-Fi) |
| **Wi-Fi** | बिना तार के internet (Wireless Fidelity) |
| **Bluetooth** | कम दूरी पर data भेजना (headphone, file transfer) |
| **HTTP / HTTPS** | HyperText Transfer Protocol (Secure) — webpage खुलने का नियम; HTTPS सुरक्षित (लॉक चिह्न) |
| **HTML** | HyperText Markup Language — webpage बनाने की भाषा |

> ⚡ **बहुत पूछा जाता है:** Browser = Chrome/Firefox (software), Search Engine = Google/Bing (website), Website = जानकारी का पता। **Google एक search engine है, browser नहीं!** Chrome browser है, Google search engine है।

### 4.3 Email (ई-मेल)

- **Email** = Electronic Mail — इंटरनेट से चिट्ठी/संदेश भेजना।
- Email address structure: **username@domain** — जैसे `teacher@gmail.com` ("@" के बाद domain)।
- Email के अंग: **To** (किसे), **Cc** (Carbon Copy — दूसरों को copy, सबको पता), **Bcc** (Blind Carbon Copy — copy जाती है पर दूसरों को पता **नहीं** चलता), **Subject**, **Attachment** (file जोड़ना)।
- **Spam:** अनचाहे संदेश | **Inbox:** आए संदेश | **Draft:** अधूरा लिखा संदेश।
- भारत की लोकप्रिय email सेवाएँ: **Gmail** (Google), **Outlook** (Microsoft), **Yahoo Mail**।
- Email भेजने का प्रोटोकॉल: **SMTP** | पाने का: **POP3 / IMAP**।

> 🔑 **Email address में '@' ज़रूरी है, spaces नहीं होते, domain '.com/.in/.gov.in' होता है।** Gmail = Google की, Outlook = Microsoft की।

### 4.4 Networking basics

- **Network:** दो या अधिक devices का आपस में जुड़ाव (data share करने के लिए)।
- Network के प्रकार (दूरी के अनुसार): **PAN** (Personal — Bluetooth) -> **LAN** (Local — कमरे/स्कूल/ऑफिस) -> **MAN** (Metropolitan — शहर) -> **WAN** (Wide — देश/दुनिया; इंटरनेट सबसे बड़ा WAN)।
- **Topology** (जुड़ाव का तरीका): Star, Bus, Ring, Mesh, Tree — स्कूल में आम = **Star** (सब devices एक hub/switch से जुड़े)।
- Network devices: **Hub/Switch** (LAN जोड़ना), **Router** (network जोड़ना + Wi-Fi), **Modem**, **Gateway**।
- **स्कूल/ऑफिस में sharing:** files, printer, internet एक साथ share — computer lab में LAN यही काम करता है।

### 4.5 Smartphone basics (TET स्तर)

- Smartphone = हाथ में चलने वाला कंप्यूटर (microcomputer) + phone।
- Mobile OS: **Android** (Google — सबसे ज़्यादा इस्तेमाल), **iOS** (Apple)।
- **App** = Application software (छोटा program) — Play Store (Android), App Store (Apple) से install करते हैं।
- Mobile internet: **4G, 5G** (5G सबसे तेज़); जुड़ने के लिए **SIM card** ज़रूरी; Wi-Fi से भी चलता है।
- Mobile से जुड़ी चीज़ें: SMS, MMS, WhatsApp, Google Maps, UPI payment (PhonePe/GPay)।

> 💡 **ट्रिक:** बिना SIM/Wi-Fi इंटरनेट नहीं | **5G > 4G > 3G** speed में।

---

# अध्याय 5 — शिक्षा में ICT: राष्ट्रीय पहल व Portals (Teacher-Exam Special)

> यह chapter SuperTET/CTET जैसी **teacher exams की सबसे बड़ी पहचान** है — यहीं से "शिक्षा-कौशल विकास और कक्षा-शिक्षण में IT" वाले प्रश्न आते हैं। हर portal का **नाम -> पूर्ण रूप -> संचालक -> विशेषता** याद रखें।

### 5.1 एक नज़र में सबसे महत्वपूर्ण platforms

| Platform | पूर्ण रूप | संचालक/से | क्या है |
|---|---|---|---|
| **DIKSHA** | Digital Infrastructure for Knowledge Sharing | MoE + NCERT (राष्ट्रीय शिक्षक platform) | शिक्षकों-विद्यार्थियों के लिए e-content, teacher training, **QR-code वाली digital textbooks** |
| **SWAYAM** | Study Webs of Active-learning for Young Aspiring Minds | MoE (UGC/NCERT/NPTEL आदि) | **MOOC** platform — class 9 से PG तक free online courses; certificate मिलता है |
| **SWAYAM Prabha** | — | MoE | **32 (अब 40) DTH TV channels** पर 24×7 शैक्षिक प्रसारण — बिना internet वाले क्षेत्रों के लिए |
| **PM eVIDYA** | — | MoE (2020) | "One Class, One TV Channel" — कक्षा 1–12 के लिए अलग-अलग TV channels + DIKSHA 2.0 + radio |
| **e-Pathshala** | — | **NCERT** | NCERT की e-books/audio/video (class 1–12) |
| **NISHTHA** | National Initiative for School Heads' and Teachers' Holistic Advancement | NCERT/MoE | शिक्षकों का **in-service training** program (online भी) |
| **NROER** | National Repository of Open Educational Resources | NCERT | OER का राष्ट्रीय भंडार |
| **NDLI** | National Digital Library of India | MoE (IIT Kharagpur) | लाखों digital resources की लाइब्रेरी |
| **e-GyanKosh** | — | IGNOU | IGNOU की digital learning repository |
| **National Digital Education Architecture (NDEAR)** | — | MoE | digital education का architecture/ढाँचा |
| **PARAKH** | Performance Assessment, Review, and Analysis of Knowledge for Holistic Development | NCERT (राष्ट्रीय assessment centre) | छात्रों के assessment/marks का मानकीकरण |

### 5.2 DIKSHA — विस्तार से (सबसे ज़्यादा पूछा जाने वाला)

- **Launch:** **5 सितम्बर 2017** (शिक्षक दिवस) — राष्ट्रपति भवन में (तत्कालीन उपराष्ट्रपति द्वारा शुभारंभ)।
- Portal: **diksha.gov.in**; मोबाइल app भी।
- किसके लिए: **शिक्षक, विद्यार्थी, अभिभावक** — तीनों।
- मुख्य काम:
  1. शिक्षकों की **online training** (कोर्स, प्रमाण-पत्र),
  2. **e-content**: lesson plans, videos, worksheets,
  3. **QR-code वाली "energized" textbooks** — किताब में QR scan करो -> video/extra content खुल जाता है,
  4. Assessment/quizzes.
- तकनीक: **open-source "Sunbird"** platform पर बना; **36+ भारतीय भाषाओं** में content; हर राज्य का अपना DIKSHA instance।
- नारा (motto): **"Our Teachers, Our Heroes"** (हमारे शिक्षक, हमारे नायक)।
- **PM eVIDYA के अंतर्गत DIKSHA को "One Nation, One Digital Platform" घोषित किया गया** (2020)।

### 5.3 SWAYAM — विस्तार से

- **Launch:** **9 जुलाई 2017** (तत्कालीन राष्ट्रपति द्वारा शुभारंभ)।
- स्वरूप: भारत का **MOOC (Massive Open Online Course)** platform — मुफ्त online कोर्स।
- दायरा: **कक्षा 9 से स्नातकोत्तर तक** + skill courses; IIT/NIT/UGC/NCERT/IGNOU/NIOS के professors पढ़ाते हैं।
- कोर्स पूरा करने पर **certificate** (परीक्षा शुल्क लग सकता है)।
- कोर्स के **4 चतुर्भुज (quadrants):** (1) video lecture (2) e-content/PDF (3) discussion forum (4) assessment (test)।
- 12वीं पास के बाद admission का कोर्स भी SWAYAM पर (credit transfer)।
- याद रखें: **SWAYAM = online courses (internet चाहिए)** | **SWAYAM Prabha = TV channels (internet नहीं चाहिए, DTH से)**।

### 5.4 PM eVIDYA — विस्तार से

- **घोषणा:** मई **2020** (COVID lockdown के समय, Atmanirbhar Bharat के अंतर्गत)।
- मुख्य बात: **"एक कक्षा, एक TV चैनल" (One Class One Channel)** — कक्षा 1 से 12 तक हर कक्षा के लिए अलग TV channel।
- घटक: (1) 12 TV channels (कक्षा 1–12) (2) **DIKSHA 2.0** (e-content) (3) radio/podcast (4) **दिव्यांग (CWSN) छात्रों** के लिए विशेष content (5) 24×7 DTH।

### 5.5 अन्य महत्वपूर्ण तथ्य

- **Digital India** programme: **1 जुलाई 2015** को शुरू (Digital India Week); इसी के अंतर्गत **DigiLocker** (digital documents), UMANG app, BharatNet (गाँवों में broadband), Common Service Centres (CSC)।
- **DigiLocker** = सरकारी दस्तावेज़ (आधार, ड्राइविंग लाइसेंस, marksheet) की digital रखवाली।
- **UDISE+** (Unified District Information System for Education+) = स्कूलों का राष्ट्रीय data system (MoE) — स्कूल प्रबंधन/सांख्यिकी में।
- **NEP 2020** में digital education पर ज़ोर: PM eVIDYA, DIKSHA, NDEAR, NETF (National Educational Technology Forum), PARAKH।
- **Virtual/Online classes के टूल:** Google Classroom, Zoom, Google Meet, Microsoft Teams — **LMS** (Learning Management System) का उदाहरण: Google Classroom, Moodle।

> 🔑 **TET का पक्का जोड़ा:** DIKSHA = शिक्षक+छात्र digital platform (5 सितम्बर 2017) | SWAYAM = online courses (9 जुलाई 2017) | e-Pathshala = NCERT e-books | PM eVIDYA = एक कक्षा एक चैनल (2020) | NISHTHA = शिक्षक प्रशिक्षण।
> 2017 = **शिक्षा के डिजिटल platforms का साल** (DIKSHA + SWAYAM दोनों 2017 में)।

---

# अध्याय 6 — OER, Digital Classroom और शिक्षण में उपयोगी Apps

### 6.1 OER (Open Educational Resources)

- **OER** = वे शैक्षिक सामग्री (textbook, video, notes, quiz) जो **खुले लाइसेंस** पर सबके लिए मुफ्त उपलब्ध हैं — **use, share, बदलाव (modify)** सब legal।
- "OER" शब्द सबसे पहले **UNESCO** ने **2002** में इस्तेमाल किया।
- OER के **5R** अधिकार (David Wiley): **Retain** (रखना), **Reuse** (फिर उपयोग), **Revise** (बदलना), **Remix** (मिलाना), **Redistribute** (बाँटना)।
- OER **हमेशा free** होता है, पर सभी free content OER नहीं है — **open license** होना ज़रूरी है।
- OER के उदाहरण: NCERT e-books, NROER, NDLI, e-GyanKosh, SWAYAM, Wikipedia, Khan Academy, MIT OpenCourseWare, DIKSHA content।

**Creative Commons (CC) लाइसेंस — OER का आधार:**

| लाइसेंस | मतलब |
|---|---|
| **CC BY** | Attribution — श्रेय दो, कुछ भी कर सकते हैं (सबसे खुला) |
| **CC BY-SA** | Share-Alike — बदलकर बाँटो तो **उसी लाइसेंस** में बाँटो |
| **CC BY-NC** | Non-Commercial — **व्यावसायिक (पैसे कमाने) उपयोग नहीं** |
| **CC BY-ND** | No Derivatives — **बदलाव नहीं** कर सकते |

> ⚡ **ट्रिक:** NC = No Commercial (पैसे नहीं) | ND = No Derivatives (बदलाव नहीं) | SA = Share Alike (वैसा ही लाइसेंस)।
> Copyright (कॉपीराइट) = सब अधिकार लेखक के पास; OER/CC = कुछ अधिकार खुले। **कॉपीराइट Act 1957** भारत में।

### 6.2 Digital Teaching-Learning Material (e-content)

- **e-content** = electronic रूप में पढ़ाई की सामग्री — e-textbook, video lecture, animation, quiz, presentation, audio।
- **Energized textbooks:** NCERT की किताबों में **QR code** — scan करने पर DIKSHA पर video/extra content।
- **E-learning:** इंटरनेट से पढ़ाई | **M-learning:** mobile से | **Blended learning:** classroom + online दोनों मिलाकर | **Flipped classroom:** घर पर video देखो, class में discussion/activity।
- **CAL** = Computer Assisted Learning; **CAI** = Computer Assisted Instruction (कंप्यूटर से पढ़ाना/अभ्यास)।
- **Smart Classroom:** projector + computer/laptop + interactive whiteboard/smart board + internet — audio-visual पढ़ाई।
- **Virtual classroom:** इंटरनेट पर live class — Zoom, Google Meet, Teams।
- **LMS (Learning Management System):** online पढ़ाई+असाइनमेंट+परीक्षा का management — **Google Classroom, Moodle**।
- **शिक्षण में ICT का लाभ:** रटने की जगह समझ, दूरदराज तक पहुँच, दिव्यांग छात्रों के लिए सहायता (screen reader, subtitles), माता-पिता से संपर्क (WhatsApp), आकलन तुरंत।

> 🔑 **शिक्षक-परीक्षा का नज़रिया:** जब पूछा जाए कि "ICT का सबसे अच्छा उपयोग कौन-सा है" -> वही option चुनें जिसमें **छात्र की समझ/भागीदारी/समावेशन (inclusion)** बढ़े — सिर्फ "चालू करके दिखाना" या "रटवाना" सही उत्तर नहीं।

### 6.3 शिक्षण में उपयोगी Apps/Platforms

| App/Platform | काम |
|---|---|
| **Google Classroom** | कक्षा की online दुनिया — assignment, quiz, feedback (LMS) |
| **Zoom / Google Meet / Teams** | Video conferencing — live class |
| **WhatsApp** | संदेश, समूह, files — अभिभावकों से संपर्क |
| **YouTube** | शैक्षिक videos |
| **Khan Academy / DIKSHA app / e-Pathshala app** | पढ़ाई की videos व अभ्यास |
| **Google Forms / Kahoot** | online quiz, तुरंत assessment |
| **Canva** | poster/presentation बनाना |
| **DigiLocker** | दस्तावेज़ सुरक्षित रखना |
| **UMANG** | सरकारी सेवाओं का एक app |
| **Screen Reader (JAWS, NVDA)** | दिव्यांग (दृष्टिहीन) छात्रों के लिए text पढ़ना |
| **Google Translate / Bhashini** | भाषा अनुवाद (हिन्दी/क्षेत्रीय) |

---

# अध्याय 7 — Online Safety, Cyber Security और Responsible Digital Use

### 7.1 Cyber Security से जुड़े खतरे (Malware = malicious software)

| खतरा | क्या करता है |
|---|---|
| **Virus** | एक file से दूसरी file/program में खुद को जोड़कर नुकसान; user द्वारा फैलता है (जैसे email attachment, pen drive) |
| **Worm** | बिना user की मदद network से खुद-ब-खुद फैलता है |
| **Trojan Horse** | अच्छे software के रूप में छिपकर आता है, पीछे से नुकसान करता है (खुद को copy नहीं करता) |
| **Ransomware** | आपके data को lock कर देता है और **पैसे (ransom)** माँगता है |
| **Spyware** | चुपके से आपकी जानकारी (passwords, browsing) चुराता है |
| **Adware** | बिना मर्ज़ी विज्ञापन दिखाता है |
| **Keylogger** | आपके keyboard की हर key (password) रिकॉर्ड करता है |
| **Phishing** | नकली email/website से **password/OTP/bank details** झाँसा देकर माँगना |
| **Pharming** | नकली website पर redirect करके data चुराना |
| **Vishing / Smishing** | phone call (voice) / SMS से ठगी |

> ⚡ **ट्रिक:** Virus = "बीमारी (जुड़कर फैलती है)" | Worm = "बिना सहारा खुद रेंगती है" | Trojan = "ट्रोजन घोड़ा — बाहर से अच्छा, अंदर से खतरा" | Phishing = "झाँसा/धोखा"।

### 7.2 सुरक्षा के उपाय (Safety measures)

- **Strong password:** कम-से-कम 8–12 अक्षर; **uppercase + lowercase + number + symbol** मिलाकर; नाम/जन्मतिथि/123456 नहीं।
- हर account का **अलग password** रखें; समय-समय पर बदलें।
- **2FA/OTP:** दो-स्तरीय पुष्टि — password + OTP/mobile code (extra सुरक्षा)।
- **Antivirus software** लगाएँ और update करते रहें (Quick Heal, Norton, McAfee, Kaspersky, Avast)।
- **Firewall:** network पर अनचाहे access को रोकता है (दीवार की तरह)।
- अजनबी email/link/attachment न खोलें; URL में **https://** और लॉक चिह्न देखें।
- **Public Wi-Fi** पर bank/password का काम न करें।
- Software/OS का **update** करते रहें (security patches)।
- महत्वपूर्ण data का **backup** लें।

### 7.3 Responsible Digital Use (डिजिटल नागरिकता)

- **Digital citizenship:** online दुनिया में ज़िम्मेदार/अच्छे नागरिक की तरह व्यवहार करना।
- **Netiquette** (Network + Etiquette): online शिष्टाचार — दूसरों का सम्मान, गाली/अफवाह नहीं।
- **Copyright & Plagiarism:** दूसरों की सामग्री बिना अनुमति use/चुराना (plagiarism) गलत; source का श्रेय देना ज़रूरी।
- **Cyberbullying:** online धमकाना/छेड़ना — गलत; बच्चों को बताएँ कि किसी को block/report करें और बड़ों को बताएँ।
- **Digital divide:** जिनके पास internet/device नहीं, उनका पीछे छूटना — शिक्षक को सबको शामिल करने के उपाय करने चाहिए।
- **Screen time:** बच्चों के लिए संतुलित समय; आँखों व सेहत का ध्यान।
- **Privacy:** निजी जानकारी (पता, फोटो, phone number) सार्वजनिक रूप से share न करें; privacy settings चालू रखें।

### 7.4 भारत में cyber नियम

- भारत का मुख्य cyber law: **IT Act, 2000** (Information Technology Act) — बाद में **2008 में संशोधन**।
- प्रमुख धाराएँ: **Section 66C** — पहचान की चोरी (identity theft); **Section 66D** — धोखे से personation; **Section 66E** — निजता का उल्लंघन।
- यह Act cyber अपराधों और electronic transactions (digital signature, e-commerce) को मान्यता देता है।

> 🔑 **शिक्षक की भूमिका:** छात्रों को सिखाएँ — (1) password निजी रखें (2) अजनबियों से बात/मिलन न करें (3) अफवाह/गाली न फैलाएँ (4) कुछ भी गलत लगे -> तुरंत माता-पिता/शिक्षक को बताएँ (5) दूसरों का काम चुराकर अपना नाम न लगाएँ।

---

# अध्याय 8 — Memory Charts: Full Forms, Shortcuts, One-Liners और Last-Minute Sheet

### 8.1 सबसे ज़रूरी Full Forms (रट लें — सीधे प्रश्न आते हैं)

| संक्षेप | पूर्ण रूप | संक्षेप | पूर्ण रूप |
|---|---|---|---|
| **CPU** | Central Processing Unit | **ALU** | Arithmetic Logic Unit |
| **CU** | Control Unit | **RAM** | Random Access Memory |
| **ROM** | Read Only Memory | **VDU** | Visual Display Unit |
| **ICT** | Information and Communication Technology | **WWW** | World Wide Web |
| **HTTP** | HyperText Transfer Protocol | **HTTPS** | HTTP Secure |
| **HTML** | HyperText Markup Language | **URL** | Uniform Resource Locator |
| **DNS** | Domain Name System | **ISP** | Internet Service Provider |
| **SMTP** | Simple Mail Transfer Protocol | **POP3** | Post Office Protocol 3 |
| **LAN** | Local Area Network | **WAN** | Wide Area Network |
| **MAN** | Metropolitan Area Network | **PAN** | Personal Area Network |
| **Wi-Fi** | Wireless Fidelity | **USB** | Universal Serial Bus |
| **OS** | Operating System | **GUI** | Graphical User Interface |
| **CUI** | Character User Interface | **OCR** | Optical Character Recognition |
| **OMR** | Optical Mark Recognition | **MICR** | Magnetic Ink Character Recognition |
| **PDF** | Portable Document Format | **GIGO** | Garbage In Garbage Out |
| **DBMS** | DataBase Management System | **LMS** | Learning Management System |
| **OER** | Open Educational Resources | **MOOC** | Massive Open Online Course |
| **DIKSHA** | Digital Infrastructure for Knowledge Sharing | **SWAYAM** | Study Webs of Active-learning for Young Aspiring Minds |
| **NISHTHA** | National Initiative for School Heads' and Teachers' Holistic Advancement | **NDEAR** | National Digital Education Architecture |
| **NROER** | National Repository of Open Educational Resources | **UDISE** | Unified District Information System for Education |
| **Mbps** | Megabits per second | **GHz** | Gigahertz |

### 8.2 याद रखने योग्य एक-पंक्ति तथ्य (One-Liners)

1. Computer शब्द लैटिन के "computare" से बना — मतलब गणना करना।
2. Father of Computer = Charles Babbage; पहली programmer = Ada Lovelace।
3. पहला electronic digital computer = ENIAC (1946); पहला commercial = UNIVAC I (1951); भारत का पहला = TIFRAC (1956)।
4. पीढ़ियाँ: Vacuum Tube -> Transistor -> IC -> Microprocessor -> AI।
5. पहला microprocessor = Intel 4004 (1971)।
6. कंप्यूटर का मस्तिष्क = CPU; CPU = ALU + CU + Registers।
7. ALU गणना और तुलना करता है; CU नियंत्रण करता है।
8. 1 Nibble = 4 bits; 1 Byte = 8 bits; 1 KB = 1024 B।
9. RAM अस्थायी (volatile); ROM स्थायी (non-volatile)।
10. सबसे तेज़ memory = Register -> Cache -> RAM -> Hard disk।
11. Keyboard सबसे सामान्य input device; Monitor सबसे सामान्य output device।
12. OMR = परीक्षा की answer sheet; MICR = बैंक cheque; OCR = printed text।
13. Touch screen input **और** output दोनों है।
14. Laser printer सबसे तेज़; Dot Matrix एक impact printer।
15. बिना OS के कंप्यूटर काम नहीं कर सकता।
16. Windows = Microsoft; Android = Google; Linux = open source।
17. Ctrl+C copy, Ctrl+V paste, Ctrl+P print, Ctrl+S save, Ctrl+Z undo, Ctrl+A select all, F5 refresh।
18. .docx = Word, .xlsx = Excel, .pptx = PowerPoint, .pdf = PDF file।
19. ARPANET (1969) से internet शुरू; WWW = Tim Berners-Lee (1989); email '@' = Ray Tomlinson (1971)।
20. Chrome/Firefox = browser; Google/Bing = search engine (Google browser नहीं है)।
21. HTTPS सुरक्षित है (लॉक चिह्न); HTTP सामान्य।
22. Email: To = मुख्य, Cc = सबको पता, Bcc = पता नहीं चलता।
23. Email भेजने का protocol = SMTP; पाने का = POP3/IMAP।
24. इंटरनेट = दुनिया का सबसे बड़ा WAN।
25. 5G सबसे तेज़ mobile internet (5G > 4G > 3G)।
26. DIKSHA = 5 सितम्बर 2017 (शिक्षक दिवस), शिक्षक+छात्र platform, QR textbooks।
27. SWAYAM = 9 जुलाई 2017, MOOC online courses; SWAYAM Prabha = DTH TV channels।
28. PM eVIDYA (2020) = एक कक्षा एक चैनल; DIKSHA = "One Nation One Digital Platform"।
29. e-Pathshala = NCERT की e-books; NISHTHA = शिक्षक प्रशिक्षण; NROER/NDLI = open resources का भंडार।
30. OER term = UNESCO 2002; OER के 5R — Retain, Reuse, Revise, Remix, Redistribute।
31. CC BY = सबसे खुला लाइसेंस; NC = non-commercial; ND = no derivatives; SA = share alike।
32. Virus जुड़कर फैलता है; Worm खुद फैलता है; Trojan छिपकर आता है; Ransomware पैसे माँगता है।
33. Phishing = नकली झाँसा (password/OTP माँगना)।
34. Strong password = बड़े+छोटे अक्षर+अंक+चिह्न (8+ characters)।
35. भारत का cyber law = IT Act 2000 (संशोधन 2008); 66C = identity theft, 66D = personation।
36. Digital India = 1 जुलाई 2015; DigiLocker = digital दस्तावेज़।
37. UDISE+ = स्कूलों का राष्ट्रीय data system।
38. Google Classroom/Moodle = LMS; Zoom/Meet = video class; WhatsApp = संचार।
39. Blended learning = classroom + online; Flipped classroom = घर video, class discussion।
40. Copyright Act 1957; plagiarism = दूसरों की रचना चुराना।

### 8.3 Frequently Confused Facts (अक्सर उलझने वाले)

| भ्रम | सही तथ्य |
|---|---|
| RAM vs ROM | RAM = अस्थायी + read/write | ROM = स्थायी + केवल read |
| Google vs Chrome | Google = search engine | Chrome = browser |
| Compiler vs Interpreter | Compiler = पूरा एक साथ | Interpreter = line-by-line |
| Internet vs WWW | Internet = network | WWW = websites की सेवा |
| Virus vs Worm | Virus जुड़कर (file से file) | Worm अकेला network पर |
| SWAYAM vs SWAYAM Prabha | SWAYAM = online courses | Prabha = DTH TV channels |
| DIKSHA vs e-Pathshala | DIKSHA = राष्ट्रीय teacher/छात्र platform | e-Pathshala = NCERT की e-books |
| CD vs DVD vs Blu-ray | 700 MB / 4.7 GB / 25 GB |
| 1 मिलियन bytes नहीं | 1 MB = 1024 KB (1000 नहीं) |
| Touch screen | Input+Output दोनों (सिर्फ input नहीं) |

### 8.4 Last-Minute Revision Sheet (परीक्षा से पहले सुबह वाला)

- पीढ़ियाँ: **V-T-I-M-A** = Vacuum, Transistor, IC, Microprocessor, AI
- CPU = **A**LU + **C**U + Registers ("A-C-R")
- Units: **B->KB->MB->GB->TB** सब 1024 से
- Volatile = RAM | Non-volatile = ROM/HDD
- 1946 ENIAC | 1951 UNIVAC | 1956 TIFRAC | 1969 ARPANET | 1971 Email | 1989 WWW
- 2015 Digital India | 2017 DIKSHA + SWAYAM | 2020 PM eVIDYA
- Full forms: CPU, RAM, ROM, ALU, CU, WWW, HTTP(S), HTML, URL, DNS, ISP, SMTP, POP3, LAN/WAN/MAN/PAN, USB, OS, GUI, OMR/OCR/MICR, PDF, ICT, OER, MOOC, LMS
- Shortcuts: C=copy, V=paste, X=cut, A=all, S=save, P=print, Z=undo, F5=refresh
- Printer: Laser fastest; Dot Matrix = impact; OMR = sheet; MICR = cheque
- Safety: Strong password + 2FA + Antivirus + https; Phishing = झाँसा
- Law: IT Act 2000 (2008 amendment); 66C identity theft
- OER: UNESCO 2002; 5R; CC: BY/SA/NC/ND

---

> 🧠 **अंतिम सलाह:** IT के 4 प्रश्न facts पर आते हैं — Tables 8.1, 8.2, 8.3 रट लें, Question Bank के सभी प्रश्न हल कर लें, और परीक्षा से एक रात पहले केवल section 8.4 दोहराएँ। **4/4 पक्के हैं।**
