import streamlit as st
import pandas as pd
from datetime import date, datetime
from io import StringIO

st.set_page_config(
    page_title="Grand Celebration | Areeba Muhammad",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Replace these sample details with your real event information.
EVENT_TITLE = "Grand Celebration"
HONOREE = "Areeba Muhammad"
EVENT_DATE = "Date to be announced"
EVENT_TIME = "Time to be announced"
EVENT_VENUE = "Venue to be announced"
EVENT_ADDRESS = "Please update with the event address"
RSVP_DEADLINE = "Please RSVP by the date shared with your invitation"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap');

:root {
  --forest: #244b32;
  --forest-deep: #183923;
  --sage: #9caf91;
  --pale-sage: #e7ede2;
  --ivory: #f8f6ef;
  --gold: #b69b55;
  --ink: #263b2d;
}
.stApp {
  background:
    radial-gradient(ellipse at 8% 4%, rgba(220,231,214,.70), transparent 28%),
    radial-gradient(ellipse at 95% 30%, rgba(231,237,226,.85), transparent 28%),
    var(--ivory);
  color: var(--ink);
  font-family: 'DM Sans', sans-serif;
}
header[data-testid="stHeader"] { background: transparent; }
.block-container { max-width: 1120px; padding-top: 1.5rem; padding-bottom: 3rem; }
.topbar {
  background: linear-gradient(110deg, #183923, #31583b);
  color: #fffdf7; padding: 1rem 1.5rem; border-radius: 16px;
  display:flex; justify-content:space-between; align-items:center; gap:1rem;
  box-shadow: 0 10px 28px rgba(31,62,39,.15);
  margin-bottom: 1.5rem;
}
.brand { font-family:'Playfair Display',serif; font-style:italic; font-size:1.6rem; }
.top-note { font-size:.82rem; letter-spacing:.08em; opacity:.92; text-align:right; }
.hero {
  position:relative; overflow:hidden; text-align:center; padding:3.5rem 1.5rem 2.5rem;
  border:1px solid rgba(156,175,145,.4); border-radius:22px;
  background:linear-gradient(135deg, rgba(255,255,255,.88), rgba(239,243,234,.82));
  box-shadow:0 14px 38px rgba(35,65,43,.07);
}
.hero:before, .hero:after { position:absolute; font-size:5.2rem; opacity:.72; line-height:1; }
.hero:before { content:'🌿'; left:-.2rem; top:.4rem; transform:rotate(-28deg); }
.hero:after { content:'🌿'; right:-.2rem; bottom:.2rem; transform:scaleX(-1) rotate(-28deg); }
.eyebrow { color:var(--forest); letter-spacing:.25em; text-transform:uppercase; font-size:.76rem; font-weight:700; }
.hero h1 { font-family:'Playfair Display',serif; color:var(--forest); font-weight:500; font-size:clamp(2.4rem,6vw,4.5rem); line-height:1.08; margin:.6rem 0 .25rem; }
.honoree { font-family:'Playfair Display',serif; font-size:clamp(1.2rem,3vw,1.8rem); letter-spacing:.12em; color:#49664c; }
.gold-divider { color:var(--gold); font-size:1.25rem; margin:.8rem 0; }
.intro { font-family:'Playfair Display',serif; font-size:1.13rem; color:#47604b; max-width:650px; margin:0 auto; }
.section-title { font-family:'Playfair Display',serif; color:var(--forest); font-size:1.8rem; text-align:center; }
.stTabs [data-baseweb="tab-list"] { justify-content:center; gap:.5rem; }
.stTabs [data-baseweb="tab"] { background:rgba(231,237,226,.75); border-radius:999px; padding:.55rem 1rem; }
.stTabs [aria-selected="true"] { background:var(--forest) !important; color:white !important; }
div[data-testid="stForm"] { background:rgba(255,255,255,.88); padding:1.5rem; border:1px solid #dce4d6; border-radius:18px; }
.stButton > button, .stFormSubmitButton > button, .stDownloadButton > button {
  background:var(--forest); color:white; border:0; border-radius:999px;
  padding:.6rem 1.3rem; font-weight:600;
}
.stButton > button:hover, .stFormSubmitButton > button:hover, .stDownloadButton > button:hover {
  background:var(--forest-deep); color:white; border:0;
}
div[data-baseweb="input"] input, div[data-baseweb="select"] > div, div[data-baseweb="textarea"] textarea {
  border-radius:10px;
}
.info-card {
  background:rgba(231,237,226,.8); border:1px solid #d5dfcf; border-radius:16px;
  padding:1.2rem; height:100%;
}
.info-card h3 { font-family:'Playfair Display',serif; color:var(--forest); margin-top:0; }
.footer { text-align:center; color:#647865; font-family:'Playfair Display',serif; font-style:italic; padding:2rem 0 0; }
.small-note { color:#647865; font-size:.85rem; }
@media (max-width: 700px) {
 .topbar { flex-direction:column; text-align:center; }
 .top-note { text-align:center; }
 .hero { padding:3rem 1rem 2rem; }
 .hero:before, .hero:after { font-size:3rem; }
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="topbar">
  <div class="brand">❧ {EVENT_TITLE}</div>
  <div class="top-note">GOOD COMPANY &nbsp; • &nbsp; HAPPY MOMENTS &nbsp; • &nbsp; BEAUTIFUL MEMORIES</div>
</div>
<div class="hero">
  <div class="eyebrow">Together in celebration</div>
  <h1>{EVENT_TITLE}</h1>
  <div class="honoree">{HONOREE}</div>
  <div class="gold-divider">───────── ♥ ─────────</div>
  <p class="intro">With joyful hearts, we invite you to be part of a special celebration.<br>
  Your presence would make the occasion even more memorable.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
tab_rsvp, tab_details, tab_location = st.tabs(["🌿 RSVP", "✿ Event Details", "⌖ Location"])

# Session state stores responses while this app session is active.
if "rsvps" not in st.session_state:
    st.session_state.rsvps = []

with tab_rsvp:
    st.markdown('<div class="section-title">Kindly Respond</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#617462'>Please let us know if you’ll be joining us.</p>", unsafe_allow_html=True)
    with st.form("rsvp_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full name *", placeholder="Enter your full name")
        with col2:
            email = st.text_input("Email address", placeholder="you@example.com")
        attendance = st.selectbox("Will you be attending? *", ["Please select", "Joyfully accepts", "Regretfully declines"])
        guests = st.selectbox("Number of guests (including you)", [1, 2, 3, 4, 5, 6])
        notes = st.text_area("A note for the hosts (optional)", placeholder="Dietary needs or a message…", height=100)
        submitted = st.form_submit_button("♥  Submit RSVP", use_container_width=True)

        if submitted:
            if not full_name.strip():
                st.error("Please enter your name.")
            elif attendance == "Please select":
                st.error("Please choose whether you will be attending.")
            else:
                st.session_state.rsvps.append({
                    "submitted_at": datetime.now().isoformat(timespec="seconds"),
                    "full_name": full_name.strip(),
                    "email": email.strip(),
                    "attendance": attendance,
                    "guest_count": guests,
                    "notes": notes.strip(),
                })
                st.success("Thank you! Your response has been recorded for this app session.")
                st.info("Important: this starter version stores responses temporarily in memory. Connect a persistent database or Google Sheets before using it for real invitations.")

with tab_details:
    st.markdown('<div class="section-title">The Celebration</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="info-card"><h3>♡ Date</h3><p>{EVENT_DATE}</p><p class="small-note">A day to remember</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="info-card"><h3>◷ Time</h3><p>{EVENT_TIME}</p><p class="small-note">Please arrive a little early</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="info-card"><h3>✿ Dress code</h3><p>Elegant festive attire</p><p class="small-note">Wear what makes you feel wonderful</p></div>', unsafe_allow_html=True)
    st.write("")
    st.info(f"RSVP reminder: {RSVP_DEADLINE}")

with tab_location:
    st.markdown('<div class="section-title">Find Your Way</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="info-card">
      <h3>⌖ {EVENT_VENUE}</h3>
      <p>{EVENT_ADDRESS}</p>
      <p class="small-note">Update the venue and address in app.py before publishing.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">With love and gratitude · We look forward to celebrating with you ♥</div>', unsafe_allow_html=True)

# Optional host-only export for the current session. This is not a persistent admin database.
with st.expander("Host tools (temporary session data)"):
    st.caption("For testing only. These responses disappear when the app session restarts. Do not use this as your permanent guest list.")
    if st.session_state.rsvps:
        export_df = pd.DataFrame(st.session_state.rsvps)
        st.dataframe(export_df, use_container_width=True, hide_index=True)
        csv_data = export_df.to_csv(index=False).encode("utf-8")
        st.download_button("Download current-session RSVPs (CSV)", csv_data, "grand_celebration_rsvps.csv", "text/csv")
    else:
        st.write("No RSVPs in this session yet.")
