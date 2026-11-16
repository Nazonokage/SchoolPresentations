# Auditory Interfaces & Sonification

## 1. Introduction to Auditory Interfaces
* **Context/Review:** Yesterday, we tackled the **touch-based interface** (kung paano natin ginagamit ang pakiramdam o touch sa screen/devices). Today, we will focus on the **auditory interface** and its different types.
* **What is an Auditory Interface?**
    * It is a bidirectional, communicative connection between a human user and a technical product.
    * **Side toward the machine:** Involves machine listening, speech recognition, and dialogue systems.
    * **Side towards the human:** Uses auditory displays (sounds) to send information to the user.
* **Why use sound?**
    * People interact with their environment through multiple senses (seeing, hearing, smelling, tasting, feeling/gestures).
    * Kapag puro visual interface (screens) ang gamit natin, biglang nagiging limitado ang input-output capabilities natin.
    * **The Danger of Visual Overload:** Interacting purely through visual screens in mobile or high-stakes situations can lead to *distraction from the primary task*, rendering it difficult, dangerous, ineffective, and frustrating.
    * *Taglish Note:* Kaya napakahalaga ng auditory interfaces—para silang excellent alternative or complement sa Human-Computer Interaction (HCI) lalo na sa mga visually-demanding or mobile situations (halimbawa, habang nagmamaneho). Flexible sila at hindi nakaka-interfere sa pag-receive natin ng visual info.

---

## 2. The Auditory Interface Processing Loop (System Model)
* *Visual Guide for Slides:* base ito sa flowchart diagram sa Lesson Preview.
* **Data:** Ang pinagmumulan ng raw information na kailangang i-proseso.
* **A: Representation & Preprocessing:** Dito inaayos at tina-translate ang raw data para maging ready sa susunod na step.
* **B: Application, Processing Loop:** Ang tuluy-tuloy na interaction at computation cycle sa loob ng system.
* **Interactions:** Dito pumapasok ang user input (hal. ang ulo/tenga ng tao sa diagram). Galing sa interaction ng user, bumabalik ang data sa processing loop.
* **C: Sonification Techniques (Rendering):** Ang proseso ng pag-convert ng data papunta sa sound waves o signal.
* **D: Technical Sound Display:** Ang physical output hardware (tulad ng speaker) na naglalabas ng tunog para marinig ng user.

---

## 3. Types of Auditory Interface

### Type 1: Audification
* **Definition:** An auditory display technique for representing a sequence of data values as sound. It is a **"direct translation"** of a data waveform to the audible domain.
* **How it works:** * Ino-interpret nito ang isang data sequence or time series bilang isang audio waveform kung saan ang input data ay direktang naka-map sa sound pressure levels.
    * Pinapayagan nito ang listener na marinig ang periodic components bilang frequencies.
    * *Requirement:* Mas gumagana ito sa malalaking data sets na may periodic features (paulit-ulit na pattern).
    * *Purpose:* Pinakasimpleng paraan para makakuha ng direct representation ng data nang hindi na kailangang i-convert pa into visuals.
* **Example/Sample:** * **Seismic/Earthquake Data:** Ang vibrations ng lupa habang may lindol ay may waveform. Kapag pabilis mo ang playback ng seismic data na ito, maririnig mo ito bilang parang kulog o dagundong (Audification ng lindol).

---

### Type 2: Sonification
* **Definition:** The use of **non-speech audio** to convey information or perceptualize data. 
* **Advantages:** Magaling ang auditory perception natin pagdating sa temporal (time), spatial (location), amplitude (loudness), at frequency resolution. Kaya magandang alternatibo o dagdag ang sonification sa karaniwang data visualization (charts/graphs).
* **The Challenge:** Nahaharap sa maraming hamon ang sonification community (gaya ng ICAD - International Community for Auditory Display) dahil mahirap mag-present at mag-analyze ng data gamit lang ang tunog. Maraming sonification attempts ang kailangang i-code from scratch dahil walang standard o flexible tool para dito. Kailangan din ng sapat na "context" para maintindihan ng nakikinig kung ano ang ibig sabihin ng tunog.
* **Example/Sample:** * **Geiger Counter:** Ang rate o bilis ng pag-click ng isang Geiger counter ay nagpapahiwatig ng level ng radiation sa paligid ng device. Kapag mas mabilis ang clicks (`click-click-click-click`), ibig sabihin mataas ang radiation. Non-speech audio ito na nagbibigay ng seryosong data.

---

### Type 3: Earcon
* **Definition:** A brief, distinctive sound that represents a specific event or conveys other information. 
* **Origin of the Name:** It is a pun on the familiar term **"icon"** sa computer interfaces. Kung ang visual icon ay "eye-con", ang auditory icon naman ay tinawag na **"earcon"** (coined by D.A. Sumikawa in 1985).
* **Characteristics:** Karaniwang synthesized tones o sound patterns ang mga ito.
* **Examples/Samples:**
    * **Operating Systems:** Ang simpleng *beep* kapag nagka-error ang computer, o kaya ang customizable sound schemes ng Windows/Mac kapag nag-a-indicate ng startup, shutdown, o low battery.
    * **Broadcast Media Cues:** * Ang alert signal na nag-a-announce ng mensahe mula sa Emergency Broadcast System.
        * Ang sikat na signature *three-tone melody* (`chime`) na nag-iidentify sa NBC radio and television broadcasts.

---

### Type 4: Voicemail System
* **Definition:** Also known as a voice message or voice bank. It is a computer-based system that allows users and subscribers to exchange personal voice messages.
* **Functionality:** It can deliver voice information, and process transactions relating to individuals, organizations, products, and services gamit lang ang ordinaryong telepono.
* **Broad Concept:** Ginagamit din ito para tukuyin ang kahit anong system na nagta-transport ng stored telecommunications voice messages, kasama na ang lumang answering machine.
* **Modern Context:** Halos lahat ng cell phone services ay may voicemail na bilang basic feature. Maraming corporate private branch exchanges (PBX) ang may kasamang versatile internal voice-messaging services.
* **Example/Sample:**
    * **\*98 Vertical Service Code:** Sa US landlines, ito ang tina-dial ng subscribers para ma-access ang kanilang voicemail box para pakinggan, i-select, o i-delete ang mga naiwang audio messages ng mga tumawag sa kanila.