# 📄 Markdown ➜ हस्तलिखित-शैली PDF सिस्टम
### Playpen Sans Deva | रंगीन बॉक्स | ऑटो TOC | पूर्ण देवनागरी सपोर्ट

---

## 1. एक लाइन में उपयोग

```bash
python3 pdf-system/md2pdf.py mynotes.md
```
→ `mynotes.pdf` तैयार।

---

## 2. सभी कमांड

```bash
cd ~/pdf-system

# बुनियादी
python3 md2pdf.py notes.md

# नाम व कवर के साथ
python3 md2pdf.py notes.md -o out.pdf \
   --title "गणित नोट्स" --subtitle "SUPER TET" --badge "22 अध्याय"

# कई फाइलें जोड़कर एक किताब
python3 md2pdf.py ch1.md ch2.md ch3.md -o book.pdf --toc

# पूरा फोल्डर (नाम के क्रम में)
python3 md2pdf.py ~/reasoning-book/ -o Reasoning.pdf --toc

# कवर/TOC बंद
python3 md2pdf.py notes.md --no-cover --no-toc

# सारे PDF एक साथ बनाएँ
bash build-all.sh
```

### सभी विकल्प

| विकल्प | काम |
|---|---|
| `-o, --output` | आउटपुट फाइल का नाम |
| `--title` | कवर का मुख्य शीर्षक |
| `--subtitle` | कवर का उप-शीर्षक |
| `--author` | लेखक का नाम |
| `--badge` | कवर पर हरा डैश-बॉक्स |
| `--toc` | विषय-सूची जोड़ें |
| `--no-toc` | विषय-सूची हटाएँ |
| `--no-cover` | कवर पेज हटाएँ |
| `--css FILE` | अतिरिक्त CSS |

> 📌 दो या अधिक फाइलें देने पर **TOC अपने आप** जुड़ जाती है।

---

## 3. फॉर्मेटिंग गाइड — क्या लिखें, क्या बनेगा

### 3.1 शीर्षक (Headings)

| Markdown | PDF में |
|---|---|
| `# शीर्षक` | **नीला भरा बैनर**, नया पेज शुरू |
| `## शीर्षक` | **बैंगनी**, नीचे डैश लाइन |
| `### शीर्षक` | **टील**, बाईं ओर मोटी पट्टी |
| `#### शीर्षक` | **एम्बर**, छोटा |

### 3.2 ⭐ रंगीन बॉक्स — दो तरीके

#### तरीका A — Blockquote (इमोजी से रंग अपने आप)

```markdown
> 💡 यह एम्बर ट्रिक-बॉक्स बनेगा
> ⚡ यह भी एम्बर

> 🔑 यह हरा बॉक्स
> ✅ यह भी हरा

> ⚠️ यह लाल चेतावनी
> ❌ यह भी लाल

> 📌 यह नीला सूचना-बॉक्स
> ℹ️ यह भी नीला

> ⭐ यह बैंगनी बॉक्स

> 🧠 यह टील नोट-बॉक्स
> 📝 यह भी टील
```

**रंग तालिका:**

| इमोजी | रंग |
|---|---|
| 💡 ⚡ 🎯 | एम्बर (ट्रिक) |
| 🔑 ✅ ✔ | हरा (नियम) |
| ⚠️ ❌ ✘ 🚫 | लाल (चेतावनी) |
| 📌 ℹ️ 📊 📚 | नीला (सूचना) |
| ⭐ 🌟 | बैंगनी (महत्वपूर्ण) |
| 🧠 📝 🗒 | टील (नोट) |
| *(कोई नहीं)* | एम्बर (डिफ़ॉल्ट) |

#### तरीका B — Callout (शीर्षक वाला बड़ा बॉक्स)

```markdown
::: trick ⚡ शॉर्टकट
84 × 5 = 840 ÷ 2 = **420**
:::

::: formula सूत्र
SI = P × R × T / 100
:::

::: trap सबसे बड़ा जाल
1900 लीप वर्ष **नहीं** है।
:::

::: example हल किया उदाहरण
25 : 36 :: 49 : ? → उत्तर **64**
:::

::: remember याद रखें
पहाड़े 25 तक रट लें।
:::

::: question अभ्यास प्रश्न
250 का 12% कितना है?
:::
```

**छह प्रकार:** `trick` (एम्बर) · `formula` (हरा) · `trap` (लाल) · `example` (बैंगनी) · `remember` (टील) · `question` (गुलाबी)

### 3.3 सारणी (Tables)

```markdown
| टॉपिक | प्रश्न | अंक |
|---|---|---|
| प्रतिशत | 3 | 3 |
```
→ नीला हेडर, बारी-बारी धारियाँ, गोल किनारे। 14+ पंक्तियों वाली सारणी अपने आप पेज पर बँट जाती है।

### 3.4 सूत्र-पत्र (Code block)

````markdown
```
औसत = योग ÷ संख्या
SI   = PRT/100
```
````
→ हरे डैश-बॉर्डर वाला बॉक्स।

### 3.5 चेकलिस्ट

```markdown
- [ ] पहाड़े 25 तक याद
- [ ] सूत्र-पत्र रिवीजन
```
→ ☐ चिह्न के साथ।

### 3.6 अन्य

| Markdown | PDF |
|---|---|
| `**मोटा**` | गहरा काला बोल्ड |
| `*तिरछा*` | बैंगनी हाइलाइट |
| `` `कोड` `` | गुलाबी इनलाइन कोड |
| `---` | नीली डॉटेड लाइन |
| `- सूची` | नीला बुलेट |
| `1. सूची` | हरा नंबर |

---

## 4. रंग बदलना (Re-skin)

`style.css` की पहली 20 पंक्तियों में `:root` है:

```css
:root{
  --c-blue:#1668c4;   --bg-blue:#eaf3ff;
  --c-green:#127a4d;  --bg-green:#e6f7ee;
  --c-amber:#a8620a;  --bg-amber:#fff3dc;
  --c-red:#c02b3a;    --bg-red:#ffecec;
  --c-purple:#6b3fa0; --bg-purple:#f3ecff;
  --c-teal:#0b6f78;   --bg-teal:#e3f7f8;
  --paper:#fffdf7;    /* पेज का रंग */
  --body:10.4pt;      /* अक्षर का आकार */
}
```

- **फॉन्ट बड़ा करना:** `--body:11.2pt`
- **सफेद पेज:** `--paper:#ffffff`
- **प्रिंटर बचाने हेतु हल्के रंग:** सभी `--bg-*` को `#fafafa` कर दें

---

## 5. फाइल संरचना

```
pdf-system/
├── md2pdf.py          ← मुख्य स्क्रिप्ट
├── style.css          ← पूरी डिज़ाइन (यहीं रंग बदलें)
├── build-all.sh       ← सारे PDF एक साथ
├── README.md          ← यह गाइड
└── fonts/
    ├── PlaypenSansDeva-400.ttf
    ├── PlaypenSansDeva-500.ttf
    ├── PlaypenSansDeva-600.ttf
    └── PlaypenSansDeva-700.ttf
```

---

## 6. नए कंप्यूटर पर सेटअप

```bash
pip install weasyprint markdown pygments
mkdir -p ~/.local/share/fonts
cp pdf-system/fonts/*.ttf ~/.local/share/fonts/
fc-cache -f
```

**Linux पर WeasyPrint को ये सिस्टम लाइब्रेरी चाहिए:**
```bash
sudo apt install libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b libffi-dev
```

---

## 7. तकनीकी टिप्पणियाँ (क्यों ऐसा बनाया)

1. **`FontConfiguration` अनिवार्य है** — इसके बिना WeasyPrint `@font-face` को चुपचाप अनदेखा कर देता है और देवनागरी □□□ (tofu) बन जाती है। स्क्रिप्ट में यह जोड़ा गया है।

2. **इमोजी → मोनोक्रोम प्रतीक** — रंगीन इमोजी फॉन्ट सिस्टम में नहीं है, इसलिए 💡→✎, 🔑→✔, ⭐→★ आदि बदल दिए जाते हैं (DejaVu Sans से)। **बॉक्स का रंग पहले तय होता है**, बदलाव बाद में — इसलिए रंग सही रहते हैं।

3. **लगातार blockquote अलग होते हैं** — Markdown में खाली लाइन से अलग किए `>` ब्लॉक **एक ही** blockquote बन जाते हैं। स्क्रिप्ट उनके बीच `<!-- -->` डालकर अलग-अलग रंगीन बॉक्स बनाती है।

4. **फॉन्ट दो जगह** — `fonts/` फोल्डर में (पोर्टेबिलिटी हेतु) और `~/.local/share/fonts` में (fallback हेतु)।

---

## 8. वर्तमान आउटपुट (`~/PDF/`)

| फाइल | पेज |
|---|---|
| SuperTET-Maths-COMPLETE.pdf | 154 |
| SuperTET-Maths-Primary-QuestionBank.pdf | 52 |
| SuperTET-Maths-Junior-QuestionBank.pdf | 45 |
| SuperTET-Maths-Primary-Notes.pdf | 31 |
| SuperTET-Maths-Junior-Notes.pdf | 25 |
| Reasoning-COMPLETE.pdf | 133 |
| Reasoning-Syllabus-Blueprint.pdf | 12 |
| **कुल** | **452 पेज** |
