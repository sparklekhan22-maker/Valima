
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Valima Invitation | Muhammad Abdul Rashid & Areeba Fatima",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stHeader"] {
    display: none !important;
}
.stApp { background: #edf2e9; }
.block-container { padding: 0 !important; max-width: 100% !important; }
div[data-testid="stHtml"] { padding: 0 !important; }
iframe { border: 0 !important; width: 100% !important; display: block; }
</style>
""", unsafe_allow_html=True)

INVITATION_HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#e9efe4">
<title>Valima Invitation</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&family=Great+Vibes&family=Playfair+Display:ital,wght@0,500;0,600;1,500;1,600&display=swap" rel="stylesheet">

<style>
:root {
--sage:#8ea486;
--sage-mid:#617a5e;
--forest:#243d30;
--forest2:#172b22;
--cream:#fffdf7;
--paper:#f8f8f0;
--gold:#b89a5c;
--gold2:#e2d1a2;
--ink:#34483a;
--muted:#718071;
--line:#d8e0d1;
--white:#fff
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: 12px; }
body {
    margin: 0;
    background: #e9efe4;
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
    -webkit-text-size-adjust: 100%;
}
a, button { font: inherit; }

.wrap {
    width: 100%;
    padding: clamp(4px,1.4vw,15px);
    background: radial-gradient(ellipse at top left,#f8faf4 0,#eaf0e5 48%,#dfe8da 100%);
}

.card {
    position: relative;
    isolation: isolate;
    max-width: 860px;
    margin: 0 auto;
    background: var(--cream);
    border: 1px solid #b9c8b0;
    overflow: hidden;
    box-shadow: 0 18px 60px #203a281c;
}
.card:before {
    content: '';
    position: absolute;
    inset: 8px;
    border: 1px solid #d9c79a;
    pointer-events: none;
    z-index: 5;
}
.card:after {
    content: '';
    position: absolute;
    inset: 13px;
    border: 1px solid #e8e0c8;
    pointer-events: none;
    z-index: 5;
}

.floral {
    position: absolute;
    pointer-events: none;
    z-index: 2;
    color: #8fa987;
    opacity: .62;
    font-family: Georgia,serif;
    line-height: 1;
    filter: drop-shadow(0 2px 1px #fff);
}
.floral.tl {
    top: 13px; left: 12px;
    font-size: clamp(40px,8vw,72px);
    transform: rotate(-25deg);
}
.floral.tr {
    top: 13px; right: 12px;
    font-size: clamp(40px,8vw,72px);
    transform: scaleX(-1) rotate(-25deg);
}
.floral.bl {
    bottom: 15px; left: 12px;
    font-size: clamp(40px,8vw,72px);
    transform: scaleY(-1) rotate(-25deg);
}
.floral.br {
    bottom: 15px; right: 12px;
    font-size: clamp(40px,8vw,72px);
    transform: scale(-1) rotate(-25deg);
}

.petal {
    position: absolute;
    top: -30px;
    z-index: 4;
    pointer-events: none;
    color: #9eb49a;
    opacity: 0;
    animation: petalFall 10s linear infinite;
}
.petal:nth-child(1) { left:14%; animation-delay:0s; font-size:15px; }
.petal:nth-child(2) { left:43%; animation-delay:3s; font-size:11px; }
.petal:nth-child(3) { left:76%; animation-delay:5s; font-size:17px; }
.petal:nth-child(4) { left:89%; animation-delay:7s; font-size:12px; }

@keyframes petalFall {
    0% { transform:translate3d(0,-15px,0) rotate(0deg); opacity:0; }
    10% { opacity:.65; }
    85% { opacity:.55; }
    100% { transform:translate3d(35px,720px,0) rotate(260deg); opacity:0; }
}

.section { position: relative; z-index: 1; }
.reveal {
    opacity: 0;
    transform: translateY(18px);
    transition: opacity .75s ease,transform .75s cubic-bezier(.2,.7,.2,1);
}
.reveal.visible { opacity:1; transform:translateY(0); }

.bismillah {
    text-align: center;
    padding: clamp(25px,4vw,39px) 20px 8px;
    position: relative;
}
.arabic {
    font-family: 'Times New Roman',serif;
    font-size: clamp(26px,5.7vw,39px);
    line-height: 1.55;
    direction: rtl;
    color: var(--forest);
}
.translation {
    font: italic 12px/1.6 'Playfair Display',serif;
    color: var(--muted);
    margin-top: 2px;
}
.ornament {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    color: var(--gold);
    font-size: 18px;
    margin: 12px auto;
}
.ornament:before, .ornament:after {
    content: '';
    height: 1px;
    width: clamp(40px,10vw,86px);
    background: linear-gradient(90deg,transparent,var(--gold));
}
.ornament:after { transform: scaleX(-1); }

.intro { text-align:center; padding:2px 30px 0; }
.eyebrow {
    font: 700 9px/1.7 'DM Sans',sans-serif;
    letter-spacing: .24em;
    text-transform: uppercase;
    color: var(--sage-mid);
}
.intro-copy {
    max-width: 620px;
    margin: 9px auto 0;
    font: 500 clamp(17px,2.8vw,21px)/1.58 'Playfair Display',serif;
    color: #536655;
}
.intro-copy strong { font-weight:600; color:var(--forest); }

.couple { text-align:center; padding:8px 20px 5px; position:relative; }
.couple-name {
    font-family: 'Great Vibes','Cormorant Garamond',serif;
    font-size: clamp(58px,10.8vw,100px);
    font-weight: 400;
    line-height: 1.04;
    letter-spacing: .005em;
    color: var(--forest);
    margin: 4px auto 0;
    text-shadow: 0 2px 0 #e8e0c8;
    overflow-wrap: anywhere;
}
.couple-with {
    font: italic 500 clamp(18px,3vw,25px)/1.2 'Playfair Display',serif;
    color: var(--gold);
    margin: 0 auto;
    letter-spacing: .04em;
}
.couple-name.second { margin-top:0; }
.name-flourish {
    color: var(--sage);
    font-size: 18px;
    letter-spacing: .35em;
    margin-top: 7px;
}

.date-section { padding:13px 20px 22px; text-align:center; }
.date-card {
    max-width: 640px;
    margin: 0 auto;
    position: relative;
    padding: 19px 16px 18px;
    background: linear-gradient(135deg,#f2f6ee 0%,#fffdf7 50%,#edf3e8 100%);
    border: 1px solid var(--gold);
    box-shadow: inset 0 0 0 5px #fffdf7,inset 0 0 0 6px #e8dfc5;
}
.date-card:before, .date-card:after {
    content:'✦';
    position:absolute;
    top:50%;
    transform:translateY(-50%);
    color:var(--gold);
    font-size:14px;
}
.date-card:before { left:13px; }
.date-card:after { right:13px; }
.date-label {
    font:700 9px 'DM Sans',sans-serif;
    letter-spacing:.24em;
    text-transform:uppercase;
    color:var(--sage-mid);
}
.date-day {
    font:500 clamp(31px,6vw,49px)/1.1 'Cormorant Garamond',serif;
    color:var(--forest);
    margin:7px 0 5px;
}
.date-time {
    font:700 10px 'DM Sans',sans-serif;
    letter-spacing:.17em;
    color:var(--sage-mid);
}

.countdown-wrap {
    margin:0 18px 24px;
    padding:22px 18px 19px;
    background:radial-gradient(circle at 50% 0%,#355743 0,#203a2d 48%,#15271f 100%);
    color:#fffdf4;
    text-align:center;
    position:relative;
    overflow:hidden;
    border:1px solid var(--gold);
    box-shadow:inset 0 0 0 5px #203a2d,inset 0 0 0 6px #8d784c;
}
.countdown-wrap:before, .countdown-wrap:after {
    content:'✧';
    position:absolute;
    color:#d8c38c;
    font-size:36px;
    opacity:.5;
    top:10px;
}
.countdown-wrap:before { left:17px; }
.countdown-wrap:after { right:17px; }
.countdown-kicker {
    font:700 9px 'DM Sans',sans-serif;
    letter-spacing:.24em;
    text-transform:uppercase;
    color:#d8c99f;
}
.countdown-title {
    font:italic 500 clamp(24px,4vw,33px)/1.1 'Playfair Display',serif;
    color:#fffdf4;
    margin:6px 0 15px;
}
.countdown-grid {
    display:grid;
    grid-template-columns:repeat(4,minmax(0,1fr));
    gap:9px;
    max-width:520px;
    margin:auto;
}
.count-unit {
    padding:12px 3px 10px;
    background:linear-gradient(180deg,#fdfbf2,#eee9d9);
    border:1px solid #cbb67f;
    border-radius:3px;
    color:var(--forest);
    box-shadow:0 5px 12px #0002;
}
.count-number {
    font:600 clamp(27px,5vw,38px)/1 'Cormorant Garamond',serif;
    font-variant-numeric:tabular-nums;
}
.count-name {
    font:700 8px 'DM Sans',sans-serif;
    letter-spacing:.15em;
    text-transform:uppercase;
    color:#667862;
    margin-top:6px;
}
.count-note {
    font:italic 12px 'Playfair Display',serif;
    color:#e4d8b7;
    margin-top:13px;
}

.venue-section { padding:0 20px 22px; text-align:center; }
.section-kicker {
    font:700 9px 'DM Sans',sans-serif;
    letter-spacing:.23em;
    text-transform:uppercase;
    color:var(--sage-mid);
}
.section-heading {
    font:500 clamp(34px,6vw,46px)/1.05 'Cormorant Garamond',serif;
    color:var(--forest);
    margin:5px 0;
}
.section-subtitle {
    font:italic 13px/1.5 'Playfair Display',serif;
    color:var(--muted);
}
.venue-card {
    max-width:640px;
    margin:15px auto 0;
    position:relative;
    overflow:hidden;
    text-align:center;
    padding:24px 18px 22px;
    background:linear-gradient(145deg,#1b3025,#2b4936 58%,#17291f);
    color:#fffdf5;
    border:1px solid var(--gold);
    box-shadow:inset 0 0 0 5px #203a2d,inset 0 0 0 6px #9d8653;
}
.venue-card:before, .venue-card:after {
    content:'❧';
    position:absolute;
    font-family:Georgia,serif;
    font-size:65px;
    line-height:1;
    color:#a5b99a;
    opacity:.27;
}
.venue-card:before { top:5px; left:8px; transform:rotate(-20deg); }
.venue-card:after { bottom:5px; right:8px; transform:rotate(160deg); }
.venue-top {
    font:700 8px 'DM Sans',sans-serif;
    letter-spacing:.25em;
    color:#e1d0a0;
    text-transform:uppercase;
}
.venue-name {
    font:500 clamp(37px,7vw,54px)/1.05 'Cormorant Garamond',serif;
    color:#fffdf5;
    margin:7px 0;
}
.pin {
    display:flex;
    align-items:center;
    justify-content:center;
    width:47px;
    height:47px;
    margin:10px auto 11px;
    border-radius:50%;
    border:1px solid #d7c18b;
    background:#e6d8b0;
    color:#203a2d;
    font-size:24px;
    box-shadow:0 0 0 5px #ffffff0b;
}
.address {
    font:500 13px/1.75 'DM Sans',sans-serif;
    color:#e8eee2;
    position:relative;
    z-index:1;
}
.map-btn {
    display:inline-flex;
    align-items:center;
    justify-content:center;
    gap:9px;
    text-decoration:none;
    margin-top:17px;
    min-height:46px;
    padding:12px 20px;
    background:#e6d7ad;
    color:#20382b;
    border:1px solid #f5e7bf;
    border-radius:2px;
    font:700 10px 'DM Sans',sans-serif;
    letter-spacing:.06em;
    box-shadow:0 4px 0 #0e2018;
    transition:transform .2s,box-shadow .2s;
}
.map-btn:hover { transform:translateY(-2px); box-shadow:0 6px 0 #0e2018; }

.timing-pill {
    display:inline-flex;
    align-items:center;
    gap:12px;
    margin:14px auto 0;
    padding:11px 19px;
    border:1px solid #d5c59a;
    background:#fbfaf2;
}
.clock-icon {
    display:flex;
    align-items:center;
    justify-content:center;
    width:36px;
    height:36px;
    border-radius:50%;
    background:var(--forest);
    color:#f4e6b9;
    font-size:21px;
}
.time-label {
    font:700 8px 'DM Sans',sans-serif;
    letter-spacing:.17em;
    text-transform:uppercase;
    color:var(--muted);
    text-align:left;
}
.time-value {
    font:500 23px/1.05 'Cormorant Garamond',serif;
    color:var(--forest);
    text-align:left;
    margin-top:3px;
}

.dua { text-align:center; padding:13px 20px 30px; position:relative; }
.dua-frame {
    max-width:600px;
    margin:auto;
    padding:14px 12px 12px;
    border-top:1px solid var(--gold);
    border-bottom:1px solid var(--gold);
    position:relative;
}
.dua-frame:before, .dua-frame:after {
    content:'❧';
    position:absolute;
    top:50%;
    transform:translateY(-50%);
    color:var(--sage);
    font-size:21px;
}
.dua-frame:before { left:-4px; }
.dua-frame:after { right:-4px; transform:translateY(-50%) scaleX(-1); }
.dua-arabic {
    font-family:'Times New Roman',serif;
    direction:rtl;
    font-size:clamp(27px,5.5vw,37px);
    line-height:1.5;
    color:var(--forest);
}
.dua-translation {
    font:italic 14px/1.6 'Playfair Display',serif;
    color:var(--muted);
    margin-top:3px;
}
.footerline {
    font:700 8px 'DM Sans',sans-serif;
    letter-spacing:.2em;
    text-transform:uppercase;
    color:var(--sage-mid);
    margin-top:13px;
}

@media(max-width:560px) {
    .wrap { padding:4px; }
    .card:before { inset:6px; }
    .card:after { inset:10px; }
    .floral.tl, .floral.tr { font-size:39px; opacity:.42; }
    .floral.bl, .floral.br { font-size:38px; opacity:.42; }
    .bismillah { padding:24px 15px 5px; }
    .intro { padding:2px 20px 0; }
    .intro-copy { font-size:16px; line-height:1.58; }
    .couple { padding:9px 12px 4px; }
    .couple-name { font-size:clamp(53px,13.4vw,74px); line-height:1.04; }
    .couple-with { font-size:19px; }
    .date-section { padding:11px 13px 17px; }
    .date-card { padding:18px 23px 17px; }
    .date-day { font-size:clamp(29px,8vw,39px); }
    .date-time { font-size:9px; letter-spacing:.1em; }
    .countdown-wrap { margin:0 9px 20px; padding:20px 12px 17px; }
    .countdown-grid { gap:5px; }
    .count-unit { padding:11px 1px 9px; }
    .count-number { font-size:clamp(25px,7vw,33px); }
    .count-name { font-size:7px; letter-spacing:.08em; }
    .countdown-title { font-size:25px; }
    .venue-section { padding:0 12px 18px; }
    .venue-card { padding:22px 12px 20px; }
    .venue-name { font-size:39px; }
    .address { font-size:12px; }
    .map-btn { width:100%; max-width:300px; padding:12px 8px; }
    .timing-pill { padding:10px 14px; }
    .dua { padding:12px 13px 25px; }
    .footerline { font-size:7px; letter-spacing:.14em; }
}
@media(prefers-reduced-motion:reduce) {
    html { scroll-behavior:auto; }
    .reveal { opacity:1; transform:none; transition:none; }
    .petal { display:none; }
    .map-btn { transition:none; }
}
</style>
</head>

<body>
<div class="wrap">
<main class="card" id="invitation">

<div class="petal" aria-hidden="true">✿</div>
<div class="petal" aria-hidden="true">❀</div>
<div class="petal" aria-hidden="true">✧</div>
<div class="petal" aria-hidden="true">❁</div>

<span class="floral tl" aria-hidden="true">❀ ❧</span>
<span class="floral tr" aria-hidden="true">❀ ❧</span>

<header class="bismillah section reveal">
    <div class="arabic" lang="ar">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
    <div class="translation">In the name of Allah, the Most Gracious, the Most Merciful</div>
    <div class="ornament">❧ ✧ ❀ ✧ ❧</div>
</header>

<section class="intro section reveal">
    <div class="eyebrow">With the blessings of Allah and our families</div>
    <p class="intro-copy">
        <strong>Mr. &amp; Mrs. Arshad Rashid</strong>
        cordially invite you to join them in celebrating the Valima of their beloved son,
    </p>
</section>

<section class="couple section reveal" aria-label="The couple">
    <h1 class="couple-name">Muhammad Abdul Rashid</h1>
    <div class="couple-with">with</div>
    <h2 class="couple-name second">Areeba Fatima</h2>
    <div class="name-flourish">— ❀ —</div>
    <p class="intro-copy" style="font-size:clamp(14px,2.4vw,17px);margin-top:12px">
        Your gracious presence and prayers will make this joyous occasion even more memorable.
    </p>
    <div class="ornament">✧ ❀ ✧</div>
</section>

<section class="date-section section reveal">
    <div class="date-card">
        <div class="date-label">A day of love · A memory forever</div>
        <div class="date-day">Friday, 13 November 2026</div>
        <div class="date-time">THE VALIMA CELEBRATION · KARACHI, PAKISTAN</div>
    </div>
</section>

<section class="countdown-wrap section reveal" aria-label="Countdown to the Valima">
    <div class="countdown-kicker">Until we celebrate together</div>
    <div class="countdown-title">The countdown is on</div>
    <div class="countdown-grid">
        <div class="count-unit"><div class="count-number" id="days">--</div><div class="count-name">Days</div></div>
        <div class="count-unit"><div class="count-number" id="hours">--</div><div class="count-name">Hours</div></div>
        <div class="count-unit"><div class="count-number" id="minutes">--</div><div class="count-name">Minutes</div></div>
        <div class="count-unit"><div class="count-number" id="seconds">--</div><div class="count-name">Seconds</div></div>
    </div>
    <div class="count-note" id="count-note">A beautiful beginning, made brighter with you.</div>
</section>

<section class="venue-section section reveal">
    <div class="section-kicker">A place to gather · A memory to cherish</div>
    <h2 class="section-heading">Join Us at the Venue</h2>
    <div class="section-subtitle">Your presence will make the evening truly special</div>

    <div class="venue-card">
        <div class="venue-top">You are warmly invited to</div>
        <div class="venue-name">Iconic Marquee</div>
        <div class="pin" aria-hidden="true">⌖</div>
        <div class="address">
            76, Block 14, Gulistan-e-Johar<br>
            Karachi, Sindh, Pakistan
        </div>
        <a class="map-btn"
           href="https://www.google.com/maps/search/?api=1&amp;query=Iconic+Marquee%2C+76%2C+Block+14%2C+Gulistan-e-Johar%2C+Karachi%2C+Pakistan"
           target="_blank" rel="noopener">
           <span aria-hidden="true">📍</span> Get Directions on Google Maps ↗
        </a>
    </div>

    <div class="timing-pill">
        <span class="clock-icon" aria-hidden="true">◷</span>
        <div>
            <div class="time-label">Ceremony begins at</div>
            <div class="time-value">7:30 PM</div>
        </div>
    </div>
</section>

<!-- RSVP/contact section intentionally removed -->

<footer class="dua section reveal">
    <div class="ornament">❧ ✧ ❀ ✧ ❧</div>
    <div class="dua-frame">
        <div class="dua-arabic" lang="ar">وَبَارَكَ اللَّهُ لَكُمَا</div>
        <div class="dua-translation">May Allah bless this union with love, mercy and joy.</div>
    </div>
    <div class="footerline">With love and blessings · The Rashid Family</div>
</footer>

<span class="floral bl" aria-hidden="true">❀ ❧</span>
<span class="floral br" aria-hidden="true">❀ ❧</span>

</main>
</div>

<script>
(function() {
    const target = new Date('2026-11-13T19:30:00+05:00').getTime();

    const ids = {
        days: document.getElementById('days'),
        hours: document.getElementById('hours'),
        minutes: document.getElementById('minutes'),
        seconds: document.getElementById('seconds')
    };

    const note = document.getElementById('count-note');

    function update() {
        const remaining = target - Date.now();

        if (remaining <= 0) {
            Object.values(ids).forEach(el => el.textContent = '00');
            note.textContent = 'Today is the day — we look forward to seeing you!';
            return;
        }

        const d = Math.floor(remaining / 86400000);
        const h = Math.floor((remaining % 86400000) / 3600000);
        const m = Math.floor((remaining % 3600000) / 60000);
        const s = Math.floor((remaining % 60000) / 1000);

        ids.days.textContent = String(d).padStart(2, '0');
        ids.hours.textContent = String(h).padStart(2, '0');
        ids.minutes.textContent = String(m).padStart(2, '0');
        ids.seconds.textContent = String(s).padStart(2, '0');
    }

    update();
    setInterval(update, 1000);

    const sections = document.querySelectorAll('.reveal');

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: .08, rootMargin: '0px 0px -25px 0px' });

        sections.forEach(section => observer.observe(section));
    } else {
        sections.forEach(section => section.classList.add('visible'));
    }
})();
</script>

</body>
</html>'''

# RSVP/contact section is removed, so the invitation needs less iframe height.
components.html(INVITATION_HTML, height=2200, scrolling=True)
