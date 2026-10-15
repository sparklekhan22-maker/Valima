# Grand Celebration Invitation App

A floral, green-and-white invitation and RSVP website built with Streamlit.

## Features

- Forest-green, sage, ivory, and botanical styling
- Responsive invitation header and celebration message
- RSVP form with attendance, guest count, email, and optional notes
- Event details and location tabs
- CSV export for responses collected during the current app session

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (optional but recommended).
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository and upload `app.py`, `requirements.txt`, `README.md`, and the `.streamlit/config.toml` file.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect GitHub, select your repository and branch, and set the main file path to `app.py`.
4. Deploy the app.
5. Update the sample event details near the top of `app.py` before sharing the invitation link.

## Customize event details

At the top of `app.py`, update these values:

- `EVENT_TITLE`
- `HONOREE`
- `EVENT_DATE`
- `EVENT_TIME`
- `EVENT_VENUE`
- `EVENT_ADDRESS`
- `RSVP_DEADLINE`

You can also edit the colors in the CSS and `.streamlit/config.toml`.

## Important RSVP storage note

This starter version keeps RSVP entries in Streamlit session memory. The entries can be exported as CSV during that session, but they are **not permanently stored** and may disappear when a session restarts or a visitor opens a new session.

Before using this for real guests, connect a persistent storage option such as Google Sheets, Supabase, or a database. Do not collect real guest information until you have configured and tested secure storage and access controls.

## Project files

```text
grand_celebration_invitation/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── config.toml
```
